# Web Frontend Delivery Evaluator

## Purpose, Scope, and Authority

This evaluator determines whether an `engineering.web` workflow outcome is supported by complete,
current, reproducible evidence. It evaluates the delivered browser-facing behavior and its handoff
record; it does not replace product acceptance, design approval, legal or accessibility conformance
decisions, security risk acceptance, deployment authorization, or release approval.

Apply this contract only to the requirements and surfaces declared by the authorized task contract.
Project overlays must supply repository commands, environments, supported browsers and assistive
technologies, accessibility targets, performance objectives, security requirements, release gates,
and decision authorities. The evaluator must not invent a missing threshold, command, target,
architecture fact, permission, reviewer, or approval. A missing organization fact is recorded as
`needs-org-input`; it blocks only claims that depend on that fact unless the task contract or Kernel
policy makes the missing fact an entry requirement for all work.

The evaluator must remain independent of the author of the evaluated outcome. It records evidence
and a verdict but does not modify implementation artifacts, suppress failures, narrow the evaluated
scope, or change the Domain lifecycle.

## Evaluation Inputs and Entry Gate

Before evaluating, bind the review to all of the following:

- task identifier, acceptance criteria, material negative paths, and acceptance authority;
- evaluated revision or immutable artifact identifier and changed-surface inventory;
- approved interface and content specification, service contract, and relevant project overlay;
- adopted accessibility target and declared browser, device, and assistive-technology matrix;
- approved security verification scope, performance objectives, and release-blocking policy;
- authorized commands, tools, environments, permissions, and evidence locations;
- baseline observations, implementation handoff, known failures, exclusions, and residual risks; and
- the versions of `DOMAIN.md`, `rules/BASE.md`, and `workflows/WORKFLOW.md` applied by the delivery.

If the outcome cannot be bound to a specific revision, its accepted requirements are unavailable,
or evidence provenance cannot be established, return `blocked` rather than inspecting an arbitrary
state. When only an organization-specific target or authority is absent, continue evaluating every
source-supported criterion that remains decidable and mark dependent criteria `needs-org-input`.

## Required Evidence Record

The evidence record must contain an index with one entry for every criterion in scope. Each entry
must identify:

1. criterion ID and requirement or rule being evaluated;
2. affected page, component, state, request, origin, resource, or browser target;
3. evaluated revision, environment, browser and version or other declared target identifier;
4. procedure or authorized command actually used, including relevant configuration and inputs;
5. expected behavior, observed behavior, and the resulting status;
6. timestamp, evidence producer, and stable location of raw or directly inspectable evidence;
7. positive and negative paths exercised, including skipped or unavailable paths;
8. rerun count or variability notes when results can fluctuate;
9. sanitization or redaction applied to protect credentials, personal data, or other protected data;
10. linked defect, exception, disposition, residual risk, and receiving authority when applicable.

Permitted criterion statuses are `pass`, `fail`, `blocked`, `not-applicable`, and
`needs-org-input`. `not-applicable` requires a reason tied to the declared scope; lack of evidence
is never evidence of non-applicability. Summaries, screenshots, or automated reports may index
evidence, but they do not substitute for the raw result or a directly inspectable artifact.

Evidence must include the actual outcome of every executed check. Failed, skipped, unavailable,
flaky, and blocked checks remain visible. Secrets and protected user data must not be copied into the
record; sanitization must preserve enough structure to reproduce the behavior safely.

## Acceptance Criteria

### WEB-EVAL-01 — Requirements, scope, and baseline traceability

**Pass conditions**

- Every claimed outcome maps to an accepted requirement, affected surface, and verification entry.
- The baseline and delivered result identify the revision, environment, method, and known pre-existing
  failures; exclusions and assumptions are explicit.
- The outcome does not claim behavior, support, conformance, performance, security, or release status
  beyond the surfaces and targets actually evaluated.

**Required evidence:** requirement-to-evidence map, changed-surface inventory, baseline record,
implementation or reviewable diff, exclusions, and delivery handoff.

