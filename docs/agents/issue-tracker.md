# Issue tracker conventions

Use one tracker per project when the tracker layer is active: **GitHub Issues** when the
project is a GitHub repository, otherwise **`docs/backlog.md`** (local mode, created at
kickoff). Never run both. A single-session project with no blockers or dependencies can
record `none` in `docs/PROJECT.md`; its current user request is its work boundary. If work
continues into another session or gains dependencies, activate one tracker before adding
new work. Once active, nothing about a unit of work exists outside its tracker entry.

## Current project override

Music Histories temporarily uses [docs/work-plan.md](../work-plan.md) as its sole
tracker, carried forward from the owner-authorized local preparation phase.
GitHub API access is now verified; this is no longer a connectivity claim.
Keep this explicit override until a one-time migration creates the issue map,
work items and dependency links, then retire the local work plan. Do not create
an independent parallel issue backlog. The conventions below still apply to the
future GitHub tracker. This restoration does not perform the migration.

## Mode selection

| Condition | Tracker |
|---|---|
| Single session with no blockers or dependencies | None; record the reason in `docs/PROJECT.md` |
| Project is (or becomes) a GitHub repo | GitHub Issues — the sole tracker |
| Local-only project | `docs/backlog.md` — created at kickoff |

Use the `gh` CLI for scripted tracker operations (`gh issue list`,
`gh issue view`, `gh issue create`, `gh issue comment`, `gh issue close`). If a
local project later gains a GitHub remote, migrate the open backlog rows to
issues once, then retire `docs/backlog.md` with a superseded banner.

## Title standard

One pattern for every issue — map, decision, task, sub-issue:

```text
<Imperative verb> <specific outcome>
```

Sentence case, no trailing period. Prefer concrete verbs: `Choose`, `Define`,
`Design`, `Prototype`, `Assemble`, `Complete`, `Verify`, `Fix`, `Maintain`.

Examples:

- `Choose the first audience and editorial promise`
- `Prototype the production pipeline`
- `Fix the broken CSV export`

Never put in a title:

- the issue number or a custom sequence (`009`, `007.02`);
- parent, blocker, or dependency references;
- status, priority, assignee, type, or milestone words;
- a type or scope prefix that duplicates structured metadata.

`#N` is the issue's stable identifier; native sub-issue and `blocked by` links
express hierarchy and order. Those relationships change without forcing a title
rename — keep identity and state out of titles.

## Wayfinder mapping

- One issue labeled `wayfinder:map` is the durable map anchoring the effort.
- Every ticket (one decision- or outcome-sized unit of work, sized to one
  session) is a sub-issue of the map. If sub-issues are unavailable, maintain
  a task-list of links in the map issue body.
- Express execution order with native `blocked by` / `blocking` dependencies;
  fall back to `Blocked by #N` in the issue body.
- Put the ticket type in the body (`research`, `prototype`, `grilling`,
  `task`), not in the title.
- Human-in-the-loop decisions stay open until the named human decides.

**Native dependencies are the ONLY open/blocked status mechanism.** The
frontier — what is open, unblocked, and unclaimed — is read from the dependency
graph, not from a list. Never hand-maintain parallel status labels (e.g.
`wayfinder:blocked`, `wayfinder:frontier`), status sections in docs, or
frontier lists: they are a second copy of state the graph already renders, and
they go stale the moment a blocker closes and no one flips them.

**One roadmap.** The map issue plus the dependency graph is the default roadmap view.
Do not also run a GitHub Project board or milestone over the same work — that is the same
parallel-copy failure as a hand-maintained status label. At kickoff, a software project
with 20+ top-level modules gets a recommendation to use GitHub Projects as the sole
roadmap view. If Projects is chosen at kickoff or adopted later, do not create a map issue,
or migrate once and close the existing map issue with a pointer to the board.

## Claiming and sessions

Claim a ticket with a **claim comment** before work begins; post a release
comment when you finish, pause, or hand off. The comment format, session tags,
and staleness rule live in [model-roles.md](model-roles.md) — one protocol,
one home.

Assignment means something different: **human ownership**. Assign an issue only
when a named human owns the decision (HITL tickets stay open until that human
decides). Every agent session authenticates as the same GitHub identity, so an
assignment cannot distinguish a live agent session from a stale one — the claim
comment is the only session signal. Do not assign to claim.

## Resolution checklist

Before closing an issue:

1. Comment with the outcome, the evidence, and any follow-up decisions.
2. Verify the work — run the tests, inspect the rendered output, or cite
   `file:line` proof. "Done" without evidence is not done.
3. Link the durable artifact — document, prototype, or commit — that records
   the result.
4. Update every doc the result touches; log significant choices in
   [../decisions.md](../decisions.md).
5. Close only when the stated decision or deliverable is complete. Do not close
   a decision ticket because research merely narrowed the options.

## Local mode: `docs/backlog.md`

Kickoff creates the file with one table and nothing else:

```markdown
| ID | Outcome | Status | Evidence |
|----|---------|--------|----------|
| B1 | Choose the first audience | open | — |
```

- IDs are stable (`B1`, `B2`, …) and never reused.
- Outcome follows the same imperative title standard as issue titles.
- Status is one word: `open`, `blocked`, `claimed`, `done`. Note the blocker
  or claimant inline (`blocked by B3`).
- Evidence links the commit or doc proving `done`.
- Completed rows stay in the table; prune only when the file stops scanning.
