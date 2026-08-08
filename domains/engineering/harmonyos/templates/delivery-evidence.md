# HarmonyOS Engineering Delivery Evidence Record

> **Template use:** Replace every `{{placeholder}}` with authoritative task, project, source, or
> observed evidence. Do not invent commands, versions, targets, paths, permissions, reviewers,
> approvals, thresholds, or results. Retain failures and superseded runs. Sanitize secrets,
> signing material, protected data, and private architecture without destroying reproducibility.

## 1. Record Identity and Task Context

| Field | Recorded value |
| --- | --- |
| Evidence record ID | `{{record-id}}` |
| Task or change ID | `{{task-id}}` |
| Requester and acceptance authority | `{{names-roles-or-needs-org-input}}` |
| Practitioner and evidence custodian | `{{names-or-roles}}` |
| Domain and version | `engineering.harmonyos@{{version}}` |
| Workflow and evaluator revisions | `{{workflow-revision}}`; `{{evaluator-revision}}` |
| Project overlay or task contract | `{{reference-or-none}}` |
| Record opened / last updated | `{{timestamps-with-time-zone}}` |
| Evaluated source revision | `{{commit-or-immutable-revision}}` |
| Candidate artifact identity | `{{build-id-digest-or-location}}` |
| Evidence root | `{{authorized-stable-location}}` |
| Sanitization method | `{{method-and-omitted-material}}` |

### Outcome and scope

- Observable outcome: `{{accepted-outcome}}`
- Affected application, modules, abilities, pages, components, and packages: `{{inventory}}`
- Affected ArkTS APIs, ArkUI state paths, lifecycle, navigation, concurrency, and persistence:
  `{{inventory}}`
- Explicit unchanged scope and exclusions: `{{items-and-authority}}`
- Material positive, negative, failure, and recovery paths: `{{case-ids-or-summary}}`

## 2. Requirements and Evidence Map

Criterion statuses are `pass`, `fail`, `blocked`, `not-applicable`, or `needs-org-input`.
`not-applicable` requires an authoritative scope reason. An independent evaluator determines the
verdict; this record does not score itself.

| Requirement ID | Authority | Acceptance condition | Affected surface | Positive / negative case IDs | Domain rule / evaluator criterion | Planned method | Criterion status | Evidence IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{REQ-001}}` | `{{contract-spec-defect-or-decision}}` | `{{observable-condition}}` | `{{surface}}` | `{{CASE-P-001 / CASE-N-001}}` | `{{HMOS-RULE-nn / HMOS-EVAL-nn}}` | `{{method}}` | `{{status}}` | `{{EVID-ids}}` |

## 3. HarmonyOS, SDK, Toolchain, and Target Baseline

Do not make version-sensitive, compatibility, migration, or device claims until their baseline is
known. Record where each value came from; the newest installed value is not an implicit baseline.

| Baseline field | Declared value | Evidence or authority | Status / limitation |
| --- | --- | --- | --- |
| HarmonyOS release | `{{release}}` | `{{reference}}` | `{{confirmed-or-needs-org-input}}` |
| Compile SDK and compatible/minimum API | `{{versions}}` | `{{configuration-or-contract}}` | `{{status}}` |
| Source and target versions for migration | `{{versions-or-not-applicable}}` | `{{reference}}` | `{{status}}` |
| DevEco Studio / build toolchain | `{{versions}}` | `{{observed-output-or-reference}}` | `{{status}}` |
| `devecocli` and required subcommands | `{{version-and-availability}}` | `{{observed-interface-output}}` | `{{authorized/unavailable/blocked}}` |
| Products, modules, profiles, build modes | `{{declared-matrix}}` | `{{project-configuration}}` | `{{status}}` |
| HAP, HAR, HSP, and App Pack intent | `{{declared-boundaries}}` | `{{architecture-or-package-decision}}` | `{{status}}` |
| Emulator targets | `{{os-api-profile-identities}}` | `{{target-record}}` | `{{status}}` |
| Physical-device targets | `{{model-os-api-form-factor-identities}}` | `{{target-record}}` | `{{status}}` |
| Dependencies and configuration | `{{versions-and-sanitized-settings}}` | `{{lockfiles-configuration-or-reference}}` | `{{status}}` |
| Freshness comparison | `{{material-changes-since-reused-evidence}}` | `{{comparison}}` | `{{current/stale}}` |

## 4. Documented Sources and Decisions

Cached Skill references and generated examples are provisional until reconciled with current,
version-relevant primary guidance and observed compiler or tool evidence.

| Source record ID | Ledger source ID | Document ID / location | Relevant section and version | Retrieval method and query | Retrieval date / context | Claim supported | Conflict or limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{SRC-001}}` | `{{HMOS-ARKTS/HMOS-STAGE/HMOS-ARKUI-V2/HMOS-ARKUI-MIGRATION/HMOS-PACKAGES/HMOS-TESTING}}` | `{{stable-location}}` | `{{section-version}}` | `{{devecocli-docs-or-authorized-manual-path}}` | `{{date-context}}` | `{{decision-or-claim}}` | `{{none-or-details}}` |

