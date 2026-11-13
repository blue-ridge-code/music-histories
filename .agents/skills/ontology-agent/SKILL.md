---
name: ontology-agent
description: "Give any agent working in this project a typed knowledge-graph model of project structure plus a deterministic pre-execution gate for tool calls, so structural questions get answered from the graph instead of re-reading files or trusting an LLM's memory of the codebase. Fire when the user asks to remember, model, or map \"the project\" across sessions; wants durable project state that survives a context reset or a switch to a different model; asks to validate, gate, or type-check a tool call's arguments before it executes; asks a structural question like \"what does X depend on,\" \"what does this module contain,\" or \"what would break if I changed Y\"; is building, extending, or growing an ontology, SHACL shapes, or a ToolCall audit trail; or an IDE agent needs cross-session, cross-model memory instead of re-deriving the project's shape every session. Also fire when composing with gauntlet-loop: gate every mutating tool call gauntlet-loop's builders propose through this skill's validator before it runs."
---

# Ontology Agent

## Problem

Without this, an agent re-derives the project's structure — what modules exist, what
depends on what, what's already been decided — by re-reading files every session, and
that re-derivation drifts a little more each time a different model or a fresh context
does it. Tool calls that mutate project state get no check before they run beyond
whatever ad hoc validation the tool itself happens to have, so a malformed argument (a
Task assigned to something that isn't a Person, a `status` value outside the real enum)
reaches execution instead of getting caught first. And an ontology with no growth
discipline accretes speculative classes for things nobody ever queries, until it's a
pile nobody trusts enough to extend carefully.

## Two separate functions — don't conflate them

This skill does two different jobs; keep them separate when deciding what to gate:

1. **Generated structural query/cache** — `bootstrap.py`'s output (`graph.jsonl`,
   queried via `query_graph.py`). Always cheap once bootstrapped; the only question is
   whether bootstrapping was warranted at all (see the threshold below).
2. **Validation of typed domain operations** — `validate_tool_call.py`'s Layer 2 shape
   check, applied only to tool calls whose `tools.json` entry declares `x-shape-target`
   naming a class the shape can meaningfully constrain: task state, dependency edges,
   reviewer routes, deployment configuration. It is not a blanket gate over every tool
   call — the shipped `assets/tool-schema-template.json` only targets `create_task`
   (`Task`) and `write_file`/`edit_file` (`File`); `run_terminal` carries no
   `x-shape-target` at all. Do not add one to a generic Markdown-editing or shell-exec
   tool just because gating is available — reserve `x-shape-target` for tools whose
   arguments really do assert a typed domain fact.

## When to use

- Bootstrapping project memory the first time an agent works in a repo with real
  structure — multiple modules, real dependency manifests — worth graphing. `bootstrap.py`
  enforces this: below 6 real top-level modules and with no real dependency manifest found,
  it prints why and exits `3` without writing anything, instead of leaving the "6+ modules"
  rule as prose an agent might skip. Use `--force-small` for a deliberate, logged exception.
  Support/agent-infrastructure folders (`inbox/`, `gauntlet/`, `sources/`) never count as
  modules — see `SUPPORT_DIR_NAMES` in `bootstrap.py`.
- Before executing any tool call that mutates project or external state: propose it,
  validate it, execute only on a pass.
- Answering "what does X contain," "what depends on X," or "give me the neighborhood
  around X before I touch it" — query the graph instead of grepping or re-reading.
- Adding a genuinely new fact type to the model — but only by running the competency-
  question procedure in `references/growing-the-ontology.md`, never ad hoc.
- Any IDE agent (or a different model picking up the same project later) needs to land
  on the same understanding of the project without starting from zero.

## When NOT to use

- **Too small to be worth it.** A single-file script or a repo with one manifest gets
  almost no benefit — `references/query-patterns.md` says this plainly about its own
  test case: "this template's own repo has exactly one manifest file, so here 'read 1
  file' and 'run one graph query' are nearly the same cost." The payoff scales with
  module count and manifest count, not with wanting to feel organized.
