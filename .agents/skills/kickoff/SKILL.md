---
name: kickoff
description: "Run the first-session orientation that turns this template into a scoped project — interview the user, define architecture, select and install skills, activate layers, line up connector authorizations, and rewrite the README for the new project. Fire whenever docs/PROJECT.md shows `Status: kickoff-pending`, before any other work (AGENTS.md Rule #1), except when origin points to the canonical blue-ridge-code/vscode-template source repository."
---

# Kickoff

## Problem

A fresh template copy is generic: no mission, no tone, no skills, no tracker, no
authorized connectors. Agents that start task work before orientation guess at scope and
leave the project unconfigured. Kickoff converts the blank template into a configured
project in one guided session.

## When to use

- [docs/PROJECT.md](../../../docs/PROJECT.md) contains `Status: kickoff-pending`, unless
  this is the canonical template-source checkout described below.
- The user says "set up this project" or "start the kickoff".

## When NOT to use

- `git remote get-url origin` points to `blue-ridge-code/vscode-template` (HTTPS or SSH).
  This is the template source; preserve its `kickoff-pending` content for new copies.
- `Status: planning-active` or later — the project is already scoped; do task work instead
  (see [docs/agents/lifecycle.md](../../../docs/agents/lifecycle.md) for the phase model).
- To re-scope a configured project. Edit docs/PROJECT.md directly and log the change in
  [docs/decisions.md](../../../docs/decisions.md) instead.

## Process

1. **Interview — one question at a time.** Never batch questions. Cover, in order:
   purpose; project type (`software | writing | research | admin-errand | organization |
   mixed`); project shape; stakeholders and audience; definition of done; hard
   constraints (deadline, budget, privacy, legal); autonomy level (additions to the
   human-gates list in AGENTS.md); tracker choice (GitHub Issues, `docs/backlog.md` local
   mode, or no tracker for a single session with no blockers or dependencies).
   - Ask: "How many top-level work areas does this project have: 1, 2-5, 6-20, or
     20+?" Explain that software counts modules, packages, applications, or services;
     other types count distinct work-product or subject-area folders. Exclude repository
     support folders.
   - For writing, research, or mixed work, ask how many source files are expected.
   - Ask whether the work is single-session or multi-session. Ask about input frequency
     and external APIs only when those answers affect layer activation.
2. **Shape-based layer selection.** Read and apply
   [docs/agents/layer-activation-guide.md](../../../docs/agents/layer-activation-guide.md).
   Walk its table with the user, state each default activation or omission, and record
   overrides with reasons. In particular:
   - Do not bootstrap `ontology-agent` from a count of provisional concerns, planned
     features, or support folders (`inbox/`, `gauntlet/`, and similar repository support
     folders never count). Activate it only once the architecture defines 6+ **real**
     modules/packages/services, or real dependency manifests and structural relationships
     exist, and the project has concrete structural questions the graph will answer.
     During early planning, before architecture is defined, record ontology in
     `docs/PROJECT.md` as "selected; activation deferred" rather than bootstrapping
     speculatively.
   - For 6+ software modules on GitHub, suggest a GitHub connector, MCP server, or CLI.
   - For 20+ software modules, recommend GitHub Projects as the sole roadmap view; do
     not maintain it beside a wayfinder map.
   - Offer the wiki layer to writing projects with 10+ expected source files.
3. **Architecture & skills selection.** Propose areas of concern / work-product structure
   for the chosen type and shape. Present the typed skill menu and let the user pick — but
   selecting a skill and installing it are different steps; step 6 installs just the
   planning-phase bucket now:
   - Planning-phase defaults for every project (install now, step 6): `wayfinder` +
     `grilling`.
   - Checked-in core/default: `human-review-queue` is already available in every template
     copy. Do not deploy its runtime queue during kickoff; install it on demand when the
     project has a concrete repeated, asynchronous, or artifact-review gate. Keep dispatch
     disabled and `single_local` loopback identity as the deployment defaults.
   - Writing → `language-persona` (ships with this template, no install needed) + docx/pdf
     skills on demand.
   - Research → `research` skill (install now) + wiki layer per
     [docs/agents/wiki.md](../../../docs/agents/wiki.md).
   - Software → `domain-modeling` + `prototype` if selected (install now, planning phase);
     `handoff` (record selected, install only at the first real session boundary);
     `codebase-design` + `tdd` + `diagnosing-bugs` + `code-review` (record selected, install
     only at `implementation-ready`); CI setup happens at the implementation gate, not here.
4. **Fill the minimal tone profile.** Minimal kickoff captures four things into
   [docs/TONE.md](../../../docs/TONE.md): target tone words, anti-tone words, audience,
   and any essential technical or participant-facing language constraint. Ask them as part
   of the interview, one at a time. Do not work through the eight component guides under
   `docs/agents/voice/` (e.g. [a1-tone.md](../../../docs/agents/voice/a1-tone.md)) at
   kickoff — each guide already documents a median default; set every guide's
   "Project setting" to
   "kickoff default — median, unrefined" rather than interviewing it. Offer the full
   A1–B3 voice workshop explicitly as a later, optional writing/artistic-direction task —
   never a condition of entering planning.
