# Web Frontend Delivery Evidence Record

> **Template use:** Replace every `{{placeholder}}` with authoritative task or project evidence.
> Delete only rows proven not applicable, and record the scope authority that makes them
> `not-applicable`. Do not invent commands, targets, thresholds, results, reviewers, approvals,
> permissions, or policy. Preserve failed, skipped, unavailable, blocked, conflicting, and flaky
> results. Sanitize secrets and protected data while retaining enough structure for safe
> reproduction.

## 1. Record Identity and Scope

| Field | Recorded value |
| --- | --- |
| Evidence record ID | `{{record-id}}` |
| Task or change ID | `{{task-id}}` |
| Accountable requester | `{{requester-or-needs-org-input}}` |
| Practitioner | `{{name-or-role}}` |
| Evidence custodian | `{{name-role-or-needs-org-input}}` |
| Domain and version | `engineering.web@{{version}}` |
| Workflow version or revision | `{{workflow-version-or-revision}}` |
| Applicable project overlay | `{{overlay-reference-or-none}}` |
| Record opened | `{{timestamp-and-time-zone}}` |
| Last updated | `{{timestamp-and-time-zone}}` |
| Evaluated revision | `{{commit-build-or-artifact-digest}}` |
| Candidate artifact or diff | `{{inspectable-location}}` |
| Evidence root | `{{authorized-location}}` |
| Data sanitization applied | `{{method-and-scope}}` |

### Desired outcome

`{{observable-user-or-system-outcome}}`

### Affected surface

- Pages, routes, or document regions: `{{items}}`
- Components and interaction states: `{{items}}`
- Data flows, requests, resources, and origins: `{{items}}`
- Presentation contexts, devices, and localization contexts: `{{items}}`
- Affected users or systems: `{{items-or-unknown}}`
- Explicit exclusions: `{{items-and-authority}}`

### Authority and execution boundary

- Authorized actions and tools: `{{authority-reference}}`
- Prohibited or out-of-scope actions: `{{constraints}}`
- Environments permitted for evidence collection: `{{environments}}`
- Dependency, deployment, production, and policy permissions: `{{references-or-needs-org-input}}`
- Service, trust, and ownership boundaries: `{{boundaries}}`

## 2. Requirements and Planned Evidence

Record observable positive and material negative behavior. Every completion claim must trace to a
requirement, tested scope, method, actual result, and evidence location.

| Requirement ID | Authority or source | Observable acceptance condition | Affected surface | Positive case IDs | Negative case IDs | Planned method | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{REQ-001}}` | `{{product-spec-contract-defect-or-rule}}` | `{{condition}}` | `{{surface}}` | `{{CASE-P-001}}` | `{{CASE-N-001}}` | `{{method}}` | `{{pass/fail/blocked/not-applicable/needs-org-input}}` | `{{links}}` |

### Assumptions, conflicts, and unresolved decisions

| ID | Type | Statement or competing interpretations | Evidence | Impacted claim or surface | Required authority | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `{{DEC-001}}` | `{{assumption/conflict/unknown}}` | `{{details}}` | `{{links}}` | `{{impact}}` | `{{owner-role-or-needs-org-input}}` | `{{open/resolved/needs-org-input}}` |

## 3. Environment, Configuration, and Revision

Evidence is reusable only when it is bound to the evaluated revision and a representative declared
environment. If relevant implementation, service contracts, targets, policies, dependencies,
configuration, or environments changed, identify the affected evidence as stale and rerun it or
limit the claim.

| Field | Recorded value |
| --- | --- |
| Source revision and dirty-state note | `{{revision-and-status}}` |
| Build or artifact identity | `{{identifier-or-digest}}` |
| Runtime and tool versions | `{{versions}}` |
| Configuration or feature flags | `{{sanitized-values-or-reference}}` |
| Rendering or integration mode | `{{authoritative-project-fact}}` |
| Service-contract revision | `{{reference}}` |
| Network, cache, and storage conditions | `{{conditions}}` |
| Test data provenance | `{{authorized-non-sensitive-source}}` |
| Environment limitations | `{{limitations-or-none-known}}` |
| Freshness comparison | `{{what-changed-since-prior-evidence}}` |
| Reproduction access owner | `{{role-or-needs-org-input}}` |

## 4. Baseline and Change Map

### Baseline observations

| Observation ID | Revision and environment | Scenario and method | Expected behavior | Actual behavior | Pre-existing status | Evidence link |
| --- | --- | --- | --- | --- | --- | --- |
| `{{BASE-001}}` | `{{revision-environment}}` | `{{scenario-method}}` | `{{expected}}` | `{{actual}}` | `{{passing/failing/unavailable/blocked}}` | `{{link}}` |

Do not attribute a baseline failure to the candidate change without evidence. Keep unavailable
checks and existing failures visible.

### Changed-surface inventory

| Change ID | Requirement IDs | Artifact, module, or surface | Before | After | User-visible effect | Trust or service boundary | Recovery unit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CHG-001}}` | `{{REQ-001}}` | `{{inspectable-reference}}` | `{{baseline}}` | `{{candidate}}` | `{{effect}}` | `{{boundary-or-none}}` | `{{smallest-recoverable-unit}}` |

