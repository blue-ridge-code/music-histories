---
name: play-canon
description: "Apply the Play Canon, literature-based play criteria labeled by source (Huizinga, Caillois, Sutton-Smith, Bateson, Csikszentmihalyi, Nachmanovitch, Carse, Leonard, Illich), to work whose quality includes how it plays or engages: games, toys, playful products, learning experiences, events, and writing meant to hold a reader. Use it for design guidance before building, for a source-labeled review of a draft, or as a criteria pack for gauntlet-loop. Fires on Play Canon, play-canon, or a canon author named as a standard."
---

# Play Canon

The Play Canon is a library of texts on play. Each source file turns one text into usable
material:

- design moves for interactions, structures, content, and style;
- anti-patterns: what the text warns against;
- a review criterion, with question seeds.

The skill draws on the library in three modes. **Guide** works before or while building.
**Review** is one pass on a draft. **Pack** supplies criteria to `gauntlet-loop`.

Author names are labels, not personas. Each one marks which tradition a suggestion or
finding comes from, so the owner can weigh it knowing the source. The agent applies the
criteria; it never speaks as the author or guesses what the author would think.

## Problem

Play-shaped work fails in ways correctness checks miss: rules that leak, feedback that
lags, a "learning game" that is a quiz in costume, a toy with nothing to come back to.
Good play also comes from moves that are easy to miss. The canon names both, with a
traceable source for each.

## When to use

- Designing or improving games, toys, playful products, learning experiences, events,
  interactive fiction, or creative practice.
- Writing meant to engage or hold a reader, using the subset of sources that fit prose.
- The user names the Play Canon, play-canon, or a canon author as a standard.
- A `gauntlet-loop` run on play-shaped work, as a criteria pack.

## When not to use

- Work judged only on correctness (an API, a form, a migration). There is no experience
  to measure against.
- Settling a question on one author's authority. Sources label traditions; the owner
  decides between them.

## Sources

Read only the files you choose. Each file's **Fit** and **Misapplied when** sections say
when to leave it out.

| Set | File | Asks | Guidance is strongest on |
|---|---|---|---|
| Huizinga | `sources/huizinga-homo-ludens.md` | Does the play-world hold? | Structures, interactions |
| Caillois | `sources/caillois-man-play-and-games.md` | What kind of play is it, and is the mix coherent? | Interactions, structures |
| Sutton-Smith | `sources/sutton-smith-ambiguity-of-play.md` | Does the stated purpose match the play delivered? | Structures, content |
| Bateson | `sources/bateson-theory-of-play-and-fantasy.md` | Is "this is play" signaled and kept? | Interactions, style |
| Csikszentmihalyi | `sources/csikszentmihalyi-flow.md` | Are goals, feedback, and challenge right, moment to moment? | Interactions, structures |
| Nachmanovitch | `sources/nachmanovitch-free-play.md` | Is it still alive? | Interactions, style |
| Carse | `sources/carse-finite-and-infinite-games.md` | Does it invite continuing? | Structures, interactions |
| Leonard | `sources/leonard-mastery.md` | Does it reward practice past the plateau? | Structures, content |
| Illich | `sources/illich-deschooling-society.md` | Is the measure standing in for the thing? | Structures, interactions |

For writing, Nachmanovitch, Csikszentmihalyi, Illich, Bateson, and Carse usually fit.
Caillois and Leonard rarely do.

## Process

### Step 1 — Fix the claim and choose sources (every mode)

1. **Read the work,** or the brief if nothing is built yet.
2. **Draft the claim:** one or two sentences, in canon terms, on what kind of play or
   engagement the work is meant to offer. For writing, the claim is the experience the
   reader should have.

   Example: "Mimicry and ilinx (Caillois), toward paidia; the imaginary rhetoric
   (Sutton-Smith); something you come back to, not a one-shot (Carse)."
3. **Propose sources.** Pick two to four whose guidance or failures matter most here,
   with a one-line reason each.
4. **Confirm** the claim and the sources with the user. Then read only those source
   files.

Everything that follows measures against the claim, never against an author's personal
taste.

### Mode A — Guide (before or while building)

From each chosen source's **Guidance** and **Anti-patterns**, take the moves that fit
the claim and turn them into a design brief for this work:

