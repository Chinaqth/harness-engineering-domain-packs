# Domain Artifact Contracts

## Human Contract

- `DOMAIN.md`: define durable purpose, ownership, in-scope and out-of-scope behavior, inputs,
  outputs, handoffs, failure modes, and maturity.
- Rules: define enforceable professional invariants and their applicability.
- Workflows: define preconditions, ordered actions, outputs, verification, failure handling, and
  handoff.
- Evaluators: define criteria, evidence, negative paths, severity, and verdict semantics.
- Templates: define reusable output structure without project-specific facts.
- Skills: package non-obvious professional workflow, references, and deterministic helpers.
- `README-CH.md`: enumerate every current non-hidden production file and directory in Chinese;
  explain each item's responsibility and actual behavior, link descriptions to the authoritative
  English artifact, and introduce no independent rule, permission, or organization fact.

## Machine Contract

- `domain.json`: follow the manifest schema and keep registry identity, version, status, and owner
  synchronized.
- `owners.json`: identify authoritative owner and required reviewers.
- `capabilities.json`: reference existing workflows, Skills, evaluators, dependencies, tools, and
  permissions.
- `routes.json`: reference existing capabilities and use discriminating task types and signals.

Schema validity is necessary but does not demonstrate professional correctness.
