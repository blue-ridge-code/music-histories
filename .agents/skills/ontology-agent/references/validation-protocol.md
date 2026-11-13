# Validation Protocol

Contract between the model (or any calling agent) and `scripts/validate_tool_call.py`.
Every tool call that mutates project or external state passes through this gate before
it may execute.

## Input to Validator

```json
{
  "tool_name": "string",
  "arguments": { ... },
  "context": {
    "project_root": "string",
    "current_graph_snapshot_id": "optional string"
  }
}
```

## Layer 1 — Type / Schema Check

- Source of truth: `.ontology-agent/schema/tools.json` (a JSON-Schema subset — no
  external `jsonschema` dependency; the checker in `validate_tool_call.py:type_check`
  covers `required`, `type`, `enum`, `minimum`/`maximum`, `minLength`, and
  `additionalProperties`).
- **Default-deny for unregistered tools.** A `tool_name` that does not appear under
  `tools.json`'s `properties` is **rejected**, not silently allowed through — the
  headline claim of this skill ("invalid actions are caught before execution") would
  be false for any tool nobody remembered to schema. Rejection looks like:

  ```json
  {
    "ok": false,
    "layer": "type",
    "errors": [
      {
        "path": "tool_name",
        "message": "Tool 'delete_everything' is not registered in .ontology-agent/schema/tools.json",
        "code": "unregistered_tool",
        "suggested_fix": "Register 'delete_everything' with a schema entry in tools.json, or if it is a pure read-only/exploratory tool that a project owner has consciously decided does not need gating, add an entry with \"x-unvalidated\": true and a non-empty \"x-unvalidated-reason\" string explaining why."
      }
    ],
    "suggested_fix": "Fix the listed type / schema violations and retry."
  }
  ```

- **The escape hatch.** A tool that genuinely doesn't need gating (typically a pure
  read-only/exploratory tool — see the "don't run the full validator on pure
  read-only exploratory calls" anti-pattern in `SKILL.md`) is still declared in
  `tools.json`, but with:

  ```json
  "grep_search": {
    "type": "object",
    "x-unvalidated": true,
    "x-unvalidated-reason": "Pure read-only text search across the workspace; no state mutation for the gate to check."
  }
  ```

  `"x-unvalidated": true` skips the `required`/`type`/`enum`/etc. checks for that
  tool's arguments entirely, and Layer 2 runs against it exactly as it would for any
  other tool (the universal `ToolCallShape` check still applies; no `x-shape-target`
  applies unless one is declared). The call is still appended to `log.jsonl` like
  every other call — the opt-out is deliberate and audited, not invisible. A tool
  marked `x-unvalidated` **without** a non-empty `x-unvalidated-reason` string fails
  closed: it is rejected with `code: "unvalidated_missing_reason"`, exactly as if it
  were unregistered. The escape hatch only takes effect when both keys are present
  and correctly typed — see `assets/tool-schema-template.json`'s
  `x-unvalidated-escape-hatch-example` for a worked, documentation-only example.
- Failures return immediately, without reaching Layer 2:

```json
{
  "ok": false,
  "layer": "type",
  "errors": [
    {
      "path": "arguments.status",
      "message": "Value 'in_review' not in enum ['open', 'in_progress', 'blocked', 'done', 'cancelled']",
      "code": "enum",
      "suggested_fix": "Use one of: open, in_progress, blocked, done, cancelled."
    }
  ],
  "suggested_fix": "Fix the listed type / schema violations and retry."
}
```

## Layer 2 — Shape Check (generic, data-driven — not per-tool code)

This is the layer the original draft got wrong: it hardcoded `if tool_name ==
"create_task": ...` / `if tool_name == "write_file": ...` branches, which meant every
new tool needed a matching new `if` — no actual shape was ever read, so any shape the
author didn't specifically anticipate was silently unenforced.

Instead, `validate_tool_call.py`'s Layer 2 is a **generic shape evaluator**
(`evaluate_shape` / `evaluate_property_shape`) that walks shape definitions loaded from
`.ontology-agent/schema/shapes.json` at runtime. It supports, for any shape, without any
per-tool branch in the code:

| Constraint | Meaning |
|---|---|
| `sh:minCount` / `maxCount` | cardinality of a property's values |
| `sh:datatype` | `string`, `integer`, `number`, `boolean`, `dateTime`, `date` |
| `sh:class` | the referenced entity's asserted type (or a registered subclass) |
| `sh:in` | value (or node) must be one of an enumerated set |
| `sh:closed` | no properties beyond those declared by the shape |
| `sh:nodeKind` | `IRI` (an entity reference) vs `Literal` (a plain value) |
| `sh:minInclusive` / `maxInclusive` | numeric range |

Two pieces of **data** (not code) connect a tool call to a shape:

1. **Every tool call** is always checked as an implicit `:ToolCall` individual
   (`{toolName, argumentsJson, outcome: "proposed"}`) against whichever shape in
   `shapes.json` declares `"targetClass": "ToolCall"`. This is unconditional and
   uniform across every tool — it is how the universal audit-trail shape gets
   enforced without special-casing any tool name.
2. **Optionally**, a tool's entry in `tools.json` may declare
   `"x-shape-target": "<Class>"` to say "these arguments represent an instance of
   `<Class>`" (e.g. `write_file` → `File`, `create_task` → `Task`), and
   `"x-property-map": {"jsonKey": "ontologyProperty"}` when an argument name differs
   from the ontology property path it fills (e.g. `create_task`'s `assignee` argument
   maps to the `ownedBy` property, which is what `TaskShape` actually constrains).

Adding a new tool that should be shape-checked means **adding two lines of JSON**
(`x-shape-target`, optionally `x-property-map`) to `tools.json` — never adding an `if`
to `validate_tool_call.py`. A shape the author never anticipated is still enforced, as
long as it is declared in `shapes.json` and targeted by a tool's `x-shape-target`.

Failure format (mirrors a SHACL validation result):

```json
{
  "ok": false,
  "layer": "shape",
  "errors": [
    {
      "focus": "tc:create_task",
      "path": "ownedBy",
      "message": "Value {'@type': 'Task'} for 'ownedBy' does not have class Person",
      "code": "ClassConstraintComponent",
      "suggested_fix": "Reference an existing Person entity for 'ownedBy'.",
      "severity": "Violation",
      "source_shape": "TaskShape"
    }
  ],
  "suggested_fix": "Satisfy the shape constraints (cardinality, datatype, class, enum) and retry."
}
```

## Success

```json
{
  "ok": true,
  "tool_call_id": "tc_20260809071200123456",
  "tool_name": "create_task",
  "message": "Type and shape checks passed. Safe to execute."
}
```

Only after `ok: true` may the tool be executed.

## Named Limitation: `shapes.json` / `shapes-core.ttl` Sync Gap

`shapes.json` is a **hand-authored JSON structural mirror** of the ontology-core
sibling piece's `references/shapes-core.ttl`. Writing a zero-dependency Turtle/SHACL
parser was ruled out of scope (no good pure-stdlib option exists), so nothing in this
repository parses `shapes-core.ttl` — `shapes.json` is read directly instead.

This means:

- If `shapes-core.ttl` gains a new shape, tightens a constraint, or renames a property,
  **a human or agent must manually update `shapes.json` to match**. There is no
  automated check that the two files agree.
- Until that sync happens, the validator enforces whatever `shapes.json` currently
  says — which may be stale relative to the "real" ontology.
- This is a real, load-bearing limitation, not a hidden gap: any process that edits
  `shapes-core.ttl` should treat updating `shapes.json` as part of the same change.

A secondary, smaller simplification: JSON has no literal-datatype tag the way RDF
does, so `sh:datatype` distinguishes `date` from `dateTime` structurally (a bare
`YYYY-MM-DD` vs. a string with a time component) rather than from an attached type.
Similarly, `sh:closed` treats the JSON-LD-style `@type`/`@id` keys as always-permitted
structural keys, not data properties a closed shape must separately allow — this
differs from strict SHACL, which would also flag an untyped `rdf:type` triple under
`sh:closed` unless `dash:ignoredProperties` listed it.

