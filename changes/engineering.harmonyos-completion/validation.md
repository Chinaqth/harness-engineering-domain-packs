# Partial Validation Evidence

## Passed

- Research ledger validation: pass; seven authoritative/repository source IDs.
- `DOMAIN.md`: independent score 96.35, all hard gates true, no findings.
- `domain.json`: independent score 97.25, all hard gates true, no findings.
- `owners.json`: independent score 99.30, all hard gates true, no findings.
- `git diff --check`: pass at the last completed artifact checkpoint.

## Failed as expected for partial state

- Partial Pack check: `content_state=incomplete`, `state=fail`; evidence is
  `evaluations/pack-check.partial.json`.
- `./scripts/domain-check.sh`: fail. The dominant reproducible failure is that `README-CH.md`
  does not enumerate the hundreds of production files in the added Skill corpora. Capabilities and
  routes are also intentionally incomplete because strict dependency-order authoring stopped.
- Final session validation, final Pack evaluation, and finalization were not run because their
  prerequisites do not pass.

## Residual risk

The bundled Skill material is largely Chinese, contains cached documentation of uncertain
freshness, and includes obsolete `mcp_codegenie-*` or `deveco-mcp` tool assumptions. It must not be
treated as authoritative or production-routable until curated and independently evaluated.
