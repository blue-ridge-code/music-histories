# Layer activation guide

Use project shape to select the smallest set of layers and skills that can support the
work. Kickoff records the shape first, then walks this table with the user. Treat each
`Activate when` cell as the default action; record any user override and its reason in
`docs/PROJECT.md`.

## Project shape

Count top-level **work areas**, not repository support folders. For software, a work area
is a module, package, application, or service. For writing, research, administration, or
mixed work, it is a distinct work-product or subject-area folder. Do not count `.git`,
`.github`, editor settings, generated output, dependencies, or agent infrastructure.

Record one scale band in `docs/PROJECT.md`: `1`, `2-5`, `6-20`, or `20+`. For writing,
research, and mixed projects, also record the expected number of source files when that
count affects the wiki decision.

## Activation heuristics

| Candidate | Activate when | Do not activate when |
|---|---|---|
| **Wiki layer** | Writing project with 10+ expected source files; or search-heavy knowledge work with 15+ documents that cross-reference | One document, or all source material fits in one tracker issue |
| **Intake layer** | Phone, chat, email, or file drops are expected at least weekly | Work has no external inputs |
| **Tracker layer** | Work spans multiple sessions, has blockers or dependencies, or more than one agent will work on it | One session with no blockers or dependencies |
| **External tools** (connectors, MCP, or CLI) | An agent needs an external API such as GitHub, Slack, or a document service | All required work and evidence are local |
| **`ontology-agent` skill** | Software has 6+ **real** top-level modules (not provisional concerns or support folders), or real dependency manifests with structural relationships to graph, and the project has concrete structural questions the graph will answer | Fewer than 6 real modules and no real manifests, or a single-pass script/task. Record as "selected; activation deferred" in `docs/PROJECT.md` if the project wants it once it grows into it |

Apply these scale-specific defaults after the table:

- **1 work area:** do not bootstrap `ontology-agent`.
- **6-20 software work areas:** activate `ontology-agent` only once those work areas are
  real modules/packages/services or have real dependency manifests — not a count of
  provisional concerns, planned features, or support folders (`inbox/`, `gauntlet/`, and
  similar repository support folders never count). During early planning, before
  architecture is defined, record ontology as "selected; activation deferred" instead of
  bootstrapping speculatively. Suggest a GitHub connector, MCP server, or CLI when the
  project uses GitHub.
- **20+ software work areas:** apply the `6-20` defaults and recommend GitHub Projects as
  the sole roadmap view. Do not run a Project board beside a wayfinder map; choose one
  during kickoff as described in [issue-tracker.md](issue-tracker.md).
- **Writing with 10+ expected source files:** offer the wiki layer even when the project
  has fewer than 6 top-level work areas.

Shape is a kickoff baseline, not a permanent limit. Revisit activation when the project
crosses a threshold or its work pattern changes. Update `docs/PROJECT.md` and log only a
significant scope or governance change in `docs/decisions.md`.
