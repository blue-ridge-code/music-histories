# Gauntlet Ledger — ontology-agent synthesis

Protocol: `gauntlet/GAUNTLET.md`. Append-only during the run; closing entry at the end.

## Round 0 — Critic calibration

ARTIFACT:   `gauntlet/versions/calibration/artifact/` (copy of ontology-kg-agent draft
            with `TaskShape.priority`'s `sh:minInclusive 1 / sh:maxInclusive 5` removed)
QUESTION:   Does TaskShape actually constrain priority to 1-5?
CRITIC:     fresh general-purpose subagent, given only SKILL.md + shapes-example.ttl
RESULT:     PASS (critic correctly answered NO, quoted the exact missing constraint,
            contrasted with the still-present `status` sh:in enumeration as a working
            example of the same mechanism)
CONCLUSION: Critic isolation and artifact-inspection are real. Proceeding to round 1.

## Split

- **P1 — Ontology core**: seed Turtle ontology + SHACL shapes + competency-question
  discipline for growth. Bar: CIDOC-CRM structural comparison.
  Questions:
  1. Is every class/property in the seed ontology accompanied by a one-line competency
     question it exists to answer (matching CIDOC-CRM's scope-note discipline)?
  2. Does the class hierarchy stay shallow (root + 1-2 levels), avoiding CIDOC-CRM's
     failure mode of nobody understanding an over-deep tree, while still being more
     expressive than a flat bag of untyped nodes?
  3. Is there a documented, concrete procedure for *adding* a class/property (not just a
     prohibition on adding one) — i.e. is evolution deliberate rather than merely rare-by-neglect?
  4. Do the SHACL shapes actually match the ontology's own domain/range declarations
     (no shape drift vs. the T-box)?

- **P2 — Validation gate**: zero-dependency scripts that type-check then shape-check a
  proposed tool call before execution, and validate results after. Bar: SHACL test suite.
  Questions:
  1. For each constraint kind the gate claims to support (minCount/maxCount, datatype,
     class, in, closed, nodeKind), does the gate's verdict match the mirrored SHACL test
     case's expected `sh:ValidationReport` on the same shapes+data?
  2. Does the gate run with zero installed dependencies (stdlib only) as claimed?
  3. Is the error payload for a rejected call specific enough (path + message + fix) that
     a model could repair without re-planning the whole task?
  4. Is it structurally impossible for a mutating tool call to reach execution without
     passing the gate (not just "the docs say to call it first")?

- **P3 — Graph & query layer**: bootstrap/build procedure + documented query patterns.
  Questions:
  1. For each documented query pattern, is it concretely faster/more reliable than the
     equivalent "grep/read N files" alternative, for a project of realistic size?
  2. Does the bootstrap procedure load real structural signals (imports, manifests, git)
     rather than requiring a full LLM extraction pass to get a useful starting graph?
  3. Can a fresh session/different model resume from the graph alone (concretely: what
     file(s) would it read, and is that sufficient)?
  4. Is the instance graph kept separate from the ontology (T-box vs A-box), so the
     ontology can be versioned independently?

- **P4 — SKILL.md + integration**: canonical manifest tying P1-P3 together.
  Questions:
  1. Does frontmatter contain only `name`/`description` (+ allowed optional fields) per
     `docs/agents/skills.md`?
  2. Does the skill explicitly compose with `gauntlet-loop` rather than reimplementing a
     critic/fan-out loop?
  3. Are anti-patterns and success criteria concrete enough to falsify (not vague
     aspirations)?
  4. Would a new model/agent reading only SKILL.md (progressive disclosure) know when to
     activate the skill and what NOT to do, without loading every reference file?

<!-- per-piece round entries follow -->

## P1 — Ontology core

ROUND 1: PASS on all 4 questions. Critic confirmed competency-question comments on all
10 classes/16 properties, flat root+1 hierarchy (flatter than CIDOC-CRM's own 2-level
chains in spots), concrete growth procedure with worked example, and zero shape/ontology
drift on manual cross-check of 5 properties. Builder self-caught and fixed two real
drift bugs during construction (FileShape/:contains vs new :declares; base EntityShape
status enum silently narrowing TaskShape's own enum). No regression, no gap. ACCEPTED.

## P2 — Validation gate

ROUND 1: FAIL. Generic SHACL-subset evaluator confirmed data-driven (no per-tool
branches), rejection payloads confirmed structured (path/message/fix), stdlib-only
confirmed, self-test's per-constraint-kind cases confirmed matching the real mirrored
W3C files (minCount-001.ttl, datatype-001.ttl) — but `selftest_validate.py` exited 1:
`bootstrap.py` never materialized `.ontology-agent/schema/tools.json`/`shapes.json`, so
the documented pipeline was broken end-to-end. GAP: bootstrap/validator seam — no shipped
`shapes.json` seed asset existed for bootstrap to copy.
ROUND 2: Authored `assets/shapes-template.json` (drift-checked against shapes-core.ttl),
wired `bootstrap.py` to copy both seed files. Independent critic re-verified: fix was
*mechanically* correct (manual bootstrap + selftest = exit 0) but selftest still exited 1
on a fresh checkout because nothing invoked bootstrap automatically — same underlying gap
(pipeline not actually self-contained) surfacing in a narrower form. FAIL, not yet a
3-round plateau (2nd occurrence, and the fix each time addressed a real distinct layer of
the same problem rather than repeating verbatim).
ROUND 3: Rewrote the integration smoke test to bootstrap an isolated `tempfile.mkdtemp()`
project itself (subprocess call to bootstrap.py, real seed/content assertions, 3 real
validate() calls including one Layer-1 and one Layer-2 rejection, `finally: rmtree`) —
no dependency on the real repo root or hardcoded path depth. Independent blind
verification: fresh run with zero manual setup, twice in a row, exit 0 both times, no
stray artifacts, confirmed the test body does real work rather than short-circuiting.
PASS. ACCEPTED.

## P3 — Graph & query layer

ROUND 1: PASS on 3 of 4 (real zero-LLM extraction confirmed against this repo's actual
manifest/dirs; query patterns confirmed mapped to populated edges, `blocked_by` honestly
documented as unpopulated rather than faked; T-box/A-box separation confirmed). Question
3 (speed/reliability comparison) came back PARTIAL: mechanism was honest but the example
overstated its win on this repo specifically, which has only one manifest file (near-
degenerate case). Folded into the P2 round-2 fix batch as a one-line doc caveat rather
than spending a dedicated round on a non-blocking gap. ACCEPTED with noted caveat.

## Interim status after wave 1

P1, P2, P3 all ACCEPTED. Proceeding to build P4 (SKILL.md integration) against the now-
stable P1-P3 file layout, per the lead agent's stated sequencing (P4 depends on the other
three's real final shape, so it is built after them rather than in the same wave).

## P4 — SKILL.md integration

ROUND 1: PASS. Canonical frontmatter confirmed, explicit gauntlet-loop composition note
confirmed against the real gauntlet-loop SKILL.md (no reimplemented fan-out/critic
machinery), spot-checked claims (class/comment count, absence of per-tool branching,
selftest function count, blocked_by inertness) all verified against sibling files with
zero overclaiming found. ACCEPTED.

## Wave 1 complete: all four pieces ACCEPTED. Proceeding to absence check + smoothing.

## Absence check (holistic, whole-tree)

Fresh critic reviewed the integrated `.agents/skills/ontology-agent/` tree against all 8
goal properties and both bars, with no per-piece questions. Found 5 real gaps a
decomposed review missed:
1. Unregistered tools silently bypassed the safety gate (Layer 1 allowed anything not in
   `tools.json`) — directly contradicted the deterministic-safety claim. SEVERITY: high.
2. `sh:class` entity-type resolution depended on an `entities.json` nothing ever wrote.
3. `assets/tool-schema-template.json`'s `query_graph` example claimed a SPARQL interface
   that `scripts/query_graph.py` doesn't implement (real interface is fixed subcommands).
4. Skill not yet synced/registered/logged (expected — install step not yet run at time
   of this check).
5. No top-level README.md, inconsistent with the sibling gauntlet-loop skill.

FIX ROUND: addressed 1, 2, 3, 5 in one batch (4 was always slated for the install step).
Fix 1: default-deny for any tool absent from `tools.json`, with an explicit
`x-unvalidated`/`x-unvalidated-reason` opt-out that itself fails closed if the reason is
missing or blank. Fix 2: entity-type resolution now reads `.ontology-agent/graph.jsonl`
directly (the file that's actually populated) instead of a phantom `entities.json`;
subclass-hierarchy matching remains a named, documented gap rather than a silent one.
Fix 3: template corrected to match the real CLI. Fix 5: thin README.md added.

INDEPENDENT VERIFICATION of fix 1 (the safety-critical one): fresh blind critic read the
actual default-deny/fail-closed logic line-by-line, re-ran the full self-test (exit 0),
and independently constructed and ran its own three-case scratch test (unregistered →
rejected; x-unvalidated with empty reason → rejected; x-unvalidated with real reason →
passes). All three matched the claimed behavior exactly. PASS.

## Closing entry

**Pieces passed:** all four (P1 ontology core, P2 validation gate, P3 graph/query layer,
P4 SKILL.md integration), plus one absence-check fix round, plus one independent
re-verification of the highest-stakes fix. No piece plateaued; no regression was ever
logged; no invariant or blast-radius collision occurred; both mirrored bars (W3C SHACL
test suite, CIDOC-CRM/Erlangen OWL) stayed reachable and were actually opened and checked
against on every round that cited them, not assumed from memory.

**Rounds spent:** 1 calibration + 4 first-round builds + 4 first-round critiques + 3
rounds on P2's bootstrap/selftest seam + 1 absence-check critique + 1 fix round + 1
verification round ≈ 15 agent dispatches total, well under the 16-round soft ceiling
stated in the budget.

**What was deliberately left out, and why:** the fan-out/harsh-critic/value-scoring
machinery present in three of the four raw sources (OGAS, the Gemini TS draft, the
deepseek script) was not carried over anywhere — it would have duplicated
`.agents/skills/gauntlet-loop/` and violated the no-new-orchestration-framework
invariant. Full Turtle/SPARQL parsing was deliberately not implemented (would require an
external dependency, violating the zero-runtime-dependency invariant); shapes live
canonically in `references/shapes-core.ttl` and are hand-mirrored into
`assets/shapes-template.json`, a named, documented limitation rather than a hidden one.

**The one thing to attack next with more budget:** subclass-hierarchy-aware `sh:class`
resolution (currently exact-type-match only) and a real Turtle/SHACL parser path for
when `pyshacl`/an MCP RDF server is available, per `references/validation-protocol.md`'s
own "prefer a real engine when present" note — neither was in scope for this run.
