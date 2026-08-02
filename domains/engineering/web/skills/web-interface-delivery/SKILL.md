---
name: web-interface-delivery
description: Deliver and verify framework-neutral browser interfaces with explicit semantics, states, boundaries, and reproducible evidence.
---

# Web Interface Delivery

Use this Skill to turn an authorized browser-interface task into a reviewable change and a
reproducible evidence handoff. It operationalizes `engineering.web` without choosing a framework,
toolchain, browser matrix, quality threshold, or release policy.

## Trigger Conditions

Invoke this Skill when the selected task includes one or more of the following:

- creating or changing a browser-delivered page, component, form, navigation surface, or custom
  interaction;
- implementing client-side state or behavior with ECMAScript or browser host APIs;
- integrating browser behavior with an HTTP service contract;
- correcting or reviewing semantic, responsive, keyboard, focus, security-boundary, performance,
  or cross-browser behavior; or
- preparing implementation and evidence for independent Web frontend evaluation.

Do not invoke it merely to define product intent, approve visual design, change backend behavior,
set organizational policy, deploy, accept risk, or issue a final evaluation verdict.

## Required Inputs

Before changing implementation, resolve these inputs from the task contract or authoritative
project overlay:

| Input | Usable evidence | Missing-input response |
| --- | --- | --- |
| Outcome | Observable expected behavior, material negative paths, and acceptance authority | Stop choices that depend on ambiguous product intent. |
| Interface specification | Approved structure, content, states, responsive behavior, and design authority | Do not invent interaction or visual decisions. |
| Execution boundary | Target surface, current revision, architecture boundary, authorized tools, commands, environments, permissions, and recovery procedure | Do not guess commands, install dependencies, or mutate outside granted scope. |
| Service contract | Methods, representations, fields, statuses, authentication context, cache behavior, and error semantics | Stop unsafe integration choices and hand the gap to the service owner. |
| Quality contract | Adopted accessibility target, browser/device/assistive-technology matrix, performance objectives, test expectations, and release blockers | Perform only supported baseline work; mark dependent claims `needs-org-input`. |
| Security and privacy contract | Origins, data and trust boundaries, approved verification scope, CSP policy when applicable, escalation route, and risk authority | Stop security-sensitive expansion rather than selecting policy. |
| Decision map | Product, design, service, accessibility, security/privacy, compatibility, performance, delivery, and release authorities applicable to the task | Record missing recipients; silence is not approval. |

If a missing organization fact does not prevent safe baseline work, continue only outside the
affected decision and record the exact claim it prevents. If proceeding would invent authority,
compatibility, security, accessibility, or release criteria, stop at that boundary.

## Workflow Mapping

This Skill executes `workflows/WORKFLOW.md` as a compact working loop rather than replacing it:

| Workflow stages | Skill operation |
| --- | --- |
| Entry gate and stage 1 | Establish the evidence spine and baseline. |
| Stages 2–5 | Design and implement the smallest authorized state model. |
| Stages 6–9 | Verify accessibility, trust boundaries, performance, and compatibility against declared targets. |
| Stage 10 | Reconcile claims, failures, recovery needs, and authority in the delivery packet. |

`rules/BASE.md` remains normative. `evaluators/EVALUATOR.md` defines independent acceptance; the
practitioner using this Skill must not self-score or issue the evaluator's verdict.

## Execution Procedure

### 1. Build the evidence spine

Create a working record bound to the task and current revision. For each acceptance criterion,
record:

1. the observable claim;
2. affected pages, components, document regions, states, requests, origins, and presentation
   contexts;
3. expected and material negative scenarios;
4. the authorized verification method and environment;
5. the evidence location; and
6. the authority required for disposition.

Keep confirmed inputs, assumptions, exclusions, existing failures, and unavailable checks visibly
separate. Capture a sanitized baseline before attributing behavior to the change. A check that could
not run is `unavailable` or `blocked`, not passing.

### 2. Expand requirements into an interface state matrix

Do not reason only from the nominal success screen. For each affected interaction, enumerate the
applicable states supplied by requirements and contracts:

