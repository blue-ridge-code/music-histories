# Query patterns

`scripts/query_graph.py` answers structural questions by traversing an
already-extracted `graph.jsonl` in memory, instead of re-reading project
files. Every pattern below is checked against two things: (1) it actually
runs against a real graph, and (2) `bootstrap.py` (or, for the one pattern
called out separately below, the ongoing tool-call-commit path) actually
populates the edges the query depends on. A query pattern documented here
is a promise that the fact-gathering side of this skill keeps.

## 1. "What does X contain?"

- **Question**: "What top-level modules does this project have?" / "What's
  directly inside module Y?"
- **Invocation**: `python scripts/query_graph.py contains project:<name>`
  (or a `module:<name>` id), or `contains(graph, entity_id)` in Python.
- **Populated by**: `bootstrap.py` walks the project root once and emits a
  `project --contains--> module` edge for every non-vendor top-level
  directory (`Module` entities; `SKIP_DIR_NAMES` excludes `.git`,
  `node_modules`, `.venv`, `dist`, `build`, etc.).
- **Cost without the graph**: `ls` / `Get-ChildItem` the root, manually
  filter out tooling directories, and repeat by hand for every module you
  care about across a session. Cheap for one lookup, but it re-derives the
  same list every time an agent asks, with no record of when it changed.
- **Cost with the graph**: one dict lookup on `out_edges[entity_id]`
  filtered to `predicate == "contains"` — O(children), no filesystem call.
- **Verified**: run against this repo, `contains project:repo-test`
  returned `docs`, `gauntlet`, `inbox`, `scripts` (vendor/tooling dirs like
  `.git`, `.claude`, `.agents` correctly excluded by the skip-list, matching
  a manual `ls` of the same tree).

## 2. "What depends on X?" / "What does X depend on?"

- **Question**: "If I change the `httpx` version, what in this repo is
  affected?" / "What does the `inbox` module pull in?"
- **Invocation**: `python scripts/query_graph.py depends-on <entity_id>
  [--depth N]`, or `depends_on(graph, entity_id, depth=None)` in Python.
  Returns both directions: `dependencies` (what X needs) and `dependents`
  (what needs X), each transitive out to `depth` hops (unbounded if
  omitted).
- **Populated by**: `bootstrap.py` parses every `package.json`,
  `requirements.txt`, `pyproject.toml`, `go.mod`, and `*.csproj` it finds
  (pruning vendor directories), and emits one `dependsOn` edge per real
  declared dependency name, attributed to the nearest top-level module (or
  the project root if the manifest lives there).
- **Cost without the graph**: answering "what depends on X" by reading
  files means opening every manifest that might mention X (and, for
  transitive answers, manifests of manifests) and grep-checking; for "what
  does X depend on", open X's manifest and manually strip version
  specifiers. Neither scales past a couple of hops before you're tracking
  a mental adjacency list by hand.
- **Cost with the graph**: `depends-on <id>` is one BFS over an
  already-built adjacency map — a single command, correct at any depth.
  The win scales with project size and manifest count: this template's own
  repo has exactly one manifest file, so here "read 1 file" and "run one
  graph query" are nearly the same cost — a near-degenerate small example.
  The comparison earns its keep on a project with many manifests scattered
  across modules, where the graph answers in one query what would otherwise
  mean opening and cross-referencing every one of them by hand.
- **Verified**: this repo has one real manifest,
  `inbox/raw/_extract/ogas_skill/ogas_skill/requirements.txt`. `depends-on
  module:inbox` returned real dependency names `pydantic-ai`, `pydantic`,
  `httpx` as `dependencies`; `depends-on dependency:pypi:httpx` returned
  `module:inbox` as a `dependent` — the reverse direction resolved
  correctly from the same edge list.

## 3. Bounded neighborhood around an entity

- **Question**: "Give me the local structural context around X before I
  touch it" (a cheaper version of "what's blocking task Z" or "what would
  a change here ripple into") — useful when you don't know in advance
  whether the relevant edges are `contains` or `dependsOn`.
- **Invocation**: `python scripts/query_graph.py subgraph <entity_id>
  --depth N` (default depth 2), or `subgraph(graph, entity_id, depth)` in
  Python. Returns every node reachable within N hops over *any* edge type
  in *either* direction, plus the connecting edges.
- **Populated by**: whatever `contains` / `dependsOn` (and, once used,
  `blocks`) edges already exist in the graph — this pattern doesn't need
  its own extraction step, it walks facts the other patterns already
  populate.
- **Cost without the graph**: manually chase references outward from one
  file/module — open it, note what it imports and what directory it's in,
  open those, repeat — bookkeeping the visited set yourself to avoid
  cycles.
- **Cost with the graph**: one bounded BFS (adjacency dict + queue +
  visited set, modeled on the traversal in `ogas`'s
  `KnowledgeGraph.get_dependency_graph()`, generalized to all predicates
  and both directions, and capped by depth instead of running until the
  component is exhausted).
- **Verified**: `subgraph project:repo-test --depth 2` returned all 8
  nodes and 7 edges in the test graph (4 `contains` + 3 `dependsOn`) in one
  call.

## Cut: task blocking (`blocked-by` / `blocking`)

`query_graph.py` ships `blocked_by(task_id)` and `blocking(task_id)`
functions — the ontology defines `Task` and a `:blocks` property, and the
CLI exposes both — but **this file does not document them as a proven
query pattern**, because nothing in `bootstrap.py` populates any `:blocks`
edge. Unlike dependencies or directories, "what's blocking what" is
dynamic project state, not a structural signal a zero-LLM repo scan can
observe (there's no manifest file that says "task A blocks task B").
Tested against an empty graph, `blocked-by <task_id>` correctly returns
"nothing recorded" rather than fabricating an answer.

This is a promise the *ongoing* graph-maintenance path has to keep, not
bootstrap: once an agent creates `Task` entities and `:blocks` edges as
part of normal work (the same append-one-line-to-`graph.jsonl` convention
bootstrap uses, or the commit step in `validate_tool_call.py`'s propose →
validate → execute → commit loop), `blocked-by` starts returning real
answers with no code changes needed. Re-promote this section to a
documented pattern once that write path exists and has been exercised —
don't take this note's word for it that the edges will show up.

## Limits, stated plainly

- The graph only knows what has been recorded. A missing manifest format,
  a dependency declared somewhere `bootstrap.py` doesn't look, or a fact
  nobody ever committed will silently make a query return "nothing" rather
  than raise an error — always sanity-check a suspiciously empty result
  against whether the fact was ever extractable in the first place.
- `contains` is direct children only (matches `bootstrap.py`, which only
  records top-level directories, not a recursive file tree) — do not
  expect a `contains` query to find a file three directories deep.
- Re-running `bootstrap.py` without `--force` never updates a stale graph;
  it only creates one if none exists yet. Use `--force` after significant
  structural change (new manifests, renamed top-level directories).
