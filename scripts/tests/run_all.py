#!/usr/bin/env python3
"""Runs every verification script under scripts/tests/ and reports a combined result.
Stdlib only. Each test_*.py is also independently runnable (`python scripts/tests/test_X.py`).

Run: python scripts/tests/run_all.py
Exit 0 = every script passed. Exit 1 = at least one script failed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent
SCRIPTS = sorted(p for p in TESTS_DIR.glob("test_*.py"))


def main() -> int:
    failed: list[str] = []
    for script in SCRIPTS:
        print(f"\n=== {script.name} ===")
        result = subprocess.run([sys.executable, str(script)])
        if result.returncode != 0:
            failed.append(script.name)
    print()
    if failed:
        print(f"FAIL: {len(failed)} script(s) failed: {failed}")
        return 1
    print(f"PASS: all {len(SCRIPTS)} verification scripts passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
