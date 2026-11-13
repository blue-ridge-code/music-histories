# play-canon

A portable skill that applies literature-based play criteria to design, review, and
gauntlet loops. The criteria come from nine texts on play, each stored as its own source
file. Author names are labels showing where each piece of guidance or criticism comes
from; the agent never plays the author.

Plain Markdown. No scripts and no dependencies.

## Install

| Harness | Location |
|---|---|
| Claude Code, project | `.claude/skills/play-canon/` |
| Claude Code, global | `~/.claude/skills/play-canon/` |
| Claude apps | Upload the folder as a skill |
| Codex, Kimi Code, Copilot | `.agents/skills/play-canon/` in the repo |
| Anything else | Paste `SKILL.md` as instructions and keep `sources/` where the agent can read it |

## Use

```
Use play-canon to guide the design of <thing>.
Review <draft> with play-canon.
Use play-canon with gauntlet-loop on <goal>.
```

Every mode starts by fixing a claim (what kind of play or engagement the work is meant
to offer) and choosing two to four sources.

## Contents

```
play-canon/
├── SKILL.md                                    the three modes and the source index
└── sources/
    ├── _TEMPLATE.md                            shape for adding a source
    ├── huizinga-homo-ludens.md
    ├── caillois-man-play-and-games.md
    ├── sutton-smith-ambiguity-of-play.md
    ├── bateson-theory-of-play-and-fantasy.md
    ├── csikszentmihalyi-flow.md
    ├── nachmanovitch-free-play.md
    ├── carse-finite-and-infinite-games.md
    ├── leonard-mastery.md
    └── illich-deschooling-society.md
```

Each source file contains:

- source details, including a note on how faithful the summary is to the text;
- core concepts;
- guidance on interactions, structures, content, and style;
- anti-patterns;
- a review criterion with question seeds;
- a calibration plant;
- a fit note;
- an optional loop check.

## Adding a source

Copy `sources/_TEMPLATE.md`, fill in every section, and add a row to the Sources table
in `SKILL.md`. A new source must fail differently from the existing ones; otherwise,
merge it into the existing source's file.

## Fidelity

Each source file records its own fidelity: what has been checked against the text (with
page numbers and the edition used), and what its **Verify** line still lists. A concept
with no page number was summarized from general knowledge or a secondary source, and
guidance or findings that cite it are marked `(unchecked)`.

## Related

- Pack contract: `gauntlet-loop`'s `references/criteria-packs.md`.
- `scripts/tests/test_criteria_packs.py`, in repositories that ship both skills, checks
  every source file against that contract.
