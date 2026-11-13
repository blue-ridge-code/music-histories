# Critic protocol

The critic is the load-bearing part. Everything else is scheduling. A loop with a weak critic does not converge on quality — it converges on whatever the critic is biased toward, and it does it for hours.

Effect sizes cited here are recorded with sources in `evidence.md`. Read that before changing anything in this file.

## The four separations

**Separation of role.** The builder never grades its own work. The builder has seen every decision and remembers why it made it, which makes it excellent at explaining why the work is reasonable. Reasonable is not the goal.

**Separation of context.** The critic gets the artifact and the bar. It does not get the builder's rationale, its self-assessment, how many rounds have run, or how hard anything was. Those are all arguments for a pass.

**Separation across retries.** A fresh critic each round. A critic that saw round 3 grades round 4 on improvement — "much better than last time" — instead of against the bar. Improvement is not the bar.

**Separation of evidence.** The critic inspects the real artifact: rendered pixels, running program, executed tests, the actual prose. Never a summary the builder wrote about the artifact.

## Verify the separations before trusting any of them

Harnesses claim context isolation they do not always deliver, and there is no way to tell from the outside: a critic that quietly inherited the build context produces fluent, warm, plausible verdicts. It just passes everything.

So test it once, at the start of a run. Take the current artifact, plant one obvious flaw, and send it through as a normal round. If the critic misses it, the isolation is not real or the critic is not opening the artifact — and every verdict for the rest of the run is decoration. Thirty seconds against hours of compute.

Re-run this if you change harness, model, or the way critics are spawned.

Check privilege the same way, every batch rather than once: after a batch of critics
returns, the working tree must be unchanged. A critic that edited the artifact has
judged its own edit. Void the batch and re-run it with tools that cannot write.

## Ask different questions, not the same question differently

This is the highest-leverage design choice in the protocol, and the least obvious.

Do not spawn several critics to render an overall judgement on the same piece. Spawn several critics that each answer one specific question about it. Decomposing evaluation into targeted binary questions raises agreement with human preference by about 6 percentage points over holistic judging, and improves both consistency between judges and correlation with human assessment. Criteria written for the specific piece substantially outperform generic ones — "does the hero headline state a benefit rather than a feature" beats "is the copy compelling".

So, per piece, before building:

1. Derive **three to five questions** from the goal, the bar, and the invariants. Each answerable yes/no or as a forced choice against the reference. Each about something observable in the artifact.
2. Spawn **one critic per question**, each with fresh context and only the evidence needed to answer its question.
3. A piece passes only when every question passes.

Write the questions into the ledger before the first build. If a question cannot be answered by looking at the artifact, it is not a question — rewrite it.

The questions are the parametric part of this protocol. They change per piece and per project. The protocol around them does not.

## The omission critic

Decomposition has a specific blind spot: it is bad at noticing what is absent. Holistic judges given a detailed rubric outperform decomposed ones on completeness, because splitting the judgement fragments the reasoning that would catch a global gap. In a controlled comparison, holistic judging matched or beat atomic judging on two of three benchmarks, with the advantage concentrated in detecting incompleteness.

So run one holistic critic per wave whose only mandate is absence: what should be here and is not. It sees the whole integrated artifact, the goal, and the bar. It does not answer the per-piece questions — those are covered — and it does not fix seams, which is the smoothing pass's job.

Without this, a loop can pass every question on every piece and ship something with a hole in it.

## Forced choice, not scores

The verdict on each question is a pick or a yes/no, never a rating. Scores drift upward across rounds because each round genuinely is better than the last, and a 7 becomes an 8 becomes a 9 while the gap to the reference has not moved. A binary answer to a specific question does not drift.

## Countering position bias

Pairwise LLM judging has a documented order effect: the option in the first slot wins more often than chance, independent of quality — roughly 10–15 points of win-rate swing depending on slot order, persisting across model families though its direction varies.

This matters more here than in most judging setups, because position bias is most pronounced when the quality gap between candidates is small. That is precisely the regime a gauntlet loop enters after a few successful rounds. The judge becomes least trustworthy exactly when the decision starts to matter.

**Countermeasure — run the comparison twice with the order swapped.**

Swapping doubles critic cost, so spend it where it buys something. In early rounds, when our artifact is plainly behind, one comparison is enough. From the round a piece first survives, and any time a verdict reads as close, run both orderings.

- Ours wins both orderings → **PASS**.
- Bar wins both orderings → **FAIL**, name the gap.
- Split verdict → **TIE**, treated as FAIL. Continue and log it. A split means the two are close enough that the judge cannot tell, which is information: near the end, a run of ties is a legitimate reason to stop.

