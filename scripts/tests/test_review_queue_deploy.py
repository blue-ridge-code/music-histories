#!/usr/bin/env python3
"""Verification scenario C from the kickoff/governance lifecycle redesign (docs/decisions.md
D-007): a project reaching its first artifact-review gate deploys human-review-queue
just-in-time, handles an occupied default port safely, confirms project identity over HTTP,
and leaves dispatch disabled. Stdlib only, zero dependencies.

Run: python scripts/tests/test_review_queue_deploy.py
Exit 0 = all PASS. Exit 1 = at least one FAIL.
"""

from __future__ import annotations

import json
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check import Reporter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
INSTALLER = REPO_ROOT / ".agents" / "skills" / "human-review-queue" / "scripts" / "install_review_queue.py"
INSTALLER_DIR = INSTALLER.parent
sys.path.insert(0, str(INSTALLER_DIR))
import install_review_queue as irq  # noqa: E402


def run_installer(repo: Path, port: int) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable, str(INSTALLER),
            "--repo", str(repo),
            "--project-id", "sample", "--project-name", "Sample Project",
            "--repository", "example/sample",
            "--reviewer-id", "owner", "--reviewer-name", "Project Owner",
            "--port", str(port),
        ],
        capture_output=True, text=True, encoding="utf-8",
    )


def test_port_probe_detects_occupied_vs_free(r: Reporter) -> None:
    occupied = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    occupied.bind(("127.0.0.1", 0))
    occupied.listen(1)
    occupied_port = occupied.getsockname()[1]
    try:
        r.check(
            "is_port_free() reports False for a port something is actually listening on",
            irq.is_port_free("127.0.0.1", occupied_port) is False,
        )
        chosen = irq.select_free_port("127.0.0.1", occupied_port)
        r.check(
            "select_free_port() picks a different port instead of the occupied one",
            chosen != occupied_port, str(chosen),
        )
        r.check(
            "select_free_port()'s chosen port is actually free",
            irq.is_port_free("127.0.0.1", chosen) is True,
        )
    finally:
        occupied.close()

    free = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free.bind(("127.0.0.1", 0))
    free_port = free.getsockname()[1]
    free.close()
    r.check(
        "select_free_port() returns the requested port when it's actually free",
        irq.select_free_port("127.0.0.1", free_port) == free_port,
    )


def test_installer_handles_occupied_port_end_to_end(r: Reporter) -> None:
    blocker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    blocker.bind(("127.0.0.1", 0))
    blocker.listen(1)
    blocked_port = blocker.getsockname()[1]
    try:
        with tempfile.TemporaryDirectory(prefix="review-queue-install-") as tmp:
            repo = Path(tmp)
            result = run_installer(repo, blocked_port)
            r.check(
                "installer does not crash when the requested port is occupied",
                result.returncode == 0, result.stdout + result.stderr,
            )
            config_path = repo / "review-queue" / "config.json"
            r.check("installer wrote config.json despite the occupied port", config_path.exists())
            if not config_path.exists():
                return
            config = json.loads(config_path.read_text(encoding="utf-8"))
            r.check(
                "installer recorded a DIFFERENT port than the occupied one, not the occupied one",
                config["server"]["port"] != blocked_port, str(config["server"]["port"]),
            )
            r.check("dispatch stays disabled by default", config["dispatch"]["adapter"] == "none")
            r.check("identity mode stays single_local by default", config["server"]["identity_mode"] == "single_local")
            contract = json.loads((repo / "review-queue" / "control-plane.json").read_text(encoding="utf-8"))
            r.check("Review Control Plane source mode stays disabled", contract["mode_default"] == "disabled")
            r.check("Review Control Plane response writes stay disabled", contract["adapters"]["response_write"] == "disabled")
    finally:
        blocker.close()


def test_installer_uses_requested_port_when_free(r: Reporter) -> None:
    probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    probe.bind(("127.0.0.1", 0))
    free_port = probe.getsockname()[1]
    probe.close()
    with tempfile.TemporaryDirectory(prefix="review-queue-install-") as tmp:
        repo = Path(tmp)
        result = run_installer(repo, free_port)
        r.check("installer succeeds when the requested port is free", result.returncode == 0, result.stdout + result.stderr)
        config = json.loads((repo / "review-queue" / "config.json").read_text(encoding="utf-8"))
        r.check("installer records the exact requested port when it's free", config["server"]["port"] == free_port)
        contract = json.loads((repo / "review-queue" / "control-plane.json").read_text(encoding="utf-8"))
        r.check("generated project records Protocol integration 1.0.0", contract["integration_version"] == "1.0.0")


