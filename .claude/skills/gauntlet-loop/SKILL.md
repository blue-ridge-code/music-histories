---
name: gauntlet-loop
description: "Set up and run a Gauntlet Loop — an agent workflow that splits work into independently judgeable pieces, gives each piece a builder and separate fresh-context critics, and compares the real output against a named real-world reference until it wins. Use this whenever the user wants something to come out excellent rather than merely finished: \"make this actually good\", \"best in class\", \"production quality\", \"as good as a named thing\", \"keep improving it until\". Also use whenever they mention gauntlet loop, fanning out subagents, blind critics, /loop, evaluator-optimizer, or looping an agent against a quality bar; when a previous run produced something adequate they now want pushed much further; and when another skill supplies criteria to loop against (a criteria pack such as play-canon)."
---

# Gauntlet Loop

A Gauntlet Loop makes an agent keep working against a standard it cannot argue with. The
lead agent splits a goal into pieces that can be judged separately. Each piece gets a
builder and separate critics with fresh context. Each critic opens the real artifact,
answers one question against a named real reference, and either passes it or names the
single biggest gap and sends it back. Repeat until an exit condition fires.

Credit: the pattern and the name are Matt Shumer's (somethingbig.ai/gauntlet-loop,
github.com/mshumer/Claude-of-Duty). It sits on the evaluator-optimizer workflow from
Anthropic's "Building Effective Agents". This skill adds the parts that decide whether a
long run produces something good or just something expensive:

- deterministic gates before any model judge;
- current practice for briefing and isolating subagents;
- an owner queue for taste calls;
- criteria packs: extra review layers supplied by other skills.

## Don't loop this

A loop costs hours and multiplies token spend by the number of builder-critic pairs. It
earns that on work where the difference between good and excellent is worth real money
or real reputation, and where you can leave it running.

Skip it for anything under an hour of ordinary agent work, anything you need in the next
ten minutes, anything with one obviously correct answer, and anything where you cannot
name what better would look like. For those, one good prompt and a review is the whole
job. A criteria pack's standalone review mode covers that case without a loop.

## Run the gate first

**1. Direction is locked, or genuinely open.** This is the fork that matters.

- If correctness is defined *outside* the model's taste (a brand system, an API
  contract, a spec, a house style, a client brief), write that down first and lock it.
  Otherwise the loop optimizes hard toward the bar and away from the brief. The
  documented version of this: a landing-page loop produced a striking site that matched
  nothing about the brand's actual design system.
- If the goal is genuinely open, a blank page is fine. Claude of Duty started from
  nothing. Do not impose an MVP requirement on green-field creative work.

**2. The output is inspectable.** The critic must open the real thing: render the page,
run the code, execute the tests, read the draft. Work that can only be judged by its
author's description cannot be gauntleted.

**3. The reference is real and reachable.** See `references/bar-selection.md`.

If the gate fails, produce the missing thing first, then come back.

## Step 1 — Fix the inputs

Ask only for what you cannot infer, then state all of them back before writing anything.

**Goal** — the destination, not the route. No architecture, no decomposition, no round
count. The lead agent decides those; that latitude is where the method's quality comes
from.

**Bar** — one named, fetchable, comparable reference. Not "award-winning design" but a
specific page, repo, post, test suite, or benchmark number. It does not need to be
reachable; it needs to be real, and out of reach is better than achievable. Read
`references/bar-selection.md`, then offer two or three and let the user pick. The bar is
where their taste enters the system and the only place it does.

Alongside it, sketch the kind of questions a critic will answer against that reference.
The lead agent writes the final per-piece questions, but if you cannot draft two good
ones now, the bar is probably too vague to judge against.

**Invariants** — what the loop may not trade away in pursuit of the bar: brand palette,
API contract, reading level, word count, license, accessibility floor, dependency ban.
Nobody supplies these unprompted, so ask. A loop with a bar and no invariants wins the
comparison and loses the brief. Where an invariant can be checked by a script or a
count, say so: it becomes an L0 gate.

