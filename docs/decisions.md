# Decisions

Music Histories entries start at D-013. D-000–D-012 are inherited template history,
retained for provenance; their active statuses describe template infrastructure,
not approval of this series, its manuscript, or its design.
For new project decisions use approved, provisional, rejected, or superseded;
record who decided and the evidence. Do not silently promote provisional choices.

Append-only log of significant decisions. Never rewrite or delete an entry: when a decision
is replaced, add a new entry that supersedes it and mark the old one
`Status: superseded-by-D-00X`.

Only log decisions that are **hard to reverse, surprising, or change scope** — not routine
choices (see the anti-scaffolding rule in `AGENTS.md`).

## Format

```
## D-00X | YYYY-MM-DD | <short title>
Status: active | superseded-by-D-00Y
Evidence:
  - Decision: [file:line](path/file.md#L10)
  - Ledger/proof: [gauntlet/ledger.md](../gauntlet/ledger.md)
  - Related issues: #42, #43
Context:    <!-- what forced the choice -->
Decision:   <!-- what was chosen -->
Consequences: <!-- benefits, costs, risks -->
Revisit when: <!-- condition that would reopen this -->
```

Every entry links its proof — the decision file, ledger or run record, and related issues.
`scripts/check-evidence-links.ps1` verifies all evidence links resolve; keep them valid.

## Entries

## D-012 | 2026-09-28 | Ship play-canon as a local skill and gauntlet-loop criteria pack

Status: active
Evidence:
  - Skill: [.agents/skills/play-canon/SKILL.md](../.agents/skills/play-canon/SKILL.md)
  - Source template: [.agents/skills/play-canon/sources/_TEMPLATE.md](../.agents/skills/play-canon/sources/_TEMPLATE.md)
  - Conformance test: [scripts/tests/test_criteria_packs.py](../scripts/tests/test_criteria_packs.py)
  - Composition: [docs/agents/skill-composition-map.md](agents/skill-composition-map.md)
  - Origin: `blue-ridge-code/projects-bucket` D-012, branch `claude/intelligent-planck-yd8u4n`
Context: A project copy needed literature-based play criteria that could do three jobs:
guide design (interactions, structures, content, style, and what to avoid), review
drafts, and act as a quality layer inside a gauntlet loop. The canon starts with nine
texts:
  - Huizinga, *Homo Ludens*
  - Caillois, *Man, Play and Games*
  - Sutton-Smith, *The Ambiguity of Play*
  - Bateson, "A Theory of Play and Fantasy"
  - Csikszentmihalyi, *Flow*
  - Nachmanovitch, *Free Play*
  - Carse, *Finite and Infinite Games*
  - Leonard, *Mastery*
  - Illich, *Deschooling Society*

Author names are labels showing which tradition a suggestion comes from, not personas.
That follows the measured persona finding in `gauntlet-loop`'s `references/evidence.md`.
Decision: Ship a local skill at `.agents/skills/play-canon/` with one file per text under
`sources/` and a `sources/_TEMPLATE.md`, so projects can add texts one file at a time.
The skill has three modes: Guide, Review, and Pack (a criteria pack for `gauntlet-loop`,
per D-011). Like the other checked-in skills, it is available in every project copy with
no install step.
Verification record:
  - Skill: play-canon
  - Source/version: local path `.agents/skills/play-canon/`, branch
    `claude/intelligent-planck-yd8u4n`
  - Verified: 2026-09-30
  - Result: pass
  - Evidence:
    - `python scripts/tests/test_criteria_packs.py` passes.
    - A negative control on a broken copy caught 4/4 planted flaws, and a second one
      (after the fidelity checks were added) caught 3/3.
    - `bash scripts/sync-skills.sh --verify` is clean.
    - The composition map rows are added.
    - No scripts or runtime dependencies.
  - Gaps: fidelity varies by source file, as of 2026-09-30. Seven source files are
    checked against their texts with page numbers, five with nothing outstanding that
    they rely on; Nachmanovitch rests partly on reading notes, and Caillois only on a
    secondary source. Each file's
    `Fidelity` and `Verify` lines say what remains, and guidance or findings that cite a
    concept with no page number are marked `(unchecked)`.
Consequences:
  - One more always-loaded skill description in every project copy.
  - A project that never does play-shaped work pays only that description's context cost.
  - Adding a text is one file plus one index row, checked in CI by the conformance test.
Revisit when: Caillois is checked against the book itself; pooled pack tallies show a
source never earning unique catches; or project copies stop using the skill.

## D-011 | 2026-09-28 | Upgrade gauntlet-loop in place: criteria packs, deterministic gates, current subagent practice

