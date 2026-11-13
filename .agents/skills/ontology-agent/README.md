# ontology-agent

A portable skill that gives an agent durable, typed project memory (a small knowledge
graph under `.ontology-agent/`) and a deterministic pre-execution gate for tool calls,
so structural questions get answered from the graph instead of re-read files or
guesswork, and malformed tool calls get caught before they run.

Start with `SKILL.md` — it has the problem statement, when (and when not) to use this,
the full process, and the success criteria this skill is held to. `references/` covers
the validation contract, query patterns, and how to grow the ontology; `scripts/` is
the zero-dependency implementation; `assets/` holds the templates `bootstrap.py` copies
into a project.