### Assumptions, conflicts, and approvals

| Decision ID | Evidence class (`documented`/`observed`/`assumed`/`approved`) | Statement | Affected claim | Evidence | Owner / authority | State |
| --- | --- | --- | --- | --- | --- | --- |
| `{{DEC-001}}` | `{{class}}` | `{{statement-or-competing-interpretations}}` | `{{impact}}` | `{{links}}` | `{{role-or-needs-org-input}}` | `{{open/resolved/needs-org-input}}` |

## 5. Baseline, Files, and Authorized Actions

### Baseline observations

| Baseline ID | Revision and target | Scenario / method | Expected | Observed | Pre-existing status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| `{{BASE-001}}` | `{{revision-target}}` | `{{scenario-method}}` | `{{expected}}` | `{{observed}}` | `{{passed/failed/unavailable/blocked}}` | `{{link}}` |

### Changed-file and action ledger

| Change ID | Requirement IDs | File, configuration, module, or package | Authorized action | Before / after | Behavioral or package effect | Recovery unit | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CHG-001}}` | `{{REQ-ids}}` | `{{inspectable-path-or-identity}}` | `{{read/create/edit/delete/dependency/module-topology/other}}` | `{{summary}}` | `{{effect}}` | `{{smallest-reversible-unit}}` | `{{links}}` |

- Authorized reads, writes, tools, environments, and targets: `{{authority-reference}}`
- Separately controlled actions (device, signing, distribution, production, rollback):
  `{{permissions-and-state}}`
- Prohibited or out-of-scope actions: `{{constraints}}`

## 6. `devecocli` Command Ledger

Resolve syntax from the installed interface. Never copy unverified flags, products, modules,
profiles, targets, or output paths from this template or a cached Skill. Command result classes are
`passed`, `failed`, `skipped`, `unavailable`, or `blocked`; they are not evaluator verdicts.

| Run ID | Evidence class (`docs`/`lint`/`compatibility`/`build`) | Requirement IDs | Availability and authorization check | Exact command | Working scope and inputs | Tool / SDK versions | Start / end | Exit status | Result class | Raw output / report / artifacts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{RUN-001}}` | `{{class}}` | `{{REQ-ids}}` | `{{evidence}}` | `{{exact-invocation}}` | `{{directory-project-module-product-profile-mode-path}}` | `{{versions}}` | `{{timestamps}}` | `{{code-or-state}}` | `{{result-class}}` | `{{stable-links}}` |

### Failures, retries, and conflicting results

