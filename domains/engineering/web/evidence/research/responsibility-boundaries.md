# Responsibility Boundaries

## In scope for the professional baseline

Web Frontend Engineering may own the reusable practice and evaluation methods for:

- Semantic document structure, browser-facing interaction, and presentation grounded in HTML and CSS standards [WEB-WHATWG-HTML-SEMANTICS] [WEB-W3C-CSS-2025].
- ECMAScript application behavior and the boundary between the language and browser-supplied host APIs [WEB-TC39-ECMA262].
- Accessibility implementation and evidence against an explicitly adopted WCAG target, including keyboard and focus behavior for custom interactive components [WEB-W3C-WCAG22] [WEB-W3C-ARIA-KEYBOARD].
- Correct client-side use of HTTP semantics and reproducible frontend-to-service integration evidence [WEB-RFC9110-HTTP].
- Browser-origin-aware implementation, frontend security verification, and defense-in-depth CSP design and observation [WEB-WHATWG-HTML-ORIGINS] [WEB-W3C-CSP3] [WEB-OWASP-ASVS].
- Browser performance instrumentation and evidence collection [WEB-W3C-PERFORMANCE-TIMELINE].
- Portable browser-facing interoperability and rendering tests [WEB-WPT-DOCS].

## Shared boundaries

### Product and design

Frontend engineering may evaluate feasibility, interaction behavior, responsiveness, accessibility, and implementation consistency. Product owners retain authority over product intent, prioritization, content policy, and acceptance of user-experience tradeoffs. Design owners retain authority over approved visual and interaction specifications unless organization policy delegates otherwise.

### Backend and platform services

Frontend engineering owns correct client behavior at the HTTP boundary and collaborates on interface contracts [WEB-RFC9110-HTTP]. Backend or service owners remain accountable for server implementation, authorization enforcement, persistence, data integrity, service availability, and server-side observability.

### Security and privacy

Frontend engineering implements and verifies client-side controls, understands origin isolation, and can supply ASVS- or CSP-aligned evidence [WEB-WHATWG-HTML-ORIGINS] [WEB-W3C-CSP3] [WEB-OWASP-ASVS]. Security and privacy authorities retain threat-model approval, control selection, exceptions, incident decisions, compliance interpretation, and residual-risk acceptance. CSP is defense in depth, not a replacement for validation and encoding [WEB-W3C-CSP3].

### Accessibility and legal conformance

Frontend engineering can implement and test WCAG-backed behavior [WEB-W3C-WCAG22] and accessible keyboard interaction [WEB-W3C-ARIA-KEYBOARD]. The organization must identify the required conformance level, applicable laws or contractual duties, supported assistive technologies, exception authority, and final approvers; the Domain must not infer them.

### Performance and reliability

Frontend engineering owns browser-side instrumentation and analysis within the adopted scope [WEB-W3C-PERFORMANCE-TIMELINE]. Product, service, site-reliability, and platform owners share responsibility for end-to-end objectives affected by networks, servers, delivery infrastructure, third parties, and business tradeoffs. Numeric budgets and release gates require organization approval.

### Delivery infrastructure

Frontend engineering may define build artifacts and requirements for browser delivery, but it does not implicitly own DNS, CDN, certificates, hosting, CI administration, deployment credentials, production access, or rollback authority. Those permissions and operational owners must be supplied by organization evidence.

## Explicitly out of scope without organization evidence

The draft professional baseline does not authorize production changes, deployment, dependency adoption, access changes, security exceptions, accessibility exceptions, legal claims, risk acceptance, or release approval. It also does not invent a framework, design system, package manager, browser matrix, internal architecture, quality threshold, command, reviewer, or approval workflow. The registered owner `platform-web` is an identity fact only [REPO-WEB-DOMAIN-IDENTITY].

## Activation boundary

Before activation, organization evidence must resolve reviewers and decision rights, permissions, internal standards, private architecture, product commands, approval evidence, browser and assistive-technology coverage, quality targets, and the security baseline. Public standards support the professional content, but they do not establish local authority or prove that the pack is ready for organizational use.
