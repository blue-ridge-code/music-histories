# Maintaining the VSCode Template

This runbook applies to `blue-ridge-code/vscode-template`. It explains how a useful
change moves from a project copy back into the template without importing project-specific
policy, private data, or unused structure.

## Feed an improvement back from a project copy

1. **Keep the project evidence.** Record the problem, the change, and the result in the
   project source of truth: a decision, issue, test, or review artifact.
2. **Extract the reusable rule.** Remove project names, credentials, absolute machine
   paths, and assumptions that do not hold across project types.
3. **Prove that it generalizes.** Name the project types that benefit and the trigger that
   makes the change useful. One successful special case is not a template default.
4. **Draft the handoff.** State the problem, proposed template change, evidence, affected
   files, and test case. Ask before posting an issue, pushing a branch, or opening a pull
   request.

Leave the change in the project copy when it depends on that project's domain language,
privacy posture, architecture, paid services, or governance.

## Workflow for template contributors

1. **Isolate the change.** Refresh `origin/main`, then create a dedicated task branch and
   worktree. Do not develop template changes in a project worktree or another session's
   checkout.
2. **Build the smallest reusable change.** Change only the canonical source. Update a
   generated mirror in the same change when the template defines one.
3. **Test a generated project.** Create a disposable project from the candidate template.
   Run the changed workflow from its documented entry point and verify the result
   end-to-end. For a documentation-only change, confirm that the generated project
   contains the files, links, commands, and kickoff state that a reader will use.
4. **Document the decision.** Add an entry to [`docs/decisions.md`](decisions.md) when a
   change alters `AGENTS.md` policy, an installed skill or default, a registry policy, or
   another significant template convention. Routine corrections do not need a decision.
5. **Commit with test evidence.** Keep the subject focused. Add
   `Tested on <project-name> for <use case>` to the commit body.
6. **Get an independent review.** Another agent or a human checks the candidate change and
   its generated-project evidence. The author fixes findings before merge.

Pushing, opening a pull request, and merging remain separate actions. Ask before each
external or irreversible step required by [`AGENTS.md`](../AGENTS.md).

## Before merge

- [ ] The branch contains one scoped template change and no project-owned work.
- [ ] A disposable generated project proves the documented path works end-to-end.
- [ ] Every pointer in `AGENTS.md`, `README.md`, and the changed docs resolves.
- [ ] A significant policy, skill/default, or registry-policy change has a decision entry.
- [ ] Changed registry entries have a current `Last evaluated` date and evidence.
- [ ] New files and directories have a load-bearing purpose; none are speculative.
- [ ] `.agents/skills/` is canonical and the Claude mirror is clean:
      `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\sync-skills.ps1 -Verify`.
- [ ] Reusable instructions use repository-relative paths and environment-variable
      secrets. Historical evidence may retain the exact path it proves.
- [ ] No secret, private project data, or paid-service authorization entered the change.
- [ ] `git diff --check` passes, and every new command was run from the documented working
      directory.
- [ ] An independent reviewer checked both the source change and test evidence.

## When to update the template

- **Major:** A project exposes a safety, privacy, governance, or core-workflow defect.
- **Medium:** Multiple project types need a proven convention, skill, integration, or
  registry policy.
- **Minor:** A correction improves clarity, repairs a link, or removes an ambiguity without
  changing behavior.

The size labels set review depth, not whether the change deserves evidence.

## When not to update the template

- A project-specific workaround, domain term, architecture choice, or governance rule.
- A one-off utility that belongs in the project's `scripts/` directory.
- A tool or layer that has not proved useful in a real project.
- A provider preference without alternatives, cost, evidence, and swap criteria.
- A convenience that adds permanent structure but has no current caller.

When in doubt, keep the change in the project that needs it. Promote it after another
project demonstrates the same need.