**Negative paths:** inspect at least one declared failure, empty, unavailable, or recovery state for
each affected user journey where the task contract identifies such a state. An omitted material
negative path is a failure unless an authorized scope source makes it not applicable.

### WEB-EVAL-02 — HTML semantics and document behavior

**Pass conditions**

- Affected document structure, metadata, landmarks, navigation, content, forms, controls, and
  interactive elements use HTML according to their defined meanings and content-model constraints
  [WEB-WHATWG-HTML-SEMANTICS].
- Native elements are used when they satisfy the required behavior. Any custom interaction records
  why native semantics were insufficient and supplies equivalent structure, naming, state, and
  behavior evidence.
- Required meaning persists across loading, empty, success, error, disabled, updated, and responsive
  states that are in scope.

**Required evidence:** inspectable markup or rendered-tree capture for each material state, semantic
inspection results, form and control behavior, and the custom-semantics rationale where applicable.

**Negative paths:** malformed or rejected input, unsuccessful submission, missing or delayed content,
and client-side state updates are exercised when applicable. A visually correct surface with wrong or
unverified meaning fails this criterion.

### WEB-EVAL-03 — CSS rendering, feature maturity, and fallback behavior

**Pass conditions**

- The implementation distinguishes stable CSS specification maturity from actual implementation
  support and ties every material CSS capability to the declared target matrix [WEB-W3C-CSS-2025].
- Required layout, content, focus indication, interaction states, and relevant media or presentation
  contexts match the accepted specification for every exercised target.
- Unsupported or unavailable features follow an approved fallback, progressive enhancement, or
  degradation policy without losing required content or operation.

**Required evidence:** material feature inventory, applicable specification or authoritative support
reference, per-target rendering evidence, responsive and relevant media states, and exercised fallback
or degradation results.

**Negative paths:** constrained viewport or presentation context, unavailable material feature, content
expansion or overflow case supplied by the task contract, and error or disabled state where applicable.
Do not infer support from publication of a CSS specification or from a single browser result.

### WEB-EVAL-04 — ECMAScript behavior and host-environment assumptions

**Pass conditions**

- Browser application behavior matches accepted state-transition and error-handling requirements and
  uses ECMAScript semantics consistently with ECMA-262 [WEB-TC39-ECMA262].
- The evidence distinguishes ECMAScript language guarantees from browser host APIs and demonstrates
  availability or approved fallback for every material host capability across the declared matrix.
- Errors, cancellation, repeated actions, stale or partial state, and cleanup behavior do not leave the
  affected experience in a silently incorrect state where those paths are applicable.

**Required evidence:** behavior or state-transition tests, inspectable implementation, console and
runtime results, host-API inventory, and per-target availability or fallback evidence.

**Negative paths:** invalid input, rejected asynchronous operation, interruption or cancellation,
repeated activation, and unavailable host feature when applicable. A passing unit test in a simulated
environment does not establish browser-host compatibility.

### WEB-EVAL-05 — HTTP integration and recovery behavior

**Pass conditions**

- Requests, representations, fields, statuses, authentication context, and cache behavior follow the
  declared service contract and shared HTTP semantics [WEB-RFC9110-HTTP].
- The client presents or performs the required behavior for every applicable outcome without treating
  client-side validation as server authorization, integrity, or trust-boundary enforcement.
- Contract mismatches are preserved and handed to the service owner; undocumented observed behavior
  is not silently promoted to the contract.

**Required evidence:** authoritative service-contract reference; sanitized request and response
records; relevant method, representation, field, status, authentication, and cache observations; and
user-visible error and recovery results.

**Negative paths:** exercise every contractually applicable class among empty, partial, invalid,
unauthenticated, unauthorized, forbidden, not found, conflict, rate limited, transient failure,
unavailable, aborted, and stale or cached responses. The task contract determines applicability; the
evaluator must not manufacture endpoint behavior or test credentials.

