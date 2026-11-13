#!/usr/bin/env python3
"""Self-test suite for scripts/validate_tool_call.py's Layer 2 (shape) evaluator.

Zero dependencies (stdlib only). One test per SHACL constraint kind the evaluator
claims to support. Each test is hand-authored JSON (not parsed from Turtle) but is
explicitly modeled on a real W3C SHACL test case under
gauntlet/reference/shacl-test-suite/ — the comment above each test names the exact
file and describes the valid/invalid data-graph individuals it mirrors.

We call evaluate_shape() directly with small ad-hoc shapes that match the shape
described in each W3C file, rather than going through the full tool-call schema,
because the W3C cases are about the generic shape evaluator itself, not about any
particular tool. An end-to-end integration smoke test at the bottom exercises the
full validate() pipeline (Layer 1 + Layer 2 + tools.json/shapes.json on disk) to
prove the pieces compose.

Run: python scripts/selftest_validate.py
Exit 0 = all PASS. Exit 1 = at least one FAIL (prints which, and why).
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_tool_call as vtc  # noqa: E402

_FAILURES: list[str] = []


def check(name: str, condition: bool, detail: str = "") -> None:
    if condition:
        print(f"PASS: {name}")
    else:
        print(f"FAIL: {name}" + (f" — {detail}" if detail else ""))
        _FAILURES.append(name)


def codes(violations: list[dict]) -> set[str]:
    return {v["code"] for v in violations}


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/property/minCount-001.ttl
#
# Real test: PersonShape-firstName has sh:path ex:firstName, sh:datatype
# xsd:string, sh:minCount 1. ex:InvalidPerson has no ex:firstName -> violation
# (MinCountConstraintComponent). ex:ValidResource has ex:firstName "John" ->
# conforms. Expected report: sh:conforms false, one MinCountConstraintComponent
# result focused on ex:InvalidPerson / ex:firstName.
# ---------------------------------------------------------------------------
def test_min_count() -> None:
    shape = {"properties": [{"path": "firstName", "datatype": "string", "minCount": 1}]}

    invalid_person = {}  # mirrors ex:InvalidPerson (no firstName)
    violations = vtc.evaluate_shape(shape, invalid_person, {}, focus="ex:InvalidPerson", shape_name="PersonShape")
    check("minCount-001: InvalidPerson (no firstName) is rejected",
          "MinCountConstraintComponent" in codes(violations), str(violations))

    valid_resource = {"firstName": "John"}  # mirrors ex:ValidResource
    violations = vtc.evaluate_shape(shape, valid_resource, {}, focus="ex:ValidResource", shape_name="PersonShape")
    check("minCount-001: ValidResource (firstName='John') conforms", violations == [], str(violations))


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/property/maxCount-001.ttl
#
# Real test: PersonShape-firstName has sh:maxCount 1. ex:InvalidPerson has TWO
# ex:firstName values ("George", "John") -> violation
# (MaxCountConstraintComponent). ex:ValidResource has exactly one -> conforms.
# ---------------------------------------------------------------------------
def test_max_count() -> None:
    shape = {"properties": [{"path": "firstName", "datatype": "string", "maxCount": 1}]}

    invalid_person = {"firstName": ["George", "John"]}  # two values, like the real InvalidPerson
    violations = vtc.evaluate_shape(shape, invalid_person, {}, focus="ex:InvalidPerson", shape_name="PersonShape")
    check("maxCount-001: InvalidPerson (2 firstName values) is rejected",
          "MaxCountConstraintComponent" in codes(violations), str(violations))

    valid_resource = {"firstName": "John"}
    violations = vtc.evaluate_shape(shape, valid_resource, {}, focus="ex:ValidResource", shape_name="PersonShape")
    check("maxCount-001: ValidResource (1 firstName value) conforms", violations == [], str(violations))


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/property/datatype-001.ttl
#
# Real test: TestShape-dateProperty expects xsd:date, TestShape-integerProperty
# expects xsd:integer. ex:InvalidResource1 has dateProperty typed xsd:dateTime
# (wrong datatype) and integerProperty 11.1 (a decimal, not an integer) ->
# two DatatypeConstraintComponent violations. ex:ValidResource has a proper
# xsd:date value and integer values -> conforms.
# ---------------------------------------------------------------------------
def test_datatype() -> None:
    shape = {"properties": [
        {"path": "dateProperty", "datatype": "date"},
        {"path": "integerProperty", "datatype": "integer"},
    ]}

    invalid_resource = {"dateProperty": "2011-01-01T00:00:00", "integerProperty": 11.1}
    violations = vtc.evaluate_shape(shape, invalid_resource, {}, focus="ex:InvalidResource1", shape_name="TestShape")
    v_codes = codes(violations)
    check("datatype-001: dateTime-shaped value rejected against xsd:date",
          "DatatypeConstraintComponent" in v_codes and
          any(v["path"] == "dateProperty" for v in violations), str(violations))
    check("datatype-001: decimal value rejected against xsd:integer",
          any(v["path"] == "integerProperty" and v["code"] == "DatatypeConstraintComponent" for v in violations),
          str(violations))

    valid_resource = {"dateProperty": "2014-09-01", "integerProperty": 1234}
    violations = vtc.evaluate_shape(shape, valid_resource, {}, focus="ex:ValidResource", shape_name="TestShape")
    check("datatype-001: ValidResource (proper date + integer) conforms", violations == [], str(violations))


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/node/class-001.ttl
#
# Real test: TestShape has sh:class ex:Person, targeting John (type
# MalePerson, a subclass of Person), Quokki (type Animal, unrelated), Someone
# (type Person directly), and Typeless (no type). Expected report: violations
# for Quokki and Typeless only; John and Someone conform.
# ---------------------------------------------------------------------------
def test_class() -> None:
    shape = {"class": "Person"}
    entities = {"_classHierarchy": {"MalePerson": ["Person"], "Animal": []}}

    violations = vtc.evaluate_shape(shape, {"@type": "MalePerson"}, entities, focus="ex:John", shape_name="TestShape")
    check("class-001: John (MalePerson, subclass of Person) conforms", violations == [], str(violations))

    violations = vtc.evaluate_shape(shape, {"@type": "Person"}, entities, focus="ex:Someone", shape_name="TestShape")
    check("class-001: Someone (Person) conforms", violations == [], str(violations))

    violations = vtc.evaluate_shape(shape, {"@type": "Animal"}, entities, focus="ex:Quokki", shape_name="TestShape")
    check("class-001: Quokki (Animal, unrelated class) is rejected",
          "ClassConstraintComponent" in codes(violations), str(violations))

    violations = vtc.evaluate_shape(shape, {}, entities, focus="ex:Typeless", shape_name="TestShape")
    check("class-001: Typeless (no asserted type) is rejected",
          "ClassConstraintComponent" in codes(violations), str(violations))


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/node/in-001.ttl
#
# Real test: TestShape has sh:in (Green Red Yellow). Green/Red/Yellow conform
# (each IS one of the enumerated nodes); ex:InvalidInstance is not in the list
# -> InConstraintComponent violation.
# ---------------------------------------------------------------------------
def test_in() -> None:
    shape = {"in": ["Green", "Red", "Yellow"]}

    for good in ("Green", "Red", "Yellow"):
        violations = vtc.evaluate_shape(shape, {"@id": good}, {}, focus=good, shape_name="TestShape")
        check(f"in-001: {good} is in the enumerated set", violations == [], str(violations))

    violations = vtc.evaluate_shape(shape, {"@id": "InvalidInstance"}, {}, focus="ex:InvalidInstance", shape_name="TestShape")
    check("in-001: InvalidInstance (not in enumerated set) is rejected",
          "InConstraintComponent" in codes(violations), str(violations))


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/node/closed-001.ttl
#
# Real test: MyShape is sh:closed true and only allows ex:someProperty.
# ex:InvalidInstance1 additionally has ex:otherProperty (and an rdf:type
# triple) -> ClosedConstraintComponent violations. ex:ValidInstance1 has only
# ex:someProperty -> conforms.
#
# Simplification (documented in references/validation-protocol.md): our JSON
# mapping treats "@type"/"@id" as structural keys that a closed shape always
# permits, unlike strict SHACL (which would also flag the rdf:type triple
# unless dash:ignoredProperties lists it). We therefore assert on the
# otherProperty violation, which is the unambiguous part of this test case.
# ---------------------------------------------------------------------------
def test_closed() -> None:
    shape = {"closed": True, "properties": [{"path": "someProperty"}]}

    invalid_instance = {"@type": "SomeClass", "otherProperty": 4, "someProperty": 3}
    violations = vtc.evaluate_shape(shape, invalid_instance, {}, focus="ex:InvalidInstance1", shape_name="MyShape")
    check("closed-001: otherProperty (not declared by the shape) is rejected",
          any(v["code"] == "ClosedConstraintComponent" and v["path"] == "otherProperty" for v in violations),
          str(violations))
    check("closed-001: someProperty (declared by the shape) is not itself flagged",
          all(v["path"] != "someProperty" for v in violations), str(violations))

    valid_instance = {"someProperty": 3}
    violations = vtc.evaluate_shape(shape, valid_instance, {}, focus="ex:ValidInstance1", shape_name="MyShape")
    check("closed-001: ValidInstance1 (only someProperty) conforms", violations == [], str(violations))


# ---------------------------------------------------------------------------
# Modeled on gauntlet/reference/shacl-test-suite/node/nodeKind-001.ttl
#
# Real test: IRITestShape has sh:nodeKind sh:IRI. ex:John (an IRI) conforms;
# the literal "true"^^xsd:boolean does not (it is a Literal, not an IRI) ->
# NodeKindConstraintComponent violation.
#
# JSON mapping: a bare string registered in the entities registry is treated
# as an IRI (an entity reference); numbers/booleans/null are always Literal.
# ---------------------------------------------------------------------------
def test_node_kind() -> None:
    shape = {"nodeKind": "IRI"}
    entities = {"john": {"type": "Person"}}

    violations = vtc.evaluate_shape(shape, {"@id": "john"}, entities, focus="ex:John", shape_name="IRITestShape")
    check("nodeKind-001: John (a known entity reference / IRI) conforms", violations == [], str(violations))

    violations = vtc.evaluate_shape(shape, {"@id": True}, entities, focus="true", shape_name="IRITestShape")
    check("nodeKind-001: boolean literal 'true' is rejected as not an IRI",
          "NodeKindConstraintComponent" in codes(violations), str(violations))


# ---------------------------------------------------------------------------
# Default-deny gate (Fix for the absence-check finding: an unregistered tool
# must not silently sail through Layer 1 with zero errors). Not modeled on a
# W3C file -- this is this skill's own headline safety-gate claim.
# ---------------------------------------------------------------------------
def test_unregistered_tool_rejected() -> None:
    schema_root = {"properties": {
        "write_file": {
            "type": "object", "required": ["path"],
            "properties": {"path": {"type": "string"}},
        }
    }}

    violations = vtc.type_check("delete_everything", {"path": "/"}, schema_root)
    check("unregistered tool is rejected at Layer 1",
          any(v["code"] == "unregistered_tool" for v in violations), str(violations))
    check("unregistered-tool error names the tool and both remediation paths",
          any("delete_everything" in v["message"] and "x-unvalidated" in v["suggested_fix"]
              for v in violations),
          str(violations))


def test_x_unvalidated_escape_hatch() -> None:
    schema_with_reason = {"properties": {
        "grep_search": {
            "type": "object",
            "x-unvalidated": True,
            "x-unvalidated-reason": "Pure read-only text search; no state mutation to gate.",
        }
    }}
    violations = vtc.type_check("grep_search", {"pattern": "TODO"}, schema_with_reason)
    check("x-unvalidated tool WITH a reason passes Layer 1 with zero errors",
          violations == [], str(violations))

    schema_missing_reason = {"properties": {
        "grep_search": {"type": "object", "x-unvalidated": True}
    }}
    violations = vtc.type_check("grep_search", {"pattern": "TODO"}, schema_missing_reason)
    check("x-unvalidated tool WITHOUT a reason fails closed (rejected)",
          any(v["code"] == "unvalidated_missing_reason" for v in violations), str(violations))

    schema_blank_reason = {"properties": {
        "grep_search": {"type": "object", "x-unvalidated": True, "x-unvalidated-reason": "   "}
    }}
    violations = vtc.type_check("grep_search", {"pattern": "TODO"}, schema_blank_reason)
    check("x-unvalidated tool with a blank/whitespace-only reason fails closed",
          any(v["code"] == "unvalidated_missing_reason" for v in violations), str(violations))


# ---------------------------------------------------------------------------
# Integration smoke test (not modeled on a single W3C file): exercises the
# full validate() pipeline — Layer 1 type_check + Layer 2 shape_check — against
# a tools.json / shapes.json bootstrapped fresh into an isolated temp
# directory. This proves the generic, data-driven wiring actually composes
# end to end, not just the evaluator in isolation, without assuming a
# .ontology-agent/ already exists anywhere (this self-test is meant to pass
# in any project this skill is copied into, on a clean checkout).
# ---------------------------------------------------------------------------
def test_integration_smoke() -> None:
    scripts_dir = Path(__file__).resolve().parent
    bootstrap_script = scripts_dir / "bootstrap.py"

    tmp_root = Path(tempfile.mkdtemp(prefix="ontology-agent-selftest-"))
    try:
        result = subprocess.run(
            # --force-small: this smoke test deliberately uses an empty temp root
            # (0 modules, 0 manifests) to prove the bootstrap/validate wiring composes
            # end to end -- it is not exercising the module/manifest activation
            # threshold, which has its own dedicated test at
            # scripts/tests/test_ontology_activation.py (repo root).
            [sys.executable, str(bootstrap_script), "--root", str(tmp_root), "--force-small"],
            capture_output=True, text=True,
        )
        check("integration: bootstrap.py runs successfully against a temp root",
              result.returncode == 0, result.stdout + result.stderr)

        kg = tmp_root / ".ontology-agent"
        tools_json = kg / "schema" / "tools.json"
        shapes_json = kg / "schema" / "shapes.json"
        check("integration: bootstrap created schema/tools.json with content",
              tools_json.exists() and tools_json.stat().st_size > 0, str(tools_json))
        check("integration: bootstrap created schema/shapes.json with content",
              shapes_json.exists() and shapes_json.stat().st_size > 0, str(shapes_json))
        if not (tools_json.exists() and shapes_json.exists()):
            return

        good = vtc.validate("create_task", {"name": "Write docs", "status": "open", "priority": 3}, kg)
        check("integration: valid create_task passes both layers", good["ok"] is True, str(good))

        bad_status = vtc.validate("create_task", {"name": "Write docs", "status": "not_a_status"}, kg)
        check("integration: create_task with bad enum status is rejected at Layer 1",
              bad_status["ok"] is False, str(bad_status))

        bad_priority_shape = vtc.validate(
            "create_task",
            {"name": "Write docs", "status": "open", "priority": 3, "assignee": "task-9"},
            kg,
        )
        # "task-9" is a well-typed string (passes Layer 1) that resolve_entity_type()
        # cannot resolve as a Person: it looks up the id in load_entities(), which now
        # reads .ontology-agent/graph.jsonl directly (see references/validation-protocol.md),
        # and no entity "task-9" has ever been committed there in this fresh temp root, so
        # the reference is unresolved. assignee maps to ownedBy (sh:class Person) via
        # x-property-map, so this correctly fails closed at Layer 2 (shape), not Layer 1.
        check("integration: create_task with unresolved/wrongly-typed assignee is rejected at Layer 2 (shape)",
              bad_priority_shape["ok"] is False and bad_priority_shape.get("layer") == "shape",
              str(bad_priority_shape))

        # Fix (absence-check finding): sh:class resolution for bare-string entity refs
        # must come from graph.jsonl, which bootstrap.py actually populates -- not from
        # a never-written entities.json. Prove a real bootstrapped id resolves.
        entities = vtc.load_entities(kg)
        project_id = f"project:{tmp_root.name}"
        check("integration: load_entities() resolves a real bootstrapped entity's type from graph.jsonl",
              entities.get(project_id, {}).get("type") == "Project", str(entities.get(project_id)))

        # Fix (absence-check finding): unregistered tools must be rejected by default,
        # not silently allowed through with zero Layer 1 errors.
        unregistered = vtc.validate("delete_everything", {"path": "/"}, kg)
        check("integration: unregistered tool is rejected end-to-end via validate()",
              unregistered["ok"] is False
              and unregistered.get("layer") == "type"
              and any(e["code"] == "unregistered_tool" for e in unregistered["errors"]),
              str(unregistered))

        # The x-unvalidated escape hatch must actually work through the full CLI path
        # (so the log-append behavior in main() is exercised too), once a project owner
        # has opted a tool out with a documented reason.
        tools_data = json.loads(tools_json.read_text(encoding="utf-8"))
        tools_data["properties"]["grep_search"] = {
            "type": "object",
            "x-unvalidated": True,
            "x-unvalidated-reason": "Pure read-only text search; no state mutation to gate.",
        }
        tools_json.write_text(json.dumps(tools_data), encoding="utf-8")

        log_path = kg / "log.jsonl"
        lines_before = log_path.read_text(encoding="utf-8").splitlines() if log_path.exists() else []

        cli_result = subprocess.run(
            [sys.executable, str(scripts_dir / "validate_tool_call.py"),
             "--root", str(tmp_root), "--tool", "grep_search", "--args", '{"pattern": "TODO"}'],
            capture_output=True, text=True,
        )
        check("integration: x-unvalidated tool with a reason is allowed through the CLI (exit 0)",
              cli_result.returncode == 0, cli_result.stdout + cli_result.stderr)
        try:
            cli_payload = json.loads(cli_result.stdout)
        except json.JSONDecodeError:
            cli_payload = {}
        check("integration: x-unvalidated tool's validate() result is ok:true",
              cli_payload.get("ok") is True, cli_result.stdout)

        lines_after = log_path.read_text(encoding="utf-8").splitlines() if log_path.exists() else []
        check("integration: x-unvalidated tool call is still appended to log.jsonl (audited, not invisible)",
              len(lines_after) == len(lines_before) + 1, f"before={len(lines_before)} after={len(lines_after)}")
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)


def main() -> int:
    tests = [
        test_min_count,
        test_max_count,
        test_datatype,
        test_class,
        test_in,
        test_closed,
        test_node_kind,
        test_unregistered_tool_rejected,
        test_x_unvalidated_escape_hatch,
        test_integration_smoke,
    ]
    for t in tests:
        print(f"\n-- {t.__name__} --")
        t()

    print("\n" + "=" * 60)
    if _FAILURES:
        print(f"FAIL: {len(_FAILURES)} check(s) failed: {_FAILURES}")
        return 1
    print("PASS: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
