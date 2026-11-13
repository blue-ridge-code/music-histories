# Skill verification checklist

Use this checklist before adding an external skill to the catalog and before installing
or updating any skill. A skill is accepted only when every item passes with inspectable
evidence. A failed or unverified item blocks acceptance; record the gap instead of
silently treating the skill as trustworthy.

## Skill verification template

- [ ] The frontmatter `description` says when the skill fires, not merely what it does.
- [ ] The skill has no unapproved external runtime dependencies. Any required runtime or
      utility is already approved in [`utilities.md`](utilities.md).
- [ ] The skill uses the portable format: Markdown with spec-subset frontmatter, relative
      paths, and provider-specific behavior kept in sidecars.
- [ ] Success criteria exist and are measurable: testable facts, commands with expected
      results, or observable output requirements rather than aspirations.
- [ ] Errors fail visibly and include clear recovery guidance; there is no silent failure.
- [ ] Composition rules are documented in
      [`skill-composition-map.md`](skill-composition-map.md), including incompatibilities
      or ordering constraints.

## Verification record

Keep one record with the catalog review, installation change, or audit evidence:

```markdown
Skill: <name>
Source/version: <repository and immutable ref, or local path and commit>
Verified: YYYY-MM-DD
Result: pass | fail
Evidence: <test output, file:line references, and composition-map entry>
Gaps: <none, or the failed checklist items and required remediation>
```

Do not add a failing candidate to the external catalog or install it as an approved skill.
For an already-installed skill that fails during a recurring audit, report the breakage and
follow the deprecation process in [`skills.md`](skills.md) until it is repaired or replaced.
