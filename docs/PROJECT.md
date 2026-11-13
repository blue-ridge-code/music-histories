# Project: <project name>

> **Status: kickoff-pending** (default for repositories created from this template)
> Agents: run the `kickoff` skill before any other work (AGENTS.md, Rule #1).
> Lifecycle: `kickoff-pending` -> `planning-active` -> `implementation-ready` -> `operational`
> (see [docs/agents/lifecycle.md](agents/lifecycle.md) for what each phase permits and the
> `Status: active` migration rule). Minimal kickoff ends at `planning-active` — it does not
> wait on optional runtimes, full provider configuration, device access, or implementation
> tooling.
> Template-source exception: if `git remote get-url origin` points to
> `blue-ridge-code/vscode-template` (HTTPS or SSH), skip kickoff and preserve this file as
> distributable template content.

## Mission

<!-- One paragraph: what this project is and why it exists. -->

## Project type

<!-- software | writing | research | admin-errand | organization | mixed -->

## Project shape

<!-- Scale band: 1 | 2-5 | 6-20 | 20+ top-level work areas.
     Count modules/packages/services for software; count distinct work-product or
     subject-area folders otherwise. Exclude repository support folders.
     Writing/research/mixed: also record expected source-file count when relevant.
     Session horizon: single-session | multi-session. -->

## Stakeholders and audience

<!-- Who this is for; who is affected; who approves external-facing output. -->

## Definition of done

<!-- Observable end state. How will we know this project succeeded? -->

## Hard constraints

<!-- Deadlines, budget, privacy requirements, legal/safety boundaries. -->

## Autonomy level

<!-- Agreed at kickoff, per AGENTS.md "Human gates". Note any project-specific
     additions to the human-owned list. -->

## Lifecycle phase

<!-- Current phase: kickoff-pending | planning-active | implementation-ready | operational.
     Record the date each phase was entered and, for implementation-ready, the owner who
     approved the transition and the date. See docs/agents/lifecycle.md. -->

## Architecture / areas of concern

<!-- Software: modules with small, non-overlapping boundaries (nested AGENTS.md per area).
     Non-software: the work products and folder conventions. Decided at kickoff. -->

## Activated layers

<!-- Apply docs/agents/layer-activation-guide.md. Record wiki, intake, tracker, and
     external-tool decisions with reasons. Delete what is not activated. -->

## Skills installed

<!-- Core/default: human-review-queue ships checked in; its runtime deploys only when the
     project has a concrete review gate. Kickoff selects skills for every phase but installs
     just-in-time, in three buckets — record each skill under the bucket it's in:
       - Installed now (planning phase): wayfinder, grilling, and any of research /
         domain-modeling / prototype the project selected. Recorded in skills-lock.json.
       - Selected; installs at first session boundary: handoff.
       - Selected; installs at implementation-ready: codebase-design, tdd, diagnosing-bugs,
         code-review (whichever the project selected).
     ontology-agent: record "selected; activation deferred" here if chosen before the
     project has 6+ real modules or real dependency manifests (see layer-activation-guide.md
     and the ontology-agent SKILL.md). -->

## Tracker

<!-- GitHub Issues (default for repos) | docs/backlog.md (local mode) |
     none (single session, no blockers or dependencies) -->
