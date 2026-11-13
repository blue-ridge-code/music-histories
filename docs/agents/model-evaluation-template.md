# Model evaluation template

Use this template when a new model or provider could replace a current pick in
[`model-roles.md`](model-roles.md). The point is a decision you can record — **swap, keep,
or monitor** — with evidence, instead of guessing. Re-verify current models and pricing
first; the numbers below rot.

## Quick check

A candidate that fails the quick check is not a fit for the role's tooling. Stop there and
record the failure rather than forcing it through the full test.

- [ ] Supports the skill mechanism this repo uses: `.agents/skills/` or `.claude/skills/`
      with spec-subset `SKILL.md` frontmatter (see [skills.md](skills.md)).
- [ ] Reads the canonical instruction file: `AGENTS.md`, or the provider's pointer to it
      (`CLAUDE.md`, `.github/copilot-instructions.md`).
- [ ] Cost per 1M tokens is published and fits the project's budget.
- [ ] Input context length covers the role's workload.
- [ ] Tool-use fidelity verified with the test below.

## Tool-use fidelity test

Follow the [risk-based exposure rule](model-roles.md#risk-based-exposure-rule): route only
no-tool-schema calls (plain chat, drafting, summarizing) until tool use is verified. Run a
small, reversible task in a scratch directory — outside the tracker — that exercises every
tool schema the role needs:

1. Read a file and report its first line.
2. Make a trivial edit to a scratch file, then revert it.
3. Run a read-only shell command (for example, list files).
4. If the role needs GitHub: one read-only call (for example, `gh auth status`).

Record which tools failed and how: silent failure, wrong schema, or permission confusion.

## Results

| Question | Answer |
|---|---|
| Quality | [Equal/Better/Worse] than [current pick] |
| Cost | [Dollars per hour of use vs. current pick] |
| Reliability | [Tool failures or edge cases observed] |
| Recommendation | Swap \| Keep current pick \| Monitor |

## Record the outcome

- **Swap**: update `Current pick`, `Alternatives`, and `Last evaluated` in
  [`model-roles.md`](model-roles.md), and add a decision entry in
  [`docs/decisions.md`](../decisions.md) citing this test as evidence.
- **Keep / Monitor**: update `Last evaluated`. For a monitored candidate, set a date to
  re-check; no decision entry is needed.
