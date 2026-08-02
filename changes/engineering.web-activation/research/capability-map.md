# Capability Map

## Identity

`engineering.web` is registered as **Web Frontend Engineering**, version `0.1.0`, status `active`, with `platform-web` as owner and reviewer. Its registered purpose is reusable Web frontend engineering delivery practice and evaluation [REPO-WEB-DOMAIN-IDENTITY]. Activation establishes routing eligibility but does not grant operational permissions.

## Source-supported capability hypotheses

### Standards-based web UI

Author and evaluate document structure with the semantics and content models defined by HTML, then apply CSS capabilities with explicit attention to specification maturity and the eventual organization-supported browser matrix [WEB-WHATWG-HTML-SEMANTICS] [WEB-W3C-CSS-2025]. This capability covers semantic markup, document metadata, forms and interaction structure, presentation, responsive behavior, cascade, layout, typography, and user-interface styling. It does not select a framework or design system.

### ECMAScript application behavior

Implement browser application logic using the ECMAScript language contract while distinguishing language semantics from APIs supplied by the browser host environment [WEB-TC39-ECMA262] [WEB-WHATWG-HTML-SEMANTICS]. Evaluation should cover observable behavior and failure handling without assuming a repository-specific compiler, package manager, framework, or state-management library.

### Accessibility engineering

Translate an organization-adopted accessibility target into testable page and component behavior. WCAG 2.2 supplies technology-independent success criteria and full-page conformance rules, including responsive variations [WEB-W3C-WCAG22]. Custom interactive components also require intentional keyboard operation, predictable focus movement, visible focus, and appropriate focus-management techniques [WEB-W3C-ARIA-KEYBOARD]. The public baseline supports evaluation, but the organization must still declare its required conformance level, browser and assistive-technology matrix, exemptions, reviewers, and approval evidence.

### HTTP integration

Design and verify frontend request, response, status, representation, field, authentication, and cache behavior against shared HTTP semantics [WEB-RFC9110-HTTP]. This capability owns correct client-side use and observable integration evidence; it does not own backend implementation, data integrity inside services, service availability, or API product policy.

### Frontend security

Respect browser-origin isolation and treat cross-origin actors as potentially hostile [WEB-WHATWG-HTML-ORIGINS]. Apply secure-development verification and defense-in-depth controls such as CSP, including report-only observation before enforcement when appropriate [WEB-W3C-CSP3] [WEB-OWASP-ASVS]. CSP is not a substitute for input validation or output encoding [WEB-W3C-CSP3], and this Domain does not grant itself security risk-acceptance authority.

### Performance observability

Instrument and retrieve navigation, resource, and application-defined performance measurements using the web Performance Timeline [WEB-W3C-PERFORMANCE-TIMELINE]. The capability can produce reproducible evidence and diagnose frontend contributions, but numeric objectives, budgets, representative environments, and release thresholds remain organization decisions.

### Cross-browser verification

Create portable browser-facing tests and rendering checks that can run across implementations, using the cross-browser web-platform-tests model as a professional baseline [WEB-WPT-DOCS]. The supported browser and device matrix, test commands, required coverage, flake policy, and release-blocking thresholds must come from organization evidence.

## Capability relationships

Semantic HTML and CSS form the presentation foundation; ECMAScript adds application behavior; accessibility and security constrain both structure and behavior; HTTP semantics govern service interaction; performance instrumentation measures runtime characteristics; and cross-browser verification supplies compatibility evidence. These are capability hypotheses supported by public professional sources, not activated internal policy.

## Activation dependencies

The `platform-web` owner/reviewer approved activation in `changes/engineering.web-activation/activation-evidence.json`. Project permissions, standards, private architecture, executable commands, browser and assistive-technology matrices, quality targets, and security baselines remain mandatory project-overlay or task-contract inputs. Missing inputs block dependent claims and actions; activation does not supply or bypass them.
