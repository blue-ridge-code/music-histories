# gauntlet-loop

A portable skill for running Gauntlet Loops: split a goal into independently judgeable pieces, give each one a builder and a separate blind critic, compare the real output against a named real-world reference, and keep looping until it wins or you stop it.

Plain markdown. No scripts, no dependencies, no state machine. Works in any harness that can use tools, inspect its own output, and get a judgement from fresh context.

## Install

| Harness | Location |
|---|---|
| Claude Code, project | `.claude/skills/gauntlet-loop/` |
| Claude Code, global | `~/.claude/skills/gauntlet-loop/` |
| Claude apps | upload the folder as a skill |
| Codex | drop in the repo, reference from `AGENTS.md` |
| Cursor / Windsurf | keep in the repo, add a rule pointing at `SKILL.md` |
| Anything else | paste `SKILL.md` as the system prompt, keep `references/` in the repo |

## Use

```
Set up a gauntlet loop for <goal>.
```

The skill fixes the inputs with you — goal, bar, invariants, blast radius, budget, owner, and any criteria packs. It writes `gauntlet/GAUNTLET.md`, `gauntlet/ledger.md`, and `gauntlet/taste.md` into the project, and hands back one short prompt to paste into a **fresh** session. That session runs the loop.

To add a review layer from another skill:

```
Use play-canon with gauntlet-loop on <goal>.
```

`references/criteria-packs.md` explains how packs plug in and how to build one.

Two files, deliberately. The launch prompt stays short so the agent keeps room to decide; the protocol lives in a file the lead agent reads. Bloating the prompt with process is the thing the original method is right about avoiding.

## Contents

```
gauntlet-loop/
├── SKILL.md                        the workflow
├── references/
│   ├── bar-selection.md            choosing a reference the agent can't talk around
│   ├── critic-protocol.md          the comparison, its biases, the countermeasures
│   ├── criteria-packs.md           the contract for review layers supplied by other skills
│   ├── harness-map.md              per-harness verbs, agent definitions, the no-subagent fallback
│   ├── failure-modes.md            what goes wrong, and its ledger symptom
│   └── evidence.md                 what each rule rests on; what was rejected
└── assets/
    └── GAUNTLET.md                 protocol template copied into the target project
```

## What this adds to the original method

The pattern is Matt Shumer's. His writeup covers the goal, the bar, the split, the separate critic, and not stopping early. That is the method and it is correct. What is missing from it — and from the published implementations — is everything about a long unattended run going quietly wrong:

- **Questions instead of verdicts.** Each critic answers one specific, piece-derived question rather than rendering an overall judgement. This is the largest measured lever in the protocol.
- **An absence check**, because decomposed critics are structurally bad at noticing what is missing.
- **No judge panels.** The intuitive upgrade — several diverse judges voting — does not survive contact with the evidence.
- **Invariants**, separate from the bar. The bar is what you chase; invariants are what you cannot trade away to reach it. Without them a loop wins the comparison and loses the brief.
- **Blast radius.** Hours of unattended tool access needs a stated limit.
- **A calibration check.** Plant a known flaw, confirm the critic catches it. If your "fresh context" critics are not actually isolated, everything downstream is decoration — and you cannot tell from the transcript.
- **Order swapping.** Pairwise LLM judges favour the first slot, worst when the two candidates are close, which is where a converging loop lives.
- **A regression guard.** Comparing only against the reference misses that round 6 broke something round 5 had right.
- **Plateau detection.** The same gap three rounds running is not convergence.
- **Evidence paths for both sides.** A critic that cannot cite the reference it opened did not open it, and will pass everything.

The 2026-09 revision adds:

- **Deterministic gates first.** Build, tests, render, lint, and invariant checks run before any model judges anything. Tracked counts ratchet, so an accepted version never makes one worse.
- **Current subagent practice.**
  - The lead only orchestrates.
  - Every subagent gets a complete, cold brief.
  - Critics are read-only, verified by an unchanged working tree after each batch.
  - A round's critics run as one parallel batch.
  - The ledger is the state the run resumes from.
- **An owner queue.** Taste calls and advisory gaps wait in `taste.md` with before/after evidence, while the loop keeps working other pieces.
- **Criteria packs.** Another skill can add a layer of criteria-based critics (for example `play-canon`). Each verdict carries a source label, and a per-set tally drops criteria that catch nothing the bar misses.

Every rule above is recorded in `references/evidence.md` with its source and effect size, separated into what has been measured and what is reasoning. Ideas that were considered and rejected on the evidence are listed there too, so nobody re-adds them.

## Credit

- Method and name: Matt Shumer — [somethingbig.ai/gauntlet-loop](https://somethingbig.ai/gauntlet-loop), [github.com/mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty)
- Practical framing and the direction-drift lesson: Jay E, RoboNuggets
- Underlying pattern: evaluator-optimizer, from Anthropic's "Building Effective Agents"
- Orchestration practice: Anthropic's "How we built our multi-agent research system" (2025) and "How we made claude.ai 3x faster in two weeks" (2026)
- Prior skill implementations worth reading: `robonuggets/gauntlet-loop`, `NicholasSpisak/gauntlet-loop`, `duolahypercho/gauntlet-loop`
