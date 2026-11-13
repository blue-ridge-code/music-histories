# Growing the ontology

`ontology-core.ttl` stays lean on purpose (see `AGENTS.md`'s "no speculative
scaffolding" rule). This is the procedure for adding to it later — modeled on
how CIDOC-CRM actually grows: a class only enters the model because a named
question could not otherwise be answered, and every class carries a scope
note that says so in place of a changelog. Do not add a class or property
without running all four steps.

## The procedure

**(a) State the competency question that can't currently be answered.**
Write it as one sentence, in the same "Answers: ..." form already used in
`ontology-core.ttl`. If you cannot write this sentence concretely — naming a
real query an agent would actually run — stop. That is what "no speculative
scaffolding" means in practice: "might be useful later" is not a competency
question.

**(b) Check whether an existing class or property already answers it**, via a
different name or a more general form. Read every `rdfs:comment` in
`ontology-core.ttl` before concluding the answer is no — CIDOC-CRM's own
history is mostly this step: most proposed new classes turn out to be an
existing class under a different name, or a value that belongs in
`:description` free text rather than a new typed field. If an existing term
covers it, use that term and stop here — do not add anything.

**(c) If truly new, write it in `ontology-core.ttl` and `shapes-core.ttl` in
the same change.** In `ontology-core.ttl`:
- New class: `rdfs:subClassOf :Entity` directly — do not create a subclass of
  a subclass; the hierarchy stays one layer deep so `:contains`/`:dependsOn`
  traversal never has to reason about depth.
- New property: pick the tightest correct `rdfs:domain`/`rdfs:range`, not
  `:Entity`/`:Entity`, unless the property is genuinely meant to apply across
  every subclass (like `:name` or `:ownedBy`).
- Either way, the `rdfs:comment` is the competency question from step (a),
  not a restatement of the label.

Then in `shapes-core.ttl`, add a shape only for constraints that trace back
to that same competency question, and keep it drift-free against what you
just wrote:
- `sh:datatype` must equal the property's `rdfs:range` exactly when the range
  is a datatype.
- `sh:class` must equal the property's `rdfs:range` exactly when the range is
  a class — not a subclass or superclass of it. If you want a narrower
  constraint than the property's declared range (e.g. "here specifically it
  must be a Symbol, not any Entity"), that is a sign you need a new,
  precisely-typed property instead of a narrowing shape — see the
  `:contains`/`:declares` split in `ontology-core.ttl` for a worked case of
  exactly this.
- Do not put a shared `sh:in` enum on a base shape if subclasses need
  different values for the same property path. SHACL's `sh:targetClass`
  matching includes subclasses, so a subclass instance must satisfy every
  shape whose target it matches — two conflicting enums on the same path
  intersect to almost nothing. `shapes-core.ttl` deliberately has no `:status`
  enum on `:EntityShape` for this reason; `:Task`, `:Decision`, and any future
  class with a status vocabulary each declare their own.

**(d) Log why, in one line, in `docs/decisions.md`** using the project's
standard entry format (Context / Decision / Consequences / Revisit when).
This is the durable trail — `ontology-core.ttl`'s comments say *what* a term
means, `docs/decisions.md` says *why it was added and when to reconsider it*.
Optionally, if the addition was itself decided in-graph (not just in the
docs), record it as a `:Decision` instance with `:changesTerm` set to the new
term's name — that property exists specifically so ontology evolution is
queryable from the graph, not only from prose history.

## Worked example: "should we add an `Environment` class?"

**(a) Competency question.** "Which environment (dev / staging / prod) was
this `ToolCall` executed against, so a destructive command run in prod can be
told apart from the identical command run in dev?" Concrete, and no existing
field answers it — proceed to (b).

**(b) Check for an existing alternative.**
- `:status` on `:Entity`? No — status is lifecycle state (open/closed,
  proposed/accepted), not a deployment target; overloading it would make the
  per-class enum discipline in `shapes-core.ttl` incoherent.
- `:description` free text on `:ToolCall`? Technically it could hold
  `"ran against prod"`, but then "show me every ToolCall against prod" is a
  string search over free text, not a query the graph can answer reliably —
  fails the actual competency question in (a).
- A naming convention on `:Module`/`:Project` (e.g. a module named
  `prod-api`)? Fragile and unqueryable structurally; also conflates two
  different things (what the module is vs. where a given call ran).
- Conclusion: no existing class or property covers this without a
  workaround that breaks the moment someone forgets the convention. Genuinely
  new — proceed to (c).

**(c) Write it.**
```turtle
:Environment a owl:Class ;
    rdfs:subClassOf :Entity ;
    rdfs:label "Environment" ;
    rdfs:comment "Answers: which deployment target (dev, staging, prod) is a ToolCall or Constraint scoped to, so a destructive action in prod can be distinguished from the same action in dev? Direct subclass of :Entity, not of :Project — an Environment can outlive or span multiple Projects." .

:executedIn a owl:ObjectProperty ;
    rdfs:domain :ToolCall ;
    rdfs:range :Environment ;
    rdfs:label "executedIn" ;
    rdfs:comment "Answers: which Environment was this ToolCall actually run against? Lets a Constraint reference :Environment via :validatedBy's target to express environment-scoped rules (e.g. 'no writes to :Environment prod without a Person owner')." .
```
And the matching shape in `shapes-core.ttl`:
```turtle
:ToolCallShape sh:property [
    sh:path :executedIn ;
    sh:class :Environment ;
    sh:maxCount 1 ;
] .
```
(`sh:class :Environment` matches `:executedIn`'s `rdfs:range` exactly — no
drift.)

**(d) Log it.** One `docs/decisions.md` entry: *Context: agents were about to
be given prod-write tool access with no graph-level way to flag it. Decision:
added `:Environment` + `:executedIn` to `ontology-core.ttl`/`shapes-core.ttl`
per the ontology-agent growing procedure. Consequences: `Constraint` rules can
now be scoped by environment. Revisit when: if a ToolCall ever needs more
than one Environment at once (e.g. a migration touching staging and prod),
`:executedIn`'s `sh:maxCount 1` will need to be dropped.*
