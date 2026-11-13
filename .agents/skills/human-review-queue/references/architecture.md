# Architecture

## Purpose

The queue separates four events:

1. A project creates a bounded Review Queue Entry.
2. An approved reviewer submits a Queue Response for an exact version.
3. The service writes an append-only decision record.
4. A terminal response can create one bounded Agent Action.

This order protects the human decision if the action bridge fails.

## Retained Leng features

The template retains these behaviors from Leng:

- one calm decision surface with previous and next navigation
- open-first and newest-first ordering
- compact completed entries
- radio choices, one recommendation, effects, notes, and `Other`
- playable video and audio, images, captions, direct artifact links, and interface review
- drafts scoped to entry ID and reviewed version
- explicit server-side draft save
- polling that does not replace an active edit
- conflict notice when another tab completes a drafted entry
- atomic JSON writes and immutable completed responses
- semantic idempotency for browser retries
- append-only decision records and a regenerated non-canonical profile
- grouped follow-up actions, idempotent GitHub markers, and retry after bridge failure
- loopback binding, same-origin checks, a per-process request token, a CSP, no-store API responses, and a 1 MiB body limit
- manual start, Windows Task Scheduler installation, scan commands, and Python and browser tests

## Reviewer routing

The reviewer registry is the authority for reviewer IDs, active state, roles, and parent links. An entry can use:

- `stages`: an explicit sequence of reviewer IDs or roles
- `parent_chain`: one starting reviewer followed by approved parent links

A stage advances only when one choice reaches its declared quorum. A `stop` option ends the route. If all assigned reviewers respond without a quorum, the queue advances to the next declared stage as a conflict. If no stage remains, the gate ends as `conflict` and dispatch stays disabled.

Each reviewer sees one filtered page. The page contains entries currently assigned to that reviewer and entries that reviewer already answered. Prior-stage decisions appear with the next review.

## Review hub

`review-queue/hub.json` lists queue sources. The default source is the current repository. A hub can add other local repository roots and combine their assigned entries into one webpage per reviewer.

Use stable reviewer IDs across source registries. Each source keeps its own queue, runtime responses, decision log, repository boundary, and dispatch config. The hub routes a response back to the source that owns the entry.

Do not use arbitrary browser-supplied paths. The server accepts only source roots declared in `hub.json`.

## Durable and local data

Commit these files:

- `review-queue/config.json`
- `review-queue/reviewers.json`
- `review-queue/hub.json`
- `review-queue/queue.json`
- `docs/agents/review-decisions/log/*.json`
- `docs/agents/review-decisions/profile.md`

Ignore `review-queue/.runtime/`. It contains machine-local queue state, draft responses, action retries, and logs. A completed response becomes durable only after the decision record reaches the target repo's system of record.

## Extension points

The default action adapter is `none`. The included `github_issue` adapter can comment on governing issues and create one labeled follow-up issue. Add another adapter only when it preserves idempotency, records failures, restricts destinations, and cannot broaden the entry boundary.

The queue is a local standard-library service. A network deployment needs an authenticated ingress, TLS, reviewer identity mapping, CSRF protection suitable for that ingress, access logs, backups, retention rules, and a threat review.
