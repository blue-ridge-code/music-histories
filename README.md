# VSCode Template

> **Already working in a generated project, not the template itself?** This README still
> describes the template's own setup flow. When kickoff runs in a generated project (see
> [`.agents/skills/kickoff/SKILL.md`](.agents/skills/kickoff/SKILL.md)), it rewrites this
> file in place to describe your project. If you are still reading the template version,
> kickoff has not run here yet — or this is the template source, where kickoff is skipped.

A universal starting point for **agent-assisted projects of any kind** — software, writing,
research, applications, file organization, life admin. It gives AI agents (Kimi Code, Claude
Code, Codex, Copilot) one consistent way to work across all your projects, so their behavior
stops diverging.

## How to use this template

**1. Generate a new project** — any of these:

- GitHub web: open this repo → **Use this template** → **Create a new repository**.
- CLI: `gh repo create <project-name> --template blue-ridge-code/vscode-template --private --clone`
- No GitHub: copy this folder and rename it (kickoff falls back to the local-mode
  tracker).

**2. Open the folder in VS Code and start any agent** — Kimi Code, Claude Code, Codex,
Copilot. Say "start the kickoff" — or just give it a task; `AGENTS.md` Rule #1 makes
kickoff happen first either way.

**3. Answer the kickoff interview** — one question at a time: purpose, project type,
stakeholders, definition of done, constraints, autonomy level, tracker choice, tone.
Say "skip" at any point to take the default.

**4. Authorize the lineup** — kickoff tests everything it can (`gh auth status`, agent
CLIs, Python) and ends with a numbered checklist of what only you can do: browser OAuth
logins, mobile-app pairing, VS Code extension installs.

**5. Commit** — kickoff never commits. Review its summary, then make the first commit
yourself.

## What's inside

| Path | Purpose |
|---|---|
| `AGENTS.md` | Canonical rules for every agent (thin; pointers to the rest) |
| `docs/PROJECT.md` | Project identity — starts as `kickoff-pending` |
| `docs/TONE.md` | Language persona profile for this project |
| `docs/decisions.md` | Append-only decision log |
| `docs/agents/` | Deep conventions: skills, services, intake, tracker, wiki, tokens, language |
| `.agents/skills/` | Canonical skills (read natively by Kimi, Codex, Copilot; mirrored to `.claude/skills/`) |
| `.vscode/`, `.mcp.json`, `.kimi-code/` | Per-host config slots (committed, secret-free) |
| `scripts/sync-skills.*` | Mirror canonical skills into `.claude/skills/` + drift check |

## Design principles

- **Kickoff before work** — every project is scoped by interview before anything is built.
- **One canonical source, thin adapters** — no per-tool divergence.
- **Provider-agnostic** — models, skills, MCPs, connectors, and utilities are registry
  entries with alternatives and swap criteria. Use what works best and is affordable.
- **Anti-scaffolding** — the template ships only what is wired up; layers (wiki, intake,
  tracker) activate at kickoff when the project actually needs them.
- **Human gates** — agents draft but never send, spend, or destroy without asking.

## After kickoff

Day-to-day: agents follow `AGENTS.md` and the docs it points to. Add skills with
`npx skills add <source>` (see `docs/agents/skills.md`). Add services via
`docs/agents/services.md`. Re-evaluate picks when something better appears — swap-ability is
the point.

## Maintaining this template

- **Feed improvements back.** When a project develops a better convention, skill, or
  registry pick, bring it back here — that is how the next project gets better than the
  last. Follow the [template maintenance runbook](docs/MAINTENANCE.md) to separate reusable
  changes from project-specific work, test a generated project, and capture review
  evidence. Working on the template repo itself? Kickoff does not run here (see the
  exception in `docs/PROJECT.md`).
- **Re-check the registries periodically.** The `Last evaluated` dates in
  `docs/agents/services.md`, `utilities.md`, `skills.md`, and `model-roles.md` rot —
  models, prices, and tools change. Swap when something better or cheaper proves out;
  that is the design, not a failure.
- **Keep the mirror in sync** after editing `.agents/skills/`: run
  `scripts/sync-skills.ps1`, then re-run it with `-Verify`. With Bash, use
  `scripts/sync-skills.sh`, then re-run it with `--verify`.
