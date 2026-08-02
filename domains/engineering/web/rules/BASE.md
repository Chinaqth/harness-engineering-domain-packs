# Web Frontend Engineering Rules

## Authority and Applicability

These rules apply when `engineering.web` designs, implements, changes, reviews, or verifies browser-delivered documents, interfaces, application behavior, client-side service integration, frontend security controls, browser performance instrumentation, or browser compatibility. They apply only within an authorized task contract and supplement, but do not weaken, Kernel authorization, security, privacy, evidence, approval, or lifecycle requirements.

The task contract must identify the affected user-visible behavior, applicable product and interface requirements, integration boundaries, adopted quality targets, supported browser and assistive-technology matrix, and authorized tools and permissions. When an organization-specific target, threshold, reviewer, command, architecture fact, or risk authority is absent, the practitioner must not invent it. Safe source-supported baseline work may continue, but the affected acceptance or release decision must be recorded as `needs-org-input` and handed to the accountable owner.

## Professional Invariants

### WEB-RULE-01 — Preserve native platform semantics

**Applies to:** document structure, metadata, navigation, content, forms, controls, and interactive elements.

- Use HTML elements according to their defined meaning and content-model constraints. Do not replace a suitable native element with a generic element plus scripted behavior merely for implementation convenience [WEB-WHATWG-HTML-SEMANTICS].
- Preserve the document and interaction meaning through responsive variants, loading states, error states, and client-side updates.
- When custom interaction is necessary, record why native semantics are insufficient and verify the additional semantics and behavior rather than assuming visual resemblance is equivalent.

**Required evidence:** reviewable markup or rendered-tree evidence for the affected states; a record of intentional custom semantics; and tests or inspection results covering structure, naming, state, and form behavior where applicable.

**Failure and handoff:** a semantic violation or an unverified custom interaction is an unresolved defect. Preserve the failing evidence, correct it within authorization, or hand it to the design or accessibility owner with the affected behavior and user impact. Do not declare the surface complete while the required meaning remains unverified.

### WEB-RULE-02 — Select Web features by maturity and declared support

**Applies to:** CSS features, browser host APIs, ECMAScript features, and presentation across relevant media or device contexts.

- Distinguish language or specification semantics from host-environment availability. ECMAScript conformance does not by itself establish that a browser API exists in every target environment [WEB-TC39-ECMA262].
- Evaluate CSS specification maturity and actual implementation support separately; a published feature is not presumed compatible with the organization-supported browser matrix [WEB-W3C-CSS-2025].
- For every feature material to required behavior, provide either evidence across the declared matrix or an explicitly accepted fallback, progressive path, or degradation policy. A fallback must retain the required content and operation identified by the task contract.
- Do not silently narrow the supported matrix, mandate a transpilation or polyfill strategy, or define a degradation threshold without organizational authority.

**Required evidence:** the declared target matrix; the material feature inventory; compatibility results or authoritative support evidence; exercised fallback or degradation behavior; and unresolved target-specific limitations.

**Failure and handoff:** if the matrix or degradation authority is missing, mark the compatibility claim `needs-org-input`. If a required target fails, retain the per-target result and hand the tradeoff to the owner of the compatibility policy; do not recast the failure as supported behavior.

### WEB-RULE-03 — Make accessibility targets testable across complete experiences

**Applies to:** full pages, responsive variations, navigation, forms, state changes, components, and custom widgets.

- Translate the organization-adopted accessibility target into testable criteria for the complete affected page or experience, including automatically presented responsive variations. Do not claim conformance from an isolated component result or automated scan alone [WEB-W3C-WCAG22].
- Every interactive function in scope must be operable by keyboard. Focus must remain visible and move predictably; focus must not become lost, trapped, or moved without an interaction-based reason [WEB-W3C-ARIA-KEYBOARD].
- Custom composite widgets must implement and verify an appropriate keyboard model and deliberate focus-management strategy. Browser-provided ARIA semantics do not supply the required keyboard behavior automatically [WEB-W3C-ARIA-KEYBOARD].
- Do not invent the adopted conformance level, assistive-technology matrix, exception authority, or legal conclusion.

