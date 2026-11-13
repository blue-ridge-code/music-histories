# services.md — services & connectors registry

Every MCP server, connector, and external service is a registry entry with alternatives and
swap criteria. Nothing is sacred; best-and-affordable wins.

> Pricing, tiers, and availability rot fast — **re-check every entry before relying on it.**
> The MCP census is a historical source-host snapshot, verified on the template author's
> machine on 2026-08-07. During kickoff step 8 in each new project copy, replace the census
> and verification date with current host results before relying on them.

## MCP census (source-host snapshot verified 2026-08-07)

At that snapshot, exactly one MCP server was registered anywhere on the source host:

| Name | Transport | URL | Registered in |
|---|---|---|---|
| runpod | http | `https://mcp.getrunpod.io/` | Codex `~/.codex/config.toml` (`[mcp_servers.runpod]`); VS Code user `C:/Users/auddi/AppData/Roaming/Code/User/mcp.json` (`servers` key); project `Leng/.mcp.json` (`mcpServers` key) |

No other MCP servers exist in Claude Code, Kimi Code, Cline, Gemini, or Copilot configs.

## Per-host config map

| Host | Project scope | User scope | Notes |
|---|---|---|---|
| Claude Code | `.mcp.json` (`mcpServers`) | — | Enable project servers in local gitignored `.claude/settings.local.json` (`enabledMcpjsonServers`) |
| Kimi Code | `.kimi-code/mcp.json` | `~/.kimi-code/mcp.json` | `bearerTokenEnvVar` for secrets; `/mcp-config` TUI to edit, `/mcp` for status |
| VS Code | `.vscode/mcp.json` (`servers`) | user `mcp.json` | Copilot and Cline read these |
| Codex | — | `~/.codex/config.toml` (`[mcp_servers.*]`) | User level only |

## Secrets rule

Pass secrets through environment variables only — Kimi's `bearerTokenEnvVar` or `${env:VAR}`
interpolation. Never commit keys. `.env` stays local (see [`.gitignore`](../../.gitignore)).

## Optional MCP servers — adopt when the trigger fires

| Name | Role | Current pick | Alternatives | Cost | Last evaluated | Swap when |
|---|---|---|---|---|---|---|
| GitHub MCP | Issues/PRs from inside the agent | `github/github-mcp-server` (official) | `gh` CLI | Free | 2026-08-07 | Adopt: project uses Issues heavily. Swap: `gh` covers the need |
| qmd | Wiki search | qmd | grep over `wiki/` | Free | 2026-08-07 | Adopt: a [wiki](wiki.md) outgrows its `index.md` |
| Serena | Symbol-level code navigation | `oraios/serena` | repomix, grep | Free | 2026-08-07 | Adopt: large codebase. Swap: project stays small |
| filesystem | Sandboxed file access | official filesystem server | direct tool permissions | Free | 2026-08-07 | Adopt: untrusted or destructive-risk workspaces |

## Future upgrade: OB1 (Open Brain) — NOT installed

[OB1](https://github.com/NateBJones-Projects/OB1) (NateBJones-Projects) adds shared
cross-agent memory: Supabase + pgvector + MCP. License FSL-1.1-MIT — personal use fine, no
commercial derivatives until it converts to MIT. Repo-local memory stays the default
([decisions](../decisions.md), D-001 territory). Adopt OB1 only as a deliberate, logged
decision — never silently.

## Required connectors

| Name | Role | Current pick | Alternatives | Cost | Last evaluated | Swap when |
|---|---|---|---|---|---|---|
| git | Version control | git | — | Free | 2026-08-07 | Never |
| GitHub | Remote + issue tracker | GitHub account + repo | GitLab, local-only mode | Free tier | 2026-08-07 | Tracker choice is a kickoff decision |
| `gh` CLI | GitHub from the shell | `gh`, authenticated | GitHub MCP, web UI | Free | 2026-08-07 | — |
| Agent CLIs | Agent sessions | `kimi`, `claude`, `codex` — installed and logged in | Web UIs | Per plan | 2026-08-07 | Provider independence rule ([AGENTS.md](../../AGENTS.md)) |

> Census note: `~/.config/gh` did not exist on 2026-08-07 — kickoff must run
> `gh auth status` and queue a login if it fails.

## Recommended connectors

| Name | Role | Current pick | Alternatives | Cost | Last evaluated | Swap when |
|---|---|---|---|---|---|---|
| GitHub mobile app | Review/respond on the go | GitHub mobile | Mobile browser | Free | 2026-08-07 | — |
| Agent mobile apps | Repo access on the go | Claude / ChatGPT / Kimi apps, each with its GitHub connector enabled | — | Per plan | 2026-08-07 | App drops connector support |
| OneDrive mobile app | Phone intake drops into `inbox/` | OneDrive | Any synced folder | Per plan | 2026-08-07 | See [intake.md](intake.md) |
| VS Code extensions | Editor integration | GitHub Pull Requests, markdownlint; Copilot and Cline if subscribed | — | Free / per plan | 2026-08-07 | Editor change |

## Authorization checklist (kickoff step 8)

Split by who can act. The kickoff skill walks this list: the agent tests what it can, then
hands the user a numbered list of human-only items. Nothing external gets authorized
silently.

**Agent can test:**

- `gh auth status` — GitHub CLI session
- `git config user.name` / `user.email` — commit identity
- CLI presence — `kimi --version`, `claude --version`, `codex --version`
- MCP connectivity — enumerate servers per the config map above, call a trivial method
- `python --version` — utility prerequisite (3.10+, see [utilities.md](utilities.md))

**Human-only:**

- Browser OAuth flows (GitHub login, `gh auth login`, MCP server authorization)
- Mobile-app pairing (GitHub, Claude/ChatGPT/Kimi, OneDrive)
- VS Code extension installs
- Creating API keys or service accounts

### Preflight vs. on-demand

Kickoff runs a small "needed now" preflight, not the full checklist above. Check only what
the next operation actually needs:

- Python usable with UTF-8, if any selected skill runs Python.
- An available PowerShell flavor (`pwsh` or Windows PowerShell) on Windows.
- Node, only if selected tooling needs it.
- `gh auth status`, only if GitHub Issues is the chosen tracker.
- Sandbox or filesystem constraints relevant to the next operation.

Defer everything else to the ticket that actually needs it: device access (ADB, Fire TV or
similar console pairing, and comparable hardware access), specialized runtimes (audio
providers, GPU/cloud compute such as RunPod), mobile-app pairing, editor extensions,
credential/API-key creation, and MCP connectivity unrelated to what was just selected.
Recording a deferral is enough — do not chase an unrelated connector during kickoff just
because it appears in this registry.

### Failure classification

Classify an environment check's failure before acting on it — the three causes need
different responses, and only one of them is a human-authorization gap:

- **Proxy/DNS/network restriction** — the sandbox or network blocks the call before it
  reaches the service. Report it as an environment constraint; do not retry as an auth
  problem.
- **Sandbox restriction** — the tool itself is disallowed or path-restricted in this
  environment. Report it as a capability gap, not a login failure.
- **Authentication failure** — the call reaches the service and is rejected for lacking
  credentials or a valid session. Only this case goes to the human-only authorization list
  above.

Never turn a proxy, DNS, or sandbox restriction into an OAuth request.