Status: active
Evidence:
  - Skill: [.agents/skills/gauntlet-loop/SKILL.md](../.agents/skills/gauntlet-loop/SKILL.md)
  - Pack contract: [.agents/skills/gauntlet-loop/references/criteria-packs.md](../.agents/skills/gauntlet-loop/references/criteria-packs.md)
  - Protocol: [.agents/skills/gauntlet-loop/assets/GAUNTLET.md](../.agents/skills/gauntlet-loop/assets/GAUNTLET.md)
  - Evidence notes: [.agents/skills/gauntlet-loop/references/evidence.md](../.agents/skills/gauntlet-loop/references/evidence.md)
  - Conformance test: [scripts/tests/test_criteria_packs.py](../scripts/tests/test_criteria_packs.py)
  - Origin: `blue-ridge-code/projects-bucket` D-011 and issue #13 (hill-climbing notes)
Context: Work in a project copy showed that `gauntlet-loop` lacked deterministic gates
and current subagent practice. It also showed that bundling a domain review layer into a
second loop skill would duplicate the loop protocol and blur both skills' triggers. The
template owner chose to upgrade the loop in place, keep review layers as separate skills,
and store the knowledge of how to build them inside `gauntlet-loop`.
Decision: Upgrade `.agents/skills/gauntlet-loop/` with:
  - L0 deterministic gates before any model judge, with tracked counts that ratchet;
  - an orchestrator-only lead;
  - a cold brief template for every subagent;
  - critics that stay read-only, verified by an unchanged working tree;
  - parallel critic batches;
  - the ledger as resumable state;
  - a named owner with a `taste.md` queue;
  - a criteria-pack layer (L2) with `SOURCE` labels, a unique-catch tally, and a kill
    rule.

The contract for building review layers lives in `references/criteria-packs.md`: the
loop consumes packs, so it owns the interface. `scripts/tests/test_criteria_packs.py`
enforces conformance for every pack skill, and CI runs it through
`scripts/tests/run_all.py` (`.github/workflows/skill-and-doc-integrity.yml`).
Consequences:
  - One loop protocol, and any review tradition can plug in as a pack without a new loop
    skill.
  - Runs write more files (`taste.md`, `packs/`).
  - The protocol template is longer.
  - The measured critic rules are unchanged. The new additions are recorded as reasoned,
    not measured, in `references/evidence.md`.
Revisit when: pooled pack tallies show packs rarely earn unique catches, or a harness
changes how subagent isolation works.

## D-010 | 2026-08-27 | Ship the dormant Review Protocol 1.0 repository contract

Status: active
Evidence:
  - Contract: [.agents/skills/human-review-queue/assets/template/review-queue/control-plane.json](../.agents/skills/human-review-queue/assets/template/review-queue/control-plane.json)
  - Installer test: [.agents/skills/human-review-queue/scripts/test_install_review_queue.py](../.agents/skills/human-review-queue/scripts/test_install_review_queue.py)
  - Generated-project trial: [scripts/tests/test_review_queue_deploy.py](../scripts/tests/test_review_queue_deploy.py)
Context: Commute Dispatch Issue #22 requires the proven repository-side contract from
Leng and Fire TV Toy to become the template's thin integration without deploying the
host Review Hub, a source, or an execution path in every generated repository.
Decision: Include `review-queue/control-plane.json` in the canonical human-review-queue
skill assets and configure it during installation. Pin integration 1.0.0 and Review
Protocol 1.0. Keep local-only privacy, disabled source mode, disabled response writes,
and separately gated listener retirement. Record protocol and template provenance.
Leave the immutable GitHub repository ID unresolved until an explicit host-enrollment
preview can verify it. Keep kickoff activation on demand.
Consequences: A generated project receives a dormant, portable repository contract and
stable reviewer binding when it installs the queue. The installer starts no process,
creates no host enrollment, changes no allowlist, and enables no dispatch or response
route. The existing generated-project test proves Python start, HTTP identity/status,
termination, and verification without depending on PowerShell.
Revisit when: Review Protocol changes major version, a second template implementation
proves a different portable service path, or host enrollment can safely resolve immutable
repository identity without adding network authority to the installer.

## D-009 | 2026-08-16 | Kickoff rewrites README.md at close (apply, guarded)

Status: active
Evidence:
  - Skill: [.agents/skills/kickoff/SKILL.md](../.agents/skills/kickoff/SKILL.md)
  - README: [README.md](../README.md)
Context: Kickoff previously drafted a project-specific README and only offered it in the
report, so generated projects kept the template-flavored README ("Generate a new project…")
until someone applied the draft by hand.
Decision: Kickoff gains a step, before Close, that rewrites README.md in place from the
gathered kickoff info (project name, mission, how to work on it, pointers to AGENTS.md and
key docs) when the file still reads as the template. If README.md is already project-specific,
it is left untouched. Kickoff still never commits — the rewrite is a local, reversible file
edit reported in the commit-ready summary.
Consequences: Generated projects exit kickoff with a project-accurate README on disk.
Documented in the skill's Process step 9 and Output section; the template README's note
updates accordingly. No change to the Git boundary.
Revisit when: The template README stops shipping template-flavored onboarding text, or the
close-step output set changes materially.

