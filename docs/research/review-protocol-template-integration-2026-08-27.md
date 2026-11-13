# VSCode-Template Review Protocol integration evidence — 2026-08-27

Issue: `blue-ridge-code/commute-dispatch#41`

## Exact boundary

The local template branch starts at
`7e605b0ef9e7a9a7b2a4bb038947e7cb1e1c0672`. It adds the dormant repository-side
Review Protocol contract to the canonical `human-review-queue` skill and its generated
Claude mirror. The template remains `kickoff-pending`; installing the skill starts no
process and creates no host enrollment, source allowlist, notification, response route,
credential, scheduler entry, or execution adapter.

## Integration and provenance

- Integration version: `1.0.0`.
- Review Protocol: `1.0`.
- Contract owner: `blue-ridge-code/commute-dispatch`.
- Template owner: `blue-ridge-code/vscode-template`.
- Last evaluated: `2026-08-27`.
- Generated default source mode: `disabled`.
- Generated response writer: `disabled`.
- Privacy: `local_only`.
- Immutable GitHub repository ID: intentionally unresolved until a later exact
  host-enrollment preview verifies it without adding network authority to the installer.

## Generated-project and skill verification

- Installer unit test — 1 passed. It verifies the generated contract, repository name,
  unresolved immutable ID, disabled mode, and disabled response writer.
- `scripts/tests/test_review_queue_deploy.py` — 21 checks passed. A disposable generated
  project installed the queue, selected a free loopback port, started the real Python
  server, returned HTTP 200 and the correct service/project identity, then terminated the
  process. This is the portable start, status/identity, verification, and stop path; it
  does not depend on PowerShell.
- Ontology validator self-test — all checks passed.
- System skill validator — `Skill is valid!`.
- Skill mirror — 58 canonical files verified with no drift.
- `git diff --check` — passed.

The generated-project test proves the portable local service lifecycle. A real remote-IDE
port-forwarding and safe browser-access trial remains unsupported and unverified; this
change does not claim remote deployment readiness.

## Canonical and mirrored changes

The canonical files live under `.agents/skills/human-review-queue/`. The repository's
`scripts/sync-skills.ps1` generated the matching `.claude/skills/human-review-queue/`
files. The skill entrypoint points agents to the detailed contract schema only when they
deploy or review a queue, preserving progressive disclosure.

## Backup and rollback

The exact Git baseline preserves every tracked file. The integration changes no runtime
or machine-local state, so no additional data backup is required. Before publication,
rollback is the reviewed removal of this isolated worktree/branch or a new branch from
the exact baseline. Keep the template source checkout and generated-project evidence
separate from project-owned work.

## Remaining disabled or unsupported paths

Host enrollment, source observation, Hub projection, response routing, notifications,
provider execution, credentials, scheduler/listener installation, public access,
remote-IDE port forwarding, push, merge, and deployment remain disabled, unsupported, or
separately gated.
