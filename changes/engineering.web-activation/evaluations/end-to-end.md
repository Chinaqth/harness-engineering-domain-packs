# Independent End-to-End Activation Evaluation

## Verdict

**Pass** at working-tree HEAD `a5e87f54e1ee0a2cca6215eed771639721f1a1dc`.

- Domain tree SHA-256: `72090b54749513b1ecbbc3737f59a0db79dc628f71947b1b0680ac44350777a6`
- Evaluated scope SHA-256: `af888a0e240534d8dc7342c747750c5639f92df2a835e070faf6d65cefe798d0`
- Environment: local read-only evaluation on Darwin arm64 with Python 3.13.1
- Findings: none

## Critical Journey

| Scenario | Expected | Actual | Result |
| --- | --- | --- | --- |
| Positive active route | Semantic Web design task selects `semantic-web-interface-engineering`. | Matching active route and capability selected. | Pass |
| Negative signal | Task type without a matching signal is rejected. | `no-task-and-signal-match`. | Pass |
| Negative task | Signal without a matching task type is rejected. | `no-task-and-signal-match`. | Pass |
| Ambiguous candidates | Higher-priority ECMAScript route wins deterministically. | ECMAScript route selected. | Pass |
| Disabled capability | Selection fails closed. | `disabled-capability`. | Pass |
| Missing dependency | Selection fails closed. | `missing-dependency`. | Pass |
| Version mismatch | Selection fails closed. | `version-mismatch`. | Pass |
| Draft lifecycle fixture | Pack is unavailable. | `lifecycle-not-active`. | Pass |
| Missing task inputs | Route may match, but execution and claims remain blocked. | `operational_allowed=false`, `claim_state=needs-org-input`. | Pass |

The last scenario omitted task authority, project commands, browser and assistive-technology matrix,
quality targets, security baseline, and operational permissions. Activation did not supply them.

## Acceptance Reconciliation

- AC-1: Pass — `platform-web` is synchronized as owner/reviewer and approval evidence is durable.
- AC-2: Pass — independent Pack check returned `content-complete` and `activation-ready`.
- AC-3: Pass — registry and manifest are `active`; repository validation and 43 tests passed.
- AC-4: Pass — active routing succeeded and missing task authority failed closed.
- AC-5: Pass — independent read-only evaluation found no P0/P1 and scored 98.30 before normalization.

## Permissions, Security, Compatibility, and Rollback

- Activation grants routing eligibility only. Dependency, deployment, production, release,
  exception, legal-conformance, and risk-acceptance permissions remain separate.
- Kernel security, privacy, authorization, evidence, approval, and lifecycle requirements remain
  intact. Frontend security testing still requires explicit target and environment authorization.
- Browser and assistive-technology matrices remain task/project inputs; missing matrices prevent
  compatibility claims.
- Rollback is one `git revert` of the scoped activation commit after publication.

## Limitations and Residual Risks

- The repository contains routing metadata, not a deployed production resolver; scenarios used a
  non-mutating in-memory resolver model.
- This evaluation covered the uncommitted scoped working tree. Commit-level rollback and remote
  publication must be verified after the Builder creates and pushes the commit.
- Unrelated working-tree changes must remain excluded from staging.
