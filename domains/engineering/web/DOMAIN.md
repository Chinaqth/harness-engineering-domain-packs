# Web Frontend Engineering

## Purpose

`engineering.web` owns the reusable professional practice for designing, implementing, and evaluating browser-delivered user interfaces. Its baseline covers standards-based document structure and presentation, ECMAScript application behavior, accessibility, client-side HTTP integration, frontend security, browser performance measurement, and cross-browser verification. It turns declared product and interface requirements into reviewable implementation artifacts and reproducible evidence without selecting an organization-specific framework, architecture, toolchain, or release policy.

The Domain is registered as **Web Frontend Engineering**, version `0.1.0`, with lifecycle status `active` and `platform-web` as owner and reviewer [REPO-WEB-DOMAIN-IDENTITY]. Activation establishes routing eligibility only; it does not grant operational permissions.

## Ownership and Decision Boundaries

The `platform-web` owner and reviewer is accountable for maintaining the professional baseline, resolving contradictions within it, and governing lifecycle review. Project- and task-specific authorities remain separate and must be named by the applicable overlay or task contract.

Within an authorized task contract, this Domain may make and evaluate frontend implementation decisions that preserve HTML semantics and content models [WEB-WHATWG-HTML-SEMANTICS], apply appropriately mature CSS capabilities [WEB-W3C-CSS-2025], use ECMAScript language semantics correctly [WEB-TC39-ECMA262], and produce evidence for the other practices defined below. It does not acquire authority over product intent, visual approval, legal conformance, privacy decisions, residual-risk acceptance, backend behavior, deployment, or production operations.

Shared decisions are handed to the accountable organizational authority:

- Product owners decide product intent, prioritization, content policy, and acceptance of product tradeoffs.
- Design owners approve visual and interaction specifications unless documented organizational policy delegates that authority.
- Service owners remain accountable for server implementation, authorization enforcement, persistence, data integrity, availability, and server-side observability; this Domain owns correct client behavior at the HTTP boundary [WEB-RFC9110-HTTP].
- Security, privacy, legal, and accessibility authorities decide applicable obligations, exceptions, control selection, incident response, and residual-risk acceptance.
- Platform, delivery, and reliability owners control CI administration, hosting, DNS, CDN, certificates, production credentials, deployment, rollback, and end-to-end reliability objectives unless explicit evidence delegates a narrower responsibility.

## In Scope

The reusable professional baseline includes:

- Structuring web documents, metadata, content, forms, and interactive elements according to defined HTML meanings and content-model constraints [WEB-WHATWG-HTML-SEMANTICS].
- Applying CSS for rendering across relevant media while distinguishing stable specifications from features with less implementation experience, and verifying adoption against the declared compatibility target [WEB-W3C-CSS-2025].
- Implementing browser application logic according to ECMAScript syntax and semantics while distinguishing language guarantees from browser host APIs [WEB-TC39-ECMA262].
- Translating an explicitly adopted accessibility target into testable page and component behavior. This includes full-page and responsive-variation evidence, keyboard operability, visible and predictable focus, and intentional focus management for custom widgets [WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD].
- Implementing and verifying client-side request, response, representation, status, field, authentication, and cache behavior against shared HTTP semantics [WEB-RFC9110-HTTP].
- Respecting browser origin boundaries, applying secure frontend development requirements, and designing defense-in-depth controls such as monitored and enforced Content Security Policy. CSP supplements rather than replaces validation and output encoding [WEB-WHATWG-HTML-ORIGINS] [WEB-W3C-CSP3] [WEB-OWASP-ASVS].
- Instrumenting and retrieving navigation, resource, and application-defined browser performance measurements [WEB-W3C-PERFORMANCE-TIMELINE].
- Creating portable browser-facing tests and rendering checks that produce interoperability evidence across a declared browser matrix [WEB-WPT-DOCS].
- Recording assumptions, limitations, failed checks, unresolved risks, and handoffs so another qualified contributor can reproduce the result.

## Out of Scope

This Domain does not, without explicit organization evidence and task authorization:

- define product requirements, approve content or design, or accept user-experience tradeoffs;
- implement or approve backend services, persistence, server authorization, data governance, or service availability;
- interpret law or policy, declare legal or accessibility conformance, approve exceptions, or accept privacy or security risk;
- select or mandate a framework, design system, package manager, state-management approach, rendering architecture, supported language target, dependency, or internal coding convention;
- invent a browser, device, assistive-technology, localization, or degradation matrix;
- set numeric performance budgets, coverage thresholds, vulnerability thresholds, or release gates;
- assume repository, dependency, deployment, production, policy-configuration, rollback, or access-management permissions; or
- operate DNS, CDN, certificates, hosting, CI infrastructure, production environments, or incident response.

