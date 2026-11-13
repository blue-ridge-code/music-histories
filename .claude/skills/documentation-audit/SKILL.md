---
name: documentation-audit
description: Verify that project documentation matches reality — find dead paths, stale commands, drifted registry entries, and contradictions between docs. Fire when the user asks to audit, review, or freshen documentation, or asks whether the docs are up to date.
---

# Documentation audit

## Problem

Docs rot. Paths get renamed, commands change, registries in `docs/agents/*.md` drift from
what is actually installed, and two docs quietly start to contradict each other. Agents
that trust rotten docs hallucinate confidently on top of them.

## When to use

- The user asks to audit, review, or freshen documentation.
- A doc's instructions just failed when followed literally.
- After a large refactor, rename, or registry change.

## When NOT to use

- To fix docs. This skill is read-only: it reports; it edits nothing unless the user
  explicitly asks for fixes afterward.
- For plan-vs-artifact gap analysis — that is the `project-gap-analyzer` skill.

## Process

1. **Enumerate the docs.** Cover `docs/**/*.md` (including `docs/agents/`), root-level
   `*.md` (`README.md`, `AGENTS.md`, `CLAUDE.md`), and any nested per-area `AGENTS.md`.
2. **Extract verifiable claims** from each doc:
   - File and directory paths, and relative markdown links between repo files.
   - Commands and scripts (`npx ...`, `scripts/*.ps1`, CLI invocations).
   - File names, config keys, env var names, skill names, label names.
   - Registry entries in `docs/agents/*.md` — every listed service, utility, skill, and
     model pick.
3. **Verify each claim against reality.** Paths must exist; referenced scripts must
   exist; referenced files must contain the claimed keys; registry entries must match
   what is installed or configured. Never execute anything destructive or
   external-facing just to "verify" it.
4. **Check internal consistency.**
   - Contradictions between docs (AGENTS.md vs docs/agents/* vs README).
   - Duplicated or overlapping docs that have drifted apart.
   - Staleness signals: old dates, version numbers, "planned/todo" language for work
     already done, references to superseded entries in docs/decisions.md that lack the
     `Status: superseded-by-D-00X` marker.
5. **Report per doc**, ordered by severity:
   - **Broken** — references something that does not exist (claim, evidence, proposed fix).
   - **Stale** — was once true but reality has moved on.
   - **Inconsistent** — conflicts with another doc (cite both).
   - Close with a summary count and the list of docs that are fully clean.

## Output

A report grouped by doc, then by severity. Every finding cites the doc location and the
verifying evidence as `file:line` (or command plus observed output). End with a summary
count of Broken / Stale / Inconsistent / unverified and the clean-doc list.

## Notes

- **Anti-hallucination clause:** if a claim cannot be verified either way, mark it
  **unverified** — never guess and present it as fact (the AGENTS.md evidence rule).
- Read-only stance: no file edits, no destructive commands, no external contact beyond
  read-only checks such as `gh auth status`.
- Composition: sibling of `project-gap-analyzer` (both read-only audits, different
  scopes) — run them separately, not stacked
  ([skill-composition-map](../../../docs/agents/skill-composition-map.md)).