| Dimension | Cases to consider when applicable |
| --- | --- |
| Data | initial, loading, empty, partial, complete, stale, invalid |
| Operation | idle, pending, succeeded, rejected, canceled, retried, repeated |
| Authority | unauthenticated, unauthorized, forbidden, expired context |
| Service | expected response, conflict, rate limit, transient failure, unavailable response |
| Presentation | declared viewport and media contexts, content expansion, fallback or degradation |
| Interaction | pointer, keyboard, focus entry/movement/restoration, dynamic update |

The task and service contracts determine applicability; do not manufacture endpoint behavior or
credentials to fill the matrix. Tie every retained state to required user feedback, permitted
actions, semantic structure, focus outcome, recovery behavior, and verification evidence.

### 3. Choose the smallest platform-shaped design

Start with native HTML elements and their defined content models. Introduce custom interaction only
when native semantics cannot satisfy accepted behavior, and record that reason
[WEB-WHATWG-HTML-SEMANTICS].

For each material CSS, ECMAScript, or browser host feature, write a short feature decision:

- required user behavior;
- relevant platform feature;
- whether the claim comes from language/specification semantics or host availability;
- declared targets that must support it;
- evidence method; and
- approved fallback or degradation behavior, if one exists.

Treat CSS specification maturity separately from browser implementation support
[WEB-W3C-CSS-2025]. Treat ECMAScript guarantees separately from browser host APIs
[WEB-TC39-ECMA262]. Do not silently add a dependency, polyfill, transpilation policy, or narrower
support matrix.

### 4. Implement by observable boundary

Keep implementation reviewable in this order:

1. semantic document structure and native controls;
2. presentation and responsive behavior that preserve required content and operation;
3. deterministic client state transitions, including interruption, repetition, stale results, and
   recovery where applicable;
4. HTTP behavior tied to the authoritative contract; and
5. origin, untrusted-content, executable-content, authentication, storage, and data-flow controls.

At the HTTP boundary, retain sanitized evidence for applicable representations, fields, statuses,
authentication assumptions, caching, cancellation, retry, and recovery. Do not infer undocumented
meaning from one observed response or present client checks as server authorization, validation,
integrity, or persistence controls [WEB-RFC9110-HTTP].

Treat distinct origins as potentially hostile unless the approved model says otherwise
[WEB-WHATWG-HTML-ORIGINS]. Apply context-appropriate safe handling for untrusted content. When CSP
is in scope, distinguish report-only observation from enforcement and treat CSP as defense in depth,
not a replacement for validation or output encoding [WEB-W3C-CSP3]. ASVS may organize the approved
verification scope but does not select a local level or authorize risk acceptance [WEB-OWASP-ASVS].

### 5. Run layered verification

Use only project-supplied commands and authorized environments. Start with the narrowest checks that
exercise the changed boundary, remediate within scope, and then run the project-defined broader set.
Record the exact procedure and actual result each time; reruns do not erase earlier failures.

Apply these layers where relevant:

- **Structure and behavior:** inspect markup or the rendered tree and exercise every retained state;
  visual resemblance is not semantic evidence.
- **Accessibility:** test the complete affected page or flow against the adopted target, including
  responsive variants. Exercise every interactive function by keyboard and record visible focus,
  entry, movement, loss or trapping, restoration, errors, and dynamic updates. Custom widgets need
  an intentional keyboard model; ARIA alone does not provide behavior
  [WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD].
- **Service integration:** verify applicable expected and negative response paths against the service
  contract, preserving sanitized mismatches [WEB-RFC9110-HTTP].
- **Security and privacy:** exercise only scenarios in the approved verification scope, retain no
  credentials or protected payloads, and never weaken policy to make a check pass
  [WEB-WHATWG-HTML-ORIGINS] [WEB-W3C-CSP3] [WEB-OWASP-ASVS].
- **Performance:** define the claim, scenario, environment, method, and approved objective before
  judging it. Retain relevant navigation, resource, or application-defined Performance Timeline
  measurements, raw results, comparison basis, variability, and limitations
  [WEB-W3C-PERFORMANCE-TIMELINE].
- **Compatibility:** run portable browser-facing scenarios across every applicable declared target.
  Retain per-target identifiers and results plus rendering or interaction evidence when assertions
  are insufficient; distinguish harness instability from implementation incompatibility
  [WEB-WPT-DOCS].

An automated scan, simulated DOM, unit suite, single browser, or component-only result supports only
the scope it actually exercised. It does not establish a full-experience or matrix-wide claim.

