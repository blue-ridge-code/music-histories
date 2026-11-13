#!/usr/bin/env python3
"""Conformance check for gauntlet-loop criteria packs (docs/decisions.md D-011, D-012).
Stdlib only, zero dependencies.

Proves what the contract in .agents/skills/gauntlet-loop/references/criteria-packs.md asks
for, so a pack skill (e.g. play-canon) can grow one source file at a time without
drifting from it:

- the contract exists and gauntlet-loop's SKILL.md and protocol template point at it;
- every pack skill (a skill whose SKILL.md points at criteria-packs.md) keeps a
  sources/_TEMPLATE.md, and its SKILL.md indexes exactly the source files on disk;
- every source file has the required sections, a complete review criterion, and a
  calibration plant;
- every source file states its fidelity and what to verify, and a file that claims any
  check against a text names what it was checked against;
- every concept a source file cites in Guidance, Anti-patterns, or its review criterion
  is one it defines under Core concepts (the fidelity whitelist critics cite from);
- loop checks state timing, question, and what a FAIL does;
- no source file tells an agent to speak as its author;
- docs/agents/skill-composition-map.md lists each pack with gauntlet-loop.

Run: python scripts/tests/test_criteria_packs.py
Exit 0 = all PASS. Exit 1 = at least one FAIL.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _check import Reporter  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILLS = REPO_ROOT / ".agents" / "skills"
GAUNTLET = SKILLS / "gauntlet-loop"
CONTRACT = GAUNTLET / "references" / "criteria-packs.md"
COMPOSITION_MAP = REPO_ROOT / "docs" / "agents" / "skill-composition-map.md"

REQUIRED_SECTIONS = [
    "Source",
    "Core concepts",
    "Guidance",
    "Anti-patterns",
    "Review criterion",
    "Calibration plant",
    "Fit",
]
CRITERION_FIELDS = [
    "Set",
    "Source",
    "Concepts",
    "Criterion",
    "Question seeds",
    "Misapplied when",
    "Default binding",
]
LOOP_CHECK_FIELDS = ["Timing", "Question", "On FAIL"]
PERSONA_PATTERNS = [
    r"\bspeak(?:s|ing)? as\b",
    r"\bin the voice of\b",
    r"\byou are (?:now )?(?:the author|huizinga|caillois|bateson|carse|illich|leonard)\b",
    r"\bpretend to be\b",
    r"\brole-?play as\b",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sections(text: str) -> dict[str, str]:
    """Split a Markdown file into its H2 sections."""
    parts = re.split(r"^## (.+)$", text, flags=re.MULTILINE)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def defined_concepts(core: str) -> set[str]:
    """Bold item names under Core concepts, including nested items (e.g. rhetorics)."""
    names = re.findall(r"^\s*- \*\*(.+?)[.:]\*\*", core, flags=re.MULTILINE)
    return {n.strip().lower() for n in names}


def cited_concepts(text: str) -> list[str]:
    """Concept tags at the end of guidance and anti-pattern items: '(A, B)'."""
    cited: list[str] = []
    for item in re.split(r"\n(?=- )", text):
        flat = " ".join(item.split())
        match = re.search(r"\(([^()]+)\)\s*$", flat)
        if match:
            cited.extend(c.strip() for c in match.group(1).split(","))
    return cited


def concept_known(name: str, known: set[str]) -> bool:
    base = name.split(":")[0].strip().lower()
    return base in known


def field(block: str, name: str) -> str | None:
    match = re.search(rf"^- \*\*{re.escape(name)}:\*\*(.*?)(?=^- \*\*|\Z)", block,
                      flags=re.MULTILINE | re.DOTALL)
    return match.group(1).strip() if match else None


def test_contract(r: Reporter) -> None:
    r.check("criteria-pack contract exists", CONTRACT.is_file(), str(CONTRACT))
    skill = read(GAUNTLET / "SKILL.md")
    template = read(GAUNTLET / "assets" / "GAUNTLET.md")
    r.check("gauntlet-loop SKILL.md points at the contract",
            "references/criteria-packs.md" in skill)
    r.check("protocol template points at the contract", "criteria-packs.md" in template)
    for ref in sorted(set(re.findall(r"`(references/[\w-]+\.md)`", skill))):
        r.check(f"gauntlet-loop pointer resolves: {ref}", (GAUNTLET / ref).is_file())


def pack_skills() -> list[Path]:
    return sorted(
        p.parent for p in SKILLS.glob("*/SKILL.md")
        if p.parent != GAUNTLET and "criteria-packs.md" in read(p)
    )


def test_source_file(r: Reporter, pack: str, path: Path) -> None:
    label = f"{pack}/{path.name}"
    text = read(path)
    secs = sections(text)
    missing = [s for s in REQUIRED_SECTIONS if s not in secs]
    r.check(f"{label}: required sections present", not missing, f"missing {missing}")
    if missing:
        return

    source = secs["Source"]
    fidelity = field(source, "Fidelity")
    r.check(f"{label}: states its fidelity", bool(fidelity))
    r.check(f"{label}: lists what to verify", field(source, "Verify") is not None)
    if fidelity and re.search(r"(?<!not )\b(?:checked|corroborated)\b", fidelity, re.I):
        r.check(f"{label}: a claimed check names what it was checked against",
                field(source, "Checked against") is not None)

    known = defined_concepts(secs["Core concepts"])
    r.check(f"{label}: defines core concepts", len(known) >= 3, f"found {sorted(known)}")

    criterion = secs["Review criterion"]
    absent = [f for f in CRITERION_FIELDS if field(criterion, f) is None]
    r.check(f"{label}: review criterion has all fields", not absent, f"missing {absent}")
    binding = (field(criterion, "Default binding") or "").lower()
    r.check(f"{label}: default binding is yes or advisory", binding in {"yes", "advisory"},
            binding)
    seeds = re.findall(r"^\s{2,}- ", field(criterion, "Question seeds") or "", re.MULTILINE)
    r.check(f"{label}: two to four question seeds", 2 <= len(seeds) <= 4, str(len(seeds)))

    listed = field(criterion, "Concepts") or ""
    listed_names = re.split(r",\s*(?![^()]*\))", " ".join(listed.split()))
    unknown_listed = [
        n for n in listed_names
        if not concept_known(re.sub(r"\s*\(.*\)$", "", n), known)
    ]
    r.check(f"{label}: criterion concepts are defined", not unknown_listed,
            f"undefined {unknown_listed}")

    cited = cited_concepts(secs["Guidance"]) + cited_concepts(secs["Anti-patterns"])
    unknown_cited = sorted({c for c in cited if not concept_known(c, known)})
    r.check(f"{label}: every cited concept is defined", not unknown_cited,
            f"undefined {unknown_cited}")

    r.check(f"{label}: calibration plant is written",
            len(secs["Calibration plant"].strip()) > 40)

    loop = next((body for name, body in secs.items() if name.startswith("Loop check")), None)
    if loop is not None:
        absent_loop = [f for f in LOOP_CHECK_FIELDS if field(loop, f) is None]
        r.check(f"{label}: loop check states timing, question, and FAIL effect",
                not absent_loop, f"missing {absent_loop}")

    persona = [p for p in PERSONA_PATTERNS if re.search(p, text, flags=re.IGNORECASE)]
    r.check(f"{label}: no persona instructions", not persona, f"matched {persona}")


def test_packs(r: Reporter) -> None:
    packs = pack_skills()
    r.check("at least one criteria pack skill found", bool(packs))
    composition = read(COMPOSITION_MAP)
    for pack in packs:
        name = pack.name
        sources = pack / "sources"
        r.check(f"{name}: sources/_TEMPLATE.md exists", (sources / "_TEMPLATE.md").is_file())
        on_disk = sorted(p.name for p in sources.glob("*.md") if not p.name.startswith("_"))
        indexed = sorted(set(n for n in re.findall(r"`sources/([\w.-]+\.md)`", read(pack / "SKILL.md"))
                             if not n.startswith("_")))
        r.check(f"{name}: SKILL.md indexes exactly the source files on disk",
                on_disk == indexed, f"disk={on_disk} indexed={indexed}")
        for path in (sources / f for f in on_disk):
            test_source_file(r, name, path)
        row = re.search(rf"\*\*{re.escape(name)}\*\*.*\*\*gauntlet-loop\*\*", composition)
        r.check(f"{name}: composition map pairs it with gauntlet-loop", row is not None)


def main() -> int:
    r = Reporter()
    test_contract(r)
    test_packs(r)
    return r.summarize("criteria packs")


if __name__ == "__main__":
    sys.exit(main())