## 5. Case Catalog

| Case ID | Requirement IDs | Path type | Preconditions | Actions or stimulus | Expected observable result | Applicable targets | Actual status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CASE-P-001}}` | `{{REQ-001}}` | `positive` | `{{conditions}}` | `{{steps}}` | `{{expected}}` | `{{targets}}` | `{{pass/fail/blocked/not-run}}` | `{{links}}` |
| `{{CASE-N-001}}` | `{{REQ-001}}` | `negative/recovery` | `{{conditions}}` | `{{failure-invalid-empty-cancel-retry-or-other-stimulus}}` | `{{expected-safe-result}}` | `{{targets}}` | `{{pass/fail/blocked/not-run}}` | `{{links}}` |

## 6. Web Engineering Results

Use the result status values `pass`, `fail`, `blocked`, `not-applicable`, and `needs-org-input`.
For an executed procedure, also retain whether an individual check was `skipped`, `unavailable`,
or `flaky`; none of these is a passing result. Cite the authoritative scope source for every
`not-applicable` entry.

### 6.1 HTML semantics and document behavior

Use HTML elements according to their defined meanings and content models, and retain meaning across
material states [WEB-WHATWG-HTML-SEMANTICS].

| Result ID | Requirement and case IDs | State or viewport | Native or custom semantic choice | Structure, name, role, state, and form observations | Custom-interaction rationale | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{SEM-001}}` | `{{REQ-001; CASE-P-001}}` | `{{state-context}}` | `{{choice}}` | `{{actual-observations}}` | `{{reason-or-not-applicable}}` | `{{status}}` | `{{markup-rendered-tree-test-or-capture}}` |

### 6.2 CSS rendering, maturity, and fallbacks

Record specification maturity separately from support in the declared target matrix
[WEB-W3C-CSS-2025].

| Result ID | Requirement and case IDs | Material CSS feature | Maturity reference | Target and context | Rendering result | Fallback or degradation exercised | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{CSS-001}}` | `{{IDs}}` | `{{feature}}` | `{{specification-or-authoritative-reference}}` | `{{browser-viewport-media-context}}` | `{{actual-result}}` | `{{result-and-policy-reference-or-none}}` | `{{status}}` | `{{links}}` |

### 6.3 ECMAScript behavior and browser host APIs

Separate ECMAScript language guarantees from browser host-API availability
[WEB-TC39-ECMA262].

| Result ID | Requirement and case IDs | State transition or behavior | ECMAScript assumption | Host API and target availability | Error, cancellation, repetition, stale-state, or cleanup result | Fallback | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{JS-001}}` | `{{IDs}}` | `{{behavior}}` | `{{language-assumption}}` | `{{host-evidence}}` | `{{actual-negative-or-recovery-result}}` | `{{approved-fallback-or-none}}` | `{{status}}` | `{{links}}` |

