"""Install the bundled human review queue into a repository."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import socket
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = SKILL_DIR / "assets" / "template"
MARKER_START = "<!-- human-review-queue:start -->"
MARKER_END = "<!-- human-review-queue:end -->"

PORT_PROBE_RANGE = 20  # how many ports past the requested one to try before failing closed


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def is_port_free(host: str, port: int) -> bool:
    """Bind-and-release probe: True if nothing is currently listening on host:port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        try:
            probe.bind((host, port))
        except OSError:
            return False
        return True


def select_free_port(host: str, requested_port: int) -> int:
    """Return requested_port if free; otherwise the next free port within
    PORT_PROBE_RANGE. Fails closed (raises) rather than silently writing a port
    nothing will actually be able to bind."""
    for port in range(requested_port, requested_port + PORT_PROBE_RANGE + 1):
        if is_port_free(host, port):
            return port
    raise SystemExit(
        f"no free port found in {requested_port}-{requested_port + PORT_PROBE_RANGE} "
        f"on {host}; pass --port explicitly to pick one outside this range"
    )


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def copy_template(repo: Path, force: bool) -> list[Path]:
    written: list[Path] = []
    for source in TEMPLATE_DIR.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(TEMPLATE_DIR)
        target = repo / relative
        if target.exists() and not force:
            raise FileExistsError(f"refusing to overwrite {target}; inspect it or use --force")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        written.append(target)
    return written


def add_gitignore(repo: Path) -> None:
    path = repo / ".gitignore"
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    lines = ["review-queue/.runtime/", "review-queue/__pycache__/", "scripts/__pycache__/"]
    missing = [line for line in lines if line not in current.splitlines()]
    if missing:
        prefix = "" if not current or current.endswith("\n") else "\n"
        path.write_text(current + prefix + "\n".join(missing) + "\n", encoding="utf-8")


def add_agent_instruction(repo: Path) -> None:
    path = repo / "AGENTS.md"
    current = path.read_text(encoding="utf-8") if path.exists() else ""
    if MARKER_START in current:
        return
    block = (
        f"{MARKER_START}\n"
        "At the start of each project session, run "
        "`python scripts/human_review_queue.py scan --json`. Treat completed Queue "
        "Responses as human decisions. Before pausing for a new gate, use the "
        "`human-review-queue` skill, enqueue a validated entry, verify its reviewer "
        "route and Agent Action boundary, and give the full fallback handoff. A Queue "
        "Response does not broaden authority.\n"
        f"{MARKER_END}\n"
    )
    prefix = "" if not current or current.endswith("\n") else "\n"
    path.write_text(current + prefix + "\n" + block, encoding="utf-8")


def configure(repo: Path, args: argparse.Namespace) -> int:
    """Writes review-queue/*.json. Returns the port actually recorded in config.json,
    which may differ from args.port if the requested port was occupied (see
    select_free_port -- fails closed instead of writing an occupied port)."""
    task_name = f"{slug(args.project_id)}-human-review-queue"
    chosen_port = select_free_port("127.0.0.1", args.port)
    if chosen_port != args.port:
        print(f"port {args.port} was occupied; recorded port {chosen_port} instead")
    config = {
        "schema_version": 1,
        "project": {"id": args.project_id, "name": args.project_name, "repository": args.repository},
        "server": {
            "port": chosen_port,
            "task_name": task_name,
            "identity_mode": "single_local",
            "default_reviewer": args.reviewer_id,
            "trusted_identity_header": "X-Review-Queue-Reviewer",
        },
        "recording": {
            "log_dir": "docs/agents/review-decisions/log",
            "profile_path": "docs/agents/review-decisions/profile.md",
        },
        "dispatch": {
            "adapter": "none",
            "repository": args.repository,
            "label": "human-review:queued",
            "fixed_boundary": "Do not push, merge, publish, release, send, spend, use credentials, or perform destructive work without separate authority.",
        },
    }
    reviewers = {
        "schema_version": 1,
        "reviewers": [{
            "id": args.reviewer_id,
            "display_name": args.reviewer_name,
            "active": True,
            "roles": ["owner", "standards", "subject-matter", "rights", "release"],
            "parent_id": None,
        }],
    }
    hub = {
        "schema_version": 1,
        "sources": [{"id": args.project_id, "name": args.project_name, "root": ".", "enabled": True}],
    }
    control_plane = {
        "schema_version": 1,
        "integration_version": "1.0.0",
        "review_protocol": {"major": 1, "minor": 0},
        "mode_default": "disabled",
        "privacy": "local_only",
        "repository": {
            "canonical_repository": args.repository,
            "github_repository_id": None,
        },
        "queue": {
            "root": "review-queue",
            "reviewer_registry": "review-queue/reviewers.json",
            "default_reviewer_id": args.reviewer_id,
        },
        "adapters": {
            "read": "review-queue-v1-read-only",
            "response_write": "disabled",
        },
        "legacy_listener": {
            "task_name": task_name,
            "retirement": "separate_owner_gate",
        },
        "provenance": {
            "contract_owner": "blue-ridge-code/commute-dispatch",
            "template_owner": "blue-ridge-code/vscode-template",
            "last_evaluated": "2026-08-27",
        },
    }
    write_json(repo / "review-queue" / "config.json", config)
    write_json(repo / "review-queue" / "reviewers.json", reviewers)
    write_json(repo / "review-queue" / "hub.json", hub)
    write_json(repo / "review-queue" / "queue.json", {"schema_version": 1, "entries": []})
    write_json(repo / "review-queue" / "control-plane.json", control_plane)
    return chosen_port


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--repo", type=Path, required=True)
    result.add_argument("--project-id", required=True)
    result.add_argument("--project-name", required=True)
    result.add_argument("--repository", required=True)
    result.add_argument("--reviewer-id", required=True)
    result.add_argument("--reviewer-name", required=True)
    result.add_argument("--port", type=int, default=4173)
    result.add_argument("--force", action="store_true")
    result.add_argument("--update-agents", action="store_true")
    return result


def main() -> int:
    args = parser().parse_args()
    repo = args.repo.resolve()
    if not repo.is_dir():
        raise SystemExit(f"repository path does not exist: {repo}")
    if not slug(args.project_id) or not slug(args.reviewer_id):
        raise SystemExit("project and reviewer IDs must contain letters or digits")
    written = copy_template(repo, args.force)
    port = configure(repo, args)
    add_gitignore(repo)
    if args.update_agents:
        add_agent_instruction(repo)
    print(f"installed human review queue in {repo}")
    print(f"wrote {len(written)} template file(s)")
    print(f"server will listen on 127.0.0.1:{port}")
    print("dispatch remains disabled until config.json is explicitly approved")
    print("run: python scripts/test_human_review_queue.py")
    print("run: node scripts/test_human_review_queue_client.js")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
