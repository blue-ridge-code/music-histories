# skills.md — skills registry & format guide

One canonical set of skills, thin per-provider adapters. `.agents/skills/` is the canonical
home — read natively by Kimi Code, Codex, **and** Copilot.

> Licenses and repo contents rot fast — **re-check every entry before relying on it.**

## Registry maintenance

`Last evaluated` dates describe a review of the upstream source, license, maintenance
state, and fit—not the installed version. Refresh this registry at least quarterly. The
checked-in [GitHub workflow](../../.github/workflows/quarterly-skills-registry-refresh.yml)
opens `Refresh skills registry` when no matching open issue exists; the
[issue template](../../.github/ISSUE_TEMPLATE/skills-registry-refresh.md) supports manual
runs. In local mode, kickoff creates a dated backlog row and each completed review adds the
next row three months later.
The weekly [template self-test](../../.github/workflows/template-self-test.yml) runs the
ontology validation suite and verifies the canonical skill mirror. Scheduled workflows
run only in repository mode; local-mode projects use the recurring backlog review.

Catalog entries marked **always-fresh** name a moving upstream repository and must be
re-evaluated before selection. Installed external skills remain reproducible because
`skills-lock.json` records their resolved ref and computed hash. Mark a catalog
**version-pinned** only when its registry entry names an immutable tag or commit; update
the pin through an explicit registry review.

### Quarterly review checklist

1. Verify each upstream source, license, maintenance state, and project fit.
2. Update only the `Last evaluated` dates for sources actually checked.
3. Confirm that each source policy is `always-fresh` or an immutable version pin.
4. Move retired picks to **Deprecated skills** with a reason, replacement, and date.
5. Review installed skills: any unused since the last kickoff or audit? Nominate for
   deprecation.
6. Apply the [skill verification checklist](skill-verification-checklist.md) to every
   installed skill, run its self-test or one representative use, and record the evidence;
   report breakage and dead dependencies.
7. Check external catalogs for newer or cheaper alternatives.
8. Add a registry changelog row. Add a decision-log entry when selection or policy
   changes, and tag audits with "Audit", evidence links, and related issues.

## Checked-in core/default skill

`human-review-queue` ships in `.agents/skills/` and its generated `.claude/skills/`
mirror, so every repository created from this template can use durable human gates
without a separate skill install. Shipping the skill does not scaffold or start its
runtime queue: deploy that on demand with the skill's installer. The installer defaults
to `dispatch.adapter: none`, `identity_mode: single_local`, and loopback-only service
access; preserve those defaults until the project owner approves a broader boundary.

## Sync to Claude Code

[`scripts/sync-skills.ps1`](../../scripts/sync-skills.ps1) (or `.sh`) mirrors
`.agents/skills/` → `.claude/skills/` **additively**: it never deletes extras, it only
ensures canonical skills are present and identical. Use `-Verify` with PowerShell or
`--verify` with Bash to report drift without copying.

## Drift detection (all providers)

`.agents/skills/` is canonical and read natively by Kimi Code, Codex, and Copilot, so the
only mirror to keep fresh is `.claude/skills/` (Claude Code). Check it **before
committing**:

- **Local verify:** `pwsh scripts/sync-skills.ps1 -Verify` (or
  `./scripts/sync-skills.sh --verify`) — reports drift without copying.
- **Pre-commit hook:** [`.github/hooks/pre-commit`](../../.github/hooks/pre-commit) is a
  template — enable it repo-locally with `git config core.hooksPath .github/hooks`, or
  copy it to `.git/hooks/pre-commit`.
- **CI:** `.github/workflows/skill-and-doc-integrity.yml` runs the verify on every
  push/PR that touches skills, docs, or the sync scripts.
- **Copilot:** reads `.agents/skills/` natively in this template, so there is no separate
  `.github/skills/` copy to check. If a derived repo later adds one, check it manually
  (no script yet).

## Canonical SKILL.md format

Write skills in the portable spec subset so they survive provider swaps:

- Frontmatter: only `name` and `description` — `description` is the routing trigger, so
  write it as "when to fire". Optional spec fields: `license`, `compatibility`, `metadata`,
  `allowed-tools`.
- Body sections, in order: Problem → When to use → When NOT to use → Process → Output →
  Notes. Put measurable success criteria in Output or in a dedicated Success criteria,
  Verify, or Exit conditions section.
- Provider extras live in sidecars (e.g. `agents/openai.yaml`), never in frontmatter.
- Relative paths only inside skills — no `${KIMI_SKILL_DIR}`-style hard-coded variables.

## Composition

How skills interlock — pairs, sequencing, orthogonality, forbidden stacks, and the
anti-patterns — lives in [`skill-composition-map.md`](skill-composition-map.md). Consult
it before stacking skills and log new relationships there when a skill ships.

