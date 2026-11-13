# Template Review & Action Items

> **Superseded — see [`docs/decisions.md`](decisions.md) D-008.** Every item below is done
> (each annotated with where — #10, #12, #13 closed by parallel work merged in
> [D-007](decisions.md), the rest by [D-008](decisions.md)). This file's relative links
> originally pointed two levels up (`../../`) when this file lives one level from repo
> root — corrected below to `../`.

**Date:** 2026-08-15  
**Reviewer:** GitHub Copilot  
**Overall:** Production-ready. Fix 5 remaining high-priority issues, then scale with confidence.

**Status:** Minor correctness issues (1–2) ✅ COMPLETED. All 13 numbered items ✅ COMPLETED
(see D-007 and D-008 evidence below).

---

## ✅ COMPLETED (2 items)

### ✅ 1. docs/PROJECT.md kickoff logic — FIXED
**PR:** #2 (merged 2026-08-15)  
**Change:** Added git remote check to skip kickoff if origin = `blue-ridge-code/vscode-template`. Template repo no longer runs unnecessary kickoff.

### ✅ 2. MCP census refresh guidance — FIXED
**PR:** #2 (merged 2026-08-15)  
**Change:** Added clarification in services.md that census is a snapshot and must be re-run in new projects during kickoff step 7.

---

## REMAINING WORK (12 items)

### High-Priority Critical Issues (Fix before next kickoff)

#### 3. Skills registry is truncated; missing alternatives
**File:** `docs/agents/skills.md` line 42–46  
**Problem:** External catalog table is cut off with `[...]`. Users can't see full comparison of alternatives and swap criteria.

**Fix:** Expand the table columns or move external catalogs to a separate `docs/agents/external-skills-catalog.md`. Show full rows for each external source (mattpocock/skills, anthropics/skills, NateBJones-Projects/OB1, muratcankoylan/Agent-Skills).

**Effort:** 2 hours  
**Status:** ✅ Done — see [`docs/agents/skills.md`](agents/skills.md)'s full External catalog
table (D-005).

---

#### 4. Layer activation has no decision tree
**File:** Missing; referenced in AGENTS.md and docs/agents/ index but no guide.  
**Problem:** Anti-scaffolding rule says "activate layers only when needed" but gives no heuristic. Users guess: wiki? intake? tracker? ontology-agent?

**Fix:** Create `docs/agents/layer-activation-guide.md` with a decision tree:

```markdown
# Layer Activation Guide

| Layer | Activate when | Skip if |
|-------|---------------|---------|
| **wiki** | 15+ cross-referenced docs or research-heavy project | Single doc or all content fits in one issue |
| **intake** | Expect phone/chat/file drops weekly+ | No external inputs; local-only work |
| **tracker** | Multi-session work; other agents will see this | Single agent session; no blockers |
| **ontology-agent** | 6+ top-level modules; software with dependencies | Single-file script or monolithic app |
| **tools** (MCP) | Agent needs external APIs (GitHub, Slack, etc.) | No integrations needed |

## Kickoff integration

When kickoff asks "Which layers do you need?", walk this table with the user.
Default: tracker (always) + nothing else until the project asks for it.
```

**Effort:** 2 hours  
**Status:** ✅ Done — see [`docs/agents/layer-activation-guide.md`](agents/layer-activation-guide.md)
(D-005).

---

#### 5. Drift detection is manual; not gated
**File:** `scripts/sync-skills.ps1` exists but is never forced to run.  
**Problem:** User can commit skill drift (`.agents/skills/` ≠ `.claude/skills/`) without catching it.

**Fix:** Add to `.github/workflows/template-check.yml`:

```yaml
name: Template self-check
on: [push, pull_request]
jobs:
  skills-drift:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check skill mirror
        run: pwsh scripts/sync-skills.ps1 --Verify
        shell: pwsh
```

For local-mode projects: add to `docs/backlog.md` template a recurring task reminder.

**Effort:** 1 hour  
**Status:** ✅ Done — see [`.github/workflows/skill-and-doc-integrity.yml`](../.github/workflows/skill-and-doc-integrity.yml)
(`sync-skills.ps1 -Verify` runs on every push/PR touching skills or docs).

---

#### 6. Skills have no deprecation signal
**File:** `docs/agents/skills.md` (add section)  
**Problem:** External skill catalogs (mattpocock/skills, NateBJones-Projects/OB1) may be archived/unmaintained. No warning when a project installs a dead skill.

**Fix:** Add to `docs/agents/skills.md`:

```markdown
## Deprecated skills

| Name | Reason | Replacement | Last working | Status |
|------|--------|-------------|--------------|--------|
| (none yet) | — | — | — | — |

**Process:** When a skill goes unmaintained or is replaced:
1. Add it here with last-known working date and replacement.
2. Do NOT delete from external catalogs — link here instead.
3. Log in docs/decisions.md why we deprecated it.
```

