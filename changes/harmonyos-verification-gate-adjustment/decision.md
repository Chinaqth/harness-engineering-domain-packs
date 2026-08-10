# Decision

## Proposed decision

Adopt `devecocli build` as the only default final compilation gate for `engineering.harmonyos`.
Run `devecocli check lint` and `devecocli check compat` only when a task contract or user explicitly
requests their distinct evidence.

## Compatibility impact

Existing consumers that relied on implicit lint or compatibility execution must request those
checks explicitly. Build evidence remains narrower than lint, compatibility, test, runtime,
signing, or release evidence.

This is published as `engineering.harmonyos` version `1.0.0` because it intentionally changes the
default verification behavior of the active `0.1.0` contract.

## Failure modes and controls

- A build failure remains failed and cannot be reported as a compilation pass.
- Skipped lint and compatibility checks cannot support lint or compatibility claims.
- Explicit task requirements remain binding and fail closed when their evidence is unavailable.

## Rollback

Revert the scoped changes to `BASE.md`, `WORKFLOW.md`, and the `harmonyos-engineering` wrapper,
restoring lint as a default check and compatibility as a conditional default check. Preserve the
change record and evaluation evidence.
