# Language persona system

One system governs how the project sounds in every register. Three layers:
settled project vocabulary in `CONTEXT.md`, a per-project profile in
[../TONE.md](../TONE.md), and the defaults in this file. **Precedence:
CONTEXT.md (which words) > TONE.md + voice settings (which persona) > this file
(defaults).** The `language-persona` skill enforces all layers at write time.

## The writer's voice framework

The writer's voice is specified component by component. Eight short guides in
`voice/` — each defines one component, the levers a writer controls, the kickoff
questions that pin it down, and a **Project setting** section that kickoff fills
when the interview shows voice matters to the project. Blank settings mean the
defaults apply.

| # | Guide | Controls |
|---|---|---|
| A1 | [Tone](voice/a1-tone.md) | Attitude toward topic and reader (NN/g four dimensions) |
| A2 | [Diction](voice/a2-diction.md) | Word choice — when and how strongly CONTEXT.md, STE-100, and Oxford 3000 bind |
| A3 | [Syntax](voice/a3-syntax.md) | Sentence structure, length, and word order |
| A4 | [Pacing](voice/a4-pacing.md) | Speed of the story or argument |
| A5 | [Point of view](voice/a5-point-of-view.md) | Who speaks, and from what distance |
| B1 | [Rhythm](voice/b1-rhythm.md) | Musical beat of long and short sentences |
| B2 | [Persona](voice/b2-persona.md) | The character the author plays on the page |
| B3 | [Attitude](voice/b3-attitude.md) | The emotional undercurrent behind the words |

Each guide includes two **Template examples**. The `Before` line is an intentionally poor
contrast. The `After` line quotes current template text and links to its source. Use these
examples to understand the component; they do not replace a project's setting.

Background research behind the framework: [voice/research-notes.md](voice/research-notes.md)
(reference reading — not loaded at write time).

## Layers

### Project vocabulary: `CONTEXT.md`

`CONTEXT.md` holds the project's settled domain language, developed through the
wayfinder process: grilling interviews sharpen candidate terms, prototyping
settles them through real use (the `domain-modeling` skill accelerates this
when installed). Each entry gives a plain definition and an `_Avoid_:` list of
banned synonyms.

- When CONTEXT.md defines a term, use **exactly that term** — it overrides every
  other vocabulary source. Project language is the load-bearing jargon the
  audience expects.
- `_Avoid_:` synonyms carry the force of the always-avoid list below.
- Create CONTEXT.md only when terminology settles through actual work — never
  write a speculative glossary (anti-scaffolding, AGENTS.md). Until it exists,
  this layer is silent.

### Per-project profile: `docs/TONE.md`

Kickoff fills TONE.md from the interview; every writer loads it first. It
carries:

- **Dials** — formality, technicality, warmth, each 1–5, with a one-line note
  on what the chosen number means.
- **Persuasion rules** — what may be claimed, what needs evidence, which asks
  are in scope.
- **Technical guardrails** — approved terms, units, capitalization.
- **Project avoid-list** — additions beyond the always-avoid list below.
- **Before → after examples** — real sentences rewritten to the profile.

Per-component voice settings live in the `voice/` guides' Project setting
sections; kickoff fills them at the same moment.

### Defaults: word-choice machinery and registers

The base standards (STE-100, Oxford 3000), the per-register binding-strength
ladder, and the register rules live in the diction guide:
[voice/a2-diction.md](voice/a2-diction.md).

## Always-avoid list (all registers)

- **AI-isms**: "delve", "tapestry", "in today's fast-paced world", "it's
  important to note", "furthermore/moreover" chains.
- **Vague intensifiers**: very, really, extremely.
- **Weasel words**: some, many, various, arguably, "it could be said".
- **Legalese** outside legal documents.
- **Passive voice** where the actor matters.
- **Exclamation marks** in formal output.
- **Emoji** unless the user uses them first.

## Modification procedure

1. Edit [../TONE.md](../TONE.md) or a voice guide's Project setting — never fork
   the profile into side files.
2. Log significant persona changes in [../decisions.md](../decisions.md), with
   the reason.
3. Let the `language-persona` skill enforce the result; do not hand-maintain
   parallel style notes.