Also update D-002 and D-003 in `docs/decisions.md` to add revisit condition:
```
Revisit when: ... OR the skill goes unused/unmaintained for 3+ months, OR a better replacement appears.
```

**Effort:** 1 hour  
**Status:** ✅ Done — see [`docs/agents/skills.md`](agents/skills.md)'s "Deprecated skills"
section (D-005).

---

### High-Priority Additions (Do within 2 weeks)

#### 7. Add decision evidence links
**File:** `docs/decisions.md` (update format)  
**Problem:** Decisions are logged but don't link to proof. Hard to audit: "Why was this choice made?"

**Fix:** Update each D-NNN entry to include:

```markdown
## D-XXX | YYYY-MM-DD | <title>

Status: active
Evidence:
  - Gauntlet ledger: [gauntlet/ledger.md](../gauntlet/ledger.md)
  - Related PR: #42
  - Triage log: [inbox/triage-log.md](../inbox/triage-log.md#L15)
Context: ...
Decision: ...
Consequences: ...
Revisit when: ...
```

Apply to D-001, D-002, D-003 immediately.

**Effort:** 1 hour  
**Status:** ✅ Done — see the D-001–D-006 entries in [`docs/decisions.md`](decisions.md),
each with an Evidence block.

---

#### 8. Add template maintenance runbook
**File:** Create `docs/MAINTENANCE.md`  
**Problem:** README says "feed improvements back" but doesn't explain how. Unclear when to update template vs. when it's project-specific.

**Fix:** Create `docs/MAINTENANCE.md`:

```markdown
# Maintaining This Template

This file is for template repo contributors (blue-ridge-code/vscode-template).
If you are using a copy as a new project, see README.md "After kickoff" instead.

## When to update the template

**Yes:**
- Bug in AGENTS.md or core workflow
- New tool/MCP/registry pick that is strictly better and affordable
- Missing guidance that causes confusion across multiple projects
- Doc rot (broken links, stale dates)

**No:**
- Project-specific hacks (stays in that project's docs/decisions.md)
- One-off utilities (stays in that project's scripts/)
- Tool swaps for budget reasons (log in decisions.md, only update template if pattern repeats)

## Contribution workflow

1. **Test.** Create a test project from the template. Run your change end-to-end.
2. **Document.** Log change in docs/decisions.md (D-NNN).
3. **Commit.** Include test project name: "Tested on <name> for <use case>."
4. **Verify.**
   - `pwsh scripts/sync-skills.ps1 --Verify` passes
   - No new speculative scaffolding (check for empty dirs)
   - All AGENTS.md pointers resolve
   - skills.md and services.md dates are current

## Quarterly maintenance

- [ ] Re-run MCP census (docs/agents/services.md line 11)
- [ ] Check Last evaluated dates in skills.md, services.md, utilities.md
- [ ] Audit external catalogs for deprecated skills
- [ ] Review decision log for patterns (if same swap repeats, update template)

Trigger: First Monday of the quarter. Log results in docs/decisions.md.
```

**Effort:** 1 hour  
**Status:** ✅ Done — see [`docs/MAINTENANCE.md`](MAINTENANCE.md).

---

#### 9. Add skill composition map
**File:** Create `docs/agents/skill-composition-map.md`  
**Problem:** Users can accidentally install incompatible skills. Ontology-agent + gauntlet-loop pair is only documented in a Note.

**Fix:** Create `docs/agents/skill-composition-map.md`:

```markdown
# Skill Composition Rules

## Pairs well

| Skill A | Skill B | Why |
|---------|---------|-----|
| **ontology-agent** | **gauntlet-loop** | Ontology gates correctness (tool calls); gauntlet judges quality. No overlap. |
| **wayfinder** | **grilling** | Grilling settles terminology → feeds wayfinder map. Sequential, not concurrent. |
| **language-persona** | (any) | Orthogonal. Applies to output of all skills. |
| **code-review** | **gauntlet-loop** | Code review is one critic pattern; gauntlet loop is the full orchestration. Compose as needed. |

## Forbidden

| Skill A | Skill B | Why |
|---------|---------|-----|
| **gauntlet-loop** | **gauntlet-loop** | No nested loops (token explosion, cost spiral). One loop per work item. |
| **GitHub Issues tracker** | **docs/backlog.md tracker** | Never run both simultaneously. One tracker per project; switch at kickoff only. |

## When in doubt

- Check if Skill B is a *composition* (builds on A's output) or a *competitor* (reimplements A's job).
- If composition: sequence them, pass output as input.
- If competitor: pick one. Log your choice in docs/decisions.md.
- Ask before installing an external skill if you haven't seen it composed with your current stack.
```

**Effort:** 1 hour  
**Status:** ✅ Done — see [`docs/agents/skill-composition-map.md`](agents/skill-composition-map.md).

---

### Medium-Priority Additions (Do within 1 month)

#### 10. Skills lack success criteria
**File:** Create `docs/agents/skill-verification-checklist.md`  
**Problem:** gauntlet-loop and ontology-agent have success criteria, but other skills don't. Hard to verify a skill is working.