## External install flow

Before a skill enters the catalog or is installed or updated, complete the
[skill verification checklist](skill-verification-checklist.md). Record a passing result
with the catalog review or installation evidence. A failed or unverified candidate is not
an accepted skill.

```powershell
npx skills@latest add <owner/repo>   # vercel-labs CLI; mirrors into per-agent dirs (70+ agents)
npx skills update                    # refresh installed skills
```

The CLI writes a hash-pinned `skills-lock.json` at project root — fields: `version`,
`skills`, `source`, `sourceType`, `ref`, `skillPath`, `computedHash`. Restore from the lock
with `experimental_install`. Commit the lock; it makes skill state reproducible. New skills
get the sync-script mirror to `.claude/skills/` afterwards.

## External catalog

| Name | Source policy | Role | Current pick | Alternatives | Cost | Last evaluated | Swap when |
|---|---|---|---|---|---|---|---|
| `mattpocock/skills` | always-fresh | Workflow skills: wayfinder, grilling, research, handoff, writing-for-agents, domain-modeling, prototype, grill-me, tdd, code-review, diagnosing-bugs | wayfinder + grilling are the template defaults | hand-rolled skills | Free (MIT) | 2026-08-07 | Skill goes unmaintained or a better equivalent lands |
| `anthropics/skills` | always-fresh | Doc skills: docx/pdf/pptx/xlsx, plus doc-coauthoring, internal-comms, skill-creator, webapp-testing, mcp-builder | on demand | [utilities](utilities.md) for one-off conversions | Free (Apache-2.0; docx/pdf/pptx/xlsx are source-available) | 2026-08-07 | License terms stop fitting the project |
| `NateBJones-Projects/OB1` skills | always-fresh | Knowledge work: meeting-synthesis, research-synthesis, panning-for-gold, heavy-file-ingestion, auto-capture, work-operating-model, claudeception | on demand | — | Free (FSL-1.1-MIT: personal use fine, no commercial derivatives until it converts to MIT) | 2026-08-07 | Commercial use before MIT conversion |
| `muratcankoylan/Agent-Skills-for-Context-Engineering` | always-fresh | Context-optimization plus 16 more | on demand | [token-efficiency.md](token-efficiency.md) conventions | Free | 2026-08-07 | Overlap with project conventions |

## Deprecated skills

Move a skill here when the project stops recommending or installing it. Keep the row so
future agents can migrate old projects instead of silently restoring an obsolete pick.

| Name | Reason | Replacement | Deprecated or removed |
|---|---|---|---|
| — | No skills are currently deprecated | — | — |

## Registry changelog

Record registry-level changes here; use `docs/decisions.md` when a change is significant.

| Date | Change | Decision |
|---|---|---|
| 2026-08-15 | Added source policies, quarterly review, and deprecation signals | D-005 |
| 2026-09-28 | Upgraded local `gauntlet-loop` (criteria packs, deterministic gates, current subagent practice); added local `play-canon` as its first criteria pack, with `scripts/tests/test_criteria_packs.py` | D-011, D-012 |
| 2026-09-30 | Finished `play-canon`: source files checked against the owner's texts with page numbers, `(unchecked)` marking for concepts without one, and fidelity checks in `test_criteria_packs.py` | D-012 |

Install only what the kickoff interview selects — external defaults are wayfinder +
grilling, while `human-review-queue` is already checked in and available. The rest is a
typed menu. Log every addition or swap in [`docs/decisions.md`](../decisions.md).

**Install just-in-time, not all at once.** Kickoff selects skills for every phase but
installs in three buckets: planning-phase skills (`wayfinder`, `grilling`, and any of
`research` / `domain-modeling` / `prototype` the project selected) install immediately;
`handoff` is recorded as selected but installs only at the first real session boundary that
needs it; implementation-phase skills (`codebase-design`, `tdd`, `diagnosing-bugs`,
`code-review`) are recorded as selected but install only once the project reaches
`implementation-ready` (see [lifecycle.md](lifecycle.md)). `docs/PROJECT.md`'s "Skills
installed" section records which bucket each selected skill is in.

## Kimi Code extras

- `/import-from-cc-codex` imports Claude/Codex settings (skills included).
- Plugins via `kimi.plugin.json` — see [model-roles.md](model-roles.md).

## Adding or swapping a skill

1. Check the catalog above and the local `.agents/skills/` first.
2. Complete the [skill verification checklist](skill-verification-checklist.md); do not
   catalog or install a candidate until it passes.
3. External skill: install with `npx skills@latest add <owner/repo>`, then run the sync
   script and commit `skills-lock.json`.
4. Local skill: author it in the canonical format above under `.agents/skills/<name>/`.
5. Log the addition or swap in [`docs/decisions.md`](../decisions.md) with the reason.