- **Not a quality loop.** This skill gates whether a tool call is well-formed; it has no
  opinion on whether the resulting work is good. For "make this excellent, judged
  against a reference," use `gauntlet-loop` — see Notes for how the two compose.
- **`shapes.json` does not auto-sync with `shapes-core.ttl`.** There is no Turtle/SHACL
  parser here (a deliberate, documented scope cut — see
  `references/validation-protocol.md`). If `shapes-core.ttl` gains a shape or tightens a
  constraint and nobody updates the deployed `.ontology-agent/schema/shapes.json` to
  match, the validator keeps enforcing the old rule and says nothing about the drift.
  Don't rely on this gate where that hand-sync won't actually happen.
- **Not a full SHACL engine.** No `sh:or`/`sh:xone` support — `DecisionShape`'s
  "needs at least one real `dependsOn` or `constrains` edge" rule is written in
  `shapes-core.ttl` but is a known, unenforced gap in `shapes.json` (documented there,
  not silently missing). No automatic supertype-shape composition either: each tool's
  `x-shape-target` selects exactly one shape, so subclass shapes restate what a
  superclass shape would otherwise give for free.
- **Task-blocking queries are inert until something feeds them.** `blocked-by` /
  `blocking` ship in `query_graph.py` but `bootstrap.py` writes no `:blocks` edges from
  a repo scan (there's no manifest that says one task blocks another) — expect empty
  results until an ongoing session actually commits those edges.

## Process

1. **Bootstrap.** `python scripts/bootstrap.py --root .` once per project. Zero LLM
   calls. Below the module/manifest threshold it exits `3` and creates nothing — see
   "When to use" above. Otherwise creates `.ontology-agent/` (copies the ontology/shapes
   references and the tool-schema/shapes templates in, then scans the repo for top-level
   modules and real dependency manifests). The `Project` entity's `status` field is read
   from `docs/PROJECT.md`'s `Status:` line when present and omitted otherwise — never
   hard-coded. Re-run with `--force` after a structural change; without it, an existing
   `graph.jsonl` is never overwritten.
2. **Propose.** Before any tool call that mutates state, state the tool name and
   arguments as you would to run it.
3. **Validate.** Run it through `scripts/validate_tool_call.py` — Layer 1 checks types
   against `.ontology-agent/schema/tools.json`; only on a Layer 1 pass does Layer 2 check
   shape against `.ontology-agent/schema/shapes.json` (every call, plus any tool whose
   entry declares `x-shape-target`). Full contract, error format, and the two-repair-
   attempt escalation rule: `references/validation-protocol.md`.
4. **Execute only on `ok: true`.** A rejection is not a suggestion to retry blindly —
   repair against the specific `path`/`message`/`suggested_fix` returned, twice at most,
   then escalate with the full validation report.
5. **Commit the result to the graph.** Append the new fact(s) as one line each to
   `.ontology-agent/graph.jsonl` (entity and/or edge records, matching the shapes
   `bootstrap.py` already writes) so the next query — this session or a later one — sees
   it without anyone having to re-derive it.
6. **Query instead of re-reading.** For structural questions, use
   `scripts/query_graph.py` (`contains`, `depends-on`, `subgraph`) — see
   `references/query-patterns.md` for what's actually proven against this repo's own
   graph, and its stated limits (direct children only, silently-empty results for facts
   nothing ever recorded).
7. **Grow the ontology only via the documented procedure.** A new class or property
   needs a written competency question, a check that nothing existing already answers
   it, matched Turtle + shape additions with no drift, and a `docs/decisions.md` entry —
   all four steps, every time. Full procedure and a worked example:
   `references/growing-the-ontology.md`.

## Output

```
.ontology-agent/
├── ontology.ttl        # copied from references/ontology-core.ttl
├── shapes.ttl           # copied from references/shapes-core.ttl
├── graph.jsonl          # instance data: one entity/edge record per line, appended to
│                        #   (also the sh:class lookup source for bare-string entity refs)
├── schema/
│   ├── tools.json       # per-tool JSON-Schema-subset + x-shape-target/x-property-map
│   └── shapes.json      # SHACL-subset shape registry (hand-mirrors shapes.ttl)
└── log.jsonl            # one line per validated tool call, accepted or rejected
```

## Notes

**Anti-patterns**

- Don't dump `ontology.ttl`, `shapes.ttl`, or the whole `graph.jsonl` into a prompt —
  query it with `query_graph.py` for the specific question at hand. Flooding context
  with the graph defeats the reason it's structured data instead of prose.
- Don't invent a class or property for a one-off fact. If you can't write the
  competency question from `growing-the-ontology.md` step (a) concretely, the fact
  belongs in `:description` free text or doesn't belong in the graph yet.
- Don't add an `if tool_name == "..."` branch to `validate_tool_call.py` for a new tool
  — that's the exact mistake `references/validation-protocol.md` documents the original
  draft making. Add two lines of JSON (`x-shape-target`, optionally `x-property-map`) to
  `tools.json` instead; the generic evaluator picks it up with no code change.
- Don't edit `shapes-core.ttl` without updating `shapes.json` (and any project's already-
  deployed copy) in the same change — see When NOT to use.
