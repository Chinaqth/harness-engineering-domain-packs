# Web Frontend Delivery Workflow

## Purpose and Authority

This workflow turns an authorized Web frontend task into a reviewable implementation and an
evidence-bearing delivery handoff. It is framework-neutral: project overlays supply repository
paths, architecture, tools, commands, quality thresholds, target environments, and release
procedures. The workflow applies `engineering.web` rules and does not authorize dependency
adoption, production access, deployment, release approval, policy changes, or risk acceptance.

The practitioner must retain failed, skipped, unavailable, and blocked results. A missing input,
permission, reviewer, target, or command is not a passing result. Safe baseline work may continue
outside the affected decision, but any claim that depends on an unresolved organization fact is
`needs-org-input`.

## Preconditions and Entry Gate

Open a delivery evidence record before implementation. Record the task identifier, accountable
requester, affected surface, evidence locations, and the current revision or artifact baseline.
Proceed only after evaluating every entry below.

| Required input | Entry evidence | If absent or contradictory |
| --- | --- | --- |
| Desired outcome and acceptance criteria | Observable expected behavior, material negative paths, and the authority that accepts product behavior | Stop the affected product decision; return the competing interpretations and user-visible impact to the product owner. |
| Approved interface and content specification | Required structure, states, content, responsive behavior, and identified design authority | Do not invent visual or interaction intent; hand unresolved states to the design or product owner. |
| Execution and integration boundaries | Authoritative project context, affected client surface, rendering or integration boundaries, and known dependencies | Limit work to verified surfaces; mark architecture-dependent decisions `needs-org-input`. |
| Service contract | Methods, representations, fields, statuses, authentication context, cache behavior, and error semantics [WEB-RFC9110-HTTP] | Do not infer a contract from one observed response; stop integration decisions that cannot be made safely and hand them to the service owner. |
| Quality targets | Adopted accessibility target, supported browser/device/assistive-technology matrix, performance objectives, test expectations, and release-blocking criteria | Continue only with source-supported baseline checks; do not claim accessibility, compatibility, performance, or release acceptance. |
| Security and privacy constraints | Applicable threat model or verification scope, origin and data boundaries, CSP policy when relevant, escalation path, and risk authority | Stop security-sensitive expansion; request the missing authority or policy rather than choosing it. |
| Authorized execution contract | Verified tools, project commands, environments, permissions, and recovery procedure | Do not guess, install, execute, deploy, or mutate beyond granted authority. Record the missing item and its effect. |
| Handoff map | Identified product, design, service, accessibility, security/privacy, compatibility, performance, delivery, and release authorities needed by the task | Record unknown roles as `needs-org-input`; absence of a recipient never implies approval. |

The entry-gate output is a scoped work record containing accepted requirements, exclusions,
assumptions, unresolved decisions, affected trust and service boundaries, authorized actions, and
the planned evidence. A reviewer must be able to distinguish confirmed inputs from assumptions.

## Ordered Delivery Procedure

### 1. Baseline the affected experience

1. Inventory the affected pages, components, document regions, interaction states, data flows,
   requests, resources, origins, and presentation contexts.
2. Reproduce the current expected and material negative paths in an authorized environment.
3. Record existing failures, unavailable checks, console or network symptoms, compatibility
   divergences, accessibility observations, and performance measurements without attributing
   them to the proposed change prematurely.
4. Map each acceptance criterion to an implementation surface and a planned verification method.

**Output and evidence:** a changed-surface inventory, sanitized baseline observations, a
requirement-to-verification map, and explicit exclusions.

**Verification:** every planned change is tied to an accepted requirement or a documented defect;
the baseline identifies the environment and method used; existing failures remain visible.

**Fail closed:** if the current behavior cannot be observed, the affected boundary is unknown, or
reproduction would require unauthorized access or protected data, do not manufacture a baseline.
Record the limitation and ask the accountable owner for a safe environment or authoritative
evidence.

### 2. Design the smallest authorized change

1. Choose native HTML structure and controls that express the required meaning before considering
   custom interaction [WEB-WHATWG-HTML-SEMANTICS].
