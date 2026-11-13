#!/usr/bin/env python3
"""Verification scenario D from the kickoff/governance lifecycle redesign (docs/decisions.md
D-007): read-only Git commands are allowed for worktree inspection (including during
kickoff); Git mutation remains prohibited. Stdlib only, zero dependencies.

The prohibition itself isn't sandboxed by tooling here (this template governs agent
instructions, not a technical sandbox) so this test proves what code CAN prove: the
read-only commands actually work in a disposable clone, and AGENTS.md documents both the
allowed list and the prohibited list in text an agent will read before acting.

Run: python scripts/tests/test_git_boundary.py
Exit 0 = all PASS. Exit 1 = at least one FAIL.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check import Reporter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
AGENTS_MD = REPO_ROOT / "AGENTS.md"

READ_ONLY_COMMANDS = [
    ["git", "status"],
    ["git", "diff"],
    ["git", "remote"],
    ["git", "config", "--get", "user.name"],
]


def run_git(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8")


def test_read_only_commands_succeed_in_a_disposable_clone(r: Reporter) -> None:
    with tempfile.TemporaryDirectory(prefix="git-boundary-") as tmp:
        clone_dir = Path(tmp) / "clone"
        clone = run_git(["git", "clone", "--depth", "1", str(REPO_ROOT), str(clone_dir)], cwd=Path(tmp))
        r.check("disposable clone succeeds (setup)", clone.returncode == 0, clone.stderr)
        if clone.returncode != 0:
            return

        # A user identity isn't guaranteed on a bare CI clone -- set one locally so the
        # config --get probe below has something real to read, matching what kickoff's
        # own connector check does (services.md "Agent can test").
        run_git(["git", "config", "user.name", "Test User"], cwd=clone_dir)
        run_git(["git", "config", "user.email", "test@example.com"], cwd=clone_dir)

        for args in READ_ONLY_COMMANDS:
            result = run_git(args, cwd=clone_dir)
            r.check(f"read-only '{' '.join(args)}' succeeds", result.returncode == 0, result.stderr)


def test_agents_md_documents_the_boundary(r: Reporter) -> None:
    text = AGENTS_MD.read_text(encoding="utf-8")
    r.check("AGENTS.md has a Git boundary section", "Git boundary" in text)
    r.check(
        "AGENTS.md names the allowed read-only commands",
        all(cmd in text for cmd in ["git status", "git diff", "git remote", "git config --get"]),
    )
    r.check(
        "AGENTS.md names the prohibited mutating commands",
        all(word in text for word in ["Commit", "push", "branch switching", "merge", "reset", "history rewrites"]),
    )
    r.check(
        "AGENTS.md states the boundary applies everywhere, not just kickoff",
        "not just during kickoff" in text or "every phase" in text,
    )


def main() -> int:
    r = Reporter()
    test_read_only_commands_succeed_in_a_disposable_clone(r)
    test_agents_md_documents_the_boundary(r)
    return r.summarize("git boundary")


if __name__ == "__main__":
    sys.exit(main())
