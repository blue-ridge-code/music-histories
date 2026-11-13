# Token efficiency conventions

Tokens are the scarcest resource in every session. Spend them on the task, not
on re-reading the project. These conventions apply to every agent and project
type; the software-only section adds repo-specific tooling.

## Structure: progressive disclosure

- **Pointer-docs discipline.** Keep always-loaded files thin. Replace depth
  with one-line context pointers that name the out-of-context material and say
  when to load it: `Full conventions: docs/agents/token-efficiency.md`. Load
  the target only when the trigger matches.
- **Nested AGENTS.md / README.md per area of concern.** Instructions live in
  the smallest directory they govern; the nearest file wins. An agent working
  in one area loads that area's file and no other. This is the agents.md
  standard — follow it instead of growing one monolithic root file.
- **Leading words.** Once a term is established, reuse it instead of
  re-defining it (`the frontier`, `the map`, `channel 1`). One word where
  twenty would do.
- **CONTEXT.md on demand.** Create a shared-vocabulary file only when
  terminology actually settles and gets reused — never scaffold it empty.

## Between sessions

- **Hand off by file, not by transcript.** An ending session writes a short
  file in `handoffs/` (create on demand): goal, status, next step, and
  artifacts referenced by path. The next session reads one file, not a re-dump
  of everything that happened.
- **Start fresh or compact at ~70%.** When context use passes roughly 70%,
  write the handoff and start a new session or compact. Output quality drops
  before the hard limit does.

## Within a session

- **Sub-agent isolation.** Delegate context-flooding work — test runs, build
  logs, doc fetches, wide searches, file dumps — to sub-agents and accept a
  distilled summary back (≤ 1–2k tokens). The main context keeps conclusions,
  not raw output.
- **Redirect + grep.** Send verbose command output to a log file, then `grep`
  out only the lines that matter. Never paste full build or test output into
  context.
- **Right-size the model.** Prefer the cheapest capable model for mechanical
  steps (renames, format conversion, boilerplate) and reserve strong models for
  judgment. Count model calls — every call is a budget event.
- **Read narrowly.** Open files at the relevant line range, search before you
  read, and glob a directory instead of loading it "to see what's there".

## Software-only tooling

- **repomix** — pack a repo for a one-shot external LLM handoff. Use
  `--compress` to strip code to signatures and `--token-budget` to fit the
  target window.
- **Serena MCP** — symbol-level navigation (find definition, list references)
  instead of reading whole files in large repos. Register it in
  [services.md](services.md) when adopted.
- **CLI-output compressors** (e.g. ppgranger/token-saver) — when command output
  dominates context, pipe through a compressor instead of raw capture.

## Anti-patterns

- Re-pasting a doc into chat when a path reference would do.
- Loading "just in case" context the task never touches.
- Re-deriving in prose what a committed file already states — link it instead.
- Keeping a dying session alive past the compact trigger to avoid a handoff.