**Blast radius** — what the loop is allowed to touch. It runs unattended for hours with
tool access. Default: work on a branch, in a working directory, with no irreversible or
outward-facing actions. Nothing is deployed, published, sent, purchased, or deleted
outside its own tree. Anything beyond that is an explicit allowlist the user states now,
not a judgement call the agent makes at 2am. Say this out loud even when it seems
obvious.

**Budget** — wall-clock, spend, or round ceiling, fixed before launch. An unbounded loop
is a cost decision made by an agent instead of by the user.

**Owner** — the named human who rules on taste calls and confirms pack catches. The loop
parks those calls in `gauntlet/taste.md` and keeps working other pieces rather than
stopping to wait. Default: the user.

**Criteria packs** (optional) — review criteria that another skill supplies on top of the
bar, such as `play-canon`. A pack adds a layer of critics, not a second loop. Load the
pack skill, run its setup to get the pack's claim and chosen criteria sets, and confirm
both with the user. How packs plug in, and how to build one:
`references/criteria-packs.md`.

## Step 2 — Write the files

Into the target project:

- **`gauntlet/GAUNTLET.md`** — the protocol the lead agent follows. Copy
  `assets/GAUNTLET.md` and fill in Goal, Bar, Invariants, Blast radius, Budget, Owner,
  and Criteria packs. Do not paraphrase the protocol; it is load-bearing.
- **`gauntlet/ledger.md`** — a header and nothing else. The lead agent appends.
- **`gauntlet/taste.md`** — a header and nothing else. Owner calls wait here.
- **`gauntlet/packs/<pack>.md`** — one per criteria pack, written by the pack's skill in
  the shape set out in `references/criteria-packs.md`. Mirrored source excerpts go in
  `gauntlet/packs/<pack>/`.
- **Agent definitions**, where the harness supports them (`references/harness-map.md`).

Keeping the protocol in a file rather than in the launch prompt matters. The method works
partly because the prompt is short and leaves the agent room. A 900-word launch prompt
buries the goal; a short prompt pointing at a protocol file gets both.

## Step 3 — Emit the launch prompt

One short prompt to paste into a fresh session, roughly 150–200 words. Adapt the harness
verbs using `references/harness-map.md`. Drop the bracketed pack clause when there are no
packs.

```
Build [GOAL].

The bar is [BAR]. It is mirrored in ./gauntlet/reference/. Compare against the real
files, not your memory of them.

Read ./gauntlet/GAUNTLET.md first and follow it exactly. You orchestrate; subagents
build and judge. Break the goal into the smallest pieces that can be improved and
judged separately — you decide the split. For each piece, brief a builder and fresh
critics cold: deterministic gates first, then the bar questions[, then the criteria
packs in ./gauntlet/packs/]. Each critic opens the actual output, answers its one
question, names the single biggest remaining gap, and sends it back. Loop until an
exit condition in GAUNTLET.md fires.

Never break anything under Invariants, and stay inside Blast radius. If closing a gap
would require either, stop and ask. Park taste calls in ./gauntlet/taste.md and keep
working other pieces.

Keep ./gauntlet/ledger.md current and maintain a live ./gauntlet/progress.html
showing the work evolving. Don't ask for approval between rounds.

[HARNESS VERBS]
```

Then stop. Do not run the loop in the session that designed it. The designer is not a
neutral judge of its own framing.

## Step 4 — What the lead agent does

The full version is in `assets/GAUNTLET.md`. This summary is here so you can explain it.

- **Orchestrate only.** The lead splits, writes questions, briefs, routes gaps, and keeps
  the ledger. It never builds or judges a piece: an orchestrator that has read everything
  cannot judge fresh.
- **Calibrate.** Before the first real round, hand a critic an artifact with a known
  planted flaw and check it catches it. Do the same once per criteria pack. It takes
  thirty seconds and tells you whether the harness's "fresh context" is real. Harnesses
  claim isolation they do not always deliver, and a critic that inherited the build
  context passes everything warmly. Nothing downstream means anything if this fails.
