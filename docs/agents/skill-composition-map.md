# skill-composition-map.md — how skills interlock

One place that answers: which skills pair, sequence, or forbid each other, and which are
orthogonal. Consult it before stacking skills, and record new relationships here when a
skill ships or its boundaries change. The registry itself lives in
[`skills.md`](skills.md); this map is about relationships, not availability.

## Composition matrix

| Skill A | Skill B | Relationship | Notes |
|---------|---------|---------------|-------|
| **ontology-agent** | **gauntlet-loop** | **Pairs well** | Gate correctness (ontology) + judge quality (gauntlet). ontology-agent validates every mutating tool call a gauntlet builder proposes; gauntlet-loop never reimplements the validator. Both sides are spelled out in `ontology-agent` SKILL.md Notes. |
| **wayfinder** | **grilling** | **Sequential** | grilling sharpens decisions and feeds them into the wayfinder map. Both are external defaults (mattpocock/skills), not checked in. |
| **language-persona** | (all) | **Orthogonal** | Applies to the output of any skill; no conflicts. It polishes prose, it does not gate or loop. |
| **gauntlet-loop** | **gauntlet-loop** | **Forbidden** | No nested loops — cost explodes and the critic isolation that makes the loop work is lost. |
| **documentation-audit** | **project-gap-analyzer** | **Siblings — run separately** | Both read-only audits with different scopes (doc correctness vs plan-vs-artifact). Stacking them in one pass doubles the surface for no extra signal; run one, act, then the other. |
| **human-review-queue** | (any skill) | **Boundary layer** | Orthogonal to skill choice: it adds a durable human gate to whatever a skill produces. Deploy only for a concrete review workflow. |
| **kickoff** | (all skills) | **Prerequisite** | kickoff selects skills for every phase but installs just-in-time: planning-phase skills now, `handoff` at the first real session boundary, implementation-phase skills at `implementation-ready`. It flips `docs/PROJECT.md` to `planning-active`. Other skills assume it ran; do not run task work before it. |
| **ontology-agent** | **language-persona** | **Orthogonal** | Graph gate and prose polish share nothing; safe to use together. |
| **play-canon** | **gauntlet-loop** | **Pairs well (criteria pack)** | play-canon supplies a criteria pack that gauntlet-loop runs as its L2 layer, after the bar questions pass. The pack contract lives only in `gauntlet-loop`'s `references/criteria-packs.md`, and the criteria live only in `play-canon`'s `sources/`; neither reimplements the other. Invoke as "use play-canon with gauntlet-loop on <goal>". `scripts/tests/test_criteria_packs.py` checks conformance. |
| **play-canon** | **language-persona** | **Orthogonal, with precedence** | `docs/TONE.md` governs the project's own prose. play-canon's style guidance applies to the play experience being designed, not to the project's voice. |

## Anti-patterns

- **Skill A imports Skill B as a file.** If a skill needs another skill's logic, compose
  via documented boundaries (shared queries, file drops, output artifacts) — never import
  and edit the other skill's code or instructions.
- **Multiple trackers.** Never run GitHub Issues and `docs/backlog.md` simultaneously —
  state duplication. One tracker per project, chosen at kickoff
  ([issue-tracker.md](issue-tracker.md)).
- **Nested gauntlet-loops.** A builder inside a loop must not start its own loop; the
  matrix marks this **Forbidden**.
- **Reimplementing a partner's job.** When two skills pair (ontology-agent +
  gauntlet-loop), each supplies its own half and neither reimplements the other's.
- **A second loop inside a criteria pack.** A pack adds critics to a gauntlet-loop run; it
  never runs a loop of its own, and a pack's standalone review stays a single pass.
- **Silent stacking.** Before combining two skills, check this map and the relevant
  SKILL.md Notes; if the pair is unlisted, add it here with the observed relationship.

## Maintenance

- When a skill is added, removed, or re-scoped, update this matrix in the same change and
  reference it from the skill's SKILL.md Notes.
- The quarterly skills audit (`docs/agents/skills.md` → Registry maintenance) re-checks
  this map for accuracy.
