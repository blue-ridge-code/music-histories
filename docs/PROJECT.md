# Music Histories

Status: implementation-ready
Planning entered: 2026-11-13, from the owner's transferred project brief (S00).
Scoped implementation recorded: 2026-11-16, from the owner's explicit requests
to build shared course records and stable-link tooling; see Lifecycle below.

## Mission

Build a modular library of standalone film-and-listening courses for adult learners.
Cinematic Music History is the documented initiative. Course I is established;
Amadeus is Chapter 1 and the first companion-workbook production pilot.
Explore culture, geography, technology, power, migration, identity, and historical
change through films and listening. A course normally combines roughly 10–15 core
films, optional extensions, curated YouTube listening, and a workbook/study guide.
Listening roles: Before, Inside, Beside, After, Bridge. Individual assignments
remain subject to the recovered manifests.

## Project type and shape

Writing, research, visual publishing, with production tools added when needed.
Multi-session. Initial work-product areas: series design and the Course I workbook
pilot (2–5 band); do not count agent infrastructure as course content.
At least 13 named source records/assets are expected; the final source count is
unknown. Future courses, titles, chapters, and scope are open questions.

## Stakeholders and audience

The primary learner is an adult using commute listening, evening film viewing,
and short seated workbook sessions around work. Typical workbook visits are
5–15 minutes; longer activities span multiple visits. Course I spans twenty weeks:
ten canonical films, with optional exploratory films in the off weeks. The course
is highly self-directed, using exposure, recall, scaffolding and accumulating
layers of meaning. Waypoints invite recollection, not tests or rubrics.
The [learning design](learning-design.md) records the four owner-defined outcomes,
research provenance, support choices and provisional waypoint examples.

The project owner is the final reviewer for
scope, series identity, copy, print proofs, and publication. Agent editorial
review is advisory; no outside reviewer has been appointed.

## Definition of done

First session: inventory known materials and access gaps; establish a minimal
local project home; bring the first visual-identity question.
First milestone: one proofed page 2, Who’s Who, with an unbroken record from
source/research brief through approved copy and prompt to exact input assets,
generated output, color/grayscale print proof, and owner disposition.
Validate the system on page 11, Mozart’s Hand, and page 9, The Commendatore Scene,
before producing the full chapter. No finished page has been produced here.

## Constraints and autonomy

The owner confirmed this is an open source project on 2026-11-16 and granted
standing authorization to commit/push routine project updates without asking again.
Documentation, framework, and Course I metadata/manifests may be public. Raw
manuscripts/prompts/images/PDFs and private locators remain excluded from this
publication scope. CC BY 4.0 covers original creative material; MIT covers original production code.
See [licensing](../LICENSE.md); third-party and inherited rights remain separate. No deadline/budget supplied.
Preserve existing puzzle grid and answer key. Copy approval precedes whole-page
prompting and generation. Source and image rights/credits must be recorded before
publication. Other human gates remain in AGENTS.md.

## Lifecycle

Implementation-ready applies to the specifically requested course-record and
stable-link production tooling, authorized by the owner on 2026-11-16. This records
the existing implementation requests, not a general approval of workbook design
or other product work. The stable-link implementation remains local and paused
while this governance restoration is completed. No operational/deployment claim
is made. Routine repository publication is authorized above.

Workbook design remains in planning. The interview proceeds one consequential
question at a time: answer, challenge, researched precedent, candidate rule,
explicit owner approval. Exact copy, visual rules and final proofs remain gated.
Do not repeat the kickoff interview for facts the owner already supplied.
Unanswered creative choices remain open.

## Architecture

The [system scope](SCOPE.md) and [record contract](../records/README.md) now define
series/course/edition/chapter/page boundaries and reusable record schemas.
Course I records live in `courses/course-i/editions/working/`; the existing
Amadeus folder remains the pilot's working production evidence. Future editions
get separate directories and stable identities; no course release exists yet.

- `docs/`: project index, decisions, work plan, series visual identity.
- `sources/`: source inventory; ignored `raw/` for private locators and originals.
- `courses/course-i/amadeus/`: pilot brief and page-production record.
- Additional course manifests, listening manifests, research, workbooks, and tools
  will be added when real sources or work require them; no invented course names.

## Layers and tooling

Source inventory/intake and local work plan active. The local work plan is the
explicit temporary tracker override; docs/agents/issue-tracker.md documents the
one-time migration path. GitHub API access was verified on 2026-11-16. Routine GitHub updates are
authorized. Keep one tracker; migrate local tasks to Issues only once when implemented. Wiki deferred until sources are recovered and cross-reference
needs are known. No ontology: no software module graph exists. No queue server
or speculative production tooling. Existing local skills remain available.
Kickoff guidance applied to the supplied brief; no external skill installation
was needed for this document-only first session. Research/editorial tools can be
selected when the relevant work item begins.

## Tone baseline

See TONE.md. Adult audience is confirmed; warmth, register, and visual tone remain
provisional until the design interview. Do not invent approved style examples.

## Open questions

Series identity and allowed variation; trim size, binding, margins, color process,
output resolution and proof method; authoritative source versions and conflicts;
full listening assignments; archival-facsimile source and rights; future course
titles and scope; permission to publish excluded source assets and third-party rights clearance.
