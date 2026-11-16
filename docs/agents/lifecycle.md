# Project lifecycle — phases and gates

The template used to treat `selected → available → configured → running → authorized` as
one state: everything from "the user picked GitHub Issues" to "credentials are live and
spending money" got waved through by the same `Status: active` flag. That collapsed gates
that protect real work into gates that only protect paperwork. This doc makes the states
explicit and pins each real gate to the transition it actually protects.

## The four phases

| Phase | Entered by | Permits |
|---|---|---|
| `kickoff-pending` | Template default | Only the `kickoff` skill acts. |
| `planning-active` | Minimal kickoff finishing | Planning, research, decision work, and expressly marked non-product prototypes (the `prototype` skill). No product code. |
| `implementation-ready` | Explicit owner approval, once the project's own planning gate is satisfied | Product code may begin. |
| `operational` | The project is in real use | Names the running state so docs stop conflating "shipped" with "planning done." Unlocks no new procedure by itself. |

Minimal kickoff ends at `planning-active`. It does not wait on optional runtimes, full
provider configuration, device access, or implementation tooling — those are configured
just-in-time, against a real ticket, in later phases (see the gate-placement table below).

`implementation-ready` is never entered silently. The agent proposes the transition; the
project owner approves it explicitly. "Planning gate satisfied" means the project has the
architecture it needs to start building and a tracker/map to build against — not a fixed
checklist, since what counts as enough planning is project-specific.

## Migration rule for existing `Status: active` projects

Projects generated before this doc existed read `Status: active` — a state that already
conflated "kickoff finished" with "cleared to build." Treat legacy `active` as equivalent to
`implementation-ready`. An agent that reopens such a project should offer, once, to relabel
it precisely:

- No product code exists yet → relabel `planning-active`.
- Product code exists, or the project is deployed/in use → relabel `implementation-ready` or
  `operational`, whichever fits.

Record the relabel as a decision if the project keeps a `docs/decisions.md`. Do not relabel
silently, and do not treat the absence of a relabel as blocking — legacy `active` keeps
working as `implementation-ready` until someone chooses to make it precise.

## Gate placement: old vs. new

| Gate | Old placement | New placement |
|---|---|---|
| Ontology (`ontology-agent`) bootstrap | Counted any 6+ folders, including provisional concerns and support folders, at kickoff | Real modules/packages/services (6+) or real dependency manifests, with concrete structural questions — checked at architecture definition, not kickoff interview |
| `human-review-queue` runtime deploy | "Available" the moment kickoff selects it | Deployed only at the project's first concrete repeated/async/artifact-review gate |
| Product code | Implicitly allowed once `Status: active` | Explicit owner approval to `implementation-ready`, after the planning gate is satisfied |
| Git mutation (commit, push, branch, merge, reset, rewrite) | Blanket "never run git commands" during kickoff | Always human-gated, every phase; read-only inspection (`status`, `diff`, `remote`, `config --get`) always allowed |
| Skill install | Every selected skill installed at kickoff | Planning-phase skills install now; `handoff` installs at the first real session boundary; implementation-phase skills install at the `implementation-ready` gate |
| Voice/tone setup | Full A1–B3 interview (8 guides) required before planning | Four minimal questions (tone words, anti-tone words, audience, essential constraints); guides default to their median setting; full workshop offered as a later task |
| Environment/connector checks | Full authorization checklist walked at kickoff | Small "needed now" preflight at kickoff; everything else deferred to the ticket that needs it |

## What never moves

Credentials, spending, publication, destructive actions, participant/human-subject data,
device/hardware permissions, and external transmission stay human-gated in **every** phase —
see `AGENTS.md`'s Human gates list. This phase model changes *when planning can start*, not
what still needs a human.


## Music Histories scope and existing authorization

Current phase and owner-authorized implementation scope are recorded in
[PROJECT.md](../PROJECT.md). The owner's direct requests to build the course-record
framework and stable-link tooling authorize those specific components; they do
not approve workbook text, visual identity, proofs, or unrelated product scope.

The Git/publication gate remains in force, but the owner has supplied standing
permission for routine project updates as recorded in AGENTS.md and D-018.
Do not turn that permission into approval of excluded assets or a waiver of
other human gates. Apply already-granted permission without repeated questions.