**Verbosity bias** is worth knowing about because it shows up as a characteristic loop pathology: judges prefer longer outputs at matched quality, measured in one study at 15–30 points of inflated preference. In a loop this appears as artifacts that grow every round. If length is not part of the bar, make it an invariant.

## One cross-vendor critic, and no jury

**Do use a different model family for the critic than the builder, where the harness allows it.** Judges rate their own family's output higher — around 10–25% — and in a loop that bias points at "pass". Swapping vendors attacks that specific mechanism. It is the cheapest single quality upgrade available.

**Do not build a panel of judges and pool their votes.** This is the intuitive next step and the evidence is against it. A panel of 9 frontier judges spanning 7 model families carried only about 2.2 independent votes' worth of information — under a quarter of nominal independence — and failed to beat its own best single member on any dataset tested. Adding judges past five bought almost nothing, and removing individual judges often improved accuracy.

Vendor boundaries are not the axis of independence people assume. Same-family judge pairs were barely more correlated than cross-family ones, and the most correlated pairs in that panel were all cross-family. Restricting the panel to one judge per family made effective independence slightly worse.

The practical consequences:

- One good critic per question beats three critics on the same question.
- **Disagreement escalates; it does not average.** When two critics split on a question, surface it to the human rather than resolving by vote.
- **Treat agreement as weak evidence.** In that panel, unanimous verdicts were still wrong about 9% of the time, against roughly 0.02% if the judges had been independent. Unanimity is not confirmation.

Caveat on transfer: these panel results come from classification and pairwise-preference benchmarks, not from judging open-ended artifacts like a rendered page or a draft. The direction is well supported; the magnitude in this setting is not established.

## Two things not to do

**Do not vary the critic's persona to manufacture diversity.** Assigning roles feels like it should produce independent perspectives. The largest study of this tested 162 roles across four model families and 2,410 questions and found personas gave no improvement over no persona at all, with other work finding role assignment can introduce bias and degrade reasoning. A persona changes the voice of the verdict, not the evidence examined. If a role seems useful, it is because it implies a different definition of failure — in which case write that as a question and skip the costume. A criteria pack is the structured form of this: definitions of failure written down as criteria, each labeled with its source so the owner can see which tradition a change comes from. See `criteria-packs.md`.

**Do not add "think step by step" to critics and expect more independence.** Chain-of-thought raised inter-judge error correlation in testing, dropping effective independence rather than raising it: shared reasoning amplifies shared errors. Use it if it makes a single critic more accurate on a hard question. Do not use it as a diversity mechanism.

## Pack critics

A criteria pack adds critics that judge the artifact against a pack's claim using one
criteria set each, after the bar questions pass. Everything in this file applies to them
unchanged: fresh context, one question, forced choice, one gap, evidence paths, order
swapping when close. Two additions:

- **Cite the source.** The verdict names the set and the concept it applied. A concept
  that is neither on the set's card nor in its excerpts voids the verdict. This is how a
  critic gets caught inventing what a source "would say".
- **Disagreement between sets escalates.** Two sets that pull opposite ways are a taste
  call for the owner, never a vote.

The full contract is in `criteria-packs.md`.

## Verdict format

One block per question. The lead agent appends each to the ledger.

```
PIECE:       <piece id>
ROUND:       <n>
LAYER:       L1 | L2:<pack>/<set> | L3:<pack>/<check> | absence
QUESTION:    <the specific question this critic answered>
SOURCE:      <set: concept applied — pack critics only>
ORDER A:     <ours first | reference first | n/a>     VERDICT: <ours | reference | yes | no>
ORDER B:     <swapped, or "not run — gap obvious">     VERDICT: <ours | reference | yes | no>
RESULT:      PASS | FAIL | TIE
BINDING:     yes | advisory
EVIDENCE:    <paths inspected — ours and the reference or card, both>
GAP:         <one gap, observable in the artifact, or "none">
REGRESSION:  <yes | no — worse than the last accepted version on any dimension?>
```

Rules the critic follows:

- **One gap.** Not a list. A list lets the builder pick the easy one and claim progress. The largest gap on this question, stated as something observable.
- **Evidence paths are mandatory.** If the critic cannot cite what it inspected, it did not inspect it. A verdict with no evidence path is void and the round does not count.
- **Prove the reference was fetched.** Every verdict must cite the actual reference artifact inspected this round. A critic that cannot reach the reference will invent the comparison and pass everything, which is the most common way a loop silently becomes theatre.
- **Regression is a fail.** If the new version is worse than the last accepted version on any dimension, that is a fail regardless of how it compares to the bar. Roll back and re-attack the gap differently.
