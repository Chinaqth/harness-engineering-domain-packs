# Migration from engineering.harmonyos 0.1.0 to 1.0.0

Consumers that require lint or source-to-target compatibility evidence must add an explicit task
contract or user instruction for `devecocli check lint` or `devecocli check compat`. Without that
explicit requirement, version `1.0.0` runs only `devecocli build` as the default final compilation
gate and records lint and compatibility as `skipped`.

Do not reinterpret a successful build as evidence that either omitted check passed. Projects that
must retain the previous default behavior should remain pinned to `0.1.0` until their overlays or
task templates explicitly request those checks.
