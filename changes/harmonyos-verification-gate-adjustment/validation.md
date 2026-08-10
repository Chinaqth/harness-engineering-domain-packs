# Validation

## Deterministic repository check

Command: `./scripts/domain-check.sh`

- First run: failed after registry and Skill validation because the system Python could not import
  `tomllib`.
- Rerun: passed with the bundled workspace Python prepended to `PATH`.
- Passing output included registry, repository Skill, and custom-agent validation plus 48 tests.

No `devecocli check lint` or `devecocli check compat` command was run. No HarmonyOS application
build was available or required for this Domain policy-text change.

## Remaining gate

Independent G2 evaluation passed with normalized score `96.65`; all hard gates passed and no
findings or blocked reasons were reported. Pull-request review remains pending. The Generator did
not issue the policy verdict.
