#!/usr/bin/env python3
"""Verification scenario E from the kickoff/governance lifecycle redesign (docs/decisions.md
D-007): Python runs UTF-8-safe, tests can use a repository-local temporary root, and
PowerShell-only-7 syntax doesn't creep into scripts this template ships (so a missing
pwsh falls back cleanly to Windows PowerShell 5.1, which is what actually ran these
scripts' own verification -- see the D-007 evidence trail). Stdlib only, zero dependencies.

Run: python scripts/tests/test_windows_env.py
Exit 0 = all PASS. Exit 1 = at least one FAIL.
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check import Reporter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]

# Files this change touched (or that were already part of the zero-dependency scripts
# convention) that must open text with explicit encoding -- a regression guard, not just
# a one-time fix, so a future edit that drops encoding= gets caught here.
ENCODING_CHECKED_FILES = [
    ".agents/skills/ontology-agent/scripts/bootstrap.py",
    ".agents/skills/ontology-agent/scripts/query_graph.py",
    ".agents/skills/ontology-agent/scripts/validate_tool_call.py",
    ".agents/skills/human-review-queue/scripts/install_review_queue.py",
    ".agents/skills/human-review-queue/assets/template/scripts/human_review_queue.py",
    ".agents/skills/human-review-queue/assets/template/scripts/human_review_queue_server.py",
]

CALL_NAME_PATTERN = re.compile(r"\b(open|read_text|write_text|NamedTemporaryFile)\s*\(")


def find_calls_with_args(text: str) -> list[tuple[str, str, int]]:
    """Returns (call_name, full_argument_text, start_offset) for each matched call,
    balancing parens by hand so a nested call like write_text(json.dumps(...), encoding=...)
    doesn't get truncated at the first inner ')' -- a plain [^)]* regex would."""
    results = []
    for match in CALL_NAME_PATTERN.finditer(text):
        call = match.group(1)
        depth = 1
        i = match.end()
        start = i
        while i < len(text) and depth > 0:
            if text[i] == "(":
                depth += 1
            elif text[i] == ")":
                depth -= 1
            i += 1
        results.append((call, text[start:i - 1], match.start()))
    return results

# PowerShell-7-only syntax that would break a plain `powershell.exe` (Windows PowerShell
# 5.1) invocation if it crept into a shipped .ps1 -- ternary, null-coalescing, and
# null-conditional operators.
PS7_ONLY_PATTERNS = [
    (re.compile(r"\?\?(?!\?)"), "null-coalescing operator ??"),
    (re.compile(r"\?\."), "null-conditional operator ?."),
    (re.compile(r"\)\s*\?\s*[^:]+:"), "ternary operator ? :"),
]


def test_encoding_present_on_file_io_calls(r: Reporter) -> None:
    for rel_path in ENCODING_CHECKED_FILES:
        path = REPO_ROOT / rel_path
        text = path.read_text(encoding="utf-8")
        offenders = []
        for call, args, start in find_calls_with_args(text):
            if call == "open" and ("'rb'" in args or '"rb"' in args or "'wb'" in args or '"wb"' in args):
                continue  # binary mode: encoding= is meaningless/forbidden
            if "encoding=" not in args:
                line_no = text.count("\n", 0, start) + 1
                offenders.append(f"{rel_path}:{line_no}: {call}({args.strip()[:60]}...)")
        r.check(f"{rel_path}: every open/read_text/write_text/NamedTemporaryFile call sets encoding=",
                not offenders, "; ".join(offenders))


def test_repo_local_temp_root_usable(r: Reporter) -> None:
    """Confirms a repository-local temp root works as a tempfile.TemporaryDirectory dir=
    target -- the same pattern human_review_queue.py's _staged_tempfile() and
    ontology-agent's own tests rely on -- so tests remain runnable when system temp access
    is restricted."""
    repo_local_root = REPO_ROOT / "scripts" / "tests" / ".tmp-verify"
    repo_local_root.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.TemporaryDirectory(dir=repo_local_root) as tmp:
            probe = Path(tmp) / "probe.txt"
            probe.write_text("ok", encoding="utf-8")
            r.check("repo-local temp root accepts a real write", probe.read_text(encoding="utf-8") == "ok")
    finally:
        try:
            repo_local_root.rmdir()
        except OSError:
            pass  # non-empty or already gone; not a test failure


def test_ps1_scripts_avoid_powershell7_only_syntax(r: Reporter) -> None:
    ps1_files = sorted(REPO_ROOT.glob("**/*.ps1"))
    ps1_files = [p for p in ps1_files if ".git" not in p.parts]
    r.check("at least one .ps1 script exists to check", len(ps1_files) > 0)
    offenders = []
    for path in ps1_files:
        text = path.read_text(encoding="utf-8")
        for pattern, label in PS7_ONLY_PATTERNS:
            if pattern.search(text):
                offenders.append(f"{path.relative_to(REPO_ROOT)}: possible {label}")
    r.check(
        "no shipped .ps1 uses PowerShell-7-only syntax (Windows PowerShell 5.1 fallback stays clean)",
        not offenders, "; ".join(offenders),
    )


def main() -> int:
    r = Reporter()
    test_encoding_present_on_file_io_calls(r)
    test_repo_local_temp_root_usable(r)
    test_ps1_scripts_avoid_powershell7_only_syntax(r)
    return r.summarize("windows restricted environment")


if __name__ == "__main__":
    sys.exit(main())
