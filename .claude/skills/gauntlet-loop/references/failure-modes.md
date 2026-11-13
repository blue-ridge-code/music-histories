# Failure modes

A gauntlet loop fails loudly almost never. It fails by running for three hours and producing a ledger of passes and an artifact you do not want. These are the ways, in rough order of how often they happen, with the ledger symptom that gives each one away.

## 1. The unreachable reference

**What happens.** The critic cannot actually fetch the bar, so it compares against its idea of the bar and passes almost everything.

**Ledger symptom.** Verdicts with no reference evidence path, or the same evidence path repeated with no timestamp. Early passes on hard pieces.

**Fix.** Mirror the reference into `gauntlet/reference/` before launch. Make every verdict cite the reference artifact inspected that round. Kill any run whose first three verdicts lack reference evidence.

## 2. Direction drift

**What happens.** The loop optimizes hard toward the bar and away from the brief. The canonical example: a landing page loop produced a beautiful site that did not match the brand's actual design system at all, because the bar rewarded visual flair and nothing protected the brand.

**Ledger symptom.** Passes accumulating while the artifact stops resembling what you asked for. Gaps named in terms of the reference's style rather than the goal.

**Fix.** Invariants, declared before launch, that the loop may not trade away. Also the MVP gate: a loop pointed at a blank page picks its own direction and defends it well.

## 3. Score creep

**What happens.** A critic that rates instead of picks watches quality genuinely improve and walks 7 → 8 → 9 while the gap to the reference is unchanged.

**Ledger symptom.** Numeric verdicts. Rising numbers, static gaps.

**Fix.** Binary answers to specific questions, never a rating.

## 4. The improvement critic

**What happens.** A critic that saw the previous round grades relative to it. Round 6 is much better than round 5, so it passes, though it is nowhere near the bar.

**Ledger symptom.** Gaps phrased as "improved", "better than before", "much closer".

**Fix.** Fresh critic instance per retry. The critic must not know the round number.

## 5. Regression thrash

**What happens.** Closing gap A breaks something that was already good. The critic only compares against the reference, so it never notices, and the next round closes gap B by breaking A again. The loop oscillates and burns budget.

**Ledger symptom.** The same two or three gaps alternating across rounds.

**Fix.** The regression check: every candidate must also beat the last accepted version. Keep accepted versions; roll back on regression rather than patching forward.

## 6. Bloat

**What happens.** Verbosity bias, running for hours. Every round adds a section, an effect, a paragraph, a dependency. Each addition wins its comparison. The whole gets worse.

**Ledger symptom.** Monotonically growing artifact size. Gaps that are always additive and never subtractive.

**Fix.** Put length, scope, or dependency count in the invariants. Add a subtractive round: a critic whose only question is what should be removed.

## 7. The cost black hole

**What happens.** Multi-agent loops with a critic per builder multiply token spend fast, and "loop until perfect" has no natural end. Published runs of hours are normal, not exceptional.

**Ledger symptom.** Rounds still running with gaps that are getting smaller and less consequential.

**Fix.** Declare a budget before launch. Plateau detection: three rounds naming the same gap is not convergence. Diminishing gaps are a legitimate reason to stop — "the remaining gaps are real but do not matter" is a mature verdict, not a failure.

## 8. Decomposition into incoherence

**What happens.** Pieces are improved separately and stop fitting together. Individually excellent, collectively a patchwork.

**Ledger symptom.** All pieces passing, integrated result feeling wrong.

**Fix.** The smoothing pass at the end of each wave — one fresh agent inspecting the whole, fixing seams, not redesigning. And do not over-split: pieces that share a visual or logical language should share a builder.

## 9. Self-grading in disguise

**What happens.** The harness reports "spawned a critic subagent" but the critic inherited the build context, or the loop is one long conversation with role labels. Everything passes.

**Ledger symptom.** Warm verdicts. Critic language echoing builder vocabulary. Very high pass rates in early rounds.

**Fix.** The calibration check, run once at the start and again after any change of harness or model: give a critic an artifact with a deliberate planted flaw and confirm it catches it. Full version in `critic-protocol.md`.

## 10. The jury illusion

**What happens.** Several critics are spawned on the same judgement and their votes pooled, on the assumption that diverse models make independent mistakes. They largely do not. A panel's agreement then reads as strong confirmation when it is weak — unanimous verdicts in one large study were still wrong about 9% of the time against roughly 0.02% predicted under independence.

**Ledger symptom.** Multiple verdicts on one question. Confident unanimity on pieces that later look wrong to you.

**Fix.** One critic per question, several questions per piece. Where two critics do disagree, escalate rather than vote. Sources in `evidence.md`.

## 11. Passing everything and shipping a hole

**What happens.** Every question passes on every piece and the result is still missing something nobody asked about. Decomposed critics are structurally bad at detecting absence.

**Ledger symptom.** A clean sweep of passes and an artifact that feels thin.

**Fix.** The absence check: one holistic critic per wave whose only mandate is what should be there and is not.

## 12. Looping on the wrong artifact

**What happens.** The loop polishes the thing that is easy to inspect rather than the thing that matters — the landing page rather than the offer, the prose rather than the argument, the dashboard rather than the data model.

**Ledger symptom.** Everything converging nicely and none of it moving the outcome you cared about.

**Fix.** Before launching, ask what would make this succeed in the world, and whether the bar measures that. This is the one failure mode no protocol catches. It is yours.

## 13. The critic that edits

**What happens.** A critic with write access "helpfully" fixes the thing it was asked to judge, then passes it. Or it leaves a stray file that the next build picks up. Either way it has graded its own work.

**Ledger symptom.** Passes arriving together with changes nobody briefed. Diffs between the builder's summary and what is actually on disk.

**Fix.** Give critics read and run tools only, and check that the working tree is unchanged after every critic batch. Void and re-run any batch that changed it.

## 14. The lead that forgets

**What happens.** A long run outlives the lead's context. After compaction or a restart, the lead rebuilds its state from memory. It re-opens passed pieces, loses owner calls, or forgets which pack sets were dropped.

**Ledger symptom.** Work on pieces the ledger already closed. Questions rewritten mid-run with no entry explaining why.

**Fix.** The ledger is the state. On any restart the lead re-reads `GAUNTLET.md`, the packs, and the last wave in the ledger before acting.

## 15. The pack that plays a character

**What happens.** A criteria pack's critic stops applying criteria and starts voicing its source: "Huizinga would find this vulgar." The verdict sounds learned, cites nothing checkable, and pulls the work toward the source's personal taste instead of the claim.

**Ledger symptom.** Pack verdicts with no `SOURCE` concept, or with concepts that aren't on the set's card. Gaps phrased as opinions rather than as something observable in the artifact.

**Fix.** Void any verdict whose concept isn't on the card or in the excerpts. Brief pack critics to apply criteria against the claim. See `criteria-packs.md`.
