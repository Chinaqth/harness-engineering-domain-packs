# HarmonyOS Engineering Rules

## Authority and Applicability

These rules apply when `engineering.harmonyos` designs, implements, migrates, reviews, diagnoses,
builds, or verifies HarmonyOS applications, ArkTS code, ArkUI interfaces, Stage-model components,
or HAP, HAR, HSP, and App Pack boundaries. They supplement, but do not weaken, Kernel security,
privacy, authorization, approval, evidence, and lifecycle requirements.

Work must remain within an authorized task contract. Organization-specific architecture,
supported-version matrices, commands, quality thresholds, signing policy, device access, and
release authority belong in a project overlay or task contract. When one is absent, the
practitioner may perform only safe, source-supported baseline work and must mark the affected
decision or verification `needs-org-input` rather than inventing it.

## Professional Invariants

### HMOS-RULE-01 — Declare the version and toolchain baseline

**Applies to:** every version-sensitive architecture, implementation, migration, compatibility,
build, test, packaging, and documentation claim.

- Record the compile SDK, compatible or minimum API level, relevant HarmonyOS release, build
  toolchain version, target device or form factor, and compatibility targets supplied by the
  project before making a version-sensitive claim.
- Distinguish required project facts from values merely observed in a local environment. Do not
  silently replace a project baseline with the newest installed SDK or a version mentioned in a
  cached example.
- If a material baseline fact is missing or contradictory, stop the affected recommendation or
  change. Continue only work whose correctness does not depend on that fact.

**Required evidence:** the declared baseline and its source; relevant project configuration;
observed toolchain versions; target matrix; unresolved conflicts; and the decisions whose validity
depends on each value.

**Failure and handoff:** an unknown or inconsistent baseline makes version-sensitive behavior
unverified. Preserve the conflicting evidence and request a decision from the platform or project
owner; do not guess a compatible target.

### HMOS-RULE-02 — Resolve platform facts from current authoritative documentation

**Applies to:** ArkTS syntax and semantics, ArkUI APIs and decorators, Stage-model lifecycle,
package semantics, compatibility, migration, testing, and tool behavior.

- Prefer version-relevant current Huawei Developer documentation over bundled reference corpora,
  generated snippets, local indexes, Skill text, remembered APIs, and search summaries
  [HMOS-ARKTS] [HMOS-STAGE] [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]
  [HMOS-PACKAGES] [HMOS-TESTING].
- Use `devecocli docs` when that interface is available and authorized to retrieve relevant
  documentation. Record the query, returned document location, applicable version, retrieval
  context, and why the result answers the question.
- Reconcile a cached reference with current authoritative documentation and observed compiler or
  test behavior before relying on it. Preserve and report unresolved disagreement.
- Never present a generated example or documentation lookup as compilation, runtime, device, or
  compatibility evidence.

**Required evidence:** source ID or authoritative document location; relevant version and retrieval
context; the claim supported; conflicting local material; and any independent compilation or test
that exercised the advice.

**Failure and handoff:** if the applicable primary documentation cannot be retrieved or does not
establish the needed signature or behavior, mark the claim unverified and stop the dependent
change. Hand off the exact question and attempted retrieval path rather than inventing an API.

### HMOS-RULE-03 — Preserve the supplied application architecture

**Applies to:** Stage components, lifecycle, context, windows, navigation, pages, state ownership,
modules, packages, processes, threads, concurrency, and service integration.

- Inventory the existing conventions and affected boundaries before editing. Preserve them unless
  the task contract explicitly authorizes an architecture change [HMOS-STAGE].
- Use `UIAbility` for user-facing components and only the documented system-defined
  `ExtensionAbility` derivative appropriate to an extension scenario; account for lifecycle,
  context, process, thread, configuration, and ArkUI integration [HMOS-STAGE].
- Select HAP, HAR, and HSP boundaries from their documented installation, runtime, publication,
  and reuse semantics, not from filename convenience [HMOS-PACKAGES].
- Do not invent private topology, navigation, storage, authentication, data contracts, shared
  package policy, or concurrency rules.

**Required evidence:** affected-boundary inventory; current conventions; architecture decision and
alternatives; lifecycle and concurrency implications; package implications when applicable; source
references; and explicitly unchanged boundaries.

**Failure and handoff:** if the requested change would alter an unapproved architecture boundary,
stop that portion and hand the decision to the named architecture or platform owner. Restore or
isolate accidental topology changes and retain the diff and impact analysis.

### HMOS-RULE-04 — Treat deprecated-interface repair as a compatibility decision