2. Identify the CSS, ECMAScript, and browser host features needed. Separate language guarantees
   from host-API availability, and separate CSS specification maturity from support in the
   declared browser matrix [WEB-TC39-ECMA262] [WEB-W3C-CSS-2025].
3. Define loading, empty, success, partial, invalid-input, authorization, failure, retry, and
   recovery states that are material to the accepted behavior and service contract.
4. Identify effects on keyboard and focus behavior, accessible names and states, origins,
   untrusted content, authentication context, caching, resource loading, performance, and browser
   compatibility.
5. Define a recovery unit that can reverse or disable the proposed client change without claiming
   authority over deployment or production rollback.

**Output and evidence:** an implementation plan listing semantic choices, material features,
states and negative paths, integration and trust boundaries, validation coverage, and recovery
needs.

**Verification:** the plan covers every accepted criterion and identifies who must decide each
tradeoff. Custom interaction includes a reason native semantics are insufficient. Material Web
features have a verification or approved fallback plan rather than presumed compatibility.

**Fail closed:** do not silently broaden scope, add a dependency, select a polyfill or
transpilation policy, weaken a security control, or narrow a support matrix without the relevant
authority.

### 3. Implement semantic structure and presentation

1. Implement document structure, metadata, landmarks, navigation, content, forms, and controls
   with HTML elements used according to their defined semantics and content models
   [WEB-WHATWG-HTML-SEMANTICS].
2. Preserve meaning and content across responsive variations and loading, error, disabled, empty,
   and updated states.
3. Apply CSS so the accepted presentation works in the required media and presentation contexts.
   Treat stable specification status and actual browser support as separate evidence questions
   [WEB-W3C-CSS-2025].
4. Provide an approved fallback or degradation path for material features not supported throughout
   the declared matrix; retain required content and operation.

**Output and evidence:** reviewable implementation artifacts or diffs; rendered or inspected
structure for affected states; the material CSS feature inventory; responsive and fallback
evidence; and known visual limitations.

**Verification:** inspect both structure and rendered behavior. Confirm that visual treatment has
not substituted for missing meaning and that responsive changes do not remove required content or
operation.

**Fail closed:** an unverified custom semantic pattern, unsupported required feature, or missing
fallback remains a defect. Correct it within scope or hand the tradeoff to the design,
accessibility, or compatibility owner.

### 4. Implement application behavior

1. Implement client logic using defined ECMAScript semantics and explicitly identified browser
   host APIs [WEB-TC39-ECMA262].
2. Keep state transitions deterministic for the accepted interaction, including re-entry,
   cancellation, repeated activation, stale results, and recovery where applicable.
3. Preserve meaningful user feedback and operability when operations are pending, fail, or return
   no usable result.
4. Avoid treating simulated environments or language-level correctness as proof that required
   host APIs work in target browsers.

**Output and evidence:** reviewable behavior changes, state-transition coverage, host-feature
inventory, negative-path results, and identified timing or concurrency limitations.

**Verification:** exercise observable behavior, not only internal functions. Tie each state and
recovery result to the relevant acceptance criterion and preserve failures.

**Fail closed:** if a required host capability is unavailable or inconsistent in the declared
matrix, use only an approved fallback. Otherwise mark the target unverified and escalate the
compatibility decision.

### 5. Integrate at the HTTP boundary

1. Implement requests and responses against the authoritative service contract and shared HTTP
   method, representation, field, status, authentication, and caching semantics
   [WEB-RFC9110-HTTP].
2. Exercise every contract outcome material to the change, including applicable success, empty,
   partial, invalid, unauthorized, forbidden, not-found, conflict, rate-limited, transient, and
   unavailable responses.
3. Verify cancellation, duplicate action, retry, cache, stale-response, and user-visible recovery
   behavior when the task contract makes them relevant.
4. Sanitize request and response evidence. Never place credentials, tokens, personal data, or
   protected payloads in the evidence record.

