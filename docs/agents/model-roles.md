# model-roles.md — provider roles

Which agent does which job, what each provider natively supports, and how concurrent
sessions stay out of each other's way.

> Models and pricing rot fast — **verify current models and pricing before choosing.**
> Placeholder rows below are filled at kickoff.

## Per-provider capability map

| Provider | Skill mechanism | Instruction file | Install paths | Extras |
|---|---|---|---|---|
| Claude Code | `.claude/skills/` (mirrored from `.agents/skills/` — see [skills.md](skills.md)) | `CLAUDE.md` → [AGENTS.md](../../AGENTS.md) | project `.claude/skills/`, personal `~/.claude/skills/`, plugin marketplace | Bundled `/code-review` `/debug` `/verify` `/run` `/doctor`; `anthropics/skills` repo |
| Codex | `.agents/skills/` scanned CWD → repo root | `AGENTS.md` | project `.agents/skills/`, user `~/.agents/skills/` | `$skill-installer`; plugins `.codex-plugin/plugin.json` from `openai/plugins` — the `openai/skills` repo is **deprecated**; `agents/openai.yaml` sidecar |
| Kimi Code | `.agents/skills/` + `.kimi-code/skills/` | `AGENTS.md` | project `.agents/skills/` + `.kimi-code/skills/`, user `~/.agents/skills/` + `~/.kimi-code/skills/`, plus `extra_skill_dirs` in `config.toml` | `/skill:<name>`; `/import-from-cc-codex`; plugins: Datasource, WebBridge, Computer Use |
| Copilot | `.agents/skills/` | `.github/copilot-instructions.md` | project `.agents/skills/`, `.github/skills/`, `.claude/skills/` | `.github/agents/*.agent.md` custom agents; `gh` skill CLI |

## Copilot: configuration map

Where Copilot reads project configuration, and what belongs where.

> Locations and formats rot fast — **re-check Copilot's docs before relying on them.**

| Item | Location | Scope | Notes |
|------|----------|-------|-------|
| Canonical instructions | `.github/copilot-instructions.md` | Repo-wide | Pointer to [AGENTS.md](../../AGENTS.md); applies to every Copilot task |
| Custom agents | `.github/agents/*.agent.md` | Per-repo | One agent per file; filename (without `.agent.md`) is the agent name; `description` required, optional `tools` / `model` / `target` frontmatter |
| Project skills | `.agents/skills/` (canonical), `.github/skills/`, `.claude/skills/` | Per-repo | Copilot reads all three natively; this repo keeps `.agents/skills/` canonical |
| Personal skills | `~/.copilot/skills`, `~/.agents/skills` | User | Shared across projects |
| Skills sync | `.agents/skills/` → `.claude/skills/` | Manual or CI | `scripts/sync-skills.ps1` after edits (see [skills.md](skills.md)); `.github/skills/` stays reserved for Copilot-specific skills |
| `gh skill` CLI | `gh` ≥ 2.90.0 | User | Discover / install / update / publish skills; installs to the correct directory for the agent host |

### Copilot custom agents: when to use instead of instructions

Custom agents are per-repo personas that Copilot switches to only when a user asks for
them — **not** a second home for project rules.

- Keep project-wide rules — kickoff gate, evidence rule, human gates, conventions — in
  `AGENTS.md`, reached through `.github/copilot-instructions.md`. Every agent and provider
  reads that one source.
- Use a custom agent for a **task-specific persona** a user will explicitly invoke (release
  manager, documentation reviewer). One file per persona; the filename becomes the agent
  name.
- Do not fragment one project's rules across several custom agents: they apply only when
  selected and disappear for every other provider — exactly the divergence this template
  prevents.

## Role guidance (proven practice)

- **Claude Code** — primary executor/implementer.
- **Kimi Code** — audits, gap analysis, long-document review, second opinion.
- **Codex** — architecture partner, plan translator, review backstop.
- **Copilot** — inline completion + repo custom agents.
- **Cline** — VSCode-embedded runner with user-level Hooks/Rules/Workflows.

Roles are guidance, not law — reassign when a model's strengths shift.

## Current-model picks

Fill only once a second provider or model is actually being considered — not a minimal-
kickoff prerequisite. Until then, the agent running the current session is the de facto
Executor/Auditor/Architect/Inline and no table entry is required. When it is time to fill
or swap a pick, evaluate the candidate with the
[model evaluation template](model-evaluation-template.md) first. Do not trust stale picks
— verify current models and pricing before recording a table entry.

| Name | Role | Current pick | Alternatives | Cost | Last evaluated | Swap when |
|---|---|---|---|---|---|---|
| Executor | Implements tasks end-to-end | fill at kickoff | Claude Code, Codex, Kimi Code | check at kickoff | — | Quality drop or better price/performance elsewhere |
| Auditor | Reviews, gap analysis, long docs | fill at kickoff | Kimi Code, Claude Code | check at kickoff | — | Same |
| Architect | Plans, translates plans, backstop review | fill at kickoff | Codex, Claude Code | check at kickoff | — | Same |
| Inline | Editor completion | fill at kickoff | Copilot | check at kickoff | — | Same |

## Concurrent sessions: claim/release protocol

Battle-tested in the author's Leng project. All tools authenticate to GitHub as **one
identity** — claim comments are the only signal that a session is live.

1. Before starting tracker work, post a claim comment on the issue:
   `<model> (session <short-hex>) started <ISO-8601 UTC>` —
   e.g. `kimi (session c4fd88c7) started 2026-08-07T20:26:56Z`.
2. When done — or abandoning the work — post the matching release comment.
3. Treat **any** unreleased claim as live forever. No staleness guessing: surface it to the
   user instead of working around it.

Claims and releases live on the issue itself (see [issue-tracker.md](issue-tracker.md)).
Before claiming, read the issue's comment thread: an unreleased claim from another session
means the work is taken.

## Risk-based exposure rule

For unverified model integrations, route only no-tool-schema calls — plain chat, drafting,
summarizing — until tool-use fidelity is verified. Expand exposure only after verification.
Verify with a small, reversible task that exercises every tool schema the role needs; only
then promote the integration in the picks table above.
