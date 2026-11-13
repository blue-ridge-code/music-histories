#!/usr/bin/env python3
"""Verification scenarios A (ontology half) and B from the kickoff/governance lifecycle
redesign (docs/decisions.md D-007). Stdlib only, zero dependencies.

Scenario A: a project with 12 provisional-concern folders (each holding only a planning
note, no manifest) must NOT activate ontology-agent -- bootstrap.py must exit 3 and create
nothing.

Scenario B: a project whose approved architecture has 6 real modules with dependency
manifests -- alongside inbox/, gauntlet/, and .agents/ support folders -- must activate
ontology-agent, build a graph from the real structure, and must not count the support
folders as product modules.

Run: python scripts/tests/test_ontology_activation.py
Exit 0 = all PASS. Exit 1 = at least one FAIL.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check import Reporter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
BOOTSTRAP = REPO_ROOT / ".agents" / "skills" / "ontology-agent" / "scripts" / "bootstrap.py"


def run_bootstrap(root: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(BOOTSTRAP), "--root", str(root), *extra_args],
        capture_output=True, text=True, encoding="utf-8",
    )


def test_scenario_a_defers_on_provisional_concerns(r: Reporter) -> None:
    with tempfile.TemporaryDirectory(prefix="oa-scenario-a-") as tmp:
        root = Path(tmp)
        (root / "docs").mkdir()
        (root / "docs" / "PROJECT.md").write_text(
            "# Project: Scenario A\n\n> **Status: planning-active**\n", encoding="utf-8"
        )
        for i in range(1, 13):
            concern_dir = root / f"concern-{i:02d}"
            concern_dir.mkdir()
            (concern_dir / "notes.md").write_text(f"Provisional concern {i}\n", encoding="utf-8")

        result = run_bootstrap(root)
        r.check(
            "scenario A: bootstrap exits 3 (deferred) for 12 provisional-concern folders, no manifests",
            result.returncode == 3, result.stdout + result.stderr,
        )
        r.check(
            "scenario A: no .ontology-agent/ directory is created",
            not (root / ".ontology-agent").exists(), str(root / ".ontology-agent"),
        )


def test_scenario_b_activates_on_real_modules(r: Reporter) -> None:
    with tempfile.TemporaryDirectory(prefix="oa-scenario-b-") as tmp:
        root = Path(tmp)
        (root / "docs").mkdir()
        (root / "docs" / "PROJECT.md").write_text(
            "# Project: Scenario B\n\n> **Status: implementation-ready**\n", encoding="utf-8"
        )

        real_modules = ["api", "worker", "web", "shared", "cli", "db"]
        for name in real_modules:
            mod_dir = root / name
            mod_dir.mkdir()
            (mod_dir / "package.json").write_text(
                json.dumps({"name": name, "dependencies": {"left-pad": "^1.0.0"}}),
                encoding="utf-8",
            )

        # Support/agent-infrastructure folders that must NOT be counted as product modules.
        for name in ("inbox", "gauntlet", "sources", ".agents"):
            support_dir = root / name
            support_dir.mkdir()
            (support_dir / "placeholder.md").write_text("not a module\n", encoding="utf-8")

        result = run_bootstrap(root)
        r.check(
            "scenario B: bootstrap activates (exit 0) with 6 real modules + manifests",
            result.returncode == 0, result.stdout + result.stderr,
        )

        graph_path = root / ".ontology-agent" / "graph.jsonl"
        r.check("scenario B: graph.jsonl was written", graph_path.exists(), str(graph_path))
        if not graph_path.exists():
            return

        records = [
            json.loads(line)
            for line in graph_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        module_names = {
            rec["name"] for rec in records if rec.get("kind") == "entity" and rec.get("type") == "Module"
        }
        r.check(
            "scenario B: exactly the 6 real module dirs are graphed, no support folders",
            module_names == set(real_modules), str(module_names),
        )

        dep_names = {
            rec["name"] for rec in records if rec.get("kind") == "entity" and rec.get("type") == "Dependency"
        }
        r.check(
            "scenario B: dependency entities parsed from the real manifests",
            "left-pad" in dep_names, str(dep_names),
        )

        project_rec = next(
            (rec for rec in records if rec.get("kind") == "entity" and rec.get("type") == "Project"),
            None,
        )
        r.check(
            "scenario B: Project entity status is read from docs/PROJECT.md, not hard-coded 'active'",
            project_rec is not None and project_rec.get("status") == "implementation-ready",
            str(project_rec),
        )


def test_force_small_overrides_the_deferral(r: Reporter) -> None:
    with tempfile.TemporaryDirectory(prefix="oa-force-small-") as tmp:
        root = Path(tmp)
        result = run_bootstrap(root, "--force-small")
        r.check(
            "--force-small is a deliberate, working override of the activation threshold",
            result.returncode == 0, result.stdout + result.stderr,
        )


def main() -> int:
    r = Reporter()
    test_scenario_a_defers_on_provisional_concerns(r)
    test_scenario_b_activates_on_real_modules(r)
    test_force_small_overrides_the_deferral(r)
    return r.summarize("ontology activation")


if __name__ == "__main__":
    sys.exit(main())