5. **Fill the project file.** Complete every section of docs/PROJECT.md, including its
   scale band, counted work areas, source-file estimate when relevant, session horizon,
   and reasons for layer activation. Log inception decisions in docs/decisions.md, using
   the next free ID (D-001 onward).
6. **Install skills just-in-time.** Install only the planning-phase bucket now: run
   `npx skills@latest add mattpocock/skills` for the selected planning-phase skills
   (`wayfinder`, `grilling`, and any of `research` / `domain-modeling` / `prototype`
   selected), then run `scripts/sync-skills.ps1` to mirror `.agents/skills` into
   `.claude/skills`. Do not install `handoff` here — record it as selected in
   `docs/PROJECT.md` and install it only at the first real session boundary that needs it.
   Do not install implementation-phase skills (`codebase-design`, `tdd`, `diagnosing-bugs`,
   `code-review`) here — record them as selected and install them only once the project
   reaches `implementation-ready`. The checked-in `human-review-queue` skill needs no
   install here; leave its runtime undeployed until a concrete review workflow calls for
   it.
7. **Activate the selected layers** — only those selected in step 2:
   - Wiki: create the `raw/` + `wiki/` + `index.md` + `log.md` skeleton.
   - Intake: create `inbox/` + `sources/` per
     [docs/agents/intake.md](../../../docs/agents/intake.md).
   - Tracker: GitHub Issues — create labels and either the wayfinder map issue or the
     chosen GitHub Project roadmap via `gh`; local mode — create `docs/backlog.md`; no
     tracker — record the reason in `docs/PROJECT.md` and create no tracker artifacts.
   - Skills maintenance: GitHub mode uses the checked-in quarterly reminder and weekly
     self-test workflows. In local mode, seed an open backlog row named
     `Refresh skills registry and run self-tests by YYYY-MM-DD`, dated three months after
     kickoff. Each completed refresh adds the next dated row.
8. **Run only the "needed now" preflight.** Per the split in
   [docs/agents/services.md](../../../docs/agents/services.md#preflight-vs-on-demand),
   check only what the next step actually needs: `python --version` (≥ 3.10, UTF-8 usable)
   if any selected skill runs Python; an available PowerShell flavor on Windows; Node only
   if selected tooling needs it; `gh auth status` and a re-run of the MCP census (replacing
   its dated source-host snapshot with current host results) only if GitHub Issues or an
   MCP connector is the chosen tracker/tooling; sandbox or filesystem constraints relevant
   to the next operation. Defer everything else — device access (ADB, mobile pairing, and
   similar), specialized runtimes, editor extensions, credentials, and MCP connectivity
   unrelated to what was just selected — to the ticket that actually needs it; record the
   deferral, do not chase it now. Classify a failure before acting on it: a proxy/DNS/
   sandbox restriction is not an auth failure — never turn an environment restriction into
   an OAuth request. Never authorize anything external silently — OAuth flows, mobile-app
   pairing, and VSCode extension installs go to the human list regardless of when they're
   triggered.
9. **Rewrite README.md.** All planning input is gathered by now — interview, shape, tone,
   project file, layers, preflight — so rewrite the template README to describe the scoped
   project. If `README.md` still describes itself as the template ("Generate a new project…"),
   rewrite it in place: project name, mission (from docs/PROJECT.md), project type and shape,
   how to work on it (pointer to `AGENTS.md`, `docs/PROJECT.md`, `docs/TONE.md`,
   `docs/decisions.md`), and the activated layers/skills where useful. Apply the write — it
   is a local, reversible file edit, kickoff never commits, and the change is listed in the
   commit-ready summary for review. If `README.md` is already project-specific, do not
   clobber it; note that it was left untouched.
10. **Close.** Flip docs/PROJECT.md from `Status: kickoff-pending` to `Status: planning-active`
    and fill the new "Lifecycle phase" section. Print a commit-ready summary of every file
    touched. Read-only Git inspection
    (`git status`, `git diff`, `git remote`, `git config --get`) is fine throughout kickoff
    per [AGENTS.md](../../../AGENTS.md)'s Git boundary; kickoff still never runs a Git
    mutation (commit, push, branch, merge, reset, rewrite).

## Output

- Completed docs/PROJECT.md at `Status: planning-active` with its Lifecycle phase section
  filled; docs/TONE.md filled with the four minimal voice answers; every voice guide's
  Project setting set to its median default; D-001+ entries in docs/decisions.md.
- Planning-phase skills installed with `skills-lock.json`, synced to `.claude/skills/`;
  `handoff` and implementation-phase skills recorded as selected but not installed.
- Activated layer skeletons (wiki / intake / tracker) as selected.
- A report: automatable checks with pass/fail, then a **numbered checklist of human-only
  authorizations**, a note on any deferred (not-yet-needed) environment items, then the
  commit-ready summary — including the README.md rewritten in place when it still read as
  the template (left untouched when already project-specific).

## Notes

- Missing optional docs: the `docs/agents/*.md` guides and `scripts/` ship with this
  template but may be absent in a trimmed copy. Follow the behavior described above
  anyway and record the gap in the kickoff report.
- This skill creates files but never commits, never sends, never authorizes.
- Keep the interview conversational; the user may say "skip" and take the default.
- Composition: prerequisite for every other skill — it selects all of them and installs
  the planning-phase bucket just-in-time; see
  [skill-composition-map](../../../docs/agents/skill-composition-map.md).