**Applies to:** deprecated, removed, incompatible, or invalid ArkTS, ArkUI, SDK, and system API use.

- Establish the declared baseline and obtain the actual diagnostic or documented compatibility
  finding before changing an interface.
- Do not run `devecocli check compat` as a default or final delivery gate. Run it only when the
  task contract or user explicitly requires compatibility evidence and the interface is available
  and authorized. Treat its output as observed diagnostic evidence for the exercised project and
  environment, not as a universal compatibility guarantee.
- Map every finding to its location, affected behavior, authoritative replacement evidence, and
  disposition. Verify the replacement against the declared baseline.
- Do not perform blind name substitution, signature guessing, bulk deletion, or behavior-changing
  replacement. A deprecated API with no verified replacement remains unresolved.

**Required evidence:** baseline; exact findings and locations; source-supported replacement or
documented absence; before-and-after behavior expectations; patch mapping; rerun results; and
remaining findings.

**Failure and handoff:** when no safe replacement is established, leave or revert the affected code
as appropriate, record compatibility and user impact, and obtain an owner decision. Do not suppress
the diagnostic or silently narrow supported targets.

### HMOS-RULE-05 — Require ArkUI State Management V2 and migrate V1 by behavior

**Applies to:** ArkUI state-management V1/V2 use, especially `Observed`, `ObjectLink`, `Track`,
`ObservedV2`, and `Trace`.

- Use State Management V2 for every new HarmonyOS project architecture, newly authored ArkUI
  component, and rewritten state-managed surface. State Management V1 is legacy migration input,
  not an allowed target architecture. Do not introduce new V1 components, decorators, storage, or
  observation mechanisms, including `@Component`, `@State`, `@Prop`, `@Link`, `@Observed`,
  `@ObjectLink`, `@Provide`, `@Consume`, or `@Watch`.
- Confirm that the declared SDK/API baseline supports the required V2 behavior before design or
  implementation. If it does not, stop the affected work and hand the architecture decision to the
  project or platform owner; do not fall back to V1 silently.
- Inventory state ownership, initialization, read/write paths, nested-object observation,
  component boundaries, lifecycle, and expected refresh behavior before migration.
- Apply the scenario-specific Huawei migration guidance. `ObservedV2` and `Trace` behavior, nested
  observation, and V1/V2 mixing constraints are version-sensitive [HMOS-ARKUI-V2]
  [HMOS-ARKUI-MIGRATION].
- Map each original behavior to an intended V2 behavior and migrate in bounded, reversible batches.
  Do not treat a textual decorator replacement as evidence of preserved data flow or rendering.
- When authorized work touches an existing V1 surface, route it through the V1-to-V2 migration
  procedure. If the required migration exceeds the authorized scope, retain the smallest unchanged
  legacy boundary, introduce no additional V1 usage, and record the migration handoff.
- Do not introduce a mixed V1/V2 boundary unless its compatibility is established for the declared
  baseline and its behavior is explicitly verified.

**Required evidence:** state and data-flow inventory; migration mapping; applicable primary
guidance; batch boundaries; compile results; behavioral tests or observations for reads, writes,
nested changes, and refresh; and any intentional mixed-mode boundary.

**Failure and handoff:** on changed observation, stale UI, excess refresh, initialization failure,
or an unsupported decorator boundary, stop the batch and revert or isolate it. Preserve the
reproduction and hand unresolved design questions to the ArkUI or architecture owner. Newly
introduced V1 state management is a policy failure; an unsupported V2 baseline is a blocker, not
permission to generate V1 code.

### HMOS-RULE-06 — Use tools through verified, bounded interfaces

**Applies to:** documentation retrieval, linting, compatibility analysis, building, packaging, and
automated repair.

- Confirm that `devecocli` and the required subcommand are installed, authorized, and applicable to
  the detected project before invocation. Supported Domain interfaces are `devecocli docs`,
  `devecocli check lint`, `devecocli check compat`, and `devecocli build` when available.
- Resolve exact project and module scope from project facts. Do not invent flags, targets,
  profiles, output paths, or substitute commands from a cached Skill.
- Record the exact invocation, working scope, relevant environment and versions, exit status, and
  raw or linked diagnostics. A zero exit status proves only the check actually performed.
- Bound automated repair attempts. Never weaken checks, delete tests, broaden ignore rules, or
  mutate unrelated files to obtain a passing result.

**Required evidence:** availability and authorization check; command interface and resolved scope;
tool and SDK versions; actual invocation; exit status and output location; changed-file inventory;
retry count; and checks not run.