## Stable Inputs

Work begins only when the task contract supplies or explicitly identifies the applicable inputs. Unknown organization facts remain blockers or recorded gaps rather than inferred defaults.

| Input | Minimum usable form |
| --- | --- |
| Desired outcome and acceptance criteria | Observable user or system behavior, relevant negative paths, and the authority that accepts the outcome |
| Interface and content specification | Approved structure, interaction states, responsive behavior, content, assets, and unresolved design decisions |
| Execution context | Target application surface, relevant architecture and integration boundaries, and constraints supplied by an authoritative project source |
| Service contract | Expected HTTP methods, representations, fields, status behavior, authentication context, cache behavior, and error semantics [WEB-RFC9110-HTTP] |
| Quality targets | Adopted accessibility target, supported browser/device/assistive-technology matrix, performance objectives, test expectations, and release-blocking criteria |
| Security and privacy constraints | Approved threat model or verification scope, origin and trust boundaries, CSP policy, data-handling constraints, escalation path, and risk authority |
| Authorized tool and command contract | Verified repository commands, available tools, granted permissions, target environments, and rollback or recovery procedure |
| Handoff map | Named owners or roles for product, design, service, accessibility, security, privacy, delivery, and release decisions needed by the task |

If an input is absent but does not prevent safe baseline work, the output must identify the assumption and affected evidence. If its absence would require inventing authority, compatibility, security, accessibility, or release criteria, work stops at the affected decision and is handed off.

## Evidence-Bearing Outputs

An output is complete only when it is traceable to inputs and accompanied by enough evidence for an independent reviewer to reproduce the claim.

| Output | Required evidence |
| --- | --- |
| Frontend implementation or implementation plan | Traceability to accepted behavior; identified HTML, CSS, ECMAScript, and host-API choices; changed-surface inventory; and reviewable artifacts or diffs |
| Semantic and visual behavior record | Inspection or test evidence for document structure, interaction states, responsive behavior, relevant presentation contexts, and known fallbacks [WEB-WHATWG-HTML-SEMANTICS] [WEB-W3C-CSS-2025] |
| Accessibility evidence | Adopted target and tested scope; page and component results; keyboard and focus observations for custom interaction; responsive variations; failures, exceptions, and reviewer handoff [WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD] |
| Service-integration evidence | Exercised request and response cases, representations and status handling, authentication and cache assumptions, error and recovery paths, and unresolved service-contract mismatches [WEB-RFC9110-HTTP] |
| Security evidence | Origin and trust-boundary assumptions, applicable verification requirements and results, injection-defense observations, CSP report-only or enforcement evidence when applicable, unresolved findings, and risk-owner handoff [WEB-WHATWG-HTML-ORIGINS] [WEB-W3C-CSP3] [WEB-OWASP-ASVS] |
| Performance evidence | Measurement method and environment, navigation/resource/application-defined observations, raw or linked results, comparison basis, variability and limitations, and disposition against organization-approved objectives [WEB-W3C-PERFORMANCE-TIMELINE] |
| Compatibility evidence | Declared matrix, portable tests or equivalent reproducible scenarios, per-target results, rendering evidence where behavior is visual, failures, degradation decisions, and flake or rerun notes [WEB-WPT-DOCS] |
| Delivery handoff | Acceptance status, commands or procedures actually executed, pass/fail evidence, residual risks, blocked decisions, rollback guidance, and named receiving authority |

Passing automated checks is not by itself proof of semantic correctness, accessible behavior, security acceptability, performance suitability, or release readiness. Failed and unavailable checks remain visible in the handoff.

## Handoffs

Handoffs are explicit control points, not implied approval:

1. Product and design ambiguities are returned with the observable decision needed, affected states, and implementation impact.
2. Service-contract mismatches are sent to the service owner with reproducible HTTP evidence and the client behavior that cannot be safely determined.
3. Accessibility uncertainties or exceptions are sent to the designated accessibility and legal authorities with the adopted target, affected pages or components, user impact, and test evidence.
4. Security, privacy, origin, CSP, vulnerability, or data-handling findings are sent to the authorized security or privacy owner with reproduction evidence and without self-approving risk.
5. Performance or compatibility shortfalls are sent to the owners of the approved objectives or matrix with the measurement context, variance, affected users, and candidate tradeoffs.
6. Deployment, production access, release, rollback, or infrastructure work is transferred to the explicitly authorized delivery owner with verified build artifacts, validation evidence, known risks, and recovery requirements.