### WEB-EVAL-06 — Accessibility across the complete affected experience

**Pass conditions**

- The evidence names the organization-adopted accessibility target and evaluates every applicable
  criterion across the complete affected page or flow, including automatically presented responsive
  variations [WEB-W3C-WCAG22].
- Every interactive function in scope is operable by keyboard; focus is visible, predictable, and not
  lost or trapped; focus entry, movement, restoration, and error behavior are verified
  [WEB-W3C-ARIA-KEYBOARD].
- Custom composite widgets demonstrate an appropriate implemented keyboard model and deliberate focus
  management; component tests and automated scans are supplemented by full-experience observations.

**Required evidence:** adopted target, applicability map, per-page or per-flow results, automated and
manual observations, keyboard-only trace, focus trace, responsive results, declared assistive-
technology results, failures, exceptions, and authoritative dispositions.

**Negative paths:** validation errors, unsuccessful operations, dynamic updates, modal or composite
widget entry and exit, focus restoration, and responsive variants when applicable. An unmet applicable
criterion remains a failure unless the authorized accessibility authority records a disposition; this
evaluator does not declare legal conformance or approve an exception.

### WEB-EVAL-07 — Origin, injection, and frontend security controls

**Pass conditions**

- The evidence inventories affected origins, data flows, executable content, third-party content, and
  trust boundaries, treating different origins as potentially hostile unless an authoritative model
  states otherwise [WEB-WHATWG-HTML-ORIGINS].
- Organization-approved secure-development requirements are evaluated for the affected surface;
  untrusted input and output contexts receive appropriate boundary validation and safe handling.
  ASVS may structure verification but does not select the organization's verification level or accept
  risk [WEB-OWASP-ASVS].
- When CSP is in scope, the policy source and report-only or enforcement state are explicit, relevant
  reports are reviewed, and CSP is treated as defense in depth rather than a substitute for validation
  or output encoding [WEB-W3C-CSP3].

**Required evidence:** origin and data-flow inventory, threat-model or verification-scope reference,
control-to-test map, sanitized positive and negative results, CSP policy and reports when applicable,
unresolved findings, and security or privacy handoff.

**Negative paths:** safely exercise applicable untrusted-content, cross-origin, navigation, resource,
messaging, authentication, and policy-violation scenarios defined by the approved verification scope.
Do not expose secrets, use production data, weaken policy, or expand testing beyond authorization.

### WEB-EVAL-08 — Measured browser performance

**Pass conditions**

- Every performance claim is supported by retrieved navigation, resource, or application-defined
  measurements appropriate to the claim [WEB-W3C-PERFORMANCE-TIMELINE].
- Evidence records scenario, environment, collection method, raw result, comparison basis, variability,
  and limitations and evaluates the result only against a cited organization-approved objective.
- Measurements avoid secrets and protected user information, and unstable results are reported as
  uncertainty rather than selected or averaged into an unsupported conclusion.

**Required evidence:** measurement definition, environment, scenario, relevant Performance Timeline
observations, raw or linked results, rerun or variability record, approved objective, and disposition.

**Negative paths:** where required by the task contract, evaluate an approved constrained, failure, or
recovery scenario as well as the expected path. Without an approved objective, measurement evidence
may pass for completeness while the performance acceptance claim remains `needs-org-input`.

### WEB-EVAL-09 — Cross-browser interoperability and rendering

**Pass conditions**

- Portable browser-facing tests or equivalent reproducible scenarios exercise required behavior on
  every target in the authoritative matrix [WEB-WPT-DOCS].
- Per-target results identify browser and version or other matrix identifier, environment, positive and
  negative paths, rendering or interaction evidence where applicable, and fallback behavior.
- Failures, reruns, and flakes distinguish implementation incompatibility from test-harness instability;
  no target is removed or reclassified without compatibility-policy-owner approval.

**Required evidence:** authoritative matrix, scenario or test definitions, per-target raw results,
visual or interaction captures where programmatic assertions are insufficient, rerun history,
divergences, fallbacks, and approved degradation dispositions.