## D-008 | 2026-08-15 | Make the project lifecycle explicit; fix kickoff/governance gate placement

Status: active
Evidence:
  - Lifecycle model: [docs/agents/lifecycle.md](agents/lifecycle.md)
  - Kickoff rewrite: [.agents/skills/kickoff/SKILL.md](../.agents/skills/kickoff/SKILL.md)
  - Ontology activation gate (code): [.agents/skills/ontology-agent/scripts/bootstrap.py](../.agents/skills/ontology-agent/scripts/bootstrap.py#L349)
  - Ontology two-function split: [.agents/skills/ontology-agent/SKILL.md](../.agents/skills/ontology-agent/SKILL.md)
  - Review-queue hardening: [.agents/skills/human-review-queue/scripts/install_review_queue.py](../.agents/skills/human-review-queue/scripts/install_review_queue.py),
    [.../assets/template/scripts/start-human-review-queue.ps1](../.agents/skills/human-review-queue/assets/template/scripts/start-human-review-queue.ps1),
    [.../assets/template/scripts/human_review_queue_server.py](../.agents/skills/human-review-queue/assets/template/scripts/human_review_queue_server.py),
    [.../assets/template/scripts/human_review_queue.py](../.agents/skills/human-review-queue/assets/template/scripts/human_review_queue.py)
  - Git boundary: [AGENTS.md](../AGENTS.md)
  - Registry updates: [docs/agents/layer-activation-guide.md](agents/layer-activation-guide.md),
    [docs/agents/skills.md](agents/skills.md), [docs/agents/skill-composition-map.md](agents/skill-composition-map.md),
    [docs/agents/services.md](agents/services.md), [docs/agents/model-roles.md](agents/model-roles.md)
  - Superseded review: [docs/REVIEW.md](../docs/REVIEW.md)
Context: A real project generated from this template surfaced a design bug — the workflow
treated `selected → available → configured → running → authorized` as one state
(`Status: active`). Kickoff over-collected before planning could start (full 8-guide voice
workshop, every connector, every optional runtime, every selected skill installed
immediately). `ontology-agent` activated off a count of provisional concerns, planned
features, and support folders (`inbox/`, `gauntlet/` were counted as "modules";
`bootstrap.py` hard-coded `status="active"` into every generated graph regardless of the
real project state) instead of real structure — the "6+ modules" rule existed only as prose,
nowhere enforced in code. `human-review-queue`'s deploy script had no real port-conflict
handling (`start-human-review-queue.ps1` treated any existing listener on the port as "this
project, already running" with no identity check; an occupied port crashed the server with
an uncaught `OSError`), staged `gh issue create` bodies in the system temp directory with no
repo-local fallback, and ran the `gh` subprocess with no explicit UTF-8 encoding. Kickoff's
git-boundary instruction was a blanket "never run git commands" that didn't distinguish
read-only inspection from mutation. `docs/REVIEW.md` described already-completed work
(D-005's layer-activation-guide.md, skill-composition-map.md, MAINTENANCE.md, decision
evidence links, the skills deprecation section, and all 8 voice guides' Template examples)
as open, with example paths broken by an extra `../`.
Decision: Adopt an explicit four-phase lifecycle — `kickoff-pending` → `planning-active` →
`implementation-ready` → `operational` — documented in `docs/agents/lifecycle.md`, with a
migration rule treating legacy `Status: active` as `implementation-ready`. Move each gate to
the transition it actually protects: minimal kickoff now ends at `planning-active` without
waiting on optional runtimes, full provider configuration, device access, or implementation
tooling; product code requires explicit owner approval to `implementation-ready`.
`ontology-agent`'s `bootstrap.py` now enforces its own activation threshold in code (6+ real
modules, excluding a new `SUPPORT_DIR_NAMES` set, or any real dependency manifest; otherwise
exits `3` and creates nothing without `--force-small`) and reads `docs/PROJECT.md`'s actual
`Status:` line instead of hard-coding one. `human-review-queue`'s installer now probes port
availability before writing config and fails closed or records the next free port;
`start-human-review-queue.ps1` calls a new unauthenticated `/api/review-queue/identity`
endpoint to confirm an existing listener actually belongs to this project before treating it
as already running; `human_review_queue.py` stages dispatch bodies in a repo-local temp
directory with a system-temp fallback and runs `gh` with explicit UTF-8 encoding. The git
boundary is now risk-based (read-only inspection always allowed; mutation always gated), not
a kickoff-specific blanket rule. Skill installs are just-in-time: kickoff installs only the
planning-phase bucket now, records `handoff` for install at the first real session boundary,
and records implementation-phase skills for install at `implementation-ready`. Voice setup at
kickoff shrinks to four questions with every A1–B3 guide defaulting to a documented median.
Environment checks split into a small "needed now" preflight versus on-demand items deferred
to the ticket that needs them, with failure causes classified (proxy/DNS/sandbox vs. real
auth failure) before escalating to a human authorization request. `docs/REVIEW.md` gets a
Superseded banner with each now-complete item annotated and its broken example links fixed.
Consequences: Planning can start without collecting infrastructure the project doesn't need
yet, while every credential/spend/publish/destructive/participant-data/device-permission gate
stays exactly as strict as before — the phase model changes *when planning starts*, not what
still needs a human. `ontology-agent` and `human-review-queue` graphs/deployments now reflect
real project state instead of a hard-coded assumption. Two categories of test coverage exist
going forward for this area: the ontology-agent skill's own `selftest_validate.py` (updated
for the new gate via `--force-small` on its deliberately-empty smoke-test root) and the
human-review-queue skill's own `test_install_review_queue.py` /
`test_human_review_queue.py` (both re-run clean after this change), plus the new
`scripts/tests/` suite (see this decision's evidence links) covering the five verification
scenarios named in the originating task.
Revisit when: A generated project's real use of `planning-active`/`implementation-ready`
shows the phase boundary is drawn in the wrong place, the `SUPPORT_DIR_NAMES` list needs a
project-specific addition upstreamed, or the review-queue identity check needs to move from
an unauthenticated endpoint to something stronger for a non-loopback deployment.

## D-007 | 2026-08-15 | Add a Copilot configuration map and a model evaluation template

Status: active
Evidence:
  - Decision: [docs/agents/model-roles.md](agents/model-roles.md)
  - Template: [docs/agents/model-evaluation-template.md](agents/model-evaluation-template.md)
Context: model-roles.md listed Copilot's capability (skill mechanism, instruction file,
custom agents) but not its configuration surface — where each item lives, how skills sync,
and when a custom agent should exist at all. It also told readers to verify current models
and pricing without a repeatable procedure, leaving every provider swap to ad-hoc judgment.
Decision: Expand model-roles.md with a Copilot configuration map and "custom agents vs
instructions" guidance, and add docs/agents/model-evaluation-template.md as the standard
quick check, tool-use fidelity test, and results record for evaluating a new model or
provider. The map records the actual sync behavior — `.agents/skills/` → `.claude/skills/`
only — and reserves `.github/skills/` for Copilot-specific skills instead of claiming a
third mirror.
Consequences: Copilot users keep project rules in AGENTS.md instead of fragmenting them into
custom agents; provider evaluations are recorded, reversible, and consistent with the
risk-based exposure rule. Adds one small reference doc to docs/agents/.
Revisit when: Copilot changes its skill directories or custom-agent format, or evaluation
outgrows a template and becomes a skill.