### 6.4 HTTP integration and recovery

Test against the authoritative service contract and record applicable method, representation,
field, status, authentication, and cache semantics [WEB-RFC9110-HTTP]. Sanitize all request and
response evidence.

| Result ID | Requirement and case IDs | Contract reference | Method and request class | Response status or outcome | Authentication and cache context | User-visible behavior and recovery | Contract mismatch | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{HTTP-001}}` | `{{IDs}}` | `{{contract-version}}` | `{{method-and-sanitized-shape}}` | `{{status-empty-partial-invalid-unauthorized-forbidden-not-found-conflict-rate-limited-transient-unavailable-aborted-stale-or-other}}` | `{{context}}` | `{{actual-result}}` | `{{details-or-none}}` | `{{status}}` | `{{links}}` |

### 6.5 Accessibility

Name the adopted target and evaluate the complete affected page or flow, including responsive
variations; an isolated component result or automated scan alone does not establish conformance
[WEB-W3C-WCAG22]. Verify keyboard operation and deliberate focus behavior for custom widgets
[WEB-W3C-ARIA-KEYBOARD].

- Adopted accessibility target and authority: `{{target-reference-or-needs-org-input}}`
- Tested page or flow scope: `{{complete-scope}}`
- Declared assistive-technology matrix: `{{matrix-reference-or-needs-org-input}}`

| Result ID | Requirement, case, and criterion IDs | Page, flow, state, and responsive variant | Method (`automated`/`manual`/`keyboard`/`assistive technology`) | Keyboard and focus trace | Actual result | Exception or disposition authority | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{A11Y-001}}` | `{{IDs}}` | `{{scope}}` | `{{method}}` | `{{entry-movement-visible-focus-trap-loss-restoration-error-observations}}` | `{{actual-result}}` | `{{reference-or-none}}` | `{{status}}` | `{{links}}` |

### 6.6 Frontend security and privacy

Treat distinct origins as potentially hostile unless an authoritative security model states
otherwise [WEB-WHATWG-HTML-ORIGINS]. Use the approved verification scope; ASVS can structure tests
but does not select a local level or accept risk [WEB-OWASP-ASVS]. When applicable, identify CSP as
report-only or enforced and treat it as defense in depth [WEB-W3C-CSP3].

| Result ID | Requirement and case IDs | Origin, data flow, executable content, or trust boundary | Approved control or verification scope | Positive and negative method | CSP source and state | Sanitized actual result | Finding IDs | Result status | Evidence links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{SEC-001}}` | `{{IDs}}` | `{{boundary}}` | `{{threat-model-ASVS-scope-policy-or-needs-org-input}}` | `{{authorized-method}}` | `{{policy-report-only-enforced-or-not-applicable}}` | `{{actual-result}}` | `{{FIND-001-or-none}}` | `{{status}}` | `{{links}}` |

Sensitive material omitted or sanitized: `{{what-was-removed-and-how-reproduction-is-preserved}}`

### 6.7 Browser performance

Base performance claims on retrieved navigation, resource, or application-defined measurements
[WEB-W3C-PERFORMANCE-TIMELINE]. Judge results only against a cited organization-approved objective.

| Result ID | Requirement and case IDs | Claim and user scenario | Environment and collection method | Measurement definition | Raw or linked observations | Reruns and variability | Approved objective or baseline | Disposition | Result status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{PERF-001}}` | `{{IDs}}` | `{{claim-scenario}}` | `{{conditions-method}}` | `{{navigation-resource-or-user-timing-measure}}` | `{{values-or-link}}` | `{{runs-variability-limitations}}` | `{{authority-reference-or-needs-org-input}}` | `{{comparison}}` | `{{status}}` |

### 6.8 Browser, device, and assistive-technology matrix

Portable browser-facing tests establish interoperability only for the targets and behaviors
actually exercised [WEB-WPT-DOCS]. A single browser, simulated DOM, or unit suite cannot stand in
for an unexecuted matrix.

- Authoritative matrix and degradation policy: `{{reference-or-needs-org-input}}`