**Negative paths:** material failure and fallback states run across the same applicable matrix as the
positive behavior. One browser, a simulated DOM, or an unexecuted target cannot support a matrix-wide
claim.

### WEB-EVAL-10 — Handoff, recovery, and authority boundaries

**Pass conditions**

- The handoff contains the candidate artifact, evidence index, exact executed procedures and outcomes,
  failed and unavailable checks, residual risks, blocked decisions, and named receiving authorities
  when known.
- Recovery guidance identifies the smallest recoverable unit and applicable client state, cache,
  service-worker, CDN, session, data, schema, and backend dependencies only when supported by project
  evidence. It uses the approved procedure or records `needs-org-input`.
- The outcome does not imply deployment permission, release approval, accessibility or legal
  conformance, security risk acceptance, or a lifecycle change.

**Required evidence:** delivery handoff, risk and decision log, recovery or rollback reference,
approval state, receiving-authority record, and unresolved organization gaps.

**Negative paths:** review what occurs when a required check, reviewer, environment, permission,
rollback procedure, or release decision is unavailable. Silence, an empty reviewer list, and successful
implementation checks never constitute approval.

## Cross-Criterion Evidence Rules

### Freshness

Evidence is current only when it is bound to the evaluated revision and to an environment and
configuration representative of the declared claim. Evidence from an earlier revision may be reused
only when the record demonstrates that neither the relevant implementation nor its material inputs,
configuration, target, or environment changed. A calendar age alone does not prove freshness, and this
Domain does not invent an expiration interval.

If a service contract, browser target, accessibility target, threat model, CSP policy, performance
objective, dependency, or relevant environment changed after collection, rerun the affected evidence
or mark it stale. Stale evidence cannot pass the dependent criterion.

### Reproducibility

An independent qualified reviewer must be able to identify the revision, reconstruct the authorized
environment, follow the recorded procedure, locate the inputs, and compare the observed output with the
expected result. Exact local paths or organization commands come from the project overlay or task
contract, never from this evaluator. If protected infrastructure prevents independent rerun, retain the
authorized execution record and identify the access owner; return `blocked` only when the missing access
prevents a trustworthy decision.

### Conflicting and flaky evidence

Contradictory current results remain visible and the affected criterion is `fail` unless the evidence
shows that a declared target or scenario could not be evaluated, in which case it is `blocked`. A rerun
does not erase an earlier failure. The record must explain the cause, scope, and disposition or preserve
the result as flaky and unverified. No favorable sample may be selected to conceal variability.

## Severity Classification

Apply the organization's stricter approved severity policy when one exists. Otherwise use this reusable
impact model without adding numeric thresholds:

| Severity | Classification |
| --- | --- |
| `P0` | Demonstrated active or readily exploitable loss of a critical trust boundary; exposure or destructive corruption of protected data; or behavior creating immediate widespread danger that requires authorized emergency handling. |
| `P1` | Required primary behavior is unusable for affected users with no acceptable recovery; an adopted accessibility requirement blocks a core journey; a supported target cannot perform required behavior; or a high-impact security, integrity, or release-blocking requirement is unmet. |
| `P2` | Material requirement, negative path, fallback, compatibility case, accessibility behavior, or performance objective is unmet, but the primary journey retains a bounded recovery or the impact is limited. |
| `P3` | Low-impact defect, evidence-quality weakness, or maintainability issue that does not invalidate the evaluated requirement but requires tracked correction. |

Severity describes impact; it does not grant authority to accept risk. When impact cannot be determined
because an organization policy or affected-user fact is missing, record the provisional evidence,
`needs-org-input`, and the authority required. Do not lower severity because a reviewer or fix is absent.

## Criterion and Overall Verdict Semantics

- `pass`: all pass conditions applicable to the criterion are satisfied by fresh, reproducible
  evidence; no unresolved contradictory result exists.
