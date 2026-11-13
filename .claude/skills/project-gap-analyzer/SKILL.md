---
name: project-gap-analyzer
description: Compare what the project planned against what actually exists — find documented-but-unbuilt work, undocumented artifacts, partial implementations, and stale TODOs. Fire when the user asks to analyze gaps, find missing work, compare plans against reality, or assess what remains to be done.
---

# Project gap analyzer

## Problem

Plans and reality drift apart in both directions: planned work that was never built, and
artifacts that exist but no doc admits to. Without a periodic cross-check, "what remains"
is guesswork and status reports are fiction.

## When to use

- The user asks for a gap analysis, a status reality-check, or "what is left to do".
- Before milestone reviews, handoffs, or re-scoping sessions.
- After a burst of work, to reconcile the tracker with the artifacts.

## When NOT to use

- To verify doc correctness (paths, commands, links) — that is the `documentation-audit`
  skill; this one checks plan-vs-artifact.
- To modify anything. This skill is read-only.

## Process

1. **Inventory the plan.** Read the scoping and tracking material:
   - [docs/PROJECT.md](../../../docs/PROJECT.md) — mission, definition of done, areas of
     concern, activated layers.
   - [docs/decisions.md](../../../docs/decisions.md) — active entries (skip superseded).
   - The tracker: open GitHub Issues via `gh issue list`, or `docs/backlog.md` in local
     mode.
   - Extract each planned work item as a checklist entry with its source (`path:line` or
     issue number).
2. **Inventory reality.** Map what actually exists, matched to the project type:
   - Software: source trees, tests, configs, CI, migrations, scripts.
   - Non-software: the work products and folder conventions declared in docs/PROJECT.md
     under "Architecture / areas of concern".
   - Activated layers: wiki (`raw/`, `wiki/`, `index.md`, `log.md`), intake (`inbox/`,
     `sources/`), installed skills in `skills-lock.json`.
3. **Cross-reference.** For each planned item, classify it:
   - **Implemented** — the artifact exists (cite `file:line` or equivalent evidence).
   - **Partial** — started but incomplete; state what is missing.
   - **Missing** — no artifact found.
   - **Superseded** — the plan was abandoned or replaced (check docs/decisions.md).
   - Also flag the reverse: artifacts with no corresponding plan or tracker entry
     (**undocumented**).
4. **Sweep for markers.** Grep for `TODO`, `FIXME`, `HACK`, `XXX`, placeholder text,
   commented-out blocks, and skipped/disabled tests; attach each to the relevant gap or
   list them separately.
5. **Report.** Produce the gap report:
   - Summary counts per classification.
   - A table: item | source | status | evidence | severity (high/med/low) | suggested next
     step.
   - A short "top gaps" list ordered by impact on the definition of done.
   - End with open questions where the docs themselves are ambiguous.

## Output

A gap report with summary counts, the classification table, the top-gaps list, marker
sweep results, and open questions. Every claim cites a real path and line, or an issue
number.

## Notes

- **Anti-hallucination clause:** if something cannot be verified, say so — never guess
  and present it as fact (the AGENTS.md evidence rule).
- Read-only stance: no file edits, no tracker mutations, no git commands.
- Judge severity against the definition of done in docs/PROJECT.md, not against your own
  opinion of what matters.
- Composition: sibling of `documentation-audit` (both read-only, different scopes) —
  run them separately, not stacked
  ([skill-composition-map](../../../docs/agents/skill-composition-map.md)).
