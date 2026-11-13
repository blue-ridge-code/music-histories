#!/usr/bin/env python3
"""Query .ontology-agent/graph.jsonl without re-reading project files.

Stdlib only. No RDF library, no NetworkX, no SPARQL engine -- the graph is
small (a project of a few hundred files yields at most a few thousand
entity/edge records), so a plain adjacency dict built once on load and
walked with breadth-first search is both correct and fast enough. Building
the index once (rather than re-scanning the JSONL file per query) matters
once an agent asks more than one question per invocation, which is the
common case.

Usable two ways:
  1. As a library: `from query_graph import load_graph, depends_on, ...`
  2. As a CLI:      `python query_graph.py depends-on module:src`

Record shapes read from graph.jsonl (see bootstrap.py):
  entity: {"kind": "entity", "id": "...", "type": "...", ...fields}
  edge:   {"kind": "edge", "subject": "...", "predicate": "...", "object": "..."}
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Graph:
    entities: dict[str, dict] = field(default_factory=dict)
    # out_edges[subject] = list of (predicate, object)
    out_edges: dict[str, list[tuple[str, str]]] = field(default_factory=dict)
    # in_edges[object] = list of (predicate, subject)
    in_edges: dict[str, list[tuple[str, str]]] = field(default_factory=dict)

    def label(self, entity_id: str) -> str:
        rec = self.entities.get(entity_id)
        if rec and rec.get("name"):
            return f'{entity_id} ("{rec["name"]}")'
        return entity_id


def default_graph_path(start: Path | None = None) -> Path:
    """Search upward from `start` (or cwd) for a .ontology-agent/graph.jsonl."""
    cur = (start or Path.cwd()).resolve()
    for candidate in (cur, *cur.parents):
        p = candidate / ".ontology-agent" / "graph.jsonl"
        if p.exists():
            return p
    return cur / ".ontology-agent" / "graph.jsonl"


def load_graph(path: str | Path) -> Graph:
    graph = Graph()
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(
            f"no graph at {p} -- run bootstrap.py first (python scripts/bootstrap.py --root .)"
        )
    with p.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{p}:{lineno}: invalid JSON ({exc})") from exc
            kind = rec.get("kind")
            if kind == "entity":
                graph.entities[rec["id"]] = rec
            elif kind == "edge":
                subj, pred, obj = rec["subject"], rec["predicate"], rec["object"]
                graph.out_edges.setdefault(subj, []).append((pred, obj))
                graph.in_edges.setdefault(obj, []).append((pred, subj))
            # unknown "kind" values are ignored, not fatal -- forward-compatible
            # with record types future pieces of this skill may add.
    return graph


# ---------------------------------------------------------------------------
# Query functions
# ---------------------------------------------------------------------------

def contains(graph: Graph, entity_id: str) -> list[str]:
    """Direct children of entity_id via a :contains edge. Not transitive."""
    return [obj for pred, obj in graph.out_edges.get(entity_id, []) if pred == "contains"]


def depends_on(graph: Graph, entity_id: str, depth: int | None = None) -> dict:
    """Transitive dependencies and dependents of entity_id, out to `depth`
    hops (None = unbounded) along :dependsOn edges.

    Returns {"dependencies": [...], "dependents": [...]} -- dependencies are
    things entity_id (transitively) depends on; dependents are things that
    (transitively) depend on entity_id. Both lists exclude entity_id itself
    and are ordered by BFS distance (closest first).
    """

    def bfs(start: str, edge_map: dict[str, list[tuple[str, str]]]) -> list[str]:
        visited = {start}
        order: list[str] = []
        queue: deque[tuple[str, int]] = deque([(start, 0)])
        while queue:
            node, dist = queue.popleft()
            if depth is not None and dist >= depth:
                continue
            for pred, neighbor in edge_map.get(node, []):
                if pred != "dependsOn" or neighbor in visited:
                    continue
                visited.add(neighbor)
                order.append(neighbor)
                queue.append((neighbor, dist + 1))
        return order

    return {
        "dependencies": bfs(entity_id, graph.out_edges),
        "dependents": bfs(entity_id, graph.in_edges),
    }


def subgraph(graph: Graph, entity_id: str, depth: int = 2) -> dict:
    """Bounded neighborhood around entity_id: every node reachable within
    `depth` hops over ANY edge (either direction), plus the edges connecting
    them. Modeled on the queue+visited-set BFS traversal in the ogas draft's
    KnowledgeGraph.get_dependency_graph(), but generalized to all predicates
    and both directions, and capped by depth instead of running until the
    whole component is exhausted.
    """
    visited = {entity_id}
    nodes = [entity_id]
    edges: list[dict] = []
    queue: deque[tuple[str, int]] = deque([(entity_id, 0)])

    while queue:
        node, dist = queue.popleft()
        if dist >= depth:
            continue
        neighbors = [(p, o, "out") for p, o in graph.out_edges.get(node, [])]
        neighbors += [(p, s, "in") for p, s in graph.in_edges.get(node, [])]
        for pred, other, direction in neighbors:
            if direction == "out":
                edges.append({"subject": node, "predicate": pred, "object": other})
            else:
                edges.append({"subject": other, "predicate": pred, "object": node})
            if other not in visited:
                visited.add(other)
                nodes.append(other)
                queue.append((other, dist + 1))

    # de-dupe edges (both directions of traversal can surface the same edge)
    seen = set()
    unique_edges = []
    for e in edges:
        key = (e["subject"], e["predicate"], e["object"])
        if key not in seen:
            seen.add(key)
            unique_edges.append(e)
    return {"nodes": nodes, "edges": unique_edges}


def blocked_by(graph: Graph, task_id: str) -> list[str]:
    """Tasks that block task_id, via a :blocks edge (subject blocks object).

    NOTE ON HONESTY: bootstrap.py does not currently populate any :blocks
    edges -- there is no zero-LLM structural signal for task-blocking
    relationships during a repo scan (unlike dependencies or directories,
    "what blocks what" is dynamic project state, not something sitting in
    a manifest file). This function is provided because the ontology
    defines Task and :blocks, and the ongoing graph-commit path (an agent
    appending Task entities and :blocks edges to graph.jsonl as it works,
    the same way validate_tool_call.py's protocol commits new facts after
    a successful tool call) can and should populate it during real use.
    Until something has written those edges, this returns an empty list --
    that is a correct, honest answer, not a broken query. See
    references/query-patterns.md for why this is NOT documented as one of
    the proven bootstrap-populated patterns.
    """
    return [subj for pred, subj in graph.in_edges.get(task_id, []) if pred == "blocks"]


def blocking(graph: Graph, task_id: str) -> list[str]:
    """Tasks that task_id currently blocks (the inverse of blocked_by)."""
    return [obj for pred, obj in graph.out_edges.get(task_id, []) if pred == "blocks"]


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _print_json(obj) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Query .ontology-agent/graph.jsonl")
    parser.add_argument("--graph", default=None, help="path to graph.jsonl (default: search upward from cwd)")
    parser.add_argument("--json", action="store_true", help="print raw JSON instead of a formatted summary")
    sub = parser.add_subparsers(dest="command", required=True)

    p_contains = sub.add_parser("contains", help="direct children of an entity via :contains")
    p_contains.add_argument("entity_id")

    p_deps = sub.add_parser("depends-on", help="transitive dependencies/dependents via :dependsOn")
    p_deps.add_argument("entity_id")
    p_deps.add_argument("--depth", type=int, default=None, help="hop limit (default: unbounded)")

    p_sub = sub.add_parser("subgraph", help="bounded neighborhood around an entity, any edge type")
    p_sub.add_argument("entity_id")
    p_sub.add_argument("--depth", type=int, default=2)

    p_blocked = sub.add_parser("blocked-by", help="tasks blocking task_id (see docstring: not bootstrap-populated)")
    p_blocked.add_argument("task_id")

    p_blocking = sub.add_parser("blocking", help="tasks that task_id blocks (see docstring: not bootstrap-populated)")
    p_blocking.add_argument("task_id")

    args = parser.parse_args(argv)

    graph_path = Path(args.graph) if args.graph else default_graph_path()
    try:
        graph = load_graph(graph_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[error] {exc}", file=sys.stderr)
        return 1

    if args.command == "contains":
        result = contains(graph, args.entity_id)
        if args.json:
            _print_json(result)
        else:
            if not result:
                print(f"{args.entity_id} contains nothing (or is unknown to the graph)")
            for child in result:
                print(f"  contains -> {graph.label(child)}")

    elif args.command == "depends-on":
        result = depends_on(graph, args.entity_id, depth=args.depth)
        if args.json:
            _print_json(result)
        else:
            print(f"dependencies of {args.entity_id}:")
            for d in result["dependencies"]:
                print(f"  -> {graph.label(d)}")
            print(f"dependents of {args.entity_id}:")
            for d in result["dependents"]:
                print(f"  <- {graph.label(d)}")

    elif args.command == "subgraph":
        result = subgraph(graph, args.entity_id, depth=args.depth)
        if args.json:
            _print_json(result)
        else:
            print(f"subgraph around {args.entity_id} (depth {args.depth}): {len(result['nodes'])} nodes")
            for e in result["edges"]:
                print(f"  {e['subject']} --{e['predicate']}--> {e['object']}")

    elif args.command == "blocked-by":
        result = blocked_by(graph, args.task_id)
        if args.json:
            _print_json(result)
        else:
            if not result:
                print(f"nothing recorded as blocking {args.task_id} (no :blocks edges in graph yet)")
            for b in result:
                print(f"  blocked by -> {graph.label(b)}")

    elif args.command == "blocking":
        result = blocking(graph, args.task_id)
        if args.json:
            _print_json(result)
        else:
            if not result:
                print(f"{args.task_id} is not recorded as blocking anything")
            for b in result:
                print(f"  blocks -> {graph.label(b)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
