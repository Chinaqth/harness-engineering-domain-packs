# Autonomous Completion Generator-Evaluator Contract

## Builder

The Builder accepts only a registered Domain ID. It owns state, budgets, delegation, and final
classification but does not author professional content or issue evaluation scores.

## Researcher

The Researcher remains read-only for repository production content. It discovers current,
authoritative public sources and repository identity facts, maps source-supported responsibilities
and capabilities, and records organization-specific gaps. It must not convert common practice into
organization policy.

## Author

The Author writes one declared artifact from the validated research ledger and existing
dependencies. It cites source IDs in its handoff and does not score its output.

## Evaluators

Artifact and Pack Evaluators remain read-only for production content. They receive raw artifacts,
requirements, the source ledger, and reproducible checks, but not Generator confidence or intended
verdicts. Every pass is digest-bound, source-bound, strictly greater than 90, and free of P0/P1 or
hard-gate failure.

## State Semantics

- `content_state=content-complete`: public professional baseline and production structure pass.
- `state=needs-org-input`: content is complete but reviewer, permission, internal policy, or
  other organization-specific activation facts remain unresolved.
- `state=activation-ready`: content and all organization-specific activation gates pass.
- `state=blocked`: authoritative public sources are unavailable, tool access is unavailable, or
  bounded iteration cannot converge.
- `state=fail`: observable evidence contradicts an in-scope criterion.

Automated completion never changes lifecycle status to `active`.