| Attempt ID | Run / check ID | Attempt number and shared retry count | Diagnostic classification | Source edit or environmental action | Result | Prior evidence retained at | Stop / handoff decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{ATTEMPT-001}}` | `{{RUN-001}}` | `{{1-of-authorized-bound}}` | `{{source/environment/dependency/permission/device/signing/other}}` | `{{action-or-none}}` | `{{observed-result}}` | `{{link}}` | `{{continue/stop/handoff}}` |

Environment, dependency, permission, signing, and device failures are not source-repair attempts.
Do not reset a retry count by changing commands, erase earlier failures, weaken checks, delete tests,
broaden ignores, or modify unrelated files to obtain a pass.

## 7. Verification Evidence by Class

Success in one row proves only that evidence class. Use `passed`, `failed`, `skipped`,
`unavailable`, or `blocked` for executions; record `not-applicable` only with a cited scope authority.

| Check ID | Evidence class | Requirement / case IDs | Exact target and environment | Method or run ID | Expected | Observed | Result | Raw evidence | Limitation / finding IDs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CHECK-001}}` | `lint` | `{{IDs}}` | `{{scope}}` | `{{RUN-id-or-authorized-method}}` | `{{expected}}` | `{{observed}}` | `{{result}}` | `{{link}}` | `{{details}}` |
| `{{CHECK-002}}` | `compatibility` | `{{IDs}}` | `{{source-target-matrix}}` | `{{RUN-id}}` | `{{expected}}` | `{{observed}}` | `{{result}}` | `{{link}}` | `{{details}}` |
| `{{CHECK-003}}` | `compilation/build` | `{{IDs}}` | `{{product-module-mode}}` | `{{RUN-id}}` | `{{expected}}` | `{{observed}}` | `{{result}}` | `{{link}}` | `{{details}}` |
| `{{CHECK-004}}` | `unit/coverage/self-inspection` | `{{IDs}}` | `{{scope}}` | `{{procedure}}` | `{{threshold-or-condition}}` | `{{observed}}` | `{{result}}` | `{{link}}` | `{{details}}` |
| `{{CHECK-005}}` | `runtime/emulator` | `{{IDs}}` | `{{exact-target}}` | `{{procedure}}` | `{{expected}}` | `{{observed}}` | `{{result}}` | `{{logs-captures-traces}}` | `{{details}}` |
| `{{CHECK-006}}` | `runtime/physical-device` | `{{IDs}}` | `{{exact-target}}` | `{{procedure}}` | `{{expected}}` | `{{observed}}` | `{{result}}` | `{{logs-captures-traces}}` | `{{details}}` |
| `{{CHECK-007}}` | `accessibility/security/performance/power/stability` | `{{IDs}}` | `{{scope-target}}` | `{{authorized-method}}` | `{{approved-condition}}` | `{{observed}}` | `{{result}}` | `{{link}}` | `{{details}}` |
| `{{CHECK-008}}` | `package/artifact creation` | `{{IDs}}` | `{{package-matrix}}` | `{{RUN-id}}` | `{{expected-artifacts}}` | `{{located-identities-digests}}` | `{{result}}` | `{{link}}` | `{{details}}` |
| `{{CHECK-009}}` | `install/signing/publication/release` | `{{IDs}}` | `{{scope}}` | `{{authorized-procedure-or-not-run}}` | `{{expected}}` | `{{observed}}` | `{{result}}` | `{{link}}` | `{{authority-and-limitations}}` |

### Scenario and target matrix

| Case ID | Path type | Preconditions and stimulus | Expected state / lifecycle / interaction result | Emulator targets | Physical-device targets | Actual result | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CASE-P-001}}` | `positive` | `{{conditions-and-actions}}` | `{{observable-result}}` | `{{targets}}` | `{{targets}}` | `{{result}}` | `{{links}}` |
| `{{CASE-N-001}}` | `negative/recovery` | `{{invalid-error-interruption-reentry-permission-denial-or-other}}` | `{{safe-result}}` | `{{targets}}` | `{{targets}}` | `{{result}}` | `{{links}}` |

## 8. Migration and Deprecation Evidence

### Deprecated or compatibility-sensitive interfaces

| Finding ID | Interface and location | Declared source / target matrix | Official deprecation source | Documented replacement or absence | Behavior, lifecycle, state, and package impact | Disposition and authority | Before / after checks | Residual risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{COMPAT-001}}` | `{{symbol-path-location}}` | `{{matrix}}` | `{{SRC-id}}` | `{{replacement-or-none}}` | `{{impact}}` | `{{remediate/retain/exception/blocked}}` | `{{CHECK-ids}}` | `{{risk-or-none}}` |

### ArkUI state-management migration batches

| Batch ID | V1 owner / construct / behavior | Intended V2 mapping and source | Observation, initialization, persistence, reuse, animation, and mixed-mode boundaries | Dependency order | Files | Verification and results | Rollback point | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{MIG-001}}` | `{{inventory}}` | `{{mapping-and-SRC-ids}}` | `{{before-after-behavior-map}}` | `{{predecessors}}` | `{{paths}}` | `{{CHECK-ids-and-observations}}` | `{{reversible-unit}}` | `{{verified/failed/blocked}}` |

Compilation alone does not prove preserved observation or rendering. Record nested mutation,
parent-child propagation, reinitialization, repeated rendering, storage restoration, reuse, and
animation results when applicable.

## 9. Findings, Permissions, and Handoffs

| Finding ID | Severity | Status | Affected requirement / target | Reproduction and impact | Evidence | Owner / receiving authority | Required action or decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{FIND-001}}` | `{{P0/P1/P2/P3/provisional-needs-org-input}}` | `{{open/resolved/accepted-by-authority/blocked}}` | `{{scope}}` | `{{details}}` | `{{links}}` | `{{role-or-needs-org-input}}` | `{{action}}` |

