# A2 · Diction — the word-choice guide

> Component of the [language persona system](../language.md). This is the project's
> word-choice authority: it holds the vocabulary machinery and decides **when and
> how strongly** each standard binds. Kickoff fills "Project setting" per project;
> blank = the default ladder below.

## What it is

Diction is word choice (Wheaton) — the specific words and phrases picked to build
meaning. Levers: formality level (formal / casual / slang — "are not angry" /
"aren't mad" / "ain't ticked"), connotation and charge ("stance" vs "spin"), verb
precision ("said" vs "declared" vs "insisted"), concrete vs abstract, and jargon
calibrated to the audience's expertise.

## The vocabulary machinery

Three sources, in precedence order:

1. **`CONTEXT.md` — settled project terms.** When it defines a term, use **exactly
   that term** in every register — it overrides the Oxford-3000 plain-synonym
   preference and any default phrasing. Project language is the load-bearing jargon
   the audience expects. Its `_Avoid_:` synonyms carry the force of the always-avoid
   list. Layer rules (when to create it, how terms settle):
   [../language.md](../language.md). **Always binding once it exists, at 100% in
   every register.**
2. **ASD-STE100 — simplified technical English.** Two parts that bind *separately*:
   the **writing rules** (short imperative sentences, one word = one meaning, active
   voice, unambiguous warnings) and the **dictionary** (approved / non-approved
   words). Ships pre-distilled in the language-persona skill — consult these, never
   the PDF: [ste-100-writing-rules.md](../../../.agents/skills/language-persona/references/ste-100-writing-rules.md)
   (the 53 rules, distilled) and [ste-100-dictionary.md](../../../.agents/skills/language-persona/references/ste-100-dictionary.md)
   (grep it, never read it whole).
3. **American Oxford 3000 — core everyday vocabulary.** For general and persuasive
   writing: when a word sits outside the list, prefer a listed synonym unless the
   term is load-bearing jargon the audience expects. Lookup table (grep):
   [oxford-3000-wordlist.md](../../../.agents/skills/language-persona/references/oxford-3000-wordlist.md).

The source PDFs stay in the skill's `references/` folder as standards of record —
open one only to settle a dispute or verify a suspicious table entry.

## How strongly each standard binds

Influence is a **dial per register, not a switch**. Percentages below are rough
binding strength — a project's own ladder (set at kickoff) overrides these defaults:

| Register / document type | CONTEXT.md | STE-100 rules | STE-100 dictionary | Oxford 3000 |
|---|---|---|---|---|
| Safety-critical procedure (aircraft maintenance manual) | 100% | **~100%** — all 53 rules | **binding** — approved words only | silent |
| Technical procedure, agent-facing doc | 100% | **~50%** — short sentences, one meaning per word, no synonym drift, warnings pattern | advisory — prefer approved words; project jargon allowed | silent |
| General project doc (README, issue, report) | 100% | light — clarity habits only | silent | preferred |
| Persuasive (letter, proposal, application) | 100% | silent | silent | **strong** — plain listed words, no jargon |
| Creative (poetry, fiction) | 100% where terms exist | **0%** | 0% | 0% |

0% never licenses bad writing: the always-avoid list in
[../language.md](../language.md) applies in every register.

## Register rules (defaults)

- **Technical sections → STE-100 guardrails.** Approved terms only; no synonym
  drift (pick one name per thing and keep it); active voice; short sentences;
  warnings that state the hazard, the consequence, and the action.
- **Persuasive sections → Oxford-3000 plain words.** No jargon; concrete asks;
  short paragraphs; one idea per sentence.
- **Mixed documents may switch register per section — and must say so.** Note the
  register at the top of any section that differs from the document's default.

## Template examples

### Name the model once

**Before:** "Maintain synchronization among the multiple skill-storage locations used by
the supported providers."

**After:** "One canonical set of skills, thin per-provider adapters."

_Why: `canonical` and `adapter` carry one stable meaning throughout the template. The
sentence removes abstract filler. Source: [`docs/agents/skills.md`](../skills.md)._

### Use the action as the label

**Before:** "Outdated documentation artifacts should not be removed and should instead be
annotated with an indication of replacement."

**After:** "**Supersede, don't delete**: stale docs get a `> Superseded …` banner pointing
at the live source."

_Why: Concrete verbs replace administrative nouns, and the exact banner text prevents
synonym drift. Source: [`AGENTS.md`](../../../AGENTS.md)._

## Kickoff questions

- Which registers does this project actually write in? (Drop unused ladder rows;
  add project-specific ones.)
- Per register: how strongly should STE-100 bind — rules and dictionary separately?
- What vocabulary does the audience expect that STE-100 or Oxford 3000 would
  reject? (Those are CONTEXT.md candidates for a grilling session.)

## Default (minimal kickoff)

The binding-strength ladder table above **is** the median default — minimal kickoff writes
"kickoff default — median, unrefined" into "Project setting" and leaves the ladder
unedited. The full A1–B3 workshop is what edits individual cells for this project's actual
registers.

## Project setting

<!-- Filled at kickoff. Suggested format: the ladder table above, edited to this
     project's registers, with a one-line reason per non-default cell. -->