**Output and evidence:** the cited service contract, sanitized request/response cases, per-status
behavior, authentication and cache assumptions, recovery results, and contract mismatches.

**Verification:** the client neither invents undocumented meanings nor claims to enforce server
authorization, validation, persistence, or integrity. Expected and negative outcomes match the
declared contract.

**Fail closed:** when observed behavior contradicts the contract, retain a sanitized reproduction
and stop relying on the contradiction. Hand it to the service owner when safe client behavior
cannot be determined.

### 6. Verify accessibility across the complete affected experience

1. Translate the organization-adopted accessibility target into applicable tests for the full
   affected pages or flows, including automatically presented responsive variations
   [WEB-W3C-WCAG22].
2. Inspect semantic structure, names, roles, states, relationships, content order, error
   communication, and state changes in every material state.
3. Exercise all interactive functions with a keyboard. Observe focus entry, visible focus,
   movement, trapping, loss, restoration, and movement caused by updates.
4. For custom composite widgets, verify the intentional keyboard model and focus-management
   technique; ARIA semantics alone do not supply keyboard behavior
   [WEB-W3C-ARIA-KEYBOARD].
5. Run assistive-technology checks only against the declared matrix and record exactly what was
   and was not exercised.

**Output and evidence:** adopted target and tested scope; per-page or per-flow results; keyboard
and focus observations; responsive results; declared assistive-technology results; failures,
exceptions, and limitations.

**Verification:** automated findings are reconciled with manual interaction evidence, and a
component-level pass is not presented as full-page conformance [WEB-W3C-WCAG22].

**Fail closed:** any unmet applicable criterion remains unresolved unless an authorized authority
records a disposition. Do not invent a conformance level, exception, assistive-technology target,
or legal conclusion.

### 7. Verify frontend security and privacy boundaries

1. Reconcile the implementation with the affected origin, resource, executable-content,
   cross-origin communication, authentication, and data-flow inventory. Treat distinct origins as
   potentially hostile unless an authoritative model says otherwise
   [WEB-WHATWG-HTML-ORIGINS].
2. Apply the organization-approved verification scope to input, DOM or template insertion,
   navigation, messaging, resource loading, storage, and sensitive-data handling. OWASP ASVS may
   structure verification but does not choose a local verification level or accept risk
   [WEB-OWASP-ASVS].
3. Verify context-appropriate safe output handling and the server-side ownership of trust-boundary
   validation; client checks are not server controls.
4. When CSP is in scope, verify the authoritative policy and whether evidence comes from
   report-only observation or enforcement. CSP is defense in depth, not a replacement for input
   validation or output encoding [WEB-W3C-CSP3].
5. Sanitize reports and test artifacts before retaining or handing them off.

**Output and evidence:** origin and data-flow inventory, trust boundaries, applicable verification
requirements, sanitized positive and negative results, CSP state and relevant violations when in
scope, and unresolved findings.

**Verification:** no security claim exceeds the approved threat model or tested surface; no policy
was weakened and no sensitive evidence was retained.

**Fail closed:** stop unsafe expansion on an origin, injection, executable-content, credential,
authentication, or sensitive-data concern. Preserve non-sensitive evidence and transfer the
finding to the security or privacy authority; never self-approve residual risk.

### 8. Measure browser performance

1. Define the claim, user scenario, environment, collection method, and organization-approved
   objective before judging performance.
2. Collect relevant navigation, resource, and application-defined measurements through suitable
   Performance Timeline capabilities [WEB-W3C-PERFORMANCE-TIMELINE].
3. Retain raw or linked results and enough environmental context to reproduce them. Record reruns,
   variability, cache or network conditions, and measurement limitations where applicable.
4. Compare results only with the approved objective or baseline; do not derive a release threshold
   from the observed sample.

**Output and evidence:** measurement definition, environment, scenario, observations, raw or
linked results, comparison basis, variability notes, limitations, and disposition against the
cited objective.

**Verification:** every performance claim is backed by retrieved measurements and qualified by
the tested conditions. Instrumentation contains no unauthorized protected information.