**Required evidence:** the adopted target and tested scope; per-page or per-flow results for applicable criteria; keyboard-only observations; focus entry, movement, restoration, and failure-path observations; responsive-variation results; relevant assistive-technology results from the declared matrix; and all failures or exceptions.

**Failure and handoff:** any unmet applicable criterion remains a failure against the adopted target unless an authorized authority records a disposition. Stop the affected completion claim and hand exceptions or unresolved applicability questions to the designated accessibility and, where required, legal authority with reproducible evidence and user impact.

### WEB-RULE-04 — Honor the declared HTTP contract

**Applies to:** browser requests, responses, representations, fields, authentication context, status handling, caching behavior, retries, and client-visible errors.

- Implement client behavior against a declared service contract and the shared semantics of HTTP methods, status codes, representations, fields, authentication, and caching [WEB-RFC9110-HTTP].
- Treat success, empty, partial, invalid, unauthorized, forbidden, not-found, conflict, rate-limited, transient-failure, and unavailable outcomes according to the applicable contract; do not infer undocumented response meaning from one observed example.
- Do not move server authorization, integrity, or validation responsibility into the browser or claim that client-side checks enforce a trust boundary.
- Preserve request and response evidence without exposing credentials, tokens, personal data, or other protected content.

**Required evidence:** the authoritative service-contract reference; exercised request and response cases applicable to the change; representation and status handling; authentication and cache assumptions; error and recovery behavior; and recorded contract mismatches.

**Failure and handoff:** when observed service behavior contradicts the contract, do not silently normalize or depend on it. Preserve a sanitized reproduction and hand the mismatch to the service owner; stop the affected integration decision when safe client behavior cannot be determined.

### WEB-RULE-05 — Treat origins and injected content as security boundaries

**Applies to:** navigation, cross-origin communication, resource loading, DOM or template insertion, executable content, third-party content, authentication context, and security policy configuration.

- Identify the origins and trust boundaries affected by the change. Treat actors from different origins as potentially hostile unless an authoritative security model establishes otherwise [WEB-WHATWG-HTML-ORIGINS].
- Apply the organization-approved secure-development and verification requirements to the affected surface; OWASP ASVS may inform verification planning but does not grant risk-acceptance authority or select an organization-specific verification level [WEB-OWASP-ASVS].
- Validate untrusted input at the appropriate trust boundary and use context-appropriate safe output handling. Do not rely on client-side validation for server trust decisions.
- Use Content Security Policy as defense in depth where the approved policy makes it applicable. CSP may restrict fetched or executed resources and may be introduced with report-only observation before enforcement, but it does not replace careful validation or output encoding [WEB-W3C-CSP3].
- Do not weaken an enforced policy, add a permissive source, expose sensitive report data, or accept residual security risk without the designated authority.

**Required evidence:** origin and data-flow inventory; identified trust boundaries; applicable verification requirements and results; injection-defense observations; sanitized negative-path evidence; and, when CSP is in scope, the policy source, report-only or enforcement state, relevant reports, and disposition of violations.

**Failure and handoff:** stop unsafe expansion when an origin, injection, executable-content, credential, authentication, or sensitive-data concern is discovered. Preserve non-sensitive evidence and escalate to the authorized security or privacy owner. Missing threat models, CSP policy, severity thresholds, or risk authority are `needs-org-input`, never implied acceptance.

### WEB-RULE-06 — Instrument performance claims before judging them

**Applies to:** claims or decisions about navigation, resource loading, rendering-related work, and application-defined browser performance.

- Base performance claims on retrieved measurements rather than subjective impressions. Use appropriate navigation, resource, and application-defined timing observations for the behavior under review [WEB-W3C-PERFORMANCE-TIMELINE].
- Record measurement environment, scenario, collection method, raw or linked results, comparison basis, variability, and known limitations so another qualified reviewer can reproduce or challenge the result.
- Evaluate results only against organization-approved objectives or budgets. Do not invent numeric targets, sample requirements, acceptable variance, release thresholds, or business tradeoffs.
- Instrument only data authorized for collection and avoid placing secrets or protected user information in marks, measures, logs, or reports.

