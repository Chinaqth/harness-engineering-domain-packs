# HarmonyOS Verification Gate Adjustment

## Motivation

The default HarmonyOS delivery gate currently requires lint and conditionally requires compatibility
checks before build. In the current tool and project environment those checks do not provide a
reliable default completion signal. The Domain owner requests that the default final compilation
gate temporarily consist only of `devecocli build`.

## Requirements

1. `devecocli build` is the only default final compilation gate.
2. `devecocli check lint` and `devecocli check compat` run only when explicitly required by the
   task contract or user.
3. Omitted lint and compatibility checks are recorded as `skipped`, never `passed`.
4. Build success must not imply lint, compatibility, test, runtime, signing, or release success.
5. Permission, evidence, rollback, and fail-closed Kernel controls remain unchanged.

## Applicability

This policy applies to delivery performed through `engineering.harmonyos`. A stricter project or
task contract may explicitly request additional checks.
