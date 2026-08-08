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
- `activation-ready`: reusable content and every automated Pack gate pass; organization-specific
  task inputs may still be unresolved.
- `blocked`: research access, authority, environment, or convergence is unavailable.
- `fail`: evidence contradicts a required criterion.

## Budgets

- Maximum artifact iterations: 5.
- Maximum whole-Pack iterations: 3.
- Stop after two consecutive score improvements below 2 points.
- Stop immediately when missing authority, unsafe permission, or Kernel weakening cannot be
  resolved within the approved scope.

## Lifecycle Finalization

After the final independent Pack evaluation passes, run `finalize_domain_pack.py` to synchronize
the registry and manifest from `draft` to `active` in the same completion workflow. Do not require
a separate owner, reviewer, or activation-evidence transaction. Publication and task-level
permissions remain separate authorities.

## Intervention Mode Gates

Default mode (默认模式) requires every gate above. When the user explicitly directs Intervention
mode (介入模式), the scoring gates above — artifact
evaluations, evaluation granularity, iteration budgets, and the final Pack evaluation — may be
waived per the recorded direction. The following deterministic gates remain mandatory in every
mode and must pass before lifecycle synchronization:

- `scripts/validate_registry.py` (schema, reference, and lifecycle validation);
- `./scripts/domain-check.sh`;
- `check_pack.py` with a validated research ledger, or an explicit recorded waiver of the ledger
  requirement naming the owner's substitute authority;
- documentation and registry consistency for every lifecycle statement;
- Kernel policy, capability permission clauses, and fail-closed behavior, which no mode may waive.

The intervention record must name every waived gate alongside the retained gate results.
Intervention-mode activation is a manual registry and manifest synchronization recorded under
`changes/<domain-id>-activation/`; it must not be represented as passing the automated evaluation
gates.
