# Lifecycle and Iteration Gates

## Artifact Gate

Require a normalized evaluation bound to the current artifact digest, score greater than 90, all
hard gates including professional source traceability, source IDs present in the validated research
ledger, no P0/P1 finding, and no blocked reason.

## Pack Gate

Require every declared artifact gate, repository validation, structural Pack validation,
representative positive and negative routing evidence, final score greater than 90, all final hard
gates, and no P0/P1 finding.

## Completion States

- `content_state=content-complete`: public professional content and structure pass, independent
  of activation readiness.
- `needs-org-input`: content passes but activation-specific organizational gaps remain.
- `activation-ready`: content and every activation-specific organizational gate pass.
- `blocked`: research access, authority, environment, or convergence is unavailable.
- `fail`: evidence contradicts a required criterion.

## Budgets

- Maximum artifact iterations: 5.
- Maximum whole-Pack iterations: 3.
- Stop after two consecutive score improvements below 2 points.
- Stop immediately when missing authority, unsafe permission, or Kernel weakening cannot be
  resolved within the approved scope.

## Lifecycle Authority

Automated completion stops at `activation-ready`. Only the Domain Owner and required Reviewers may
approve coordinated `draft` to `active` changes in the registry and manifest.