**Failure and handoff:** fail closed when the tool, subcommand, permission, project fact, or required
environment is missing. Report the exact limitation and a reproducible manual or owner handoff;
never fabricate an execution or passing result.

### HMOS-RULE-07 — Separate static, build, runtime, device, signing, and release evidence

**Applies to:** every correctness, quality, compatibility, package, deployment, and readiness
claim.

- Use `devecocli build` as the only default final compilation gate when available and authorized.
  Do not run `devecocli check lint` or `devecocli check compat` by default and do not make either a
  prerequisite for the default final compilation result. Run them only when the task contract or
  user explicitly requires their distinct evidence. Project-defined tests and inspections remain
  conditional on explicit task requirements and authorization [HMOS-TESTING].
- Report lint success, compatibility results, compilation, build, unit tests, coverage,
  self-inspection, emulator behavior, physical-device behavior, packaging, signing, and release
  authorization as distinct evidence classes.
- Record lint and compatibility checks omitted under the default gate as `skipped`, never as
  `passed`. A successful build establishes only the configured compilation and artifact outcome.
- Exercise material expected and negative paths on the declared targets. A passing lint or build
  does not prove runtime behavior, compatibility, accessibility, security, performance, power,
  package installability, signature validity, or release readiness.
- Do not access signing material, devices, protected data, distribution services, or production
  operations without explicit permission.

**Required evidence:** acceptance criterion to check mapping; exact executed checks and outcomes;
environment and target identity; applicable test, coverage, self-inspection, emulator, and device
artifacts; skipped or blocked checks; signing and release authority status; and residual risks.

**Failure and handoff:** a missing tool, permission, signing asset, emulator, device, account, or
release authority leaves the corresponding claim unverified. Stop before bypassing the control and
handoff the reproducible evidence to the authorized owner.

### HMOS-RULE-08 — Keep completion claims traceable and reversible

**Applies to:** every implementation, review, migration, compatibility, verification, and handoff
under this Domain.

- Trace every claim to a requirement, baseline, source or project fact, tested scope, method,
  observed result, and evidence location. Keep failures, warnings, skipped checks, and unavailable
  checks visible.
- Distinguish documented claims, observed tool output, assumptions, and organizational approvals.
  Never fabricate documentation, commands, results, device coverage, signatures, approvals, or
  reviewer conclusions.
- Preserve the smallest reversible change consistent with the supplied architecture. Record
  changed and unchanged scope, remaining risks, rollback guidance, and the receiving authority for
  unresolved decisions.
- Passing checks do not authorize publication, distribution, deployment, production operation,
  risk acceptance, or Domain activation.

**Required evidence:** an evidence index; acceptance mapping; source and baseline references;
executed procedures and actual results; explicit exclusions; changed-file inventory; residual-risk
record; rollback guidance; and handoff status.

**Failure and handoff:** if required evidence, authority, or acceptance criteria are absent, do not
declare completion. Preserve the current state and transfer the artifact and reproduction details
to the accountable owner; silence is not approval.

### HMOS-RULE-09 — Keep pages, Dialog pages, components, and routes structurally explicit

**Applies to:** every new or materially changed ArkUI page, Dialog page, modal, sheet, popup,
overlay, embedded component, route declaration, page metadata contract, and navigation call.

- Classify navigable screen roots as pages, modal or overlay destinations as Dialogs, and reusable
  embedded UI as components. Place them under `pages/`, `dialogs/`, and `components/` respectively,
  or record one established project-equivalent mapping that preserves those responsibilities.
- Keep route identifiers, page metadata, and route parameters under `router/` or one recorded
  equivalent. Declare route protocol strings once as named ArkTS constants and reuse them in
  destination declarations and navigation calls; they are program identifiers, not localizable
  strings.
- When a project already selects HMRouter, declare ordinary and Dialog destinations through the
  locked framework contract, mark Dialog destinations explicitly, and verify the applicable core
  and compiler-plugin integration. `HMROUTER-UPSTREAM` is authoritative only for HMRouter; it does
  not turn HMRouter into a HarmonyOS platform requirement.
- Preserve the approved navigation architecture and framework. Do not introduce HMRouter, replace
  another router, rename public routes, or change generated integration without explicit scope and
  compatibility authority.
- Keep pages, Dialogs, and components declarative. They render state, own only ephemeral view-local
  state, and forward intent; network execution, asynchronous orchestration, and business decisions
  remain in their accepted non-View boundaries.

