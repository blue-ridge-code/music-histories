---
name: Skills registry refresh & skill audit
about: Run the quarterly skills maintenance check — registry review and installed-skill audit
title: 'Refresh skills registry'
---

> Recurring quarterly task. Registry and composition guidance: `docs/agents/skills.md`
> and `docs/agents/skill-composition-map.md`. Log findings in `docs/decisions.md` with an
> "Audit" tag, evidence links, and related issues.

## Outcome

Every external catalog row in `docs/agents/skills.md` has current maintenance, license,
source-policy, and replacement evidence; installed skills still work and are still used.

## Review

Follow the **Quarterly review checklist** in `docs/agents/skills.md`:

- [ ] Apply `docs/agents/skill-verification-checklist.md` to every installed skill,
      including self-test or representative-use evidence.
- [ ] Review installed skills: any unused since the last kickoff or audit? Move them to
      the "Deprecated skills" table with a reason, replacement, and date.
- [ ] Confirm each skill's dependencies still resolve and the tools or services it calls
      still exist.
- [ ] Check external catalogs for newer or cheaper alternatives; update `Last evaluated`.
- [ ] Confirm `docs/agents/skill-composition-map.md` still matches what is installed.

## Acceptance evidence

<!-- Link the upstream sources checked and the registry, changelog, deprecation, or
     decision-log changes. Close with evidence of each tested skill. -->
