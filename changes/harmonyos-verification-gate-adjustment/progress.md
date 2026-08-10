# Progress

## Implemented

- Changed the default final compilation gate to `devecocli build`.
- Made lint and compatibility checks explicit opt-in evidence procedures.
- Preserved evidence-class separation and `skipped` status for omitted checks.
- Passed `./scripts/domain-check.sh` with the bundled workspace Python runtime.
- Independently evaluated `rules/BASE.md`; normalized score `96.65`, verdict `pass`, no findings or
  blocked reasons.
- Selected version `1.0.0` for the breaking default-verification behavior change and synchronized
  the Domain manifest, registry, and Domain documentation.

## Pending

- Owner review through a pull request.
- Affected-project notification at merge time.

## Validation note

The first repository check used the system Python and failed because that interpreter lacked
`tomllib`. The same unchanged check passed with the bundled workspace Python; the initial
environment failure is retained in `validation.md`.
