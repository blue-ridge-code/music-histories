# Shared-record contract · schema 1

[Scope](../docs/SCOPE.md) · [Course catalog](../courses/catalog.json) ·
[Course I working edition](../courses/course-i/editions/working/README.md)

UTF-8 CSV holds reviewable tables; JSON holds catalog/edition metadata; Markdown
explains decisions and evidence. GitHub renders these without a database service.
Private originals and source locators stay in ignored sources/raw/.
Routine public project updates are authorized by D-018; excluded raw assets and
private locators remain local. Metadata publication is not asset-rights clearance.

## Identity, editions, and releases

- Mint an immutable course ID, such as MH-C001. Display numbers/titles can change.
- Child IDs (F film, CH chapter, L listening, P page) are stable within that course
  lineage. Initial numeric suffixes were allocated from this source snapshot;
  they are not ongoing sequence numbers. Reordering changes sequence, not IDs.
- New courses get new namespaces. Do not reuse a deleted/retired ID. Refer to
  course ID + edition ID + record ID when citing a version.
- A new edition copies the [template](../templates/course-edition/README.md) or a
  prior edition. Give it a unique edition_id and directory, set based_on to the
  prior edition ID, and register it in the course catalog. Preserve IDs for
  unchanged entities; mint IDs for distinct new ones.
- Routine edits remain in an active draft; Git tracks revisions. When selection,
  intended experience, scope, or audience changes, propose a new edition.
- A release is a reviewed snapshot/tag of an edition, not a synonym for a course.
  Set release_tag only after the owner authorizes the tag/release. Keep released
  directories unchanged; a correction or variant starts a new draft based_on it.
- Color/monochrome share records unless content differs. Record format-specific
  outputs/proofs separately in the linked page-production evidence.
- Schema version describes table structure; edition ID describes course content.
  A schema change requires updated templates, validator, and migration notes.

No release or edition is approved by copying a directory. Git operations remain
subject to AGENTS.md and the owner's publication boundary.

## Five registers

| File | Identity and content |
|---|---|
| films.csv | film_id; core/extension, chapter, order, title/year, story anchor, place, functions/relationship, rationale, questions/bridge, source approval and availability |
| listening.csv | listening_id; chapter/order, common roles and original role, exact preferred/selected recording, candidate/manual/selected URLs, assigned excerpt/timings/duration, scope, source approval/playback evidence |
| chapters-pages.csv | record_id; chapter or page, film/chapter links, page number, purpose/action/load, listening IDs, copy/design/production/approval states, deliverable, criteria, reviewer, evidence |
| sources-rights.csv | source_id; title/version/date, bytes/hash/local asset, retrieval and approval, rights/credit/permitted use, publication status, reviewer |
| decisions.csv | decision_id; edition/scope, rationale, decision/status, decider/date, supersession, sources/evidence, reviewer |

Template CSV headers are the exact machine-readable field list. Empty cells mean
unknown/not yet recorded, never zero, approval, permission, or not applicable.

## References and state

All rows except source records repeat course_id and edition_id; source records
belong to the edition directory. source_refs uses semicolon-separated source IDs,
optionally #tab!cell-range or #PAGE n. Existing Sxx IDs retain their source-index
meaning. Full locators, raw exports and hashes are in the ignored local intake.

Source locators and local_asset_ref are not download links or grants of rights.
evidence_path is relative to the edition directory. It links a working production
record or decision rationale; published snapshots should link versioned evidence.
For now Amadeus's existing records are working evidence, not frozen release proof.

approval_status:
- source_recorded: the imported source reports selection/authority; no new approval.
- unreviewed / provisional / unknown: review remains.
- approval_conflict: competing approval evidence needs owner resolution.
- owner_instruction / preserve_existing: source handling authority, not print proof.
- not_approved_visual_direction: recovered production evidence, not a style exemplar.
- approved: only with named owner, date and exact evidence in a decision record.

Copy, visual, production, retrieval, rights and publication states are independent.
An imported Approve cell does not mean playable now, rights-cleared, copy-approved,
or authorized for public distribution. Source dates are not verification dates for
this repository. Keep the original source_role beside normalized roles; labels
outside the five-role vocabulary require review rather than silent conversion.

Decisions may be provisional, source_recorded, approved, rejected, or superseded.
Approved entries need owner/date/evidence. Add a new entry referencing supersedes;
do not erase the earlier rationale. Inherited registry decisions remain source
references; this course log adds specific conflicts and new owner decisions.

The local work plan is the sole task tracker. Registers describe course content
and production artifacts; they do not create a parallel issue backlog.
Each planned artifact still identifies a deliverable, criteria and reviewer.

## Review and validation

Run from the repository root:
`python3 scripts/validate-course-records.py`

The check enforces headers, identity/reference integrity, source citations,
URL selection precedence, approval metadata, and release metadata. It reports
unresolved draft information separately. It does not judge history, learning
quality, musical accuracy, permissions, playback or actual print quality.
Use --with-local-assets to additionally verify recovered original hashes locally.
