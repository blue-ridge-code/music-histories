#!/usr/bin/env python3
"""Bootstrap a minimal .ontology-agent/ directory for the current project.

Zero LLM calls. Zero third-party dependencies (stdlib only: json, os, re,
pathlib, xml.etree). Safe to re-run; will not overwrite existing instance
data unless --force.

Format choice (deliberate deviation from earlier drafts of this skill that
used a single `graph.ttl` Turtle file): instance data is stored as
`graph.jsonl` -- JSON Lines, one entity or edge record per line -- instead
of RDF Turtle. Reasons:
  - stdlib `json` reads/writes it natively; no rdflib or any RDF library
    needed anywhere in this skill.
  - it is trivially appendable: a running agent (or the validation-gate's
    commit step) can add one fact by opening the file in append mode and
    writing one line, no re-serialization of the whole graph.
  - it is trivially greppable/diffable line-by-line, which plain Turtle
    (with its `;`-continued multi-line statements) is not.
The T-box (ontology classes/properties) is intentionally NOT re-invented
here -- if the sibling "ontology core" piece has published
references/ontology-core.ttl and references/shapes-core.ttl next to this
script, they are copied verbatim into the project's .ontology-agent/ dir
so there is exactly one authored copy of the ontology. If those files do
not exist yet (parallel build), bootstrap still succeeds; it just skips
that copy step.

Directory layout produced (mirrors the .ontology-kg/ layout from the
original draft, renamed to .ontology-agent/, minus the parts owned by
sibling pieces of this skill):

    .ontology-agent/
    |-- ontology.ttl     (copied from the skill's references/, if present)
    |-- shapes.ttl        (copied from the skill's references/, if present)
    |-- graph.jsonl       (instance data seeded by this script -- OUR job)
    |-- schema/
    |   |-- tools.json    (copied from the skill's assets/, if present)
    |   `-- shapes.json   (copied from the skill's assets/, if present)
    `-- log.jsonl         (validation/mutation audit trail, empty until used)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

# Directories that are never useful as "Module" entities and are expensive
# or pointless to descend into while looking for nested package manifests.
# Build artifacts, VCS internals, and virtualenvs -- never real project structure.
SKIP_DIR_NAMES = {
    ".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv",
    "env", "dist", "build", ".idea", ".vscode", "bin", "obj", "target",
    ".mypy_cache", ".pytest_cache", ".tox", "site-packages", ".ontology-agent",
}

# Repository support / agent-infrastructure folders (per this template's
# docs/agents/intake.md and layer-activation-guide.md) -- real, but never product
# modules. Kept separate from SKIP_DIR_NAMES above because the reason differs:
# those are build junk, these are legitimate folders that just are not "the software".
SUPPORT_DIR_NAMES = {"inbox", "gauntlet", "sources"}

MANIFEST_NAMES = {"package.json", "pyproject.toml", "requirements.txt", "go.mod"}

# Below this many real product modules, ontology-agent should not activate unless
# real dependency manifests were also found -- see docs/agents/layer-activation-guide.md.
MIN_MODULES_FOR_ACTIVATION = 6


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def is_skippable_dir(name: str) -> bool:
    return name in SKIP_DIR_NAMES or name in SUPPORT_DIR_NAMES or name.startswith(".")


# Files with only these suffixes (or no suffix and a well-known planning filename)
# don't distinguish a real module from a folder of provisional notes.
PLANNING_ONLY_SUFFIXES = {".md", ".markdown", ".txt", ".rst"}


def has_real_content(module_dir: Path) -> bool:
    """A top-level folder only counts as a real module when it holds something
    beyond planning notes: a recognized dependency manifest, or any file whose
    suffix isn't in PLANNING_ONLY_SUFFIXES. A folder containing only a notes.md
    (a "provisional concern") returns False -- see docs/agents/layer-activation-guide.md."""
    for dirpath, dirnames, filenames in os.walk(module_dir):
        dirnames[:] = [d for d in dirnames if not is_skippable_dir(d)]
        for fname in filenames:
            if fname in MANIFEST_NAMES or fname.endswith(".csproj"):
                return True
            if Path(fname).suffix.lower() not in PLANNING_ONLY_SUFFIXES:
                return True
    return False


def read_project_status(root: Path) -> str | None:
    """Read the lifecycle status token out of docs/PROJECT.md's Status line, e.g.
    "> **Status: kickoff-pending**" -> "kickoff-pending". Returns None if the file,
    the line, or a parseable token is absent -- callers should omit the Project
    entity's status field rather than guess, per docs/agents/lifecycle.md."""
    project_md = root / "docs" / "PROJECT.md"
    try:
        text = project_md.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r"Status:\s*([A-Za-z0-9_-]+)", text)
    if not match:
        return None
    return match.group(1)


