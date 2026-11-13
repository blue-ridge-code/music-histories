---
name: language-persona
description: Enforce the project's tone profile and language standards on all written output — apply the technical or persuasive register, approved-vocabulary rules, and the always-avoid list. Fire whenever drafting or editing prose the project produces (letters, applications, docs, READMEs, issues, proposals).
---

# Language persona

## Problem

Without enforcement, project prose drifts: AI-isms creep in, jargon leaks into persuasive
pieces, technical sections get vague, and tone varies by whoever (or whatever) wrote
last. This skill makes [docs/TONE.md](../../../docs/TONE.md) and
[docs/agents/language.md](../../../docs/agents/language.md) executable on every draft.

## When to use

- Drafting or editing any prose the project produces: letters, applications, docs,
  READMEs, issues, proposals, emails.
- Reviewing a draft before it goes to a human gate.

## When NOT to use

- Code, config, commit messages, or log output — precision matters there, persona does
  not.
- Before kickoff has filled docs/TONE.md: apply the template defaults in
  docs/agents/language.md instead and say so.

## Process

1. **Load the profile.** Read docs/TONE.md (audience, register dials, persuasion rules,
   project avoid-list additions), docs/agents/language.md (layers, always-avoid list),
   and the filled "Project setting" sections in docs/agents/voice/ (A1–B3 — skip
   guides that are still blank). If CONTEXT.md exists, load it too: its settled
   project terms win on word choice, overriding the Oxford-3000 plain-synonym
   preference and any default phrasing. Precedence: CONTEXT.md (words) > TONE.md +
   voice settings (persona) > template defaults.
2. **Consult the ready-made instruction sets.** The standards ship pre-distilled inside
   this skill — use these, and never re-parse the PDFs:
   - [references/ste-100-writing-rules.md](references/ste-100-writing-rules.md) — the 53
     writing rules, distilled. Read the relevant section at draft/review time.
   - [references/ste-100-dictionary.md](references/ste-100-dictionary.md) — approved and
     non-approved word table. Grep it; never read it whole.
   - [references/oxford-3000-wordlist.md](references/oxford-3000-wordlist.md) — the core
     vocabulary table. Grep before using an off-list word in persuasive register.

   The PDFs in this same folder remain the standards of record: open one only to settle
   a dispute or verify a table entry that looks wrong.
3. **Pick the register** per piece, or per section within a piece, and apply the
   binding strength from docs/agents/voice/a2-diction.md — its default ladder, or the
   project's own ladder if kickoff filled one:
   - **Technical register** — STE-100 at the strength the ladder sets: approved
     terms, one meaning per word, no synonym drift, short sentences, active voice,
     warnings before steps.
   - **Persuasive register** — Oxford-3000 plain words, no jargon, short sentences,
     concrete asks (who does what by when), warmth per the dial.
4. **Draft or edit** to the profile: audience knowledge, the formality / technicality /
   warmth dials, persuasion rules, technical guardrails.
5. **Enforce the avoid-lists.** Remove the always-avoid patterns from
   docs/agents/language.md (weasel words, AI-isms, vague intensifiers, legalese outside
   legal docs), every project addition listed in docs/TONE.md, and every `_Avoid_:`
   synonym banned by CONTEXT.md.
6. **Flag, don't improvise.** If a new pattern feels ban-worthy, ask the user before
   adding it to an avoid-list. Never invent new banned patterns silently.

## Output

Prose that conforms to the profile, with a one-line note of which register was applied.
On request, a short before → after diff of the edits, suitable for the examples section
of docs/TONE.md.

## Notes

- The PDFs are the standards of record; the markdown instruction sets are derived from
  them. The two lookup tables are script-generated — regenerate rather than hand-edit
  rows (parser scripts: `references/build/`; regeneration needs the PDFs). The
  writing-rules file is a curated distillation — edit it directly, but stay faithful to
  the PDF.
- If docs/TONE.md is still the placeholder, say so and apply the template defaults.
- If CONTEXT.md does not exist yet, the vocabulary layer is silent — terminology has
  not settled. Note candidate terms for a future grilling session instead of inventing
  a glossary.
- Persona controls style, never facts. Do not soften, omit, or embellish content to fit
  a register.
- Composition: orthogonal — applies to the output of any skill and conflicts with none
  ([skill-composition-map](../../../docs/agents/skill-composition-map.md)).
