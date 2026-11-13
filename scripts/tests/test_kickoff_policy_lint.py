#!/usr/bin/env python3
"""Static lint of the canonical kickoff skill (docs/decisions.md D-007), covering the parts
of verification scenario A that can't be exercised without an actual LLM-driven interview:
kickoff's own instructions must promise the planning-active exit state, must not install
implementation-phase skills unconditionally, and must never invoke the review-queue
installer. A regression here means the documented policy drifted, even if no code enforces
it directly.

Run: python scripts/tests/test_kickoff_policy_lint.py
Exit 0 = all PASS. Exit 1 = at least one FAIL.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check import Reporter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
KICKOFF_SKILL = REPO_ROOT / ".agents" / "skills" / "kickoff" / "SKILL.md"
CLAUDE_MIRROR = REPO_ROOT / ".claude" / "skills" / "kickoff" / "SKILL.md"

IMPLEMENTATION_PHASE_SKILLS = ["codebase-design", "tdd", "diagnosing-bugs", "code-review"]


def test_kickoff_exits_at_planning_active(r: Reporter, text: str, label: str) -> None:
    r.check(
        f"{label}: kickoff's close step flips status to planning-active",
        "Status: kickoff-pending` to `Status: planning-active" in text or
        "`Status: planning-active`" in text,
        "expected close step to name planning-active as the exit state",
    )
    r.check(
        f"{label}: kickoff does not claim to flip status to plain 'active'",
        "to `Status: active`" not in text,
        "found a stale 'flip to Status: active' instruction",
    )


def test_implementation_skills_are_deferred(r: Reporter, text: str, label: str) -> None:
    install_step_start = text.find("**Install skills just-in-time.**")
    r.check(f"{label}: has a just-in-time install step", install_step_start != -1)
    if install_step_start == -1:
        return
    # The install step's own text must say these install at implementation-ready, not now.
    next_step_start = text.find("\n7.", install_step_start)
    install_step_text = text[install_step_start:next_step_start if next_step_start != -1 else install_step_start + 2000]
    for skill in IMPLEMENTATION_PHASE_SKILLS:
        r.check(
            f"{label}: install step names '{skill}' as deferred to implementation-ready, not installed now",
            skill in install_step_text and "implementation-ready" in install_step_text,
            install_step_text,
        )
        r.check(
            f"{label}: install step does not run 'npx skills' for '{skill}' unconditionally",
            f"add {skill}" not in install_step_text.lower(),
        )


def test_review_queue_never_invoked(r: Reporter, text: str, label: str) -> None:
    r.check(
        f"{label}: never invokes install_review_queue.py",
        "install_review_queue.py" not in text,
        "kickoff must not deploy the review-queue runtime; it only records the skill as available",
    )
    r.check(
        f"{label}: explicitly says not to deploy the review-queue runtime during kickoff",
        "Do not deploy its runtime queue during kickoff" in text,
    )


def test_ontology_not_gated_on_folder_count(r: Reporter, text: str, label: str) -> None:
    r.check(
        f"{label}: ontology guidance excludes provisional concerns and support folders",
        "provisional concerns" in text and "support folders" in text,
    )
    r.check(
        f"{label}: ontology guidance offers the deferred-selection state",
        "activation deferred" in text,
    )


def test_git_boundary_is_risk_based(r: Reporter, text: str, label: str) -> None:
    r.check(
        f"{label}: does not contain the old blanket 'never run git commands' instruction",
        "Never run git commands." not in text,
    )
    r.check(
        f"{label}: close step allows read-only git inspection",
        "git status" in text and "git diff" in text,
    )


def run_for_file(path: Path, label: str) -> Reporter:
    r = Reporter()
    if not path.exists():
        r.check(f"{label}: SKILL.md exists", False, str(path))
        return r
    text = path.read_text(encoding="utf-8")
    test_kickoff_exits_at_planning_active(r, text, label)
    test_implementation_skills_are_deferred(r, text, label)
    test_review_queue_never_invoked(r, text, label)
    test_ontology_not_gated_on_folder_count(r, text, label)
    test_git_boundary_is_risk_based(r, text, label)
    return r


def main() -> int:
    canonical = run_for_file(KICKOFF_SKILL, "canonical (.agents)")
    mirror = run_for_file(CLAUDE_MIRROR, "mirror (.claude)")
    failures = canonical.failures + mirror.failures
    print()
    if failures:
        print(f"FAIL: kickoff policy lint: {len(failures)} check(s) failed: {failures}")
        return 1
    print("PASS: kickoff policy lint: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