- `fail`: observed behavior or evidence contradicts an applicable requirement, or required evidence or
  a material path was omitted despite being available and authorized.
- `blocked`: a required input, artifact, environment, permission, or trustworthy evidence path is
  unavailable, so the evaluator cannot determine the criterion. `blocked` is not a softer pass.
- `not-applicable`: an authoritative scope source demonstrates that the criterion does not apply.
- `needs-org-input`: source-supported evaluation can continue, but a missing organization-owned
  target, matrix, threshold, policy, reviewer, command, or authority prevents the dependent acceptance
  or release claim.

The overall verdict is:

- `pass` only when every applicable criterion is `pass`, no unresolved `P0` or `P1` finding exists,
  all required evidence is fresh and reproducible, and no required approval is being inferred;
- `fail` when any applicable criterion is `fail`; or
- `blocked` when no criterion fails but at least one required criterion cannot be determined because of
  a blocker.

Record `needs-org-input` separately from the behavioral verdict. A delivery may satisfy the reusable
professional baseline while remaining ineligible for organization acceptance, release, or Domain
activation. If an organization-owned input is itself required by the task's entry contract, its absence
makes the overall verdict `blocked`; otherwise it limits only the dependent claim.

## Required Evaluation Output

Return a review record containing:

- evaluated task, revision, environment, scope, exclusions, evaluator identity, and evaluation time;
- applied Domain, rule, workflow, overlay, service-contract, and source-ledger versions;
- criterion-by-criterion status with evidence links and positive and negative paths;
- findings with severity, affected requirement and users or systems, reproduction, and owner;
- stale, conflicting, flaky, skipped, unavailable, and sanitized evidence notes;
- residual risks, recovery implications, handoffs, and recorded dispositions;
- organization-specific gaps and the exact claims they prevent;
- overall `pass`, `fail`, or `blocked` verdict plus a separate organization-readiness statement.

The record must never claim that the evaluator approved an exception, accepted risk, authorized an
operational action, or activated `engineering.web`.

## Organization-Specific Gaps

The reusable evaluator deliberately leaves the following as `needs-org-input` until authoritative
evidence supplies them:

- required engineering, product, design, accessibility, security, privacy, service, compatibility,
  performance, delivery, and release reviewers and their decision rights;
- repository, dependency, test, policy, deployment, production, recovery, and rollback permissions;
- project architecture, rendering model, service and authentication topology, design-system and
  framework conventions, dependency policy, supported language target, and observability stack;
- authoritative install, development, analysis, test, build, preview, accessibility, security,
  deployment, and rollback commands and evidence formats;
- supported browsers and versions, devices, assistive technologies, localization contexts, and
  degradation policy;
- adopted WCAG conformance level, performance objectives and budgets, coverage and interoperability
  expectations, vulnerability thresholds, and release-blocking criteria; and
- approved threat model, ASVS scope or verification level, CSP rollout policy, incident path,
  risk-acceptance authority, and production approval record.

These gaps prevent dependent organizational claims and activation readiness; they do not authorize the
evaluator to weaken the public professional baseline or fabricate a substitute.

## Source Basis

This evaluator uses the validated `engineering.web` research ledger: Domain identity
[REPO-WEB-DOMAIN-IDENTITY], HTML semantics and browser origins
[WEB-WHATWG-HTML-SEMANTICS] [WEB-WHATWG-HTML-ORIGINS], CSS specification maturity
[WEB-W3C-CSS-2025], ECMAScript semantics [WEB-TC39-ECMA262], WCAG 2.2 and keyboard/focus guidance
[WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD], HTTP semantics [WEB-RFC9110-HTTP], CSP and application
security verification guidance [WEB-W3C-CSP3] [WEB-OWASP-ASVS], browser performance instrumentation
[WEB-W3C-PERFORMANCE-TIMELINE], and cross-browser testing practice [WEB-WPT-DOCS]. Source IDs resolve
through the completion change's validated research ledger.