- **Interactions:** what the player does, and how the work responds.
- **Structures:** sessions, progression, boundaries, and how the pieces fit.
- **Content:** what fills the structure.
- **Style:** tone, look, sound, and voice.
- **Avoid:** anti-patterns that are a live risk for this work.
- **Tensions:** places where two sources pull in opposite directions, written as choices
  for the owner.

Rules:

- Every item is a concrete move for *this* work, tagged `[Source: concept]`. Restated
  theory doesn't count as a move.
- Include a category only when a chosen source has something specific to say about it.
- At most five items per category. Keep the ones that most change the work.
- State tensions as choices; leave resolving them to the owner. Caillois's ludus against
  Nachmanovitch's free improvisation is a design choice, not an error. Start from the
  **Tension** and **Overlaps** lines in the chosen sources' **Fit** sections.

### Mode B — Review (one pass on a draft)

1. For each chosen source, turn its question seeds into one to three questions specific
   to the artifact.
2. Answer each question against the real artifact: play it, render it, run it, read it.
   If the harness has subagents, give each question to a fresh critic with only the
   artifact, the claim, that source's **Review criterion**, and the question. Otherwise,
   answer each question on its own, looking only at the artifact.
3. Record one block per question:

   ```
   QUESTION:  <one question>
   SOURCE:    <set: concept>
   RESULT:    PASS | FAIL
   EVIDENCE:  <where in the artifact>
   GAP:       <one gap, observable in the artifact, or "none">
   MOVE:      <one move from that source's Guidance that would close the gap, or "none">
   ```

4. A finding whose concept isn't in the source file's **Concepts** list is void; drop it.
5. Summarize: failed questions ranked by how much they undercut the claim, then tensions
   for the owner.

### Mode C — Pack (with gauntlet-loop)

Follow `gauntlet-loop`'s `references/criteria-packs.md`. Write `gauntlet/packs/play-canon.md`
with these sections:

- **Claim:** from Step 1.
- **Criteria sets:** copy each chosen source's **Review criterion**, and set `Binding` to
  the source's default unless the owner changes it.
- **Loop checks:** copy every source file's **Loop check** section (today: Illich,
  Leonard, and Carse), with its timing. They run on the loop itself, even when those
  sources aren't among the chosen criteria sets.
- **Calibration plant:** copy each chosen source's **Calibration plant**.
- **Excerpts:** if the user supplies passages from the books, save them under
  `gauntlet/packs/play-canon/` and list them here.

Keep to two to four criteria sets unless the owner approves more. Every set multiplies
critic cost.

## Adding a source

1. Copy `sources/_TEMPLATE.md` to `sources/<author>-<short-title>.md`.
2. Fill every section, and record fidelity in **Fidelity**, **Checked against**, and
   **Verify**. Give each concept checked against the text its page number.
3. Check that it fails differently from every existing source. If it would flag the same
   gaps as an existing source, merge it into that file instead.
4. Add a row to the Sources table above.
5. Run the conformance checklist in `gauntlet-loop`'s `references/criteria-packs.md`.

## Output

- **Guide:** a design brief covering the categories that apply, plus Avoid and Tensions.
  Every item carries a `[Source: concept]` tag.
- **Review:** one block per question, plus a ranked summary of the failures, with moves.
- **Pack:** `gauntlet/packs/play-canon.md`, passing the criteria-pack conformance
  checklist.
- **In every mode:**
  - every item names a source and a concept from that source's file;
  - an item citing a concept that has no page number in its file (not yet traced to the
    text) carries `(unchecked)` after the concept, e.g. `[Caillois: Agôn (unchecked)]`;
  - nothing is quoted except text the user supplied.

## Notes

- **Composition.** Pairs with `gauntlet-loop` as a criteria pack. With `language-persona`,
  the project's tone profile governs the project's own prose; canon style guidance
  applies to the play experience being designed. Both relationships are recorded in
  `docs/agents/skill-composition-map.md`, in repositories that ship it.
- **Why criteria, not personas.** Giving critics personas produced no measurable gain in
  the studies behind `gauntlet-loop` (see its `references/evidence.md`). What a source
  can add is a different definition of failure, so each file writes that definition
  down as a criterion and labels it with its source.
- **Fidelity.** Each source file's **Fidelity** line says what has been checked against
  the text, with page numbers, and **Checked against** names the edition. A file not
  yet checked says it was summarized from general knowledge. **Verify** lists what
  still needs the text. Update all three together when a file is checked.