A third simplification: real SHACL's `sh:targetClass` applies a shape to a node's
class *and every subclass of it* — `shapes-core.ttl` leans on this (a `Task`, being
`rdfs:subClassOf :Entity`, must satisfy `EntityShape`'s `:name` constraint via
inheritance, and `TaskShape` itself does not restate `:name`). This evaluator does not
implement automatic supertype-shape composition — each tool's `x-shape-target` selects
exactly one shape. `shapes.json` therefore keeps each shape **self-contained**,
restating constraints like `:name` directly on `TaskShape` rather than relying on
`EntityShape` inheritance, so nothing silently goes unenforced. This is a real
divergence from `shapes-core.ttl`'s structure, not just its serialization — worth
re-checking whenever `shapes-core.ttl` adds a new subclass-only constraint.

## Named Limitation: `sh:class` Resolution for Bare-String Entity References

`sh:class` needs to know a *referenced* entity's asserted type. Two conventions are
supported:

1. **Inline typed reference** — `{"@id": "task-9", "@type": "Task"}`. This always
   works, unconditionally, with no dependency on any file on disk.
2. **Bare string id** — `"task-9"`. This requires a lookup: `resolve_entity_type()`
   calls `load_entities()`, which reads entity type records directly out of
   `.ontology-agent/graph.jsonl` (the file `bootstrap.py` and the ongoing
   propose/validate/execute/commit loop actually populate — see `SKILL.md`'s
   Process step 5). There is exactly one source of truth for "what type is entity
   X"; there is no separate `entities.json` file (an earlier draft of this script
   read one, but nothing ever wrote it, so `sh:class` checks against bare-string
   references silently could never resolve — that dead path has been removed, not
   worked around).

This means bare-string `sh:class` resolution is **resolved, with one plain
condition**: it only sees ids that have actually been recorded as
`{"kind": "entity", "id": ..., "type": ...}` lines in `graph.jsonl`. Concretely:

- After `bootstrap.py` has run, ids like `project:<name>`, `module:<name>`, and
  `dependency:<ecosystem>:<name>` resolve correctly (their types come straight from
  the repo scan).
- An id that only exists because an agent's own work created it (e.g. a `Task` or
  `Person` an agent proposes) resolves only **after** that entity has been
  committed to `graph.jsonl` per Process step 5 — the same "not populated until
  something writes it" honesty already documented for `:blocks` edges in
  `references/query-patterns.md`. Before that commit, the reference is unresolved
  and `sh:class` correctly reports a violation (it fails closed, not open).
- **Still a real gap, not fixed by this change:** subclass matching
  (`_is_a_or_subclass`'s walk over an `entities_root["_classHierarchy"]` map) has no
  populator anywhere in this skill. `graph.jsonl` records an entity's own asserted
  type only, never a class hierarchy. A `sh:class` check therefore only succeeds on
  an **exact** type match today; a value asserted as a subclass of the expected
  class will incorrectly fail until something populates `_classHierarchy`.

## Repair Contract

- On a Layer 1 or Layer 2 rejection, the calling agent may attempt to repair the
  arguments and resubmit.
- **Maximum two automatic repair attempts** per original tool call before escalating
  to the user or a higher-level planner with the full validation report. The validator
  itself is stateless per invocation — the calling agent is responsible for counting
  its own repair attempts and stopping at two.
- Escalation should include: the original proposed call, both repair attempts and
  their error payloads, and a plain-language summary of what constraint keeps failing.

## Audit Log

Every accepted or rejected call appends one line to `.ontology-agent/log.jsonl`:

```json
{"ts":"2026-08-09T07:12:00+00:00","tool":"write_file","ok":true,"layer":"shape"}
```

## Implementation Notes

- Zero external dependencies: pure Python 3 stdlib (`json`, `re`, `datetime`,
  `pathlib`, `argparse`). No `pip install`, no `rdflib`, `jsonschema`, or `pyshacl`.
- When an MCP SHACL/RDF server is present, prefer it; otherwise fall back to this
  script.
- Keep error messages short, machine-parseable, and actionable so the model can
  repair without re-planning the whole task.