- **Split.** The smallest independently judgeable pieces. The lead agent decides.
- **Question.** Per piece, write three to five specific questions a critic can answer by
  looking at the artifact, plus one question per criteria set that fits the piece.
  Targeted questions beat holistic judging by a measurable margin, and piece-specific
  questions beat generic criteria. This is the parametric part: the questions change per
  piece, the protocol does not.
- **Brief cold.** Every subagent gets a complete brief (role, objective, input paths,
  one ask, allowed tools, return shape, done condition) and nothing else. Critics never
  see the builder's rationale, the round number, or other verdicts.
- **Gate (L0).** Deterministic checks run before any critic. A red gate is the next gap.
  Tracked counts ratchet: an accepted version may not make one worse.
- **Build.** One builder per piece, fresh context, no critic history. Builders run in
  parallel only when their paths don't overlap, or in separate worktrees. Gap priority:
  gate, then bar, then binding pack criterion, then regression.
- **Judge (L1).** One critic per question, a fresh instance every round, never the
  builder. It sees the artifact, the reference, and its one question. Forced choice or
  yes/no, not a score. No panels and no persona variation: both are covered, with
  sources, in `references/evidence.md`. All of a round's critics run as one parallel
  batch, and the working tree must be unchanged afterwards. Full protocol in
  `references/critic-protocol.md`.
- **Judge packs (L2).** Pack critics apply one criteria set each, cite its source concept,
  and run once the bar questions pass. A conflict with the bar or an invariant goes to the
  owner.
- **Check for absence.** Once per wave, one holistic critic asking only what should be
  there and is not. Decomposed critics are specifically bad at noticing absence.
- **Regression check.** The new version must beat the last accepted version, not merely
  approach the bar. Loops move backwards more often than anyone expects.
- **Smooth.** After each wave, one fresh agent checks the integrated whole for seams.
  Pieces improved separately drift apart. Distinct from the absence check: this one
  reconciles what exists.
- **Owner queue.** Escalations and advisory gaps go to `taste.md` with before/after
  evidence; the loop keeps working other pieces while they wait.
- **Log.** Every verdict goes into the ledger with its evidence paths. The ledger is the
  run's state, so the lead resumes from it after a restart or context compaction.

## Exit conditions

First one to fire. Any of them is a valid stop.

- **Win** — the critic picks our output over the bar, both orderings, and every binding
  pack question passes.
- **Plateau** — the same underlying gap named three rounds running. Not converging; stop
  and report. Three is a dial, not a law — lower it when rounds are expensive.
- **Budget** — the ceiling from Step 1.
- **Invariant or blast-radius collision** — hard stop, ask the user.
- **Broken bar** — the critic cannot actually open the reference. A loop judged against a
  hallucinated reference passes everything. Stop immediately.

Never a fixed round count as the primary exit. Rounds are a budget, not a goal.

## Step 5 — Land it

When the loop stops, read the closing entry, then spot-check one piece that passed by
looking at it yourself against the reference. If your judgement and the ledger disagree,
the questions are usually the thing to fix, not the artifact. A piece that passes
everything and still looks wrong was asked the wrong questions.

Clear `gauntlet/taste.md` with the owner. With criteria packs, read the pack tally and
record which sets earned their place. Then decide: accept, rerun a piece with a tighter
gap, raise the bar, or change the packs.

## Reference files

- `references/bar-selection.md` — choosing and validating the bar; worked examples by
  domain
- `references/critic-protocol.md` — the comparison, its known biases, and the
  countermeasures
- `references/criteria-packs.md` — the contract for criteria packs: what a pack
  provides, how the loop uses it, how to build one, and the conformance checklist
- `references/harness-map.md` — Claude Code, Codex, Cursor, agent definitions, and the
  no-subagent fallback
- `references/failure-modes.md` — what goes wrong and how it shows up in the ledger
- `references/evidence.md` — what each rule rests on, what was rejected, and what is
  reasoning rather than measurement
- `assets/GAUNTLET.md` — the protocol template to copy into the project
- `../../../docs/agents/skill-composition-map.md` — stacking rules; this skill forbids
  nesting itself inside another gauntlet-loop