# ---------------------------------------------------------------------------
# Manifest parsing -- each returns a list of dependency names (strings).
# Deliberately simple: we want real package names, not resolved versions.
# ---------------------------------------------------------------------------

def parse_package_json(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    names: list[str] = []
    for key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
        section = data.get(key)
        if isinstance(section, dict):
            names.extend(section.keys())
    return names


def parse_requirements_txt(path: Path) -> list[str]:
    names: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        # Strip environment markers, extras, and version specifiers.
        line = line.split(";", 1)[0].strip()
        name = re.split(r"[<>=!~\[\s]", line, maxsplit=1)[0].strip()
        if name:
            names.append(name)
    return names


def parse_pyproject_toml(path: Path) -> list[str]:
    names: list[str] = []
    text: str
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []

    try:
        import tomllib  # Python 3.11+, stdlib
        data = tomllib.loads(text)
    except Exception:
        data = None

    if data is not None:
        project = data.get("project", {})
        for dep in project.get("dependencies", []) or []:
            name = re.split(r"[<>=!~\[\s]", str(dep), maxsplit=1)[0].strip()
            if name:
                names.append(name)
        for group in (project.get("optional-dependencies", {}) or {}).values():
            for dep in group or []:
                name = re.split(r"[<>=!~\[\s]", str(dep), maxsplit=1)[0].strip()
                if name:
                    names.append(name)
        poetry = data.get("tool", {}).get("poetry", {})
        for section_key in ("dependencies", "dev-dependencies"):
            for key in (poetry.get(section_key, {}) or {}).keys():
                if key.lower() != "python":
                    names.append(key)
        return names

    # Fallback regex parse for Python < 3.11 (no tomllib available).
    deps_block = re.search(r"dependencies\s*=\s*\[(.*?)\]", text, re.S)
    if deps_block:
        for m in re.finditer(r'["\']([^"\']+)["\']', deps_block.group(1)):
            name = re.split(r"[<>=!~\[\s]", m.group(1), maxsplit=1)[0].strip()
            if name:
                names.append(name)
    poetry_block = re.search(r"\[tool\.poetry(?:\.dev)?-?dependencies\]\s*(.*?)(?:\n\[|\Z)", text, re.S)
    if poetry_block:
        for m in re.finditer(r"^([A-Za-z0-9_.-]+)\s*=", poetry_block.group(1), re.M):
            if m.group(1).lower() != "python":
                names.append(m.group(1))
    return names


def parse_go_mod(path: Path) -> list[str]:
    names: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []
    in_block = False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("require ("):
            in_block = True
            continue
        if in_block and line == ")":
            in_block = False
            continue
        if in_block:
            parts = line.split()
            if parts:
                names.append(parts[0])
        elif line.startswith("require "):
            parts = line[len("require "):].split()
            if parts:
                names.append(parts[0])
    return names


def parse_csproj(path: Path) -> list[str]:
    names: list[str] = []
    try:
        tree = ElementTree.parse(path)
    except (OSError, ElementTree.ParseError):
        return []
    for el in tree.getroot().iter():
        if el.tag.split("}")[-1] == "PackageReference":
            include = el.get("Include")
            if include:
                names.append(include)
    return names


def dependencies_from_manifest(path: Path) -> tuple[str, list[str]]:
    """Returns (ecosystem, [dependency names]) for a recognized manifest file."""
    name = path.name
    suffix = path.suffix.lower()
    if name == "package.json":
        return "npm", parse_package_json(path)
    if name == "requirements.txt":
        return "pypi", parse_requirements_txt(path)
    if name == "pyproject.toml":
        return "pypi", parse_pyproject_toml(path)
    if name == "go.mod":
        return "go", parse_go_mod(path)
    if suffix == ".csproj":
        return "nuget", parse_csproj(path)
    return "unknown", []


# ---------------------------------------------------------------------------
# Graph record helpers
# ---------------------------------------------------------------------------

def entity_record(entity_id: str, etype: str, **fields) -> dict:
    rec = {"kind": "entity", "id": entity_id, "type": etype, "createdAt": now_iso()}
    rec.update(fields)
    return rec


def edge_record(subject: str, predicate: str, obj: str) -> dict:
    return {"kind": "edge", "subject": subject, "predicate": predicate, "object": obj, "createdAt": now_iso()}


def build_graph_records(root: Path) -> tuple[list[dict], int, int]:
    """Returns (records, product_module_count, manifest_count). The two counts are
    exposed so main() can apply the activation threshold without re-walking the tree."""
    records: list[dict] = []

    project_id = f"project:{root.name}"
    has_git = (root / ".git").exists()
    project_fields: dict = {
        "name": root.name,
        "path": str(root),
        "vcs": "git" if has_git else "none",
    }
    status = read_project_status(root)
    if status is not None:
        project_fields["status"] = status
    records.append(entity_record(project_id, "Project", **project_fields))

    # Top-level directories -> Module entities, Project --contains--> Module.
    # A directory only becomes a Module if it has_real_content(): a bare top-level
    # folder is not evidence of a real module -- a folder holding nothing but
    # planning notes (a "provisional concern") must not be graphed as one, per
    # docs/agents/layer-activation-guide.md's "real modules, not a folder count" rule.
    top_level_modules: dict[str, str] = {}  # dirname -> module_id
    try:
        top_entries = sorted(p for p in root.iterdir() if p.is_dir())
    except OSError:
        top_entries = []
    for entry in top_entries:
        if is_skippable_dir(entry.name) or not has_real_content(entry):
            continue
        module_id = f"module:{entry.name}"
        top_level_modules[entry.name] = module_id
        records.append(entity_record(
            module_id, "Module",
            name=entry.name,
            path=str(entry.relative_to(root)),
        ))
        records.append(edge_record(project_id, "contains", module_id))

    # Walk for package manifests (bounded: prune SKIP_DIR_NAMES so we never
    # descend into node_modules/.venv/etc). Attribute each manifest's
    # dependencies to the nearest top-level module, or the project itself
    # if the manifest sits at the project root.
    seen_dependencies: dict[str, str] = {}  # (ecosystem, name) key -> dependency_id
    manifest_count = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not is_skippable_dir(d)]
        dpath = Path(dirpath)
        manifest_files = [f for f in filenames if f in MANIFEST_NAMES or f.endswith(".csproj")]
        if not manifest_files:
            continue
        manifest_count += len(manifest_files)

        try:
            rel_parts = dpath.relative_to(root).parts
        except ValueError:
            rel_parts = ()
        owner_id = project_id
        if rel_parts:
            owner_id = top_level_modules.get(rel_parts[0], project_id)

        for fname in manifest_files:
            manifest_path = dpath / fname
            ecosystem, dep_names = dependencies_from_manifest(manifest_path)
            for dep_name in dep_names:
                key = f"{ecosystem}:{dep_name}"
                dep_id = seen_dependencies.get(key)
                if dep_id is None:
                    dep_id = f"dependency:{key}"
                    seen_dependencies[key] = dep_id
                    records.append(entity_record(
                        dep_id, "Dependency",
                        name=dep_name,
                        ecosystem=ecosystem,
                    ))
                records.append(edge_record(owner_id, "dependsOn", dep_id))

    return records, len(top_level_modules), manifest_count


