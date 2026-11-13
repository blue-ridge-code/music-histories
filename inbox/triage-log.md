# Inbox triage log

Committed record of every item that has passed through `inbox/raw/`. See
[docs/agents/intake.md](../docs/agents/intake.md) for the channel rules and
dispositions.

| Date | Filename | SHA-256 | Disposition | Destination |
| --- | --- | --- | --- | --- |
| 2026-08-09 | gauntlet-loop.zip | 26dd2c2026ab92b8cd1136f19592335d29e0d25aeda1d6b0e5d384b46d460ba3 | Promote to docs | `.agents/skills/gauntlet-loop/` (synced to `.claude/skills/gauntlet-loop/`); raw file archived to `inbox/archive/2026-08-09/2026-08-09-gauntlet-loop.zip` |
| 2026-08-09 | ontology-kg-agent-chat-export.zip | 57f156298887c33244d872e72d4ae9efc91270807b38f2174a039b1ee4c44c2b | Promote to docs (synthesis input) | Strongest of four competing drafts; synthesized into `.agents/skills/ontology-agent/`. Archived to `inbox/archive/2026-08-09/2026-08-09-ontology-kg-agent-chat-export.zip` |
| 2026-08-09 | ogas_skill.zip | 5a0b243ea860f5192724f5715868b48d34c660b5d448616f82eeabeace37b93f | File as evidence (synthesis input, not adopted as-is) | Fan-out/critic/value-scoring framework and pydantic-ai/rdflib/networkx dependency stack rejected — duplicates `.agents/skills/gauntlet-loop/` and violates the zero-runtime-dependency invariant. Archived to `inbox/archive/2026-08-09/2026-08-09-ogas-skill.zip` |
| 2026-08-09 | Gemini - Ontological Agent Skill - chat_export.zip | 91b48c4cb1a67b64249947cf5461331caeb007afde95529efbeb531e4eeb28a1 | File as evidence (synthesis input, not adopted as-is) | TypeScript/Zod/N3/SHACL implementation with the same fan-out/critic apparatus rejected for the same reasons as ogas_skill.zip. Archived to `inbox/archive/2026-08-09/2026-08-09-gemini-ontological-agent-skill-chat-export.zip` |
| 2026-08-09 | deepseek_python_otological-agent-20260809_6e592d.py | 3860215736738acd0d04791921765018761dc887992b359e1085684a152f5bd6 | Delete after archiving (weakest input — simulated/theatrical, no real value beyond a discarded idea) | Monolithic script with simulated tool execution and hardcoded value-score formulas; no concept from it survived synthesis. Archived to `inbox/archive/2026-08-09/2026-08-09-deepseek-ontological-agent-prototype.py` for provenance only |
