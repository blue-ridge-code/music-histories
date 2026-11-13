"""Shared PASS/FAIL reporter for scripts/tests/*.py. Stdlib only, zero dependencies --
matches the convention already used by .agents/skills/ontology-agent/scripts/selftest_validate.py.

Each test_*.py creates its own Reporter() instance (never a shared module-level list) so
multiple test modules can be imported into one process -- e.g. by run_all.py -- without one
module's failures leaking into another's count.
"""

from __future__ import annotations


class Reporter:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if condition:
            print(f"PASS: {name}")
        else:
            print(f"FAIL: {name}" + (f" -- {detail}" if detail else ""))
            self.failures.append(name)

    def summarize(self, label: str = "") -> int:
        prefix = f"{label}: " if label else ""
        print()
        if self.failures:
            print(f"FAIL: {prefix}{len(self.failures)} check(s) failed: {self.failures}")
            return 1
        print(f"PASS: {prefix}all checks passed")
        return 0