| Target ID | Browser and version | Device, OS, or presentation context | Assistive technology, if applicable | Scenario IDs | Positive result | Negative or fallback result | Rendering or interaction evidence | Rerun or flake notes | Overall status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{TARGET-001}}` | `{{browser-version}}` | `{{context}}` | `{{technology-version-or-not-applicable}}` | `{{case-IDs}}` | `{{actual}}` | `{{actual}}` | `{{links}}` | `{{history}}` | `{{pass/fail/blocked/unavailable/flaky}}` |

## 7. Executed Procedures, Methods, and Outputs

Record actual authorized procedures. Never substitute example commands from this template for
project commands.

| Procedure ID | Requirement and result IDs | Purpose and method | Exact command or manual steps | Working context and inputs | Start and end time | Exit or completion state | Actual output or inspectable link | Sanitization | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{PROC-001}}` | `{{IDs}}` | `{{purpose-method}}` | `{{authoritative-command-or-numbered-steps}}` | `{{directory-environment-inputs}}` | `{{timestamps}}` | `{{exit-code-state}}` | `{{output-or-link}}` | `{{details}}` | `{{passed/failed/skipped/unavailable/blocked/flaky}}` |

### Conflicting, stale, or flaky evidence

| Evidence ID | Classification | Conflicting or prior results | Cause analysis | Scope affected | Reruns | Current disposition | Claim impact |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `{{EVID-001}}` | `{{conflicting/stale/flaky}}` | `{{all-results-retained}}` | `{{known-cause-or-unknown}}` | `{{scope}}` | `{{history}}` | `{{unresolved/resolved-with-authority}}` | `{{impact}}` |

## 8. Findings and Severity

Use an approved organization severity policy when supplied. Otherwise apply the evaluator's
reusable `P0`–`P3` impact model. Severity describes impact and never grants risk-acceptance
authority.