**Fail closed:** an absent objective, unstable result, or unavailable representative environment
prevents an acceptance claim. Retain the uncertainty and hand target setting or business
tradeoffs to the accountable owner.

### 9. Verify compatibility across the declared matrix

1. Run portable browser-facing tests or equivalent reproducible scenarios for every required
   target and material expected or negative path [WEB-WPT-DOCS].
2. Retain rendering or interaction evidence where correctness cannot be established by a
   programmatic assertion alone.
3. Record target identifiers, environment, results, reruns, divergences, fallbacks, and degradation
   behavior. Separate test instability from implementation incompatibility.
4. Reconcile compatibility results with the material HTML, CSS, ECMAScript, host-API,
   accessibility, HTTP, security, and performance choices already recorded.

**Output and evidence:** authoritative matrix reference, portable scenario definitions,
per-target results, visual or interaction evidence where needed, negative-path outcomes, and
failure, flake, fallback, and degradation records.

**Verification:** the compatibility claim names only targets and behaviors actually exercised. A
single browser, simulated DOM, or passing unit suite does not stand in for an unexecuted matrix.

**Fail closed:** an unavailable target remains unverified and a failing target remains
incompatible until corrected or dispositioned by the compatibility owner. Do not remove a target
or redefine required degradation to obtain a pass.

### 10. Reconcile evidence and prepare the delivery handoff

1. Re-run the narrow authorized checks affected by remediation, then the full project-defined
   verification set required by the task contract. Record the actual procedures and results; do
   not invent commands or claim checks that did not run.
2. Index every acceptance criterion to its implementation artifact, method, result, and evidence
   location. Include expected and negative paths and label each check passed, failed, skipped,
   unavailable, or blocked.
3. Review the changed surface for unintended scope, exposed sensitive data, weakened controls,
   undocumented dependencies, and disagreement between implementation and documentation.
4. Record residual risks, known limitations, unresolved decisions, affected users or systems,
   recovery guidance, and the receiving authority for every handoff.
5. Package the reviewable artifact and evidence for the authorized product, design, service,
   accessibility, security/privacy, compatibility, performance, delivery, and release reviewers
   applicable to the task.

**Output and evidence:** implementation artifact or diff, evidence index, requirements trace,
executed-procedure record, failed and unavailable checks, residual-risk register, recovery note,
and handoff status.

**Verification:** evidence and actual behavior agree; all exclusions are explicit; no passing
claim depends on missing evidence; and no reviewer silence is recorded as approval.

**Fail closed:** do not label the work release-ready when a task-defined release blocker fails,
required evidence is missing, or the responsible authority has not provided its required
disposition. Stop before deployment or production action unless the execution contract explicitly
authorizes it.

## Negative-Path Control Table

| Condition | Required response | Completion effect |
| --- | --- | --- |
| Requirement, content, or interaction intent is ambiguous | Preserve alternatives and impact; request a product or design decision. | Block only claims and implementation choices dependent on the ambiguity. |
| Tool, command, environment, permission, or dependency authority is unverified | Do not guess, install, execute, or claim a result; request an authoritative project source. | Mark the affected check unavailable or blocked. |
| Semantic, keyboard, focus, responsive, or state behavior fails | Preserve reproduction evidence; remediate within scope; rerun the relevant checks. | Keep the affected behavior failed until verified or dispositioned by its authority. |
| Service response contradicts the declared contract | Sanitize and retain the exchange; stop depending on undocumented behavior; hand off to the service owner. | Block the affected integration claim. |
| Origin, injection, policy, credential, authentication, or protected-data concern appears | Stop unsafe expansion; preserve non-sensitive evidence; escalate to security or privacy. | Block the affected security and release claims; no self-approved exception. |
| Performance objective is missed or measurement is unstable | Preserve raw results and context; distinguish repeatable regression from uncertainty; escalate the tradeoff. | Do not redefine the objective or claim acceptance. |
| Browser result fails, flakes, or cannot run | Record each result and rerun; distinguish harness instability from incompatibility. | Target remains failed or unverified; matrix cannot be silently narrowed. |
| Required reviewer, threshold, matrix, or risk authority is unknown | Record `needs-org-input` with the evidence required and impacted decision. | Public baseline work may continue, but dependent acceptance and release claims stop. |
| Deployment or rollback authority is absent | Transfer the verified artifact, evidence, and recovery needs to the delivery owner. | No operational action is authorized by this workflow. |