- **Composition with `gauntlet-loop`:** this skill runs no fan-out, no builder/critic
  personas, no scoring loop of its own — that machinery already exists in
  `.agents/skills/gauntlet-loop/`. When a Gauntlet Loop is running, gate every mutating
  tool call each builder proposes through `scripts/validate_tool_call.py` before it
  executes; this skill supplies the deterministic safety gate and durable project graph,
  gauntlet-loop supplies the iterative quality judgment, and neither should reimplement
  the other's job.
- Composition rules for the whole stack live in
  [skill-composition-map](../../../docs/agents/skill-composition-map.md).

**Success criteria** (checkable facts about this skill's actual files, not aspirations)

1. Every constraint kind the shape evaluator claims to support — `minCount`, `maxCount`,
   `datatype`, `class`, `in`, `closed`, `nodeKind` — has a passing test modeled on a real
   W3C SHACL test case (verified: `scripts/selftest_validate.py`, all 8 test functions
   including the end-to-end integration smoke test pass on a clean checkout).
2. A rejected tool call's error always includes `path`, `message`, and `suggested_fix`
   (verified: every violation in `scripts/validate_tool_call.py` is constructed through
   `make_error()`, which requires all three).
3. Zero external runtime dependencies anywhere in the scripts — stdlib only (`json`,
   `re`, `argparse`, `pathlib`, `datetime`, `xml.etree`, `tomllib`), no `pip install`
   (verified: the import blocks at the top of `bootstrap.py`, `query_graph.py`,
   `validate_tool_call.py`, `selftest_validate.py`).
4. Enforcing a new tool's shape requires editing only JSON data — zero new lines in
   `validate_tool_call.py` — because it reads `x-shape-target`/`x-property-map` off
   `tools.json` generically rather than branching on tool name (verified: no
   `if tool_name ==` branch exists anywhere in `scripts/validate_tool_call.py`; the four
   tools in `assets/tool-schema-template.json` are enforced entirely through that data).
5. `bootstrap.py` records real, checkable facts with zero LLM calls: `dependsOn` edges
   come from actually parsing `package.json`/`requirements.txt`/`pyproject.toml`/
   `go.mod`/`*.csproj`, `contains` edges from an actual top-level directory walk
   (verified against this repo in `references/query-patterns.md` §1–2, e.g. `depends-on
   module:inbox` returning the real names `pydantic-ai`, `pydantic`, `httpx`).
6. Every class in `references/ontology-core.ttl` carries an `rdfs:comment` phrased as
   the competency question it answers, not a restatement of its label (verified:
   11/11 classes in the file).
7. A query pattern is written up in `references/query-patterns.md` as proven only once
   some path actually populates the edge it reads — `blocked_by`/`blocking` ship in
   `query_graph.py` but are explicitly excluded from the documented patterns because
   `bootstrap.py` writes no `:blocks` edge (verified: query-patterns.md's "Cut" section).
8. Every validated tool call — accepted or rejected — appends exactly one line to
   `.ontology-agent/log.jsonl` (verified: `append_log()` is called exactly once per
   `main()` invocation in `scripts/validate_tool_call.py`).