def test_repo_local_temp_fallback(r: Reporter) -> None:
    """human_review_queue.py's _staged_tempfile() must prefer a repo-local scratch dir
    (review-queue/.runtime/tmp/) so gh dispatch staging works when system temp access is
    restricted, per docs/agents/services.md's Windows-restricted-environment guidance."""
    hrq_path = REPO_ROOT / ".agents" / "skills" / "human-review-queue" / "assets" / "template" / "scripts"
    sys.path.insert(0, str(hrq_path))
    import human_review_queue as hrq  # noqa: E402

    with tempfile.TemporaryDirectory(prefix="hrq-tempfile-") as tmp:
        root = Path(tmp)
        queue = hrq.ProjectQueue.__new__(hrq.ProjectQueue)
        queue.root = root
        path_str = queue._staged_tempfile("hello world", ".md")
        try:
            staged = Path(path_str)
            expected_dir = root / "review-queue" / ".runtime" / "tmp"
            r.check(
                "_staged_tempfile() writes into the repo-local scratch dir, not system temp",
                staged.parent == expected_dir, str(staged),
            )
            r.check("staged file content round-trips", staged.read_text(encoding="utf-8") == "hello world")
        finally:
            Path(path_str).unlink(missing_ok=True)


def test_gh_subprocess_uses_utf8_encoding(r: Reporter) -> None:
    hrq_source = (
        REPO_ROOT / ".agents" / "skills" / "human-review-queue" / "assets" / "template" / "scripts" / "human_review_queue.py"
    ).read_text(encoding="utf-8")
    run_gh_start = hrq_source.find("def _run_gh")
    run_gh_body = hrq_source[run_gh_start:run_gh_start + 400]
    r.check(
        "_run_gh()'s subprocess call passes encoding='utf-8' explicitly",
        'encoding="utf-8"' in run_gh_body,
        run_gh_body,
    )


def test_identity_endpoint_confirms_project_over_http(r: Reporter) -> None:
    """Starts the real server against a freshly installed project and hits the new,
    unauthenticated /api/review-queue/identity endpoint -- this is what
    start-human-review-queue.ps1 now calls before treating an existing listener as
    "already running for this project" instead of assuming."""
    with tempfile.TemporaryDirectory(prefix="review-queue-identity-") as tmp:
        repo = Path(tmp)
        probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        probe.bind(("127.0.0.1", 0))
        port = probe.getsockname()[1]
        probe.close()

        install_result = run_installer(repo, port)
        r.check("identity test: install succeeds", install_result.returncode == 0, install_result.stderr)
        if install_result.returncode != 0:
            return

        server_script = repo / "scripts" / "human_review_queue_server.py"
        proc = subprocess.Popen(
            [sys.executable, str(server_script), "--port", str(port), "--no-dispatch"],
            cwd=repo, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding="utf-8",
        )
        try:
            url = f"http://127.0.0.1:{port}/api/review-queue/identity"
            payload = None
            status = None
            last_error: Exception | None = None
            for _ in range(50):
                try:
                    with urllib.request.urlopen(url, timeout=1) as resp:
                        status = resp.status
                        payload = json.loads(resp.read().decode("utf-8"))
                    break
                except (urllib.error.URLError, ConnectionError, TimeoutError) as exc:
                    last_error = exc
                    time.sleep(0.1)
            r.check("identity endpoint answers HTTP 200", status == 200, str(last_error))
            r.check(
                "identity endpoint names this project's id (project_id=sample)",
                payload is not None and payload.get("project_id") == "sample", str(payload),
            )
            r.check(
                "identity endpoint identifies as the human-review-queue service",
                payload is not None and payload.get("service") == "human-review-queue", str(payload),
            )
        finally:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()


def main() -> int:
    r = Reporter()
    test_port_probe_detects_occupied_vs_free(r)
    test_installer_handles_occupied_port_end_to_end(r)
    test_installer_uses_requested_port_when_free(r)
    test_repo_local_temp_fallback(r)
    test_gh_subprocess_uses_utf8_encoding(r)
    test_identity_endpoint_confirms_project_over_http(r)
    return r.summarize("review-queue deploy hardening")


if __name__ == "__main__":
    sys.exit(main())