**Fix:** Create `docs/agents/skill-verification-checklist.md`:

```markdown
# Skill Verification Checklist

Every skill must pass before installing or updating:

- [ ] Description (frontmatter) describes *when* to fire, not *what* it does
- [ ] No external runtime dependencies (use utilities.md for approved deps)
- [ ] Portable format (Markdown + frontmatter only, no hidden scripts)
- [ ] Success criteria exist and are testable facts, not aspirations
- [ ] Errors are explicit with clear guidance (no silent failures)
- [ ] Composition rules documented (incompatibilities called out)
- [ ] References any external repo/version that must stay in sync

Use this as a gate for external skills (mattpocock, anthropics, NateBJones).
```

**Effort:** 1 hour  
**Status:** ✅ Done — see [`docs/agents/skill-verification-checklist.md`](agents/skill-verification-checklist.md)
(D-007, merged in parallel with D-008).

---

#### 11. Voice guides need concrete examples
**File:** `docs/agents/voice/` (all 8 guides: A1–B3)  
**Problem:** Guides are abstract. Before kickoff fills them, no concrete before/after examples exist.

**Fix:** Add to each guide (e.g., `docs/agents/voice/a1-tone.md`):

```markdown
### Template example

**Before:**
"It is hereby directed that subsequent operations shall be executed..."

**After:**
"Follow `AGENTS.md` Rule #1 — run the `kickoff` skill before any other work."

_Why: Direct imperative, no legalese, assumes capable reader._
```

Apply to all 8 guides. Use examples from actual AGENTS.md, README.md, or skills.

**Effort:** 2 hours  
**Status:** ✅ Done — all 8 guides under `docs/agents/voice/` have a "Template examples"
section, e.g. [`docs/agents/voice/a1-tone.md`](agents/voice/a1-tone.md).

---

#### 12. Add model evaluation template
**File:** Create `docs/agents/model-evaluation-template.md`  
**Problem:** model-roles.md says "verify current pricing" but gives no procedure.

**Fix:** Create `docs/agents/model-evaluation-template.md`:

```markdown
# Evaluating a New Model

Use this checklist when considering a model to add to model-roles.md.

## Quick check

- [ ] Supports skill mechanism (e.g., .claude/skills/, system prompts)?
- [ ] Cost per 1M input tokens?
- [ ] Cost per 1M output tokens?
- [ ] Max input context?
- [ ] Tool-use fidelity?

## If you pass quick check, run this test

[Pick a small, reversible task that exercises the skills you plan to use.]

## Record results

```markdown
### Evaluation: <model name>

Date: YYYY-MM-DD
Tested on: [task description]

**Quality:** Equal/Better/Worse than [current pick]
**Cost:** $X per hour vs. [current pick]
**Reliability:** [Any failures or edge cases?]
**Recommendation:** Swap | Keep current | Monitor

Log this in docs/decisions.md before committing changes.
```

**Effort:** 1 hour  
**Status:** ✅ Done — see [`docs/agents/model-evaluation-template.md`](agents/model-evaluation-template.md)
(D-007, merged in parallel with D-008).

---

### Low-Priority Nice-to-Haves (Do if you have time)

#### 13. Copilot configuration underdocumented
**File:** `docs/agents/model-roles.md` (expand)  
**Problem:** Copilot users may create custom agents when they should use unified AGENTS.md.

**Fix:** Add section to model-roles.md with Copilot configuration map and guidance on when to use custom agents vs. unified instructions.

**Effort:** 30 min  
**Status:** ✅ Done — see the "Copilot: configuration map" section in
[`docs/agents/model-roles.md`](agents/model-roles.md) (D-007, merged in parallel with D-008).

---

## Summary: Work Breakdown

| Priority | Count | Items | Status |
|----------|-------|-------|--------|
| ✅ Completed | 2 | PROJECT.md kickoff, services.md census | Done |
| 🔴 Critical | 4 | Skills registry, layer guide, drift gate, deprecation | ✅ Done (#3–6, D-008) |
| 🟠 High-priority | 3 | Decision evidence, maintenance runbook, composition map | ✅ Done (#7–9, D-008) |
| 🟡 Medium-priority | 2 | Skill verification (#10), voice examples (#11) | ✅ Done (D-007, D-008) |
| 🟢 Nice-to-have | 1 | Model evaluation (#12), Copilot config (#13) | ✅ Done (D-007) |

All 13 numbered items are closed. #10, #12, and #13 were built by a parallel branch
(`agent/tool-reliability-e1-e2` / `agent/provider-independence-f1-f2`, logged as D-007)
that merged into `main` while this file's own #1–9 and #11 fixes (D-008) were in progress
on a separate branch — reconciled here rather than duplicated.

---

## Next Steps

None. Every item in this review is closed (see each item's Status line for evidence, and
D-007/D-008 in `docs/decisions.md` for the two merged bodies of work).