## D-006 | 2026-08-15 | Require a tested path for feeding improvements back

Status: active
Evidence:
  - Runbook: [docs/MAINTENANCE.md](MAINTENANCE.md)
  - Entry point: [README.md](../README.md#maintaining-this-template)
Context: The README asked projects to feed useful conventions, skills, and registry picks
back into the template, but it did not explain how to separate a reusable improvement from
project-specific work. It also did not define the test or review evidence required before
merge.
Decision: Use `docs/MAINTENANCE.md` as the source of truth for template contributions.
Each change uses a dedicated worktree, proves the candidate in a disposable generated
project, records significant policy or capability changes, includes test evidence in the
commit body, and receives an independent review. Project-specific policy and unproved
scaffolding stay in the project that needs them.
Consequences: Template changes require more evidence than ordinary local documentation
edits. In return, improvements have a repeatable route back to the source template without
carrying private data, machine paths, or narrow project assumptions into future projects.
Revisit when: Automated generated-project tests replace the manual test step, or
contribution volume requires a pull-request template or a dedicated intake workflow.

## D-005 | 2026-08-15 | Scale kickoff by project shape and maintain the skills registry

Status: superseded-by-D-008
Evidence:
  - Decision: [docs/agents/layer-activation-guide.md](agents/layer-activation-guide.md)
  - Registry + checklist: [docs/agents/skills.md](agents/skills.md#L8)
  - Reminder workflow: [.github/workflows/quarterly-skills-registry-refresh.yml](../.github/workflows/quarterly-skills-registry-refresh.yml)
Context: Kickoff selected layers and skills from project type alone. That treated a small
single-area project like a multi-module codebase, offered no shared activation threshold,
and left external skill catalogs without a deprecation path or recurring review signal.
Decision: Record project shape as a `1`, `2-5`, `6-20`, or `20+` top-level work-area band.
Apply the activation heuristics in `docs/agents/layer-activation-guide.md`; activate
`ontology-agent` for multi-pass software with 6+ modules, offer the wiki to writing work
with 10+ expected sources, and raise a sole-roadmap GitHub Projects choice at 20+ modules.
Add source-policy and deprecation fields to the skills registry. Use a quarterly GitHub
workflow and manual issue template in repository mode, or a rolling dated backlog row in
local mode, to trigger review.
Consequences: Small projects avoid ontology and unused layers. Larger projects receive
structure and integration prompts at kickoff. Skill sources expose whether they move or
are pinned, retired choices retain migration context, and stale evaluations create visible
work. GitHub Projects replaces rather than duplicates the wayfinder roadmap when selected.
Revisit when: Real projects show that the module or source thresholds select the wrong
layers, or the tracker gains a native recurring-maintenance mechanism that replaces the
scheduled workflow and local backlog convention.

## D-004 | 2026-08-15 | Ship human review queue as a core/default skill

Status: active
Evidence:
  - Skill: [.agents/skills/human-review-queue/SKILL.md](../.agents/skills/human-review-queue/SKILL.md)
  - Registry: [docs/agents/skills.md](agents/skills.md#L33)
  - Sync script: [scripts/sync-skills.ps1](../scripts/sync-skills.ps1)
Context: Repositories created from this template need a consistent way to run repeated,
asynchronous, media, and artifact review without rebuilding ad hoc approval surfaces.
Leng already had a reusable, tested skill at source commit `770e823`; its canonical
24-file directory was unchanged in the source worktree before import.
Decision: Import only Leng's canonical `.agents/skills/human-review-queue/` directory and
generate this template's `.claude/skills/human-review-queue/` mirror with
`scripts/sync-skills.ps1`. Treat the checked-in skill as a core/default capability in
every generated repository, but do not scaffold or start a runtime queue during kickoff.
Deploy the runtime only for a concrete review workflow, with dispatch disabled,
`single_local` reviewer identity, and loopback access as defaults.
Consequences: Every generated repository can deploy the same durable human-gate system
without another skill install, while projects without review queues gain no unused
service or runtime files. Enabling dispatch, multiple identities, or non-loopback access
remains an explicit, separately reviewed boundary change.
Revisit when: A lighter built-in gate replaces the queue, the runtime becomes necessary
for nearly every project, or the local-only identity and dispatch defaults no longer fit.

## D-003 | 2026-08-09 | Add ontology-agent skill, synthesized from four competing inbox drafts via gauntlet-loop

Status: active
Evidence:
  - Ledger/proof: [gauntlet/ledger.md](../gauntlet/ledger.md)
  - Triage: [inbox/triage-log.md](../inbox/triage-log.md)
  - Skill: [.agents/skills/ontology-agent/SKILL.md](../.agents/skills/ontology-agent/SKILL.md)
Context: Four competing drafts of an "ontology agent" idea arrived via the phone/OneDrive
inbox channel (`inbox/raw/`): `ontology-kg-agent-chat-export.zip`, `ogas_skill.zip`,
`Gemini - Ontological Agent Skill - chat_export.zip`, and a standalone Python prototype.
Inspected per the untrusted-intake rule before use. Used the installed `gauntlet-loop`
skill to run a real builder/critic loop (scaffolding at `gauntlet/`) rather than picking
one draft by inspection alone: two real, mirrored bars — the official W3C SHACL test
suite and the CIDOC-CRM (Erlangen OWL) ontology — anchored the critics, split into four
independently-built pieces (ontology core, validation gate, graph/query layer, SKILL.md
integration), each verified by a fresh blind critic re-running the actual code rather
than trusting builder self-reports. The loop caught and fixed real bugs a single-pass
synthesis would likely have missed: an ontology/shape drift bug, a broken bootstrap/
validator seam (self-test failing end-to-end), and — found only by a final holistic
absence check — unregistered tools silently bypassing the safety gate entirely.
Decision: Adopt `ontology-kg-agent`'s zero-dependency, standards-based (RDFS/OWL/SHACL)
design as the base, rewritten and hardened. Explicitly reject the fan-out/harsh-critic/
value-scoring orchestration framework present in the other three drafts (`ogas_skill`,
the Gemini TS draft, the deepseek prototype) — that machinery would duplicate
`.agents/skills/gauntlet-loop/` and pull in dependencies (`pydantic-ai`, `rdflib`,
`owlready2`, `networkx`, or a TypeScript/N3/Zod stack) this project's provider-
independence rule forbids. Installed at `.agents/skills/ontology-agent/`, synced to
`.claude/skills/ontology-agent/` via `scripts/sync-skills.ps1`. Full run logged in
`gauntlet/ledger.md`; raw sources triaged in `inbox/triage-log.md` and archived to
`inbox/archive/2026-08-09/`.
Consequences: `ontology-agent` gives any agent in this project a deterministic
pre-execution gate for tool calls plus a queryable project graph, documented to compose
with `gauntlet-loop` (this skill gates well-formedness; gauntlet-loop judges quality)
rather than reimplement it. Known, documented limitations: `shapes.json` is hand-synced
against `shapes-core.ttl` (no bundled Turtle/SHACL parser), no `sh:or`/`sh:xone` support,
and `blocked_by`/`blocking` queries are inert until something populates `:blocks` edges.
Revisit when: a Turtle/SHACL parser or MCP RDF/SHACL server becomes available and the
hand-sync limitation is worth closing, or the skill goes unused/unmaintained.

## D-002 | 2026-08-09 | Add gauntlet-loop skill (local, via inbox)

Status: active
Evidence:
  - Skill: [.agents/skills/gauntlet-loop/SKILL.md](../.agents/skills/gauntlet-loop/SKILL.md)
  - Triage: [inbox/triage-log.md](../inbox/triage-log.md)
Context: A skill package (`gauntlet-loop.zip`) arrived via the phone/OneDrive inbox
channel (`inbox/raw/`). Inspected per the untrusted-intake rule before use — plain
markdown, no scripts, canonical `name`/`description`-only frontmatter, no embedded
instructions aimed at the agent. It implements an evaluator-optimizer loop (builder +
blind critic per piece, judged against a named real-world reference) credited to Matt
Shumer (somethingbig.ai/gauntlet-loop), adding calibration checks, an absence critic,
regression guards, and order-swapping to counter judge bias.
Decision: Install as a local canonical skill at `.agents/skills/gauntlet-loop/`, synced
to `.claude/skills/gauntlet-loop/` via `scripts/sync-skills.ps1`. Logged in
`inbox/triage-log.md`; raw zip archived to `inbox/archive/2026-08-09/`.
Consequences: `gauntlet-loop` is available alongside the existing local skills for any
future "make this excellent, judged against a named reference" request.
Revisit when: The upstream method changes meaningfully, or the skill goes unused/unmaintained.

## D-001 | 2026-08-08 | Writer's voice framework: component guides under docs/agents/voice/

Status: active
Evidence:
  - Hub: [docs/agents/language.md](agents/language.md)
  - Guides: [docs/agents/voice/a1-tone.md](agents/voice/a1-tone.md)
  - Research: [docs/agents/voice/research-notes.md](agents/voice/research-notes.md)
Context: The language persona system governed word choice and tone dials only. The
wider writer's voice (syntax, pacing, POV, rhythm, persona, attitude) had no home,
and nothing told agents how strongly STE-100 / Oxford 3000 should bind per register.
Decision: Add `docs/agents/voice/` — one light guide per voice component (A1–A5,
B1–B3), each with levers, kickoff questions, and a "Project setting" section. The
A2 diction guide absorbed the base-standards and register guidance from language.md
and adds a per-register binding-strength ladder (0% creative → ~50% technical
procedure → ~100% safety-critical). Kickoff populates the settings only when voice
matters to the project; language.md stays the thin hub. Research background:
voice/research-notes.md (Wheaton, NN/g, Journalism U, LitCharts, Literary Devices).
Consequences: The persona system is tailorable per project at kickoff and updatable
later via the modification procedure. The kickoff and language-persona skills now
reference the guides. Guides start deliberately thin; depth accretes per project.
Revisit when: A project finds a guide too thin to steer output, or a component
proves useless and should be dropped.

## D-000 | 2026-08-07 | Project scaffolded from VSCode Template

Status: active
Evidence:
  - Project: [docs/PROJECT.md](PROJECT.md)
  - Conventions: [AGENTS.md](../AGENTS.md)
Context: Project created from the universal agentic project template.
Decision: Adopt the template's conventions (AGENTS.md, docs/agents/*, kickoff orientation).
Consequences: All agents share one instruction source; project-specific choices are
recorded here from D-001 onward.
Revisit when: The template itself is replaced or forked.

## D-013 | 2026-11-13 | Establish Music Histories and the Amadeus pilot
Status: approved — explicit owner instruction S00; underlying source files uninspected.
Owner: project owner.
Evidence:
  - Scope: [PROJECT.md](PROJECT.md)
  - Intake: [source inventory](../sources/SOURCE_INDEX.md)
Context: The fresh template lacked a project identity; the owner supplied a concrete brief.
Decision: Music Histories is a modular adult course library; Cinematic Music History
is the documented initiative. Course I and Amadeus Chapter 1 are established.
First session is inventory and identity interview; first production milestone is a
traceable proofed Who’s Who page. Future course scope remains open.
Consequences: Proceed in planning-active; do not invent missing manuscript or manifests.
Revisit when: Recovered authoritative sources conflict with this brief.

## D-014 | 2026-11-13 | Prepare locally and hold publication
Status: superseded-by-D-018 — original decision was approved — owner instruction S00; no visibility choice yet.
Owner: project owner.
Evidence:
  - Publication work item: [W07](work-plan.md#w07--decide-visibility-and-publication-scope)
  - Current boundary: [AGENTS.md](../AGENTS.md)
Context: GitHub reports public; a read-only repository-page check confirmed the Public
marker and isPrivate:false on 2026-11-13.
Decision: Use local branch setup/music-histories-pilot. Keep raw/private locators
ignored. Do not push, create public issues/PRs, or change visibility without owner
direction and approval of publication scope. The authorized branch was created.
Consequences: Use the local work plan as sole tracker during the hold, adapting the
template's GitHub-first default. No remote writes or commits authorized by this entry.
Revisit when: The owner gives an explicit visibility decision and publication scope.

## D-015 | 2026-11-13 | Keep source approval separate from retrieval
Status: approved — implementation of owner's requested source inventory.
Owner: project owner for underlying source approvals; agent records observations.
Evidence:
  - Inventory: [SOURCE_INDEX.md](../sources/SOURCE_INDEX.md)
Context: Approved manuscript and prototype versions were reported, but files are
not accessible in this session.
Decision: Label manuscript approval as owner-reported; label prototypes v0.2 as
reported versions with approval unknown. Unknown dates stay unknown. Preserve
source IDs, immutable originals, hashes, approval evidence and source conflicts.
Consequences: No output is a recovered approved asset until the exact file is inspected.
Revisit when: Files and approval records are supplied.

## D-016 | 2026-11-13 | Validate three page types before full production
Status: approved — explicit owner workflow S00; design choices remain open.
Owner: project owner.
Evidence:
  - Pilot: [Amadeus](../courses/course-i/amadeus/README.md)
  - Gated production record: [Who’s Who](../courses/course-i/amadeus/page-02-production.md)
  - Open identity question: [series identity](design/series-identity.md)
Context: Series recognition must survive different genres and different learning activities.
Decision: Begin with page 2, preserve grid/key, approve copy before image prompting,
and proof at print size in color/grayscale. Then test page 11's archival engagement
and page 9's quiet listening before expanding. Demanding listening gets lighter
activity (Inverse Play Law, project principle reported by owner).
Consequences: No typography, palette, archival image, exact copy, or generated page
is approved yet. Agent tone defaults in TONE.md are provisional.
Revisit when: The owner resolves the identity interview or changes the page workflow.

## D-017 | 2026-11-16 | Prepare versioned shared records
Status: provisional — owner requested the framework; specific storage design awaits review.
Owner: project owner.
Evidence:
  - Scope: [SCOPE.md](SCOPE.md)
  - Contract: [shared records](../records/README.md)
  - Course I: [working edition](../courses/course-i/editions/working/README.md)
Context: The owner requested a complete-system scoping document and shared records
for Course I that can support many course versions.
Decision: Use portable CSV registers and JSON metadata with stable course/entity
IDs, separately identified course editions, release references and print formats.
Import source selections without inventing new approvals, rights, or listening scopes.
Consequences: Future editions can preserve identity while changing sequence/content.
Private originals remain ignored. Source-derived records are prepared locally;
public GitHub publication still needs the visibility/exact-scope decision in D-014.
Revisit when: The owner reviews the structure or a future edition needs schema changes.


## D-018 | 2026-11-16 | Authorize routine open source project updates
Status: approved — explicit owner instruction in chat; supersedes D-014.
Owner: project owner.
Evidence:
  - Standing authority: [AGENTS.md](../AGENTS.md)
  - Public scope: [PROJECT.md](PROJECT.md)
Context: The owner approved publishing the prepared scope, framework and Course I
metadata, confirmed an open source project, and said to push when needed without
asking each time.
Decision: Commit/push routine project updates and use review branches/PRs without
repeat permission. Keep the repository public. Raw manuscripts, prompts, PDFs,
images and private source links remain outside the approved publication scope.
Consequences: The earlier publication hold is lifted for project updates. Rights,
source-asset publication, final creative approval and license selection remain
separate. No license is invented by this decision.
Revisit when: The owner changes publication scope or selects an open source license.

## D-019 | 2026-11-16 | Adopt standard CC BY 4.0 and MIT licenses
Status: approved — owner agreed to the proposed policy with no special CC amendment.
Owner: project owner.
Evidence:
  - Scope and exclusions: [LICENSE.md](../LICENSE.md)
  - Creative license: [CC BY 4.0](../LICENSES/CC-BY-4.0.txt)
  - Software license: [MIT](../LICENSES/MIT.txt)
  - Designated credit: [ATTRIBUTION.md](../ATTRIBUTION.md)
Context: The owner wants permissive reuse and commercial adaptation with contributor
credit and the repository supplied as the source link, using standard terms.
Decision: License original creative materials under CC BY 4.0 and original
production code under MIT. Designate Music Histories contributors as the collective
credit and the public repository URL as supplied source information. Add no special
sale, link-placement, revenue-sharing, or share-alike conditions.
Consequences: Preserve individual/source notices. Third-party and inherited assets
retain their own rights; unverified inherited rights are not relicensed. Existing
raw-asset publication exclusions remain. License texts were reproduced from SPDX's
license-list-data; CC text is unchanged and only MIT's copyright holder/year is filled.
Revisit when: A new asset needs an exception or the owner proposes a licensing change;
existing grants cannot simply be withdrawn from recipients following their terms.

## D-020 | 2026-11-16 | Restore template instruction wiring
Status: approved — owner requested the reviewed restoration, push and merge.
Owner: project owner.
Evidence:
  - Canonical instructions: [AGENTS.md](../AGENTS.md)
  - Lifecycle: [lifecycle.md](agents/lifecycle.md)
  - Tracker override: [issue-tracker.md](agents/issue-tracker.md)
  - Regression scenarios: [test_instruction_wiring.py](../scripts/tests/test_instruction_wiring.py)
Context: The shortened project AGENTS.md removed operational entry points even
though dependent skills, adapters and scripts remained. Keeping an archived copy
did not keep those instructions active. Earlier keyword tests missed that loss.
Decision: Restore the canonical-source declaration, kickoff/lifecycle gates,
complete authority map, human/review-queue gates, evidence/intake routing,
provider independence, token/file handoffs, documentation hygiene, operational
index and platform/date/secret conventions. Preserve Music Histories additions
and explicit owner authorization as a separate project policy section.
Consequences: Template operational norms remain active. The local work plan stays
the sole tracker under a documented temporary override until a one-time migration.
Record implementation-ready only for the already requested course-record and
stable-link tools; workbook creative approvals remain pending. GitHub API reads
and authenticated repository access are now verified; this does not establish
every administration scope. Unfinished stable-link edits are excluded from this
restoration commit and merge. Browser-unavailable cases report their limitation.
Revisit when: Template workflow changes, tracker migration, or new owner scope approval.

## D-022 | 2026-11-16 | Define Course I as a self-directed twenty-week learning journey
Status: approved for owner-confirmed audience, cadence, outcomes and method;
specific waypoint wording, placement and effort budgets remain proposed.
Owner: project owner.
Evidence:
  - Learning design and research boundaries: [learning-design.md](learning-design.md)
  - Owner answers: [S16](../sources/SOURCE_INDEX.md)
Context: The owner specified adult learning around commutes/work, revised the
horizon to ten canonical films over twenty weeks, named four outcomes and chose
exposure, recall, scaffolding and added layers of meaning without tests/rubrics.
Decision: Support interpretation of film/music/culture, musical discrimination
and historical/pop-cultural connections, people-to-work relationships, and
anticipation of musical structure. Use optional private recall and returns with
accessible hints/notes, not scores, mastery gates or a compulsory review schedule.
Consequences: Preserve correct facts and production review without assessing the
learner. Before/Inside/Beside/After/Bridge roles remain; commute use does not move
all assignments before viewing. Exact scheduling is a course-design hypothesis,
not an empirically established optimum. Research from a private owner-authorized
repository is retained locally; no source copies/private links are published.
No manuscript/puzzle changes or learner-data collection are approved by this entry.
Revisit when: Pilot experience reveals workload/friction or the owner revises outcomes.

D-021 is reserved for the separate stable-link implementation in PR #2; this
learning-design branch does not duplicate or supersede that decision.

## D-023 | 2026-11-17 | Design for short, resumable workbook visits
Status: approved for the time preference; exact pause/resume cues remain proposed.
Owner: project owner.
Evidence:
  - Learning design: [learning-design.md](learning-design.md)
  - Owner update: [S16 addendum](../sources/SOURCE_INDEX.md)
Context: The owner refined the typical workbook visit to 5–15 minutes and asked
that longer activities be considered over multiple visits.
Decision: Design short visits and break longer activities into resumable encounters,
without timed assessment or requiring a longer sitting. This refines D-022's
previously open effort budget; it does not replace its learning approach.
Consequences: Propose natural pause points and return cues; pilot their usability.
The target concerns seated workbook use, not the duration of films or listening.
Revisit when: Pilot experience or owner preference suggests a different rhythm.
