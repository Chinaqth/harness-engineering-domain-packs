# Engineering Web Completion Generator-Evaluator Contract

## Builder

The Builder owns orchestration, durable state, artifact order, iteration budgets, deterministic
normalization, and final classification. It does not author professional claims or issue scores.

## Researcher

A fresh read-only Researcher returns the exact three-field handoff envelope required by the
research contract. The Builder persists it without adding, deleting, or reinterpreting claims.

## Authors

Each fresh Author writes exactly one declared production artifact from the validated ledger and
existing dependencies. Authors do not evaluate their own work.

## Evaluators

Each artifact and the assembled Pack receives a fresh read-only evaluation. The Builder persists
the exact raw payload and uses deterministic normalization to bind the verdict to the current
artifact digest and validated source IDs.

## Gates and Budgets

- Artifact pass: score greater than 90, every hard gate true, no P0/P1 finding, no blocked reason,
  and current digest/source binding.
- Maximum artifact iterations: 5.
- Maximum Pack iterations: 3.
- Stop after two consecutive improvements below two points.
- Automated completion never changes lifecycle status to `active`.

## Fulfillment

Every latest artifact evaluation and the whole-Pack evaluation is independently produced,
source-bound, digest-bound, strictly above 90, and free of P0/P1 findings and blocked reasons.
The final session validates with `--require-final`; the resulting classification is
`content-complete` plus `needs-org-input` while lifecycle remains `draft`.
