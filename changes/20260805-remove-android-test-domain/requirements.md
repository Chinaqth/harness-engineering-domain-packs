# Remove the Android Test Domain

## Objective

Remove the test-only `engineering.android` draft identity and its incomplete scaffold from the
authoritative Domain Pack repository.

## Scope

- Remove `engineering.android` from `registry/domains.json`.
- Remove `domains/engineering/android/`.
- Remove current documentation and integration-test assumptions that the draft is registered.
- Preserve historical change and isolated fixture evidence.
- Align the Harness routing example so Android is reported as an unregistered capability rather
  than a registered draft.

## Non-goals

- Do not change or deactivate `engineering.web`.
- Do not create a replacement Android Domain.
- Do not rewrite historical evidence that accurately records prior test activity.
- Do not change Domain registration, completion, or activation semantics.

## Acceptance Criteria

1. The authoritative registry contains no `engineering.android` entry.
2. The authoritative Android Domain directory no longer exists.
3. Current READMEs do not instruct users to complete the removed Domain.
4. Registry validation and the complete Domain integrity gate pass.
5. Harness examples describe Android as unregistered and continue to fail closed.

## Risk

G1. The removed Pack is an incomplete `draft` that cannot receive production routing. The change is
version-controlled and reversible, and it grants no operational permission or external effect.

## Rollback

Restore the removed registry entry and complete `domains/engineering/android/` scaffold together,
then restore the README and integration-test references and run both repository integrity gates.