| Permission or approval ID | Controlled scope | Required authority | State | Evidence / decision record | Claims enabled or prevented |
| --- | --- | --- | --- | --- | --- |
| `{{AUTH-001}}` | `{{repository/device/signing/distribution/production/rollback/other}}` | `{{role-or-needs-org-input}}` | `{{authorized/denied/pending/not-requested/needs-org-input}}` | `{{reference-or-none}}` | `{{claims}}` |

| Handoff ID | Topic and artifact package | Receiving authority | Requested decision or action | Evidence | Trigger / due state | Acknowledgement / disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{HANDOFF-001}}` | `{{architecture-ArkUI-security-privacy-test-compatibility-performance-release-or-other}}` | `{{named-role-or-needs-org-input}}` | `{{request}}` | `{{links}}` | `{{condition}}` | `{{reference-pending-or-needs-org-input}}` |

## 10. Residual Risks and Organization Gaps

| Risk / gap ID | Missing fact or residual condition | Affected claim | Impact | Mitigation / containment | Required owner or source | State |
| --- | --- | --- | --- | --- | --- | --- |
| `{{RISK-001}}` | `{{condition}}` | `{{claim}}` | `{{impact}}` | `{{action-or-none}}` | `{{role-source-or-needs-org-input}}` | `{{open/blocked/dispositioned/needs-org-input}}` |

## 11. Recovery and Rollback

Describe only project-authorized recovery. This section does not grant permission to revert,
uninstall, alter signing, distribute, or perform a production rollback.

| Field | Recorded value |
| --- | --- |
| Last known good revision / artifact | `{{identity-and-evidence}}` |
| Smallest reversible batch or artifact | `{{unit}}` |
| Rollback procedure authority | `{{project-reference-or-needs-org-input}}` |
| Preconditions and permissions | `{{details}}` |
| State, persistence, data, and migration implications | `{{details}}` |
| Module, package, dependency, and signing implications | `{{details}}` |
| Device / installation implications | `{{details}}` |
| Post-recovery verification | `{{authorized-method-and-check-ids}}` |
| Recovery owner and handoff | `{{authority-and-HANDOFF-id}}` |

## 12. Delivery Summary and Evidence Index

| Claim | Exact scope | Criterion status | Supporting evidence | Limitation or prevented claim |
| --- | --- | --- | --- | --- |
| `{{claim}}` | `{{scope-revision-baseline-targets}}` | `{{pass/fail/blocked/not-applicable/needs-org-input}}` | `{{EVID-CHECK-RUN-ids}}` | `{{limitations}}` |

| Evidence ID | Description and producer | Bound revision, baseline, environment, and target | Requirements / criteria supported | Stable location | Freshness | Access / sanitization notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{EVID-001}}` | `{{description-and-producer}}` | `{{binding}}` | `{{IDs}}` | `{{location}}` | `{{current/stale}}` | `{{notes}}` |

- Open failed checks: `{{IDs-or-none}}`
- Skipped, unavailable, blocked, conflicting, stale, or flaky evidence: `{{IDs-or-none}}`
- Open `P0` or `P1` findings: `{{IDs-or-none}}`
- Pending handoffs, permissions, and approvals: `{{IDs-or-none}}`
- Candidate and evidence package location: `{{authorized-location}}`
- Independent evaluation state: `{{not-started/in-progress/completed-with-reference}}`

This record supports independent review. It does not accept risk, approve an exception, authorize
signing, installation, distribution, publication, release, production action, rollback execution,
or activation of `engineering.harmonyos`.

## Source Basis

Professional guidance in this template traces to the validated `engineering.harmonyos` research
ledger: ArkTS constraints [HMOS-ARKTS], Stage-model architecture [HMOS-STAGE], ArkUI V2 observation
[HMOS-ARKUI-V2], V1-to-V2 migration [HMOS-ARKUI-MIGRATION], package semantics [HMOS-PACKAGES], and
HarmonyOS testing services [HMOS-TESTING]. Registered identity and lifecycle remain governed by
[REPO-HARMONYOS-IDENTITY]. Project-specific baselines, commands, permissions, matrices, thresholds,
reviewers, and approval evidence must come from the applicable project overlay or task contract.