**Required evidence:** changed UI artifact classification; recorded project-equivalent paths;
route-identifier and metadata map; locked navigation-framework and compiler-plugin versions when
applicable; public route/export diff; build evidence; and task-required navigation, Dialog
open/close, dismissal, repeated-interaction, failure, and recovery observations.

**Failure and handoff:** an incorrectly classified artifact, anonymous or duplicated route ID,
unapproved navigation-framework change, route contract outside its accepted boundary, or View-owned
network/business orchestration is a policy failure. If the locked framework version, generated
integration, route compatibility, or required runtime target is unknown or produces warnings,
preserve the finding and limit only the dependent compatibility or runtime claim. Do not fail or
block unrelated UI structure, resource, or comment outcomes solely because versions differ. Fail
only on observed behavior/build failure or an explicit project hard gate; block only when a required
claim cannot be established. Hand unresolved compatibility to the project navigation or
architecture owner, and do not infer it from the CatchElf sample or a different HMRouter version.

### HMOS-RULE-10 — Externalize UI resources and require meaningful Chinese comments

**Applies to:** every new or materially changed ArkTS/ArkUI source file and its affected application
resources.

- Declare user-visible text in `src/main/resources/base/element/string.json`, application-owned
  colors in `color.json`, and reusable font sizes, spacing, dimensions, corner radii, and similar UI
  measurements in `float.json`. Use an applicable system resource or established project token
  when one already owns the semantic value.
- Reference resources from ArkUI source through the project's supported `$r(...)` form. Use stable
  semantic keys that describe purpose, keep required locale and qualifier variants aligned, and do
  not embed a duplicate fallback literal in the View.
- Do not apply resource rules blindly to non-UI literals. Route IDs, log formats, regular
  expressions, serialization keys, endpoint fragments, and enum discriminators use named ArkTS
  constants or typed contracts. Dynamic user-visible messages still compose localizable resources.
- New or materially changed classes, structs, ArkUI components, ViewModels, public methods, and
  non-obvious business methods must contain meaningful Chinese comments that explain applicable
  responsibility, intent, input/output contract, state transition, side effect, failure handling,
  lifecycle dependency, or rationale.
- Comments must match current behavior. Line-by-line narration, identifier repetition, translated
  syntax, or filler added only to satisfy comment presence is not acceptable. Trivial accessors and
  self-evident local expressions do not require individual comments unless they enforce a material
  contract.
- Treat the Chinese-language requirement as an explicit Domain Owner policy
  [OWNER-UI-RESOURCE-COMMENT-CONTRACT], not as a HarmonyOS or ArkTS platform requirement. Any
  language-policy exception or change requires a scoped owner decision and migration record.

**Required evidence:** resource-key additions, updates, removals, and qualifier impact; changed-file
review for visible-text, color, repeated-measurement, and fallback literals; named non-UI constant
inventory; resource-reference build result; and a semantic review of required Chinese comments.

**Failure and handoff:** a new unexplained UI magic literal, missing resource key or qualifier,
value-based duplicate key, unsafe resource removal, or absent, stale, or meaningless required
Chinese comment fails the affected criterion even when compilation succeeds. When semantic
classification of a literal, localization ownership, qualifier policy, or comment-language
exception requires an unavailable organization decision, preserve the smallest unchanged boundary
and hand off the exact finding rather than guessing.

### HMOS-RULE-11 — Resolve network tools before reuse and bound every request outcome

**Applies to:** every new or materially changed endpoint, request/response model, repository,
service, network-client dependency, interceptor, authentication hook, request lifecycle, and
ViewModel network orchestration.

- Before generating an import or request call, prove the candidate dependency in stages: the
  affected module declares or is authoritatively supplied the package; the exact target and package
  entrypoint resolve; the required tool and public types are exported; the implementation's own
  dependencies, platform kits, configuration and permissions resolve for the declared SDK/API
  baseline; and the affected configured module build verifies the integration. Static inspection
  never substitutes for the final build state.
- Prefer an effective task-supplied or module-declared tool. If it is unavailable or unsuitable,
  search the authorized project scope for established exported network clients, request functions,
  platform-network imports, endpoint/base-address managers, request configuration, response/error
  contracts, interceptors and repository implementations. Record every credible candidate and its
  selection or rejection reason; do not infer usability from a filename or private source path.
- When no supplied or established exported project tool is suitable, stop the dependent network
  implementation and hand the exact discovery evidence to the architecture owner. Business-module
  development must not create a feature-owned transport abstraction, an official HarmonyOS SDK
  adapter, an `api/transport/` directory, an external dependency or shared network infrastructure,
  and must not invent authentication, certificates, retry, cache, backend response, base URL,
  Toast, routing or logging policy.