### 6. Reconcile the delivery packet

Before handoff, reconcile the implementation, requirements, and evidence. The packet must contain:

- task, revision, scope, environment, changed-surface inventory, assumptions, and exclusions;
- requirement-to-implementation-to-evidence index;
- exact procedures executed and results labeled `passed`, `failed`, `skipped`, `unavailable`, or
  `blocked`;
- expected and negative-path evidence, including browser or assistive-technology target identifiers
  where applicable;
- existing failures, new failures, conflicting or flaky results, limitations, and sanitized raw or
  linked artifacts;
- unresolved decisions, residual risks, affected users or systems, and receiving authorities; and
- the smallest recoverable unit plus the organization-approved recovery reference, or
  `needs-org-input` when no procedure is supplied.

Distinguish source reversal, feature disablement, client-state recovery, build-artifact replacement,
and operational rollback only when authoritative project evidence establishes that they apply. The
handoff may support independent review; it does not grant deployment, release, exception, conformance,
risk-acceptance, or lifecycle authority.

## Evidence Quality Rules

- Bind evidence to the evaluated revision, configuration, target, environment, scenario, and method.
- Reuse prior evidence only when the record shows that no material implementation, input,
  configuration, target, contract, policy, objective, or environment changed.
- Preserve every contradictory current result. Explain the cause and disposition or leave the claim
  failed or unverified; do not select only a favorable rerun.
- Sanitize request, response, console, report, screenshot, and measurement artifacts before storage
  or handoff.
- Do not claim properties that were not exercised, and do not turn missing evidence into an assumed
  pass.

## Stop and Escalation Conditions

Stop the affected action and preserve non-sensitive evidence when:

- product, content, or interaction intent has competing interpretations;
- the service contract contradicts observed behavior and safe client behavior cannot be determined;
- a required tool, command, target, environment, dependency decision, or permission is unverified;
- a required host feature has no verified support or approved fallback for a declared target;
- semantic, keyboard, focus, responsive, required-state, or compatibility behavior remains failed;
- an origin, injection, executable-content, authentication, credential, policy, or protected-data
  concern appears;
- an adopted performance objective is missed or the measurement is too unstable to support a claim;
- work would require changing policy, narrowing a matrix, approving an exception, accepting risk,
  accessing production, deploying, releasing, or executing rollback without explicit authority; or
- Kernel, Domain, overlay, and task requirements conflict and the stricter authorized behavior cannot
  be determined without crossing an ownership boundary.

Escalate with the decision requested, affected requirement and surface, available options, user or
system impact, sanitized reproduction evidence, and the accountable authority when known. Use
`needs-org-input` for a missing organization-owned target, matrix, threshold, policy, reviewer,
command, architecture fact, or authority, and name the claim that remains unavailable.

## Organization and Project Overlay Boundary

This Skill supplies reusable professional technique only. The organization or project overlay must
supply repository paths, rendering architecture, framework and design-system conventions, package
and dependency policy, tools and exact commands, permissions, service and authentication topology,
supported language target, browser/device/assistive-technology matrix, localization contexts,
accessibility target, performance objectives, coverage and release thresholds, threat model, ASVS
scope, CSP rollout policy, evidence format, reviewers, deployment procedure, and recovery procedure.

An overlay may specialize or strengthen this Skill. It must not weaken Kernel or Domain rules, invent
authority, or convert missing organization facts into reusable defaults. Record unresolved conflicts
and route them to the relevant owner.

## Source Basis

Source IDs resolve through the validated `engineering.web` research ledger:

- HTML semantics and browser origins: [WEB-WHATWG-HTML-SEMANTICS]
  [WEB-WHATWG-HTML-ORIGINS]
- CSS maturity and ECMAScript semantics: [WEB-W3C-CSS-2025] [WEB-TC39-ECMA262]
- accessibility, keyboard, and focus: [WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD]
- HTTP semantics: [WEB-RFC9110-HTTP]
- CSP and application-security verification: [WEB-W3C-CSP3] [WEB-OWASP-ASVS]
- browser performance instrumentation: [WEB-W3C-PERFORMANCE-TIMELINE]
- cross-browser testing practice: [WEB-WPT-DOCS]

The registered Domain identity and ownership are grounded in [REPO-WEB-DOMAIN-IDENTITY].
