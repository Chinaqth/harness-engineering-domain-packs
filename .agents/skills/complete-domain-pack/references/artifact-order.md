# Artifact Dependency Order

Build artifacts in this order unless the change contract records a justified dependency override:

1. `DOMAIN.md`: purpose, ownership, boundaries, stable inputs, outputs, and handoffs.
2. `domain.json`: identity, applicability, compatibility, and evidence placeholders.
3. `owners.json`: primary owner and required reviewers.
4. `rules/`: professional invariants that specialize but never weaken Kernel policy.
5. `workflows/`: repeatable delivery sequences with inputs, outputs, checks, and failure paths.
6. `evaluators/`: acceptance and evidence contracts for workflow outcomes.
7. `skills/`: reusable execution guidance backed by defined workflows and evaluators.
8. `templates/`: reusable output structures required by capabilities.
9. `capabilities.json`: assembly of existing workflows, Skills, tools, evaluators, permissions,
   and dependencies.
10. `routes.json`: selection metadata referencing existing capabilities.
11. Activation evidence: reproducible validation and representative routing results.

Do not create placeholder downstream artifacts merely to satisfy references.

