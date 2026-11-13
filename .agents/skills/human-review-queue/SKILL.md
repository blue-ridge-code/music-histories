---
name: human-review-queue
description: Deploy and operate a durable human review queue in a repository, with inspectable evidence, bounded choices, version-scoped decisions, append-only records, reviewer assignment and approval chains, per-reviewer unified views, safe follow-up dispatch, and local service installation. Use when a project needs structured human gates, asynchronous approvals, reviewer routing, media or artifact review, decision provenance, or a reusable alternative to ad hoc approval prompts.
---

# Human review queue

Deploy a repository-owned review service that records the human response before it starts follow-up work. Keep decision authority separate from agent execution authority.

## Choose the operation

- **Review an existing queue:** Inspect its config, queue entries, runtime state, tests, listener, decision log, and follow-up adapter. Do not change state unless the user asks.
- **Deploy a queue:** Run the installer, set the reviewer registry, configure the dispatch adapter, and run all tests.
- **Add a gate:** Create one Review Queue Entry, validate it, enqueue it, and verify the exact artifact is inspectable.
- **Operate a gate:** Scan first. Treat a completed Queue Response as a human decision. Do not ask the reviewer to repeat it.
- **Add reviewers or routing:** Update the approved reviewer registry first. Then add explicit routing stages or a reviewer-parent chain.
- **Build a review hub:** Register repository queue roots in one hub. Give each approved reviewer one filtered page across the registered sources.

Read [references/architecture.md](references/architecture.md) before deployment or architecture changes. Read [references/schema.md](references/schema.md) before creating config, reviewer, route, or entry JSON. Read [references/security.md](references/security.md) before any non-loopback deployment or identity change.

## Deploy

1. Inspect the target repo's instructions, dirty worktree, tracker, and existing gate language.
2. Run:

   ```powershell
   python <skill-dir>\scripts\install_review_queue.py --repo . --project-id <id> --project-name "<name>" --repository <owner/repo> --reviewer-id <id> --reviewer-name "<name>"
   ```

3. Review `review-queue/config.json`, `review-queue/reviewers.json`,
   `review-queue/hub.json`, and the dormant `review-queue/control-plane.json` contract.
   Resolve its immutable GitHub repository ID before proposing host enrollment.
4. Keep `dispatch.adapter` set to `none` until the user approves the exact follow-up system, repository, label, and boundary.
5. Add the instruction block from [references/handoff.md](references/handoff.md) to the repo's agent instructions. Preserve stronger existing rules.
6. Run the installed Python and browser tests.
7. Start with `scripts/start-human-review-queue.ps1 -NoDispatch`.
8. Verify the loopback URL and API return HTTP 200. Do not state that the page opened unless it did.
9. Add one disposable test entry. Confirm media, drafts, response recording, decision logging, routing, and a no-dispatch terminal result.
10. Remove the disposable entry only if it is clearly test data and has no durable response.

The installer never overwrites an existing queue unless the operator uses `--force`. Treat `--force` as destructive. Inspect every target first.

Composition: boundary layer — orthogonal to skill choice; it gates any skill's output behind a durable human review ([skill-composition-map](../../../docs/agents/skill-composition-map.md)).

## Create a Review Queue Entry

1. Name the exact reviewed version. Use a hash when the artifact can change in place.
2. Classify the gate as actionable Type A or B. Keep Type C information out of the action queue.
3. Give numbered review steps and named success criteria.
4. Render the exact item as video, audio, image, or a direct HTTPS or loopback link. Use `none` only when the queue page is the reviewed item.
5. Ask one bounded question. Provide mutually exclusive choices, one recommended choice, effects, and `Other`.
6. Define a route that resolves only to active reviewers in the registry. Use explicit stages for role separation. Use a parent chain only for real approval escalation.
7. Declare the possible Agent Action with `job`, `tool`, `categories`, `output`, and `boundary` even when dispatch is disabled.
8. Validate and enqueue:

   ```powershell
   python scripts/human_review_queue.py validate path\to\entry.json
   python scripts/human_review_queue.py enqueue path\to\entry.json
   ```

9. Scan the queue and confirm the entry is assigned to the intended reviewer.

## Pause at the human gate

Follow [references/handoff.md](references/handoff.md). Put the full review path, choices, effects, recommendation, fallback response, and record location in the final response.

Open the queue page or review link in the default browser (`Start-Process <url>` on Windows, `open <url>` on macOS, `xdg-open <url>` on Linux) so the reviewer does not copy-paste the URL.

When the queue is available, its form is the response path. Do not also require an IDE reply. Release any tracker claim before waiting when the target repo requires claim comments.

## Process a response

- Preserve the Queue Response before any follow-up.
- Record each stage response as an append-only decision record.
- Advance only through the declared route.
- Show prior-stage decisions to the next reviewer.
- Start follow-up only after a terminal stage and only when the selected option permits dispatch.
- Batch actions only when their entries share an explicit action group.
- Retry the action bridge without rewriting or duplicating the human response.
- Treat a changed artifact as a new reviewed version and a new gate.

## Fixed safety boundary

A Queue Response grants only the authority declared by its entry. It does not authorize push, merge, publication, release, external delivery, spend, credentials, destructive action, sensitive-data access, or broader rights unless the gate names that exact authority and the project permits it.

The queue is decision infrastructure. It is not an authentication provider. Keep `single_local` and `local_switcher` modes on loopback. Use `trusted_header` only behind an approved authenticated proxy. Fail closed when identity, reviewer assignment, source path, repository, or dispatch target is unclear.

## Verify

Run:

```powershell
python scripts/test_human_review_queue.py
node scripts/test_human_review_queue_client.js
python scripts/human_review_queue.py scan --json
```

Also run the skill validator after any skill change:

```powershell
python <skill-creator-dir>\scripts\quick_validate.py <skill-dir>
```

Report deployment files, reviewer mode, hub sources, Review Protocol integration version,
tests, service state, dispatch state, and uncommitted changes separately. Installing the
contract does not enroll or enable a source.