def dedupe_records(records: list[dict]) -> list[dict]:
    """Keep first occurrence of each entity id; keep unique (subject, predicate, object) edges."""
    out: list[dict] = []
    seen_entities: set[str] = set()
    seen_edges: set[tuple[str, str, str]] = set()
    for rec in records:
        if rec["kind"] == "entity":
            if rec["id"] in seen_entities:
                continue
            seen_entities.add(rec["id"])
            out.append(rec)
        else:
            key = (rec["subject"], rec["predicate"], rec["object"])
            if key in seen_edges:
                continue
            seen_edges.add(key)
            out.append(rec)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap .ontology-agent/ for the project")
    parser.add_argument("--root", default=".", help="Project root (default: cwd)")
    parser.add_argument("--force", action="store_true", help="Recompute graph.jsonl and overwrite copied ontology/shapes even if present")
    parser.add_argument("--force-small", action="store_true", help="Bootstrap anyway below the module/manifest activation threshold (a deliberate, logged exception)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"[error] root does not exist: {root}", file=sys.stderr)
        return 1

    oa = root / ".ontology-agent"
    graph_path = oa / "graph.jsonl"
    graph_already_exists = graph_path.exists()

    # Compute (and gate on) the graph before creating any .ontology-agent/ artifacts,
    # so a below-threshold project is left with nothing bootstrapped at all -- not a
    # half-created directory with an empty/missing graph.jsonl.
    raw_records: list[dict] | None = None
    if not graph_already_exists or args.force:
        raw_records, module_count, manifest_count = build_graph_records(root)
        if module_count < MIN_MODULES_FOR_ACTIVATION and manifest_count == 0 and not args.force_small:
            print(
                f"[deferred] only {module_count} real product module(s) and "
                f"{manifest_count} dependency manifest(s) found (threshold: "
                f"{MIN_MODULES_FOR_ACTIVATION} modules or any real manifest). Per "
                "docs/agents/layer-activation-guide.md, ontology-agent should not "
                "activate from a count of provisional concerns or support folders. "
                "Re-run with --force-small for a deliberate exception.",
                file=sys.stderr,
            )
            return 3

    oa.mkdir(parents=True, exist_ok=True)
    schema_dir = oa / "schema"
    schema_dir.mkdir(exist_ok=True)  # holds validate_tool_call.py's tool schemas

    # Copy the canonical ontology/shapes from the skill's own references/,
    # if the sibling "ontology core" piece has published them. We only
    # ever read those files, never write them.
    skill_root = Path(__file__).resolve().parent.parent
    skill_references = skill_root / "references"
    for src_name, dst_name in (("ontology-core.ttl", "ontology.ttl"), ("shapes-core.ttl", "shapes.ttl")):
        src = skill_references / src_name
        dst = oa / dst_name
        if src.exists() and (args.force or not dst.exists()):
            shutil.copy2(src, dst)
            print(f"[ok] copied {src.name} -> {dst}")
        elif not src.exists():
            print(f"[skip] {src} not published yet -- run bootstrap again once it lands")

    # Copy the validation-gate piece's shipped seeds for tools.json / shapes.json
    # into schema/ using the exact same idempotent/--force pattern as above --
    # these are the tool-call type schema and SHACL-subset shape registry that
    # validate_tool_call.py reads at runtime (see references/validation-protocol.md).
    skill_assets = skill_root / "assets"
    for src_name, dst_name in (("tool-schema-template.json", "tools.json"), ("shapes-template.json", "shapes.json")):
        src = skill_assets / src_name
        dst = schema_dir / dst_name
        if src.exists() and (args.force or not dst.exists()):
            shutil.copy2(src, dst)
            print(f"[ok] copied {src.name} -> {dst}")
        elif not src.exists():
            print(f"[skip] {src} not published yet -- run bootstrap again once it lands")

    if graph_already_exists and not args.force:
        print(f"[skip] {graph_path} already exists (use --force to recompute)")
    else:
        assert raw_records is not None
        records = dedupe_records(raw_records)
        with graph_path.open("w", encoding="utf-8") as fh:
            for rec in records:
                fh.write(json.dumps(rec, ensure_ascii=False))
                fh.write("\n")
        n_entities = sum(1 for r in records if r["kind"] == "entity")
        n_edges = sum(1 for r in records if r["kind"] == "edge")
        print(f"[ok] wrote {graph_path} ({n_entities} entities, {n_edges} edges)")

    log_path = oa / "log.jsonl"
    if not log_path.exists():
        log_path.write_text("", encoding="utf-8")
        print(f"[ok] created {log_path}")

    print(f"\nBootstrap complete under {oa}")
    print("Query it with: python scripts/query_graph.py contains project:<name>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