The receiving authority and its disposition must be recorded when known. Silence, missing reviewers, or an absent escalation path does not constitute acceptance.

## Failure Modes and Required Response

| Failure mode | Required response |
| --- | --- |
| Requirements or acceptance criteria are ambiguous | Stop the affected decision; enumerate the ambiguity, feasible interpretations, user-visible impact, and required decision owner. |
| Repository command, tool, permission, or environment is unverified | Do not guess or claim execution; record the missing authority or compatibility fact and request an authoritative source. |
| Implementation violates HTML, CSS, ECMAScript, or HTTP semantics | Preserve failing evidence, identify affected behavior, correct within authorization, and rerun the narrow relevant checks. |
| Keyboard, focus, responsive, or other accessibility behavior fails | Treat the result as unresolved against the adopted target; record scope and user impact, remediate when authorized, and escalate exceptions rather than self-approving them. |
| Origin, injection, CSP, authentication, or sensitive-data concern is found | Stop unsafe expansion, preserve evidence without exposing secrets, and hand off to the authorized security or privacy owner; do not treat CSP as a substitute for validation or encoding [WEB-W3C-CSP3]. |
| Service behavior contradicts the declared HTTP contract | Capture the request/response evidence, avoid silently normalizing the mismatch, and coordinate contract ownership before relying on undocumented behavior. |
| Performance result is unstable or misses an approved objective | Retain raw results and environmental context, distinguish measurement noise from a reproducible regression, and escalate any threshold or business tradeoff. |
| Browser result is inconsistent or flaky | Record each target and rerun outcome, isolate test instability from implementation incompatibility, and do not narrow the supported matrix without approval. |
| Automated evidence is unavailable or incomplete | State exactly what did not run and why, provide any safe manual evidence, and avoid claiming the unverified property. |
| Release, deployment, or rollback authority is absent | Stop before the operational action and transfer the verified artifact and evidence to an authorized owner. |

## Maturity and Task-Level Organization Inputs

This Domain is an active source-supported professional baseline at version `0.1.0`. The following organization and project inputs remain mandatory for every dependent task claim or action:

- required engineering, accessibility, security, design, product, and release reviewers, including their decision rights;
- permissions for repository and dependency changes, deployment, production access, rollback, and policy configuration;
- internal coding standards, framework and design-system conventions, dependency policies, supported language targets, and documentation requirements;
- private rendering and application architecture, API and authentication topology, state-management approach, hosting topology, and observability stack;
- authoritative commands for installation, development, linting, type checking, testing, building, security and accessibility checks, preview, deployment, and rollback;
- required approval records and evidence formats for activation and production-facing work;
- supported browsers, versions, devices, assistive technologies, localization contexts, and degradation policy;
- the adopted WCAG conformance level, performance objectives and budgets, interoperability and coverage thresholds, and release-blocking criteria; and
- the approved threat model, ASVS scope or verification level, CSP rollout policy, vulnerability thresholds, incident escalation path, and risk-acceptance authority.

Activation evidence is stored under `changes/engineering.web-activation/`. Nothing in this contract supplies project-specific facts or operational approvals; missing inputs remain `needs-org-input` for the affected task and must fail closed.

## Source Basis

This contract is grounded in the registered Domain identity [REPO-WEB-DOMAIN-IDENTITY], the HTML semantics and browser-origin standards [WEB-WHATWG-HTML-SEMANTICS] [WEB-WHATWG-HTML-ORIGINS], the CSS stable-specification snapshot [WEB-W3C-CSS-2025], ECMAScript language specification [WEB-TC39-ECMA262], WCAG 2.2 and keyboard-interface guidance [WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD], HTTP semantics [WEB-RFC9110-HTTP], CSP and application-security verification guidance [WEB-W3C-CSP3] [WEB-OWASP-ASVS], the browser Performance Timeline [WEB-W3C-PERFORMANCE-TIMELINE], and the cross-browser web-platform-tests practice [WEB-WPT-DOCS]. Source IDs resolve through the validated research ledger for this Domain completion change.