## Handoffs and Decision Records

Each handoff must state the decision requested, affected requirement and surface, available
options, user or system impact, sanitized evidence, urgency when supplied by the task contract,
and receiving authority. Record the disposition and its source when received.

- Product and design receive unresolved intent, state, content, responsive, and visual tradeoffs.
- Service owners receive HTTP-contract mismatches and client behavior that cannot be determined
  safely.
- Accessibility and, where required, legal authorities receive applicability questions,
  exceptions, affected users, and reproducible interaction evidence.
- Security and privacy authorities receive trust-boundary, CSP, injection, authentication,
  credential, or data-handling findings without exposed secrets.
- Performance and compatibility policy owners receive missed objectives, unstable measurements,
  target failures, degradation proposals, and affected-user analysis.
- Delivery and release owners receive the candidate artifact, complete evidence index, unresolved
  blockers, recovery requirements, and approval state.

## Recovery, Rollback, and Limitations

Before handoff, document the smallest recoverable unit, dependencies between changes, data or
state implications, cache and client-version considerations, monitoring or validation needed after
reversal, and how to verify restored behavior. Use only the organization-approved rollback or
recovery procedure. If none is supplied, mark rollback `needs-org-input` and do not invent or
execute one.

A client artifact may not be immediately recoverable after publication because browser caches,
service workers, CDN behavior, long-lived sessions, stored client state, schema changes, or
backend dependencies can outlive a release. These conditions must be derived from authoritative
project context, not presumed. The handoff must distinguish source reversal, build-artifact
replacement, feature disablement, data recovery, and operational rollback, and identify the owner
authorized for each applicable action.

This workflow cannot by itself establish product approval, legal or accessibility conformance,
security acceptance, production readiness, support for an undeclared browser matrix, or
performance suitability without adopted objectives and evidence.

## Organization-Specific Inputs Still Required

The reusable workflow intentionally does not supply:

- required engineering, product, design, accessibility, security, privacy, delivery, and release
  reviewers or their decision rights;
- repository, dependency, policy, deployment, production, recovery, or rollback permissions;
- project architecture, rendering model, service and authentication topology, design-system and
  framework conventions, dependency policy, or observability stack;
- authoritative install, development, analysis, test, build, preview, security, accessibility,
  deployment, or rollback commands;
- supported browsers, versions, devices, assistive technologies, localization contexts, or
  degradation policy;
- adopted WCAG conformance level, performance objectives, coverage expectations, vulnerability
  thresholds, interoperability thresholds, or release blockers; or
- threat model, ASVS verification scope, CSP rollout policy, incident path, evidence format, risk
  authority, or production approval record.

Until authoritative project or task evidence resolves these inputs, dependent workflow outcomes
remain `needs-org-input`. Active Domain routing does not make an underspecified task executable and
this workflow supplies no operational permission.

## Source Basis

This workflow uses the validated `engineering.web` research ledger: HTML semantics
[WEB-WHATWG-HTML-SEMANTICS], CSS specification maturity [WEB-W3C-CSS-2025], ECMAScript semantics
[WEB-TC39-ECMA262], WCAG 2.2 [WEB-W3C-WCAG22], keyboard and focus guidance
[WEB-W3C-ARIA-KEYBOARD], HTTP semantics [WEB-RFC9110-HTTP], browser origins
[WEB-WHATWG-HTML-ORIGINS], Content Security Policy [WEB-W3C-CSP3], application-security
verification guidance [WEB-OWASP-ASVS], Performance Timeline instrumentation
[WEB-W3C-PERFORMANCE-TIMELINE], and cross-browser testing practice [WEB-WPT-DOCS].
