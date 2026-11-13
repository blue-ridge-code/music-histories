# Configuration and entry schema

## Project config

`review-queue/config.json` defines the source project and fixed action boundary.

- `project.id`, `project.name`, `project.repository`: stable source identity.
- `server.port`, `server.task_name`: local service defaults.
- `server.identity_mode`: `single_local`, `local_switcher`, or `trusted_header`.
- `server.default_reviewer`: required for `single_local`.
- `server.trusted_identity_header`: required for `trusted_header`.
- `recording.log_dir`, `recording.profile_path`: repo-relative durable outputs.
- `dispatch.adapter`: `none` or `github_issue`.
- `dispatch.repository`, `dispatch.label`: exact GitHub destination when enabled.
- `dispatch.fixed_boundary`: text added to every dispatched action.

## Reviewer registry

`review-queue/reviewers.json` contains `reviewers` with:

- `id`: stable lowercase identifier.
- `display_name`: visible reviewer name.
- `active`: whether new work can route to the reviewer.
- `roles`: stable reviewer roles.
- `parent_id`: next reviewer in a parent chain, or `null`.

All referenced reviewers must be active. Parent links must not form a cycle. Disabling a reviewer with assigned open work is a migration. Reassign that work first.

## Review Control Plane integration

`review-queue/control-plane.json` is the dormant repository-side Protocol 1.0 contract.
It records the integration and protocol versions, canonical repository identity, queue
and reviewer-registry paths, stable default reviewer ID, local-only privacy, read adapter,
disabled response writer, and separately gated legacy-listener retirement. The installer
leaves `repository.github_repository_id` null because it does not call GitHub; resolve and
review the immutable repository ID before host enrollment. The host owns source IDs,
enrollment receipts, operating mode, health, findings, and allowlists.

Generated repositories always start with `mode_default: disabled` and
`adapters.response_write: disabled`. Changing either value requires a source-specific
owner decision outside the installer.

## Hub sources

`review-queue/hub.json` contains `sources` with:

- `id`: stable source identifier.
- `name`: visible project name.
- `root`: absolute path or a path relative to the hub repository.
- `enabled`: whether the hub loads the source.

The default is `{ "id": "current", "root": "." }`.

## Review Queue Entry

Required entry fields:

- `id`, `kind`, `title`, `project`, `issue`, `ticket`, `touchpoint`, `due`
- `version`, `criteria`, `steps`, `media`, `question`, `options`
- `recommendation`, `record`, `decision_type`, `human_owned_category`
- `reversible`, `routing`, `agent_action`

`touchpoint` must be `A` or `B`.

`media.type` can be `video`, `audio`, `image`, `link`, or `none`. Embedded media requires `src`. A link requires an HTTPS or loopback HTTP `href`. Captions are optional for video.

Each option requires unique `value`, `label`, and `effect`. Exactly one option has `recommended: true`. Optional fields:

- `route`: `advance`, `complete`, or `stop`. The default advances when another stage exists and completes at the last stage.
- `dispatch`: whether a terminal selection can create follow-up work.

The UI always adds `Other`. `Other` requires notes, stops the declared route, and never dispatches automatically unless the entry sets `other_dispatch: true`.

## Routing

Explicit stages:

```json
{
  "mode": "stages",
  "stages": [
    {"id": "subject", "roles": ["subject-matter"], "approvals_required": 1},
    {"id": "owner", "reviewer_ids": ["owner"], "approvals_required": 1}
  ]
}
```

Parent chain:

```json
{"mode": "parent_chain", "start_reviewer_id": "editor", "include_start": true}
```

A stage can use `reviewer_ids`, `roles`, or both. The resolved set must contain at least `approvals_required` active reviewers.

## Agent Action

Always declare:

- `enabled`, `group`, `job`, `tool`, `categories`, `output`, `boundary`

The project config owns the adapter, repository, and label. An entry cannot override those destinations.

## Queue Response

The service adds source, reviewer, route stage, exact version, criteria, timestamps, and a content-derived response ID. Completed responses are immutable. Correct a changed decision with a new entry or reviewed version.
