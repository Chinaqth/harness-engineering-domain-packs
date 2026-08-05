# Progress and Handoff

- Change ID: `20260805-remove-android-test-domain`
- Updated: 2026-08-05
- Risk: G1
- Status: done

## Current State

The user explicitly requested removal of the test-only Android function. `engineering.android` has
been removed from the authoritative registry and its scaffold directory no longer exists. The only
remaining authoritative registered Domain is active `engineering.web`.

## Verification

- Baseline confirmed Android was draft with empty routes, empty capabilities, and no activation evidence.
- Domain registry validation: passed.
- Repository Skill validation: passed.
- Project Custom Agent validation: passed.
- Unit tests: 48 passed.
- Complete `./scripts/domain-check.sh`: passed.
- Harness `./scripts/harness-check.sh`: passed with 20 tests after example alignment.
- `git diff --check`: passed in both repositories.

## Scope Boundary

The active Web Domain and historical change evidence remain unchanged. Synthetic unit-test fixtures
were renamed to `engineering.mobile-test` so they cannot be confused with an authoritative Android
function. Historical Android references remain only where they accurately preserve prior evidence
or document this deletion.

## Residual Risks

- Projects that locally referenced the unpublished draft must remove that overlay entry; no such
  project overlay was in the authorized scope.
- No Android professional capability is routable until it is registered and completed again.

## Rollback

Restore the registry entry and the full deleted scaffold as one unit, restore current references,
and rerun both integrity gates. Git retains the deleted content for recovery.