| Finding ID | Status | Severity | Affected requirement and users or systems | Description and impact | Safe reproduction | Evidence links | Owner or receiving authority | Required action or decision | Disposition reference |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{FIND-001}}` | `{{open/resolved/accepted-by-authority/blocked}}` | `{{P0/P1/P2/P3/provisional-needs-org-input}}` | `{{scope}}` | `{{details}}` | `{{steps}}` | `{{links}}` | `{{role-or-needs-org-input}}` | `{{action}}` | `{{approval-or-decision-reference-or-none}}` |

## 9. Residual Risks, Handoffs, and Approvals

### Residual risks and blocked decisions

| Risk or decision ID | Evidence and affected claim | Impact | Mitigation or containment | Required authority | State |
| --- | --- | --- | --- | --- | --- |
| `{{RISK-001}}` | `{{references}}` | `{{impact}}` | `{{action-or-none}}` | `{{owner-role-or-needs-org-input}}` | `{{open/blocked/dispositioned}}` |

### Handoffs

| Handoff ID | Topic and artifact package | Receiving authority | Requested decision or action | Evidence links | Due or trigger | Acknowledgement or disposition |
| --- | --- | --- | --- | --- | --- | --- |
| `{{HANDOFF-001}}` | `{{product-design-service-accessibility-security-privacy-compatibility-performance-delivery-release-or-other}}` | `{{named-role-or-needs-org-input}}` | `{{request}}` | `{{links}}` | `{{condition-or-date}}` | `{{reference-pending-or-needs-org-input}}` |

### Approval state

Passing implementation checks do not authorize deployment, approve release, establish legal or
accessibility conformance, accept security risk, or change the Domain lifecycle. Reviewer silence
and an empty reviewer list are not approval.

| Approval ID | Decision scope | Required authority | Decision | Evidence or signed record | Constraints or expiry | Claims enabled or still prevented |
| --- | --- | --- | --- | --- | --- | --- |
| `{{APPROVAL-001}}` | `{{scope}}` | `{{named-role-or-needs-org-input}}` | `{{approved/rejected/pending/not-requested/needs-org-input}}` | `{{reference-or-none}}` | `{{constraints}}` | `{{claims}}` |

## 10. Organization-Specific Gaps

Record missing organization inputs without fabricating substitutes.

| Gap ID | Missing authoritative input | Evidence already available | Dependent claim, procedure, or decision prevented | Required owner or source | Next handoff | State |
| --- | --- | --- | --- | --- | --- | --- |
| `{{ORG-GAP-001}}` | `{{reviewer-permission-architecture-command-matrix-target-threshold-policy-risk-authority-or-other}}` | `{{links-or-none}}` | `{{exact-impact}}` | `{{role-source-or-unknown}}` | `{{handoff-ID-or-action}}` | `needs-org-input` |

## 11. Recovery and Rollback Guidance

Describe only recovery supported by authoritative project evidence. Do not imply deployment or
production rollback permission.

| Field | Recorded value |
| --- | --- |
| Smallest recoverable unit | `{{feature-component-client-artifact-or-other}}` |
| Recovery or rollback procedure authority | `{{project-reference-or-needs-org-input}}` |
| Preconditions and required permissions | `{{details}}` |
| Client-state implications | `{{details-or-not-applicable-with-authority}}` |
| Cache or service-worker implications | `{{details-or-not-applicable-with-authority}}` |
| CDN or delivery implications | `{{details-or-not-applicable-with-authority}}` |
| Session or authentication implications | `{{details-or-not-applicable-with-authority}}` |
| Data, schema, service, or backend dependencies | `{{details-or-not-applicable-with-authority}}` |
| Post-recovery verification | `{{authorized-method}}` |
| Unknown recovery facts | `{{needs-org-input-items}}` |
| Recovery authority and handoff | `{{named-role-and-handoff-reference}}` |

## 12. Delivery Summary and Evidence Index

### Claim summary

| Claim | Scope | Status | Supporting evidence | Limitation or prevented claim |
| --- | --- | --- | --- | --- |
| `{{claim}}` | `{{scope}}` | `{{pass/fail/blocked/not-applicable/needs-org-input}}` | `{{links}}` | `{{limitations}}` |

### Evidence index

| Evidence ID | Description | Bound revision and environment | Requirements and results supported | Location | Freshness | Access or sanitization notes |
| --- | --- | --- | --- | --- | --- | --- |
| `{{EVID-001}}` | `{{description}}` | `{{revision-environment}}` | `{{IDs}}` | `{{location}}` | `{{current/stale}}` | `{{notes}}` |

### Delivery status

- Behavioral evidence status: `{{pass/fail/blocked; independent evaluator determines verdict}}`
- Organization-readiness state: `{{ready/not-ready/needs-org-input; authorized authority determines state}}`
- Failed checks still open: `{{IDs-or-none}}`
- Unavailable, skipped, blocked, or flaky checks: `{{IDs-or-none}}`
- Unresolved `P0` or `P1` findings: `{{IDs-or-none}}`
- Required handoffs and pending approvals: `{{IDs-or-none}}`
- Candidate package location: `{{artifact-and-evidence-location}}`

This record is evidence for review. It does not itself approve an exception, accept risk, authorize
deployment or production action, declare legal or accessibility conformance, approve release, or
activate `engineering.web`.

## Source Basis

Professional guidance in this template traces to the validated `engineering.web` research ledger:
HTML semantics [WEB-WHATWG-HTML-SEMANTICS], browser origins
[WEB-WHATWG-HTML-ORIGINS], CSS maturity [WEB-W3C-CSS-2025], ECMAScript semantics
[WEB-TC39-ECMA262], accessibility and keyboard/focus behavior [WEB-W3C-WCAG22]
[WEB-W3C-ARIA-KEYBOARD], HTTP semantics [WEB-RFC9110-HTTP], frontend security verification and CSP
[WEB-OWASP-ASVS] [WEB-W3C-CSP3], browser performance measurement
[WEB-W3C-PERFORMANCE-TIMELINE], and cross-browser testing [WEB-WPT-DOCS]. Source IDs resolve
through `changes/engineering.web-completion/research/sources.json`.
