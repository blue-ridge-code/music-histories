#!/usr/bin/env python3
"""Two-layer, zero-dependency validation gate for agent tool calls.

Layer 1 (type):  JSON-Schema-subset check against .ontology-agent/schema/tools.json.
                  Default-deny: a tool_name absent from tools.json is REJECTED, not
                  silently passed through. The only way for a tool to skip type/shape
                  gating is an explicit, audited opt-out on its tools.json entry:
                  "x-unvalidated": true plus a required, non-empty
                  "x-unvalidated-reason" string (e.g. a pure read-only/exploratory
                  tool a project owner has consciously decided doesn't need gating).
                  A missing or empty reason fails closed — the call is still rejected.
Layer 2 (shape): a *generic* SHACL-subset evaluator that reads shape definitions
                  from .ontology-agent/schema/shapes.json — it does not branch on
                  tool_name anywhere. Behaviour is entirely data-driven:
                    - tools.json may annotate a tool with "x-shape-target": "<Class>"
                      to say "validate these arguments as an instance of <Class>".
                    - tools.json may annotate a tool with "x-property-map" to rename
                      a JSON argument key to the ontology property path it represents
                      (e.g. {"assignee": "ownedBy"}), when the names differ.
                    - Every tool call, regardless of name, is *also* checked as an
                      implicit :ToolCall individual against ToolCallShape. This is
                      how the universal audit-trail constraints are enforced without
                      a single `if tool_name == ...` anywhere in this file.

Known, named limitation: shapes.json is a hand-authored JSON mirror of the sibling
ontology-core piece's `references/shapes-core.ttl`. Nothing here parses Turtle or
SHACL — if shapes-core.ttl changes, a human/agent must update shapes.json to match.
See references/validation-protocol.md for the full contract.

Usage:
  python validate_tool_call.py --tool write_file --args '{"path":"foo.py","content":"..."}'
  echo '{"tool_name":"create_task","arguments":{...}}' | python validate_tool_call.py --stdin

Exits 0 on success, 1 on validation failure. Prints a single JSON object to stdout.
Every call (accepted or rejected) appends one line to .ontology-agent/log.jsonl.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date as _date
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

RUNTIME_DIRNAME = ".ontology-agent"

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------


def _load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"[fatal] malformed JSON in {path}: {exc}")


def load_tools_schema(kg_dir: Path) -> dict[str, Any]:
    return _load_json(kg_dir / "schema" / "tools.json", {})


def load_shapes(kg_dir: Path) -> dict[str, Any]:
    return _load_json(kg_dir / "schema" / "shapes.json", {"shapes": {}})


def load_entities(kg_dir: Path) -> dict[str, Any]:
    """Registry mapping known entity id -> {"type": "<Class>"}, used by sh:class
    checks to resolve a *referenced* entity's asserted type when the reference is
    a bare string (e.g. "alice") rather than an inline {"@id": ..., "@type": ...}
    object.

    Reads this directly out of .ontology-agent/graph.jsonl — the file
    bootstrap.py (and the ongoing propose/validate/execute/commit loop) actually
    populates — rather than a separate `entities.json` that nothing in this skill
    ever wrote. Only entity records ({"kind": "entity", "id": ..., "type": ...})
    contribute; edge records are ignored. See references/validation-protocol.md
    for when this resolves and when it stays empty.

    Absence of graph.jsonl (bootstrap never run) is not an error — inline typed
    references still work without it; only bare-string entity-id lookups come
    back empty until bootstrap or a graph commit has actually recorded that id.
    """
    graph_path = kg_dir / "graph.jsonl"
    entities: dict[str, Any] = {}
    if not graph_path.exists():
        return entities
    try:
        lines = graph_path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return entities
    for lineno, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"[fatal] malformed JSON in {graph_path}:{lineno}: {exc}")
        if rec.get("kind") == "entity" and "id" in rec and "type" in rec:
            entities[rec["id"]] = {"type": rec["type"]}
    return entities


def append_log(kg_dir: Path, entry: dict) -> None:
    log_path = kg_dir / "log.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def make_error(*, path: str, message: str, code: str, suggested_fix: str,
                focus: str | None = None, severity: str | None = None,
                source_shape: str | None = None) -> dict:
    err: dict[str, Any] = {"path": path, "message": message, "code": code,
                            "suggested_fix": suggested_fix}
    if focus is not None:
        err["focus"] = focus
    if severity is not None:
        err["severity"] = severity
    if source_shape is not None:
        err["source_shape"] = source_shape
    return err


# ---------------------------------------------------------------------------
# Layer 1: type / JSON-Schema-subset check
# ---------------------------------------------------------------------------


def type_check(tool_name: str, arguments: dict[str, Any], schema_root: dict[str, Any]) -> list[dict]:
    """Minimal JSON-Schema-like checker (no external dependency).

    Default-deny for unregistered tools: a tool_name absent from
    schema_root["properties"] is REJECTED, not silently passed through. The only
    sanctioned way around gating is an explicit opt-out on the tool's tools.json
    entry: "x-unvalidated": true plus a non-empty "x-unvalidated-reason" string,
    for cases where a project owner has consciously decided a tool (typically
    pure read-only/exploratory) doesn't need the full validator. A tool marked
    x-unvalidated without a reason fails closed (rejected, same as unregistered)
    rather than silently being treated as a valid opt-out.
    """
    errors: list[dict] = []
    tools = schema_root.get("properties", {})

    if tool_name not in tools:
        errors.append(make_error(
            path="tool_name",
            message=f"Tool '{tool_name}' is not registered in .ontology-agent/schema/tools.json",
            code="unregistered_tool",
            suggested_fix=(
                f"Register '{tool_name}' with a schema entry in tools.json, or if it is a "
                'pure read-only/exploratory tool that a project owner has consciously decided '
                'does not need gating, add an entry with "x-unvalidated": true and a non-empty '
                '"x-unvalidated-reason" string explaining why.'
            ),
        ))
        return errors

    tool_schema = tools[tool_name]

    if tool_schema.get("x-unvalidated"):
        reason = tool_schema.get("x-unvalidated-reason")
        if not isinstance(reason, str) or not reason.strip():
            errors.append(make_error(
                path=f"schema.properties.{tool_name}",
                message=(
                    f"Tool '{tool_name}' is marked \"x-unvalidated\": true but has no "
                    'non-empty "x-unvalidated-reason" string'
                ),
                code="unvalidated_missing_reason",
                suggested_fix=(
                    'Add a non-empty "x-unvalidated-reason" string to this tool\'s tools.json '
                    "entry explaining why it is exempt from gating, or remove \"x-unvalidated\" "
                    "and give it a real schema."
                ),
            ))
            return errors
        # Explicit, documented escape hatch: skip type/shape gating for this tool.
        # It still passes through Layer 2's universal ToolCallShape check and is
        # still appended to log.jsonl by the caller -- it is audited, not invisible.
        return errors

    required = set(tool_schema.get("required", []))
    props = tool_schema.get("properties", {})
    additional = tool_schema.get("additionalProperties", True)

    for key in required:
        if key not in arguments:
            errors.append(make_error(
                path=f"arguments.{key}",
                message=f"Missing required property '{key}'",
                code="required",
                suggested_fix=f"Provide a value for '{key}' and retry.",
            ))

    for key, value in arguments.items():
        if key not in props:
            if additional is False:
                errors.append(make_error(
                    path=f"arguments.{key}",
                    message=f"Additional property '{key}' is not allowed",
                    code="additional_properties",
                    suggested_fix=f"Remove '{key}' or extend the tool schema to allow it.",
                ))
            continue
        prop = props[key]
        expected = prop.get("type")
        type_ok = {
            "string": isinstance(value, str),
            "integer": isinstance(value, int) and not isinstance(value, bool),
            "number": isinstance(value, (int, float)) and not isinstance(value, bool),
            "boolean": isinstance(value, bool),
        }
        if expected in type_ok and not type_ok[expected]:
            errors.append(make_error(
                path=f"arguments.{key}",
                message=f"Expected {expected}, got {type(value).__name__}",
                code="type_mismatch",
                suggested_fix=f"Provide a {expected} value for '{key}'.",
            ))
        if "enum" in prop and value not in prop["enum"]:
            errors.append(make_error(
                path=f"arguments.{key}",
                message=f"Value '{value}' not in enum {prop['enum']}",
                code="enum",
                suggested_fix=f"Use one of: {', '.join(map(str, prop['enum']))}.",
            ))
        if "minimum" in prop and isinstance(value, (int, float)) and value < prop["minimum"]:
            errors.append(make_error(
                path=f"arguments.{key}",
                message=f"Value {value} below minimum {prop['minimum']}",
                code="minimum",
                suggested_fix=f"Use a value >= {prop['minimum']}.",
            ))
        if "maximum" in prop and isinstance(value, (int, float)) and value > prop["maximum"]:
            errors.append(make_error(
                path=f"arguments.{key}",
                message=f"Value {value} above maximum {prop['maximum']}",
                code="maximum",
                suggested_fix=f"Use a value <= {prop['maximum']}.",
            ))
        if "minLength" in prop and isinstance(value, str) and len(value) < prop["minLength"]:
            errors.append(make_error(
                path=f"arguments.{key}",
                message=f"String shorter than minLength {prop['minLength']}",
                code="minLength",
                suggested_fix=f"Provide a string of at least {prop['minLength']} characters.",
            ))

    return errors


# ---------------------------------------------------------------------------
# Layer 2: generic SHACL-subset shape evaluator
# ---------------------------------------------------------------------------

_MISSING = object()

_XSD_ALIASES = {
    "http://www.w3.org/2001/XMLSchema#string": "string",
    "http://www.w3.org/2001/XMLSchema#integer": "integer",
    "http://www.w3.org/2001/XMLSchema#decimal": "number",
    "http://www.w3.org/2001/XMLSchema#double": "number",
    "http://www.w3.org/2001/XMLSchema#boolean": "boolean",
    "http://www.w3.org/2001/XMLSchema#dateTime": "dateTime",
    "http://www.w3.org/2001/XMLSchema#date": "date",
}


def _normalize_datatype(name: str) -> str:
    return _XSD_ALIASES.get(name, name)


_DATE_ONLY_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def check_datatype(value: Any, datatype: str) -> bool:
    """sh:datatype — supports string/integer/number/boolean/dateTime/date.

    Booleans are excluded from integer/number checks (Python's bool is a subclass
    of int; SHACL/XSD treat xsd:boolean and xsd:integer as distinct datatypes).

    date vs dateTime: JSON has no literal type tag the way RDF does, so both are
    plain strings. We distinguish them structurally — xsd:date must be a bare
    YYYY-MM-DD with no time component; xsd:dateTime must parse as ISO-8601 with a
    time component (a 'T' or ' ' separator). A dateTime-shaped string therefore
    correctly fails an xsd:date constraint (mirrors property/datatype-001.ttl).
    """
    dt = _normalize_datatype(datatype)
    if dt == "string":
        return isinstance(value, str)
    if dt == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if dt == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if dt == "boolean":
        return isinstance(value, bool)
    if dt == "date":
        if not isinstance(value, str) or not _DATE_ONLY_RE.match(value):
            return False
        try:
            _date.fromisoformat(value)
            return True
        except ValueError:
            return False
    if dt == "dateTime":
        if not isinstance(value, str) or ("T" not in value and " " not in value):
            return False
        try:
            datetime.fromisoformat(value.replace("Z", "+00:00"))
            return True
        except ValueError:
            return False
    # Unknown datatype name: fail closed (cannot verify => treat as violation)
    return False


def resolve_entity_type(value: Any, entities: dict[str, Any]) -> str | None:
    """sh:class support: determine the asserted type of a referenced value.

    Two supported conventions (documented in validation-protocol.md):
      1. Inline typed reference: {"@id": "...", "@type": "Person"}
      2. Bare string id looked up in the optional entities registry.
    """
    if isinstance(value, dict) and "@type" in value:
        return value["@type"]
    if isinstance(value, str) and value in entities:
        return entities[value].get("type")
    return None


def _is_a_or_subclass(actual: str | None, expected: str, entities_root: dict[str, Any]) -> bool:
    if actual is None:
        return False
    if actual == expected:
        return True
    hierarchy = entities_root.get("_classHierarchy", {}) if isinstance(entities_root, dict) else {}
    seen = set()
    frontier = [actual]
    while frontier:
        cls = frontier.pop()
        if cls in seen:
            continue
        seen.add(cls)
        parents = hierarchy.get(cls, [])
        if expected in parents:
            return True
        frontier.extend(parents)
    return False


def node_kind_of(value: Any, entities: dict[str, Any]) -> str:
    """Best-effort mapping of a JSON value onto an RDF term kind.

    - numbers / booleans / null -> Literal
    - dict with @id or @type -> IRI (an inline entity reference)
    - bare string known to the entities registry -> IRI
    - any other bare string -> Literal
    """
    if value is None or isinstance(value, (bool, int, float)):
        return "Literal"
    if isinstance(value, dict):
        return "IRI" if ("@id" in value or "@type" in value) else "BlankNode"
    if isinstance(value, str):
        return "IRI" if value in entities else "Literal"
    return "Unknown"


def _as_list(value: Any) -> list:
    if value is _MISSING:
        return []
    return value if isinstance(value, list) else [value]


def evaluate_property_shape(prop_shape: dict, individual: dict, entities: dict,
                             focus: str, shape_name: str) -> list[dict]:
    path = prop_shape["path"]
    raw = individual.get(path, _MISSING)
    values = _as_list(raw)
    count = len(values)
    violations: list[dict] = []

    if "minCount" in prop_shape and count < prop_shape["minCount"]:
        violations.append(make_error(
            path=path,
            message=f"Property '{path}' has {count} value(s); minCount is {prop_shape['minCount']}",
            code="MinCountConstraintComponent",
            suggested_fix=f"Provide at least {prop_shape['minCount']} value(s) for '{path}'.",
            focus=focus, severity="Violation", source_shape=shape_name,
        ))
    if "maxCount" in prop_shape and count > prop_shape["maxCount"]:
        violations.append(make_error(
            path=path,
            message=f"Property '{path}' has {count} value(s); maxCount is {prop_shape['maxCount']}",
            code="MaxCountConstraintComponent",
            suggested_fix=f"Provide at most {prop_shape['maxCount']} value(s) for '{path}'.",
            focus=focus, severity="Violation", source_shape=shape_name,
        ))

    for v in values:
        if "datatype" in prop_shape and not check_datatype(v, prop_shape["datatype"]):
            violations.append(make_error(
                path=path,
                message=f"Value {v!r} for '{path}' does not have datatype {prop_shape['datatype']}",
                code="DatatypeConstraintComponent",
                suggested_fix=f"Provide a {prop_shape['datatype']} value for '{path}'.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))
        if "class" in prop_shape:
            actual = resolve_entity_type(v, entities)
            if not _is_a_or_subclass(actual, prop_shape["class"], entities):
                violations.append(make_error(
                    path=path,
                    message=f"Value {v!r} for '{path}' does not have class {prop_shape['class']}",
                    code="ClassConstraintComponent",
                    suggested_fix=f"Reference an existing {prop_shape['class']} entity for '{path}'.",
                    focus=focus, severity="Violation", source_shape=shape_name,
                ))
        if "in" in prop_shape and v not in prop_shape["in"]:
            violations.append(make_error(
                path=path,
                message=f"Value {v!r} for '{path}' is not in {prop_shape['in']}",
                code="InConstraintComponent",
                suggested_fix=f"Use one of: {', '.join(map(str, prop_shape['in']))}.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))
        if "nodeKind" in prop_shape and node_kind_of(v, entities) != prop_shape["nodeKind"]:
            violations.append(make_error(
                path=path,
                message=f"Value {v!r} for '{path}' is not of nodeKind {prop_shape['nodeKind']}",
                code="NodeKindConstraintComponent",
                suggested_fix=f"Provide a {prop_shape['nodeKind']}-shaped value for '{path}'.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))
        if "minInclusive" in prop_shape and isinstance(v, (int, float)) and v < prop_shape["minInclusive"]:
            violations.append(make_error(
                path=path,
                message=f"Value {v} for '{path}' below minInclusive {prop_shape['minInclusive']}",
                code="MinInclusiveConstraintComponent",
                suggested_fix=f"Use a value >= {prop_shape['minInclusive']}.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))
        if "maxInclusive" in prop_shape and isinstance(v, (int, float)) and v > prop_shape["maxInclusive"]:
            violations.append(make_error(
                path=path,
                message=f"Value {v} for '{path}' above maxInclusive {prop_shape['maxInclusive']}",
                code="MaxInclusiveConstraintComponent",
                suggested_fix=f"Use a value <= {prop_shape['maxInclusive']}.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))

    return violations


def evaluate_shape(shape: dict, individual: dict, entities: dict,
                    focus: str = "(anonymous)", shape_name: str = "(shape)") -> list[dict]:
    """Evaluate one node shape (its node-level constraints + all property shapes)
    against one JSON individual. Fully generic: driven only by the `shape` dict
    loaded from shapes.json, never by the caller's tool name.
    """
    violations: list[dict] = []

    for prop_shape in shape.get("properties", []):
        violations.extend(evaluate_property_shape(prop_shape, individual, entities, focus, shape_name))

    if "class" in shape:
        actual = individual.get("@type")
        if not _is_a_or_subclass(actual, shape["class"], entities):
            violations.append(make_error(
                path="@type",
                message=f"Node does not have class {shape['class']}",
                code="ClassConstraintComponent",
                suggested_fix=f"Assert rdf:type {shape['class']} on this node, or fix the reference.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))

    if "in" in shape:
        node_id = individual.get("@id", focus)
        if node_id not in shape["in"]:
            violations.append(make_error(
                path="@id",
                message=f"Node {node_id!r} is not in {shape['in']}",
                code="InConstraintComponent",
                suggested_fix=f"Use one of: {', '.join(map(str, shape['in']))}.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))

    if "nodeKind" in shape:
        node_id = individual.get("@id", focus)
        if node_kind_of(node_id, entities) != shape["nodeKind"]:
            violations.append(make_error(
                path="@id",
                message=f"Node {node_id!r} is not of nodeKind {shape['nodeKind']}",
                code="NodeKindConstraintComponent",
                suggested_fix=f"Provide a {shape['nodeKind']}-shaped node.",
                focus=focus, severity="Violation", source_shape=shape_name,
            ))

    if shape.get("closed"):
        allowed = {p["path"] for p in shape.get("properties", [])}
        for key in individual.keys():
            if key in ("@id", "@type"):
                continue
            if key not in allowed:
                violations.append(make_error(
                    path=key,
                    message=f"Property '{key}' is not allowed by closed shape {shape_name}",
                    code="ClosedConstraintComponent",
                    suggested_fix=f"Remove '{key}' or add it to {shape_name}'s allowed properties.",
                    focus=focus, severity="Violation", source_shape=shape_name,
                ))

    return violations


def _shape_for_class(shapes_root: dict, class_name: str) -> tuple[str, dict] | None:
    for shape_name, shape in shapes_root.get("shapes", {}).items():
        if shape.get("targetClass") == class_name:
            return shape_name, shape
    return None


def shape_check(tool_name: str, arguments: dict[str, Any], shapes_root: dict[str, Any],
                 tools_schema: dict[str, Any], entities: dict[str, Any]) -> list[dict]:
    """Layer 2 entry point. Generic: reads tools_schema[tool_name]'s declared
    x-shape-target / x-property-map (data), never branches on tool_name itself.
    """
    violations: list[dict] = []

    # 1) Universal: every tool call is checked as an implicit ToolCall individual.
    tool_call_individual = {
        "@type": "ToolCall",
        "toolName": tool_name,
        "argumentsJson": json.dumps(arguments, sort_keys=True),
        "outcome": "proposed",
    }
    found = _shape_for_class(shapes_root, "ToolCall")
    if found:
        shape_name, shape = found
        violations.extend(evaluate_shape(
            shape, tool_call_individual, entities,
            focus=f"tc:{tool_name}", shape_name=shape_name,
        ))

    # 2) Optional: tool declares which entity class its arguments represent.
    tool_meta = tools_schema.get("properties", {}).get(tool_name, {})
    target_class = tool_meta.get("x-shape-target")
    if target_class:
        found = _shape_for_class(shapes_root, target_class)
        if found:
            shape_name, shape = found
            prop_map = tool_meta.get("x-property-map", {})
            mapped = {"@type": target_class}
            for key, value in arguments.items():
                mapped[prop_map.get(key, key)] = value
            violations.extend(evaluate_shape(
                shape, mapped, entities,
                focus=f"tc:{tool_name}", shape_name=shape_name,
            ))

    return violations


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def validate(tool_name: str, arguments: dict[str, Any], kg: Path) -> dict:
    tools_schema = load_tools_schema(kg)
    shapes_root = load_shapes(kg)
    entities = load_entities(kg)

    type_errors = type_check(tool_name, arguments, tools_schema)
    if type_errors:
        return {
            "ok": False,
            "layer": "type",
            "errors": type_errors,
            "suggested_fix": "Fix the listed type / schema violations and retry.",
        }

    shape_errors = shape_check(tool_name, arguments, shapes_root, tools_schema, entities)
    if shape_errors:
        return {
            "ok": False,
            "layer": "shape",
            "errors": shape_errors,
            "suggested_fix": "Satisfy the shape constraints (cardinality, datatype, class, enum) and retry.",
        }

    return {
        "ok": True,
        "tool_call_id": f"tc_{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f')}",
        "tool_name": tool_name,
        "message": "Type and shape checks passed. Safe to execute.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help=f"Project root containing {RUNTIME_DIRNAME}")
    parser.add_argument("--tool", help="Tool name")
    parser.add_argument("--args", help="JSON object of arguments")
    parser.add_argument("--stdin", action="store_true", help="Read full payload from stdin")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    kg = root / RUNTIME_DIRNAME
    if not kg.exists():
        print(json.dumps({
            "ok": False,
            "layer": "bootstrap",
            "errors": [{
                "path": str(kg),
                "message": f"{RUNTIME_DIRNAME}/ missing — run scripts/bootstrap.py first",
                "code": "not_bootstrapped",
                "suggested_fix": f"Run bootstrap.py --root {args.root} to create {RUNTIME_DIRNAME}/.",
            }],
        }, indent=2))
        return 1

    if args.stdin:
        payload = json.load(sys.stdin)
        tool_name = payload["tool_name"]
        arguments = payload.get("arguments", {})
    else:
        if not args.tool or args.args is None:
            print(json.dumps({
                "ok": False,
                "errors": [{
                    "path": "argv",
                    "message": "Provide --tool and --args, or --stdin",
                    "code": "bad_invocation",
                    "suggested_fix": "Pass --tool <name> --args '<json>' or --stdin with a JSON payload.",
                }],
            }, indent=2))
            return 1
        tool_name = args.tool
        arguments = json.loads(args.args)

    result = validate(tool_name, arguments, kg)
    append_log(kg, {
        "ts": datetime.now(timezone.utc).isoformat(),
        "tool": tool_name,
        "ok": result["ok"],
        "layer": result.get("layer", "shape" if result["ok"] else "unknown"),
    })
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
