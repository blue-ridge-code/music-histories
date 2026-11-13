"""Loopback human review hub with approved-reviewer routing."""

from __future__ import annotations

import argparse
import json
import logging
import mimetypes
import re
import secrets
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from human_review_queue import QueueError, ReviewHub


ROOT = Path(__file__).resolve().parent.parent
MAX_BODY_BYTES = 1024 * 1024


class ReviewQueueServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, address, handler, hub: ReviewHub, token: str, logger: logging.Logger):
        super().__init__(address, handler)
        self.hub = hub
        self.token = token
        self.queue_lock = threading.RLock()
        self.logger = logger


class ReviewQueueHandler(BaseHTTPRequestHandler):
    server: ReviewQueueServer

    def log_message(self, format_string: str, *args) -> None:
        self.server.logger.info("%s - %s", self.address_string(), format_string % args)

    def end_headers(self) -> None:
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header(
            "Content-Security-Policy",
            "default-src 'self'; script-src 'self'; style-src 'self'; media-src 'self'; "
            "img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'",
        )
        super().end_headers()

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/":
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", "/review-queue/")
            self.end_headers()
            return
        if parsed.path == "/api/review-queue/identity":
            # Unauthenticated on purpose: exposes only project id/name, never queue
            # data, so a caller (start-human-review-queue.ps1, or anything else
            # probing an already-bound port) can confirm a listener belongs to this
            # project before treating it as "already running" -- see
            # docs/agents/lifecycle.md's review-queue gate-placement note and
            # references/security.md.
            project = self.server.hub.host_config.get("project", {})
            self._write_json(HTTPStatus.OK, {
                "service": "human-review-queue",
                "project_id": project.get("id", ""),
                "project_name": project.get("name", ""),
            })
            return
        if parsed.path == "/api/review-queue":
            try:
                reviewer_id = self._reviewer_id(parsed)
                with self.server.queue_lock:
                    payload = self.server.hub.state(reviewer_id)
                payload["csrf_token"] = self.server.token
                self._write_json(HTTPStatus.OK, payload)
            except QueueError as exc:
                self._write_json(HTTPStatus.FORBIDDEN, {"error": str(exc)})
            return
        if parsed.path.startswith("/review-queue/"):
            relative = unquote(parsed.path.removeprefix("/review-queue/")) or "index.html"
            self._serve_path(ROOT / "review-queue", relative)
            return
        if parsed.path.startswith("/media/"):
            parts = unquote(parsed.path.removeprefix("/media/")).split("/", 1)
            if len(parts) != 2 or parts[0] not in self.server.hub.sources:
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            self._serve_path(self.server.hub.sources[parts[0]].root, parts[1])
            return
        self.send_error(HTTPStatus.NOT_FOUND)

    def do_HEAD(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path.startswith("/review-queue/"):
            relative = unquote(parsed.path.removeprefix("/review-queue/")) or "index.html"
            self._serve_path(ROOT / "review-queue", relative, send_body=False)
            return
        if parsed.path.startswith("/media/"):
            parts = unquote(parsed.path.removeprefix("/media/")).split("/", 1)
            if len(parts) == 2 and parts[0] in self.server.hub.sources:
                self._serve_path(self.server.hub.sources[parts[0]].root, parts[1], send_body=False)
                return
        self.send_error(HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path not in {"/api/review-queue/respond", "/api/review-queue/import", "/api/review-queue/retry"}:
            self._write_json(HTTPStatus.NOT_FOUND, {"error": "unknown endpoint"})
            return
        if not self._same_origin():
            self._write_json(HTTPStatus.FORBIDDEN, {"error": "cross-origin request rejected"})
            return
        if self.headers.get("X-Review-Queue-Token") != self.server.token:
            self._write_json(HTTPStatus.FORBIDDEN, {"error": "invalid review queue token"})
            return
        try:
            reviewer_id = self._reviewer_id(parsed)
            body = self._read_json_body()
            with self.server.queue_lock:
                if parsed.path == "/api/review-queue/respond":
                    result = self.server.hub.respond(body, reviewer_id, source="human-review-queue-web")
                elif parsed.path == "/api/review-queue/import":
                    result = self.server.hub.import_legacy(body, reviewer_id)
                else:
                    result = self.server.hub.process_pending_actions()
                state = self.server.hub.state(reviewer_id)
            self._write_json(HTTPStatus.OK, {"result": result, "state": state})
        except QueueError as exc:
            self._write_json(HTTPStatus.BAD_REQUEST, {"error": str(exc)})
        except (json.JSONDecodeError, UnicodeDecodeError):
            self._write_json(HTTPStatus.BAD_REQUEST, {"error": "invalid JSON body"})
        except Exception as exc:
            self.server.logger.exception("human review queue request failed")
            self._write_json(HTTPStatus.INTERNAL_SERVER_ERROR, {"error": str(exc)})

    def _reviewer_id(self, parsed) -> str:
        config = self.server.hub.host_config["server"]
        mode = config["identity_mode"]
        if mode == "single_local":
            reviewer_id = config.get("default_reviewer", "")
        elif mode == "local_switcher":
            reviewer_id = (parse_qs(parsed.query).get("reviewer") or [""])[0]
        elif mode == "trusted_header":
            header = config.get("trusted_identity_header", "X-Review-Queue-Reviewer")
            reviewer_id = self.headers.get(header, "")
        else:
            raise QueueError(f"unsupported identity mode: {mode}")
        if not self.server.hub.registry.active(reviewer_id):
            raise QueueError("request does not identify an active approved reviewer")
        return reviewer_id

    def _same_origin(self) -> bool:
        origin = self.headers.get("Origin")
        if not origin:
            return True
        parsed = urlparse(origin)
        return parsed.scheme == "http" and parsed.hostname in {"127.0.0.1", "localhost"} and parsed.port == self.server.server_port

    def _read_json_body(self):
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0 or length > MAX_BODY_BYTES:
            raise QueueError("request body must be between 1 byte and 1 MiB")
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def _serve_path(self, base: Path, relative: str, send_body: bool = True) -> None:
        base = base.resolve()
        target = (base / relative).resolve()
        try:
            target.relative_to(base)
        except ValueError:
            self.send_error(HTTPStatus.FORBIDDEN)
            return
        if not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        size = target.stat().st_size
        start = 0
        end = size - 1
        status = HTTPStatus.OK
        range_header = self.headers.get("Range")
        if range_header:
            match = re.fullmatch(r"bytes=(\d*)-(\d*)", range_header.strip())
            if not match:
                self.send_error(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
                return
            if match.group(1):
                start = int(match.group(1))
                end = int(match.group(2)) if match.group(2) else end
            elif match.group(2):
                length = int(match.group(2))
                start = max(0, size - length)
            if start >= size or end < start:
                self.send_response(HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE)
                self.send_header("Content-Range", f"bytes */{size}")
                self.end_headers()
                return
            end = min(end, size - 1)
            status = HTTPStatus.PARTIAL_CONTENT
        length = max(0, end - start + 1)
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(length))
        self.send_header("Accept-Ranges", "bytes")
        if status == HTTPStatus.PARTIAL_CONTENT:
            self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.end_headers()
        if not send_body:
            return
        with target.open("rb") as stream:
            stream.seek(start)
            remaining = length
            while remaining:
                chunk = stream.read(min(1024 * 1024, remaining))
                if not chunk:
                    break
                self.wfile.write(chunk)
                remaining -= len(chunk)

    def _write_json(self, status: HTTPStatus, payload) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)


def action_worker(server: ReviewQueueServer, stop: threading.Event, interval: int) -> None:
    while not stop.wait(interval):
        try:
            with server.queue_lock:
                server.hub.process_pending_actions()
        except Exception:
            server.logger.exception("human review action retry failed")


def build_logger(log_path: Path) -> logging.Logger:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(f"human-review-queue:{log_path}")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        for handler in (logging.FileHandler(log_path, encoding="utf-8"), logging.StreamHandler()):
            handler.setFormatter(formatter)
            logger.addHandler(handler)
    return logger


def main() -> int:
    config = json.loads((ROOT / "review-queue" / "config.json").read_text(encoding="utf-8"))
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=config["server"].get("port", 4173))
    parser.add_argument("--no-dispatch", action="store_true")
    parser.add_argument("--retry-seconds", type=int, default=30)
    args = parser.parse_args()

    runtime = ROOT / "review-queue" / ".runtime"
    logger = build_logger(runtime / "human-review-queue.log")
    hub = ReviewHub(ROOT, enable_dispatch=not args.no_dispatch)
    try:
        server = ReviewQueueServer(("127.0.0.1", args.port), ReviewQueueHandler, hub, secrets.token_urlsafe(32), logger)
    except OSError as exc:
        logger.error("could not bind 127.0.0.1:%s (%s) -- is another service already using this port? "
                     "Check with the /api/review-queue/identity endpoint before assuming it's this project.",
                     args.port, exc)
        return 1
    stop = threading.Event()
    worker = threading.Thread(target=action_worker, args=(server, stop, args.retry_seconds), name="human-review-action-worker", daemon=True)
    worker.start()
    logger.info("human review queue listening at http://127.0.0.1:%s/review-queue/", args.port)
    try:
        server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        server.server_close()
        logger.info("human review queue stopped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