**Required evidence:** measurement definition and scope; environment and scenario; navigation, resource, or application-defined observations relevant to the claim; raw or linked results; repeated-run or variability notes where applicable; and disposition against a cited approved objective.

**Failure and handoff:** an uninstrumented, non-reproducible, or unstable observation cannot support a performance acceptance claim. Retain the uncertainty and hand missed objectives or target-setting decisions to their accountable owner; do not redefine the objective after measurement.

### WEB-RULE-07 — Verify required behavior across the declared browser matrix

**Applies to:** behavior, rendering, input, accessibility, network integration, and fallbacks that can vary between supported browsers or browser configurations.

- Use portable browser-facing tests or equivalent reproducible scenarios across the declared matrix. Cross-browser tests provide interoperability evidence only for the targets and behaviors actually exercised [WEB-WPT-DOCS].
- Cover both expected and negative paths material to the change. Where correctness is visual or interaction-dependent, retain rendering or interaction evidence in addition to programmatic assertions.
- Record the browser and version or other matrix identifier, environment, result, rerun behavior, and any divergence. Separate test instability from implementation incompatibility.
- Do not substitute one browser, a simulated DOM, or a passing unit suite for an unexecuted matrix claim; do not remove a failing target without policy-owner approval.

**Required evidence:** the authoritative matrix; portable test or scenario definitions; per-target results; visual or interaction evidence when applicable; negative-path outcomes; and failure, retry, flake, fallback, and degradation records.

**Failure and handoff:** preserve inconsistent or flaky results and attempt only authorized diagnosis. An unavailable target remains unverified, and a failing target remains incompatible until corrected or dispositioned by the compatibility owner.

### WEB-RULE-08 — Keep evidence and authority explicit

**Applies to:** every completion, review, conformance, compatibility, security, performance, and release-readiness claim under this Domain.

- Trace each claim to the applicable requirement, tested scope, method, result, and evidence location. Keep failed, skipped, blocked, and unavailable checks visible.
- Distinguish implementation evidence from organizational approval. Passing checks do not authorize deployment, establish legal conformance, accept security risk, or change the Domain lifecycle.
- Never fabricate commands, results, browser coverage, accessibility observations, performance measurements, security findings, approvals, or reviewer dispositions.
- Record residual risks, affected users or systems, rollback or recovery needs, and the named receiving authority when known.

**Required evidence:** an evidence index tying requirements to results; executed procedures and actual outcomes; explicit exclusions and unavailable checks; residual-risk and recovery notes; and handoff status.

**Failure and handoff:** if a required check, tool, permission, environment, reviewer, or decision authority is unavailable, state exactly what is missing and the impact on the claim. Stop before unauthorized operational action and transfer the artifact plus evidence to the authorized owner. Silence or missing escalation does not constitute acceptance.

## Rule Precedence and Conflict Handling

When these rules conflict with a task contract, project overlay, or another Domain, apply the stricter authorized requirement unless it would cross an ownership boundary or weaken Kernel policy. Record the conflict, the affected rule and behavior, available evidence, and the authority required to resolve it. Do not choose silently, broaden permissions, or self-approve an exception.

## Source Basis

These rules use the validated `engineering.web` research ledger: HTML semantics [WEB-WHATWG-HTML-SEMANTICS], browser origins [WEB-WHATWG-HTML-ORIGINS], CSS specification maturity [WEB-W3C-CSS-2025], ECMAScript semantics [WEB-TC39-ECMA262], WCAG 2.2 [WEB-W3C-WCAG22], keyboard and focus guidance [WEB-W3C-ARIA-KEYBOARD], HTTP semantics [WEB-RFC9110-HTTP], Content Security Policy [WEB-W3C-CSP3], application-security verification guidance [WEB-OWASP-ASVS], browser performance instrumentation [WEB-W3C-PERFORMANCE-TIMELINE], and cross-browser testing practice [WEB-WPT-DOCS].
