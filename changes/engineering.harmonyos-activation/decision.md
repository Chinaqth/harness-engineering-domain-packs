# HarmonyOS Engineering Activation Decision

## Decision

Activate the reusable public HarmonyOS Engineering baseline with `platform-harmony` acting as
both the accountable owner and the authorized reviewer.

Project SDK/API baselines, toolchain versions, device matrices, commands, quality thresholds,
signing material, and operational permissions are project/task inputs. Their absence does not
block Domain activation, but it must block every dependent task claim or action. Activation
grants routing eligibility only.

## Authority

On 2026-08-08, the user explicitly stated that they own the HarmonyOS profession, that the six
bundled Skill packages are trusted inputs from their familiar domain, directed that the
per-Skill artifact scoring stage be skipped, and asked for the Domain lifecycle to change from
`draft` to `active`. This record preserves that attestation without claiming a personal identity
not supplied by the approver.

## Skill scoring waiver

The standard `finalize_domain_pack.py` gate requires one passing independent evaluation per
production file (741 session-visible files, including the six preserved Skill corpora). The
owner explicitly waived this stage for these owner-authored packages. Consequences:

- The strict finalizer was not run to completion; activation is a manual, owner-directed
  lifecycle change recorded here, mirroring the `engineering.web` activation precedent.
- Previously recorded `blocked` Skill evaluations under
  `changes/engineering.harmonyos-completion/evaluations/` are retained as historical evidence,
  not as gates.
- The six Skill packages remain non-authoritative discovery aids. The `harmonyos-engineering`
  wrapper quarantine policy, `devecocli` evidence boundary, and fail-closed permission clauses
  are unchanged and remain normative.
- Deterministic gates still pass: registry validation, the validated research ledger,
  `check_pack.py` reporting `content-complete` / `activation-ready`, and
  `./scripts/domain-check.sh`.

## Consequences

- A resolver may consider the Domain for matching tasks.
- Capability permission clauses and task contracts remain authoritative and fail closed.
- Device access, signing, distribution, production operation, release approval, exceptions, and
  risk acceptance continue to require separate explicit authority.

## Rollback

Revert the scoped activation change: restore `draft` in `registry/domains.json` and
`domains/engineering/harmonyos/domain.json`, clear `activation.evidence`, and remove
`changes/engineering.harmonyos-activation/`. Preserve unrelated user work.
