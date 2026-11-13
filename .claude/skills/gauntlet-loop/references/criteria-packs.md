# Criteria packs

A criteria pack is a set of review criteria, supplied by another skill, that a Gauntlet
Loop applies on top of the bar. The bar asks "is ours at least as good as this
reference?" A pack asks "does ours hold up by these standards?" The standards might be
play, accessibility, a house style, or a literary tradition. A pack adds a layer of
critics to the loop. It never adds a second loop.

This file is the contract between the loop and every pack, and the one place that
describes how to build one. The loop's side lives in `../assets/GAUNTLET.md` (layers L2
and L3). A pack skill conforms to the shape below. `play-canon` is the reference
implementation.

## Criteria, not personas

This is the rule that makes packs work. Giving critics a persona produced no measurable
gain over no persona (see `evidence.md`). A role helps only when it carries a different
definition of failure. So a pack holds criteria: each criteria set writes its definition
of failure down directly and draws it from one named source.

The source's name is a label. It tells the owner which tradition a suggested change comes
from, so taste calls are made knowing the source. Critics apply the criteria; nobody
plays the author, the brand, or the expert.

## What a pack provides

At setup, a pack skill writes `gauntlet/packs/<pack>.md` with these sections, in this
order:

1. **Claim.** One or two sentences, in the pack's terms, on what the work is meant to
   be. Critics measure the artifact against the claim, never against a source's personal
   preferences.
2. **Criteria sets.** Each set has seven fields:
   - `Set`: a short label, usually the source's name.
   - `Source`: the text or standard it comes from.
   - `Concepts`: named concepts a critic may cite. This list is what the fidelity check
     (see How the loop uses a pack) tests against.
   - `Criterion`: one positive sentence describing what passing looks like.
   - `Question seeds`: two to four observable questions the lead turns into questions
     specific to each piece.
   - `Misapplied when`: the guard against applying the set where it doesn't belong.
   - `Binding`: `yes` or `advisory`.
3. **Loop checks** (optional). Criteria applied to the ledger rather than the artifact.
   Each check states:
   - **Timing:** `every wave`, `from wave N`, `at plateau`, or `at exit`.
   - **What a FAIL does:** reopen a piece, adjust the process, or propose a change to the
     owner.
4. **Calibration plant.** At least one planted flaw per chosen set, with the concept the
   critic should cite when it catches it.
5. **Excerpts** (optional). Source passages mirrored into `gauntlet/packs/<pack>/`.
   Critics may quote only these.

Size: by default, two to four criteria sets per run across all packs. Each set
multiplies critic cost by pieces × rounds, so going past four needs the owner's
approval.

## How the loop uses a pack

- **Placement.** Pack critics run in round 1 of every piece as a baseline read. After
  that, they run each round once the piece's L0 gates and L1 questions pass.
- **One critic per pack question.** The brief carries the artifact, the claim, one set's
  card, any excerpts, and the one question. It also carries the reference when that bears
  on the question.
- **Verdict.** The standard block, with `LAYER: L2:<pack>/<set>`, a
  `SOURCE: <set>: <concept>` line, and `BINDING`.
- **Fidelity.** A verdict that cites a concept missing from the set's `Concepts` and from
  the excerpts is void.
- **Gap routing.** Binding gaps go to builders carrying their `SOURCE` label, ranked below
  L0 and L1 gaps. Advisory gaps go to `gauntlet/taste.md`.
- **Conflicts.** A pack gap that would break an invariant or lose to the bar goes to the
  owner. When two sets disagree, the pair goes to the owner with both labels. No vote
  settles either.
- **Loop checks.** These run during wave review, at their stated timing.
- **Tally and kill rule.**
  - A *unique catch* is a pack gap the owner confirms that no L1 question or absence
    critic raised for that piece in the same wave.
  - After two waves, drop any set with zero unique catches, unless the owner keeps it for
    a stated reason.
  - The closing entry reports the tally per set.

## Building a pack skill

1. **Name the tradition and pick sources.** Use one source per criteria set, and make
   each set fail differently from the others. Two sets that would flag the same gaps are
   really one set.
2. **Give each source its own file** in the pack skill (`sources/<slug>.md`), so sources
   can be added, corrected, or retired one at a time. The pack's `SKILL.md` indexes them.
   Include a template file so new sources follow the same shape.
3. **Write the criterion positively,** and write the question seeds as things a critic
   can see in the artifact.
4. **Write `Misapplied when`.** Every tradition has places it doesn't reach.
5. **Give the pack a standalone mode** that applies the same criteria and verdict
   discipline as a single review pass. If the tradition supports it, add a guidance mode
   that applies the criteria before anything is built. Most work doesn't deserve a loop.
6. **Record provenance and fidelity:** which parts are summarized from memory and which
   are checked against the text.
7. **Add a row to `docs/agents/skill-composition-map.md`:** `<pack> + gauntlet-loop:
   Pairs well (criteria pack)`.

## Conformance checklist

Run this before a pack's first use and after any edit to it. Every item passes, or the
pack isn't used.

- [ ] Setup writes `gauntlet/packs/<pack>.md` with Claim, Criteria sets, and Calibration
      plant. Loop checks and Excerpts are optional.
- [ ] Every criteria set has all seven fields, a positive `Criterion`, and question seeds
      a critic can answer by looking at the artifact.
- [ ] No set tells a critic to adopt a voice, role, or persona.
- [ ] Every set names its `Concepts`, so the fidelity check can run.
- [ ] Every loop check states its timing and what a FAIL does.
- [ ] Standalone mode uses the same verdict discipline: one question per critic, forced
      choice, evidence paths, and a `SOURCE` line.
- [ ] `docs/agents/skill-composition-map.md` lists the pack.