- Put outbound business request payload classes under `src/main/ets/models/request/` and inbound
  response payloads, response envelopes and response-error data under
  `src/main/ets/models/response/`, creating those directories when the authorized module lacks
  them. Keep other entities, value objects, enums, state and pure data definitions below
  `src/main/ets/models/` or an explicitly recorded project-equivalent model boundary. Model code
  must not execute requests or depend on repositories, services, network clients, ViewModels or
  Views.
- Keep only endpoint declarations, repository contracts and implementations, request execution and
  HTTP-facing services below `src/main/ets/api/` or an explicitly recorded project-equivalent API
  boundary. `api/` must not declare business request, response or other pure data classes. Views
  never execute network requests; ViewModels orchestrate typed domain outcomes; repository
  implementations invoke the verified project tool; services do not own presentation or navigation
  unless an accepted existing project contract assigns that side effect.
- Every request path must settle exactly once with a typed success or failure. Network
  unavailability, invalid configuration, protocol failure, business rejection, decoding failure,
  timeout, cancellation and SDK exception must not leave a pending Promise or collapse into an
  indistinguishable empty value. Define applicable cancellation, stale-result, deduplication,
  idempotency and lifecycle behavior before implementation.
- Redact credentials, authorization headers, cookies, tokens, personal data and unauthorized
  request or response content from logs and evidence. Verbose tracing, protected log access,
  cleartext network use, certificate changes, production hosts and authentication changes require
  the applicable project or security authority.

**Required evidence:** affected network-entry inventory; candidate and owning-module map; manifest,
lock or local-target resolution; package entrypoint and symbol exports; implementation dependency,
SDK/API, configuration and permission resolution; selection/rejection record; `models/request`,
`models/response` and other model inventory; model-to-API reverse-dependency review; API directory
and responsibility map; typed success/error and lifecycle contract; sensitive-data disposition;
affected configured build; task-required success, business-failure, protocol-failure, offline,
timeout, decode, cancellation, lifecycle and overlapping-request observations; and explicit skipped
or blocked paths.

**Failure and handoff:** an undeclared or unresolved dependency, unavailable export, incomplete
implementation chain, new or materially changed business DTO below `api/`, model-to-API reverse
dependency, business-owned Transport or SDK adapter, View-owned request, unapproved third-party
installation, invented project policy, pending failure path, collapsed error, or sensitive-data log
fails the affected criterion. When no candidate can be verified or proceeding requires an
unapproved SDK, dependency, permission, authentication, certificate, network-infrastructure or
service decision, stop the dependent implementation and hand the exact discovery evidence to the
project, platform or security owner. Do not copy `PROJECT-DRILL-UGC-NETWORK-EXEMPLAR` names or
behavior as a fallback.

## Rule Precedence and Conflict Handling

Apply the stricter authorized requirement when these rules overlap a project overlay, task
contract, Kernel rule, or another Domain, unless doing so would cross an ownership boundary.
Kernel red lines always remain in force. Record the conflicting requirements, affected behavior,
available evidence, and authority needed to resolve the conflict; do not choose silently or
self-approve an exception.

## Source Basis

These rules use the validated `engineering.harmonyos` research ledger: ArkTS language constraints
[HMOS-ARKTS], Stage-model architecture [HMOS-STAGE], ArkUI V2 observation
[HMOS-ARKUI-V2], V1-to-V2 state migration [HMOS-ARKUI-MIGRATION], application package semantics
[HMOS-PACKAGES], and HarmonyOS testing services [HMOS-TESTING]. Registered identity and lifecycle
remain governed by [REPO-HARMONYOS-IDENTITY]. Page/Dialog structure, resource externalization, and
Chinese-comment policy additionally use `OWNER-UI-RESOURCE-COMMENT-CONTRACT`,
`PROJECT-CATCHELF-SAMPLE`, and `HMROUTER-UPSTREAM` from
`changes/20260828-harmonyos-ui-resource-comment-policy/research/sources.json`; the project sample
and third-party framework do not override platform or project-version evidence.
Network dependency discovery, authorized project search, fail-closed handoff, model/API placement,
request completion, and redaction additionally use `OWNER-HMOS-MODEL-API-BOUNDARY` and
`OWNER-HMOS-NETWORK-REQUEST-CONTRACT` and
`PROJECT-DRILL-UGC-NETWORK-EXEMPLAR` from
`changes/20260829-harmonyos-network-request-policy/research/sources.json`; the exemplar remains
project evidence and does not make its package, tool, response, authentication, UI or network
choices reusable authority.
