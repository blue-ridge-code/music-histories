# Evidence

What each mechanism in this skill rests on, so it can be argued with rather than inherited. Split into measured and reasoned. If you change the protocol, update this file — a rule with no line here is a rule nobody can audit.

## Measured

| Mechanism | Finding | Source |
|---|---|---|
| Decompose into targeted questions rather than holistic judging | Checklist decomposition raised exact agreement with human preference by 5.8pp | TICK, arXiv:2410.03608 |
| Binary sub-questions over scales | Improved inter-model consistency (Fleiss κ up to 0.72) and ~+0.10 Spearman/Kendall correlation with human assessment | CheckEval, Lee et al. |
| Piece-specific questions over generic criteria | Question-specific rubrics substantially outperform domain-agnostic dimensions | Rubric survey, arXiv:2606.08625 |
| A separate holistic omission critic | Decomposition fragments completeness reasoning; holistic judging matched or beat atomic on 2 of 3 benchmarks, advantage concentrated in incompleteness detection | arXiv:2606.08625; arXiv:2603.28005 |
| Swap comparison order | Position bias swings win rate 10–15pp by slot; strongest when candidates are close | Zheng et al. 2024 (MT-Bench); Shi et al. 2024 |
| Length as an invariant | Verbosity bias inflates preference for longer outputs by 15–30pp at matched quality | Wang et al. 2023 |
| Cross-vendor critic | Judges rate their own family's output ~10–25% higher | Zheng et al. 2024 |
| No judge panels | 9 judges / 7 families carried ~2.2 independent votes (24% of nominal); panel never beat its best single member (+0.2, −6.5, −2.5pp); judges past 5 added almost nothing | Kohli 2026, arXiv:2605.29800 |
| Vendor diversity is not independence | Same-family pairs only +0.047 more correlated than cross-family; the three most correlated pairs were all cross-family; one-judge-per-family *lowered* effective independence to 1.93 | ibid. |
| Agreement is weak evidence | Unanimous panel verdicts were wrong ~9% of the time vs ~0.02% predicted under independence | ibid. |
| No chain-of-thought for diversity | CoT raised inter-judge correlation (φ .391 → .456), lowering effective independence 2.18 → 1.94 | ibid. |
| No persona variation | 162 roles × 4 model families × 2,410 questions: personas gave no improvement over no persona; role assignment can introduce bias and degrade reasoning | arXiv:2311.10054; arXiv:2408.08631 |

**Transfer caveat, applying to every row from Kohli 2026.** Those results come from classification and pairwise-preference benchmarks (ChaosNLI, RewardBench), not from judging open-ended artifacts — a rendered page, a running program, a draft. The paper says as much in its limitations. The direction is well supported. The magnitude in this setting is not established, and open-ended judging could correlate less (richer evidence) or more (shared aesthetic priors).

## Reasoned, not measured

These are here because they address a failure that has been observed in practice, not because anyone has measured that they help. Treat them as defaults worth keeping until something better arrives, not as findings.

- **Invariants** — from the documented case of a landing-page loop producing a striking site that matched nothing about the brand's design system.
- **Blast radius** — hours of unattended tool access needs a stated limit. No study; obvious once stated.
- **Regression guard** — comparing only against the reference cannot notice that round 6 broke what round 5 had right.
- **Plateau detection at three rounds** — the number is a dial, not a finding.
- **The calibration check** (plant a known flaw, confirm the critic catches it) — the reasoning is sound and the cost is thirty seconds, but nobody has measured how often harnesses silently fail context isolation.
- **The MVP gate** — from the practitioner report on direction drift, not a controlled comparison.
- **Mirroring the reference locally** — removes a known failure (unreachable bar) rather than improving a measured outcome.

### Added in the 2026-09 revision

These come from published engineering practice rather than controlled comparisons of
judging quality. They are defaults worth keeping until something better arrives.

- **Deterministic gates (L0) before any model judge, with counts that ratchet.** In
  Anthropic's two-week speed sprint on claude.ai ("How we made claude.ai 3x faster in two
  weeks", 2026), instruction counts replaced noisy wall-clock time as the gate. A CI
  ceiling that only moves down kept each win. On two hot paths, cutting instructions by
  48% and 31% cut wall-clock time by 78% and 44%. That is evidence that a well-chosen
  count tracks the real outcome, not evidence about critics.
- **Cold, complete subagent briefs; compact returns; the lead orchestrates only.** From
  Anthropic's "How we built our multi-agent research system" (2025): vague subagent
  task descriptions caused duplicated and missed work, and an orchestrator that
  delegates with explicit objectives, output formats, and boundaries did better. Compact
  returns keep the lead's context for decisions.
- **Least privilege, verified by an unchanged working tree.** From the Claude Code
  subagent documentation (per-agent tool allowlists), plus the self-grading failure
  mode: a critic that edits the artifact has judged its own work. The unchanged-tree
  check is a cheap test of what the tool allowlist is supposed to guarantee.
- **The ledger as resumable state.** Long runs outlive context windows. No study; the
  failure it prevents (a lead that rebuilds state from memory after compaction) is
  obvious once named.
- **A named owner and a taste queue.** From the same speed sprint: every thread had a
  named human owner who ruled on user-perceptible changes from before/after evidence,
  while the work kept moving.
- **Criteria packs instead of personas.** This follows the persona finding in the table
  above: the only thing a role can usefully add is a different definition of failure, so
  a pack writes that definition down and labels its source. Nobody has measured whether a
  given pack adds catches beyond the base loop. The per-set unique-catch tally and kill
  rule in `criteria-packs.md` measure that inside each run.

## Considered and rejected

- **Persona-varied critics.** See the table. Intuitive, and the evidence is against it.
- **Judge panels with vote pooling.** See the table. Note the apparent conflict with PoLL (Verga et al. 2024), which found diverse panels beat a single large judge: PoLL compared panels against the *average* individual judge, where diversification naturally wins. Kohli compared against the *best* individual, which the panel did not beat. Both can be true. Since you get to pick your judge, the relevant comparison is against the best one.
- **Swapping the builder's model on plateau.** Plausible — a different prior might escape a local optimum where the current model is stuck. No evidence either way, and cross-model builders demonstrably multiply the integration problem the smoothing pass exists to solve. Left out until someone measures it.
- **Cross-model builders generally.** No supporting evidence found.

## Open questions worth testing

- Does criterion decomposition hold up on visual and code artifacts, where the evidence is richer than a text pair?
- Does effective independence between judges look different when they are inspecting a running program rather than classifying a sentence pair?
- Is three to five questions per piece the right number, or does it track piece complexity?
- Which criteria packs earn unique catches on which kinds of work? Pool the closing-entry
  tallies across runs before trusting any single run's answer.
