---
name: hmos-business-module-development
description: Develop or revise a HarmonyOS business HAR after scaffolding using bounded MVVM, State Management V2, dependency-aware network delivery, API/UI classification, routing, shell delegation, and an optional provider bridge. Use for complete business-module feature work; do not use for scaffold-only initialization or generic ArkUI work outside a business module.
---

# HarmonyOS Business Module Development

Deliver one bounded business-module change without collapsing UI, mutable presentation state,
network access, routing, shell integration, or external contracts into one layer.

## Mandatory Domain Execution Plan Checkpoint

Before editing, integrate the concrete MVVM, page/Dialog/component, routing, provider, model/API,
network dependency, public-contract, verification and recovery steps into the target project's
`changes/<change-id>/task.md`. Present the complete Markdown plan and stop. Resume mutation only
after explicit confirmation of the current digest is recorded by the Kernel. Revise and completely
re-present the plan after any requested material change; routing or silence is not approval.

## Required Inputs

Confirm before editing:

- project root, business HAR path and module name;
- whether a companion `<module>provider` HAR exists or is required;
- declared SDK/API and State Management V2 baseline;
- requested pages, dialogs, components, service behavior and external consumers;
- existing navigation, network, dependency-injection or service-registration conventions;
- supplied network dependency/tool, module manifests and locks, public package entrypoints and
  exports, current SDK/API networking support, request/error/authentication/logging ownership, and
  permission to inspect the authorized project for an established exported network capability;
- authorized files, build target, acceptance scenarios and rollback boundary.

Resolve the scaffold state explicitly:

- when neither business nor provider HAR exists and initialization is requested, invoke
  `hmos-init-business-module` first, then return here;
- when the business HAR exists and the provider is absent, proceed without provider behavior and
  record that the provider branch is not applicable to this change. Do not invoke the pair
  initializer or hand-create the provider: the registered initializer refuses an existing business
  target. If the change's external consumers require a provider contract, note the gap in the
  handoff as an unresolved decision for the architecture owner rather than blocking the business
  work; and
- when the provider HAR exists but the business HAR is absent, do not overwrite, delete or
  repurpose the provider, and do not run the pair initializer. Proceed only with the explicitly
  authorized business-module work, treat the existing provider as read-only context for contract
  compatibility, and record the unpaired provider in the handoff for an owner decision.

Do not extend the initializer's scaffold script to implement this workflow.

## Architecture Contract

Read [business-module-architecture.md](references/business-module-architecture.md) and
[ui-page-dialog-conventions.md](references/ui-page-dialog-conventions.md) before planning or
editing. Read [network-request-conventions.md](references/network-request-conventions.md) whenever
the task adds or materially changes network dependencies, endpoints, request/response models,
repositories, services or request lifecycle. Apply `HMOS-RULE-05`: new or rewritten state-managed surfaces use State Management V2.
Treat the project exemplar recorded as `PROJECT-UGC-EXEMPLAR` as structural evidence only; it does
not override the current project or authoritative SDK guidance.

## Composition With Existing Capabilities

This Skill is the primary orchestrator only when the routed task type is
`harmonyos-business-module-development`. Compose existing capabilities without transferring its
architecture authority:

- use `hmos-init-business-module` only to create a missing business/provider scaffold, then return
  here before adding implementation;
- use `hmos-arkui-develop-skill` for bounded page, dialog or component implementation after this
  Skill has fixed the View/ViewModel ownership, directory and navigation boundaries;
- use ArkTS retrieval or static-correctness Skills to resolve language/API questions and
  diagnostics without relocating responsibilities or changing public contracts; and
- use `harmonyos-build-and-runtime-verification` to collect the required evidence without treating
  a successful build as approval of MVVM, provider or dependency-direction decisions.

If a composed Skill recommends a conflicting state model, directory, route, provider contract,
dependency direction or public export, stop composition and return the conflict to the task's
architecture decision owner. Do not silently select the most convenient recommendation.

## Workflow

1. Inventory the current module, provider, public exports, navigation, state ownership, network
   calls, dependency manifests and locks, package entrypoints and exports, project network tools,
   request/response model locations, network-tool implementations, typed result/error contracts,
   UI artifacts, tests and build target.
   Record deviations from the architecture contract.
2. Record the selected subordinate capabilities and the architecture decisions they are forbidden
   to change. Define the smallest vertical slice and map each file to View, ViewModel, model/UI-state, API,
   router, shell-delegate or provider responsibility. Do not move unrelated legacy code.
3. Keep pages, dialogs and components declarative. They render state, forward user intent and own
   only ephemeral view-local state; business decisions, asynchronous orchestration and mutable
   presentation data belong to the ViewModel.
   Classify navigable roots under `pages/`, modal or overlay destinations under `dialogs/`, and
   reusable embedded UI under `components/` or an explicitly recorded project equivalent.
4. Implement ViewModels and mutable UI-facing model objects with `@ObservedV2`; annotate each
   property whose mutation must refresh the UI with `@Trace`. Keep untraced internal fields private
   when practical and do not introduce V1 decorators.
5. Put outbound business request payload classes under `src/main/ets/models/request/`; put inbound
   response payloads, response envelopes and response-error data under
   `src/main/ets/models/response/`; and keep other entities, value objects, enums, state and pure
   data definitions under `src/main/ets/models/` or an explicitly recorded project-equivalent
   model boundary. Create the request or response directory when the authorized module needs it.
   Models do not execute requests or depend on API, ViewModel or View code. Put only endpoint
   declarations, repository contracts and implementations, request execution and HTTP-facing
   services under `src/main/ets/api/`; do not declare business data classes there. View code must
   not call the network client directly. Before generating imports, prove the supplied network tool
   through declaration, target/entrypoint resolution, exported symbols and implementation
   completeness. If it is ineffective, search the authorized project for an established compatible
   exported abstraction. When none exists, stop the dependent implementation and hand the candidate
   map to the architecture owner. Do not create a feature-owned Transport, official-SDK adapter or
   `api/transport/` directory, and never copy a reference project's package names, tool symbols,
   authentication, routing, Toast, response envelope, URLs, retry, cache or logging behavior.
6. Require every request path to settle exactly once with a typed success or failure. Keep offline,
   protocol, business, decode, timeout, cancellation and SDK failures distinguishable when the
   accepted behavior depends on them. Define lifecycle, stale-result, overlap, deduplication and
   idempotency behavior where applicable. Repository and Service code return typed outcomes;
   ViewModels own presentation-state mapping. Redact credentials, headers, cookies, tokens,
   personal data and unauthorized payloads from logs and evidence.
7. Classify reusable embedded UI under `components/`, modal or overlay UI under `dialogs/`, and
   navigable screen roots under `pages/`. Keep business route paths, page metadata and route
   parameters under `router/`.
   When the project uses HMRouter, use named route constants, mark Dialog destinations with
   `dialog: true`, and verify the locked core/compiler-plugin integration instead of assuming a
   remembered annotation contract.
8. Keep shell-project adaptation under `hmdelegate/` (or the explicitly mapped project-equivalent
   directory). It may adapt the business module to host-shell contracts but must not become a
   second location for business state, network access or route definitions.
9. When `<module>provider` exists, keep it as the sole external compile-time bridge. Declare
   `XxxServiceProvider` and `XxxComponentProvider` contracts plus the single `XxxProvider`
   factory/access point in the provider HAR; implement the contracts in the business HAR. External
   consumers depend on the provider contract, not business implementation paths.
10. Update public exports deliberately. Export only required pages, route contracts, shell delegates
   or provider contracts; do not expose ViewModel internals, repositories or network clients by
   convenience.
11. Before writing or changing ArkUI literals, declare user-visible strings in `string.json`,
    application-owned colors in `color.json`, and reusable UI measurements in `float.json` under
    `src/main/resources/base/element/`. Use named ArkTS constants for non-UI protocol values such as
    route IDs. Add meaningful Chinese comments to new or materially changed classes, components,
    ViewModels, public methods, and non-obvious business methods.
12. Inspect changed source for UI magic literals, missing resource keys, route duplication, incorrect
    UI classification, and absent, stale, or meaningless Chinese comments. Run the configured build
    for the affected module and every explicitly required lint, test or
    device scenario. Record structure and dependency-direction checks separately from compilation
    and runtime evidence.

## Verification Checklist

- UI artifacts are in exactly one of `components/`, `dialogs/` or `pages/` according to behavior.
- UI code renders state and delegates actions; ViewModels own business/presentation behavior.
- Mutable UI-facing classes use `@ObservedV2` and refresh-driving fields use `@Trace`.
- Outbound request DTOs are below `models/request/`; inbound response payloads, envelopes and
  response-error data are below `models/response/`; other pure data definitions remain below
  `models/`; models have no reverse dependency on API, ViewModel or View code.
- `api/` contains only endpoint declarations, repository contracts and implementations, request
  execution and HTTP-facing services; it declares no business request, response or other pure data
  classes.
- Every selected network tool has recorded declaration, target, entrypoint, export, implementation
  and configured-build evidence; unavailable supplied tools trigger project search and fail-closed
  owner handoff when no suitable exported project tool exists.
- No business-owned Transport, official-SDK network adapter or `api/transport/` directory is
  introduced; absence of a verified supplied or project network tool blocks dependent implementation.
- Every request path settles with a typed result; applicable offline, protocol, business, decode,
  timeout, cancellation, lifecycle and overlapping-request paths have explicit dispositions.
- Network logs and evidence redact credentials, authorization headers, cookies, tokens, personal
  data and unauthorized payloads; repository and Service code do not own presentation effects unless
  preserved by an explicit project contract.
- `router/` contains module route paths, page metadata and route parameter contracts.
- `hmdelegate/` contains only host-shell adaptation.
- User-visible strings, application-owned colors, and reusable UI measurements are resource-backed;
  route IDs and other non-UI protocol strings are named ArkTS constants.
- New or materially changed classes, components, ViewModels, public methods, and non-obvious
  business methods contain meaningful and current Chinese comments.
- HMRouter projects centralize route IDs and mark Dialog destinations explicitly; the locked
  framework and compiler-plugin integration is recorded and build-verified.
- When a provider HAR exists, provider interfaces are declared in `<module>provider`, implemented
  in `<module>`, and external consumers import the provider rather than implementation-internal
  paths.
- When a provider HAR exists, the `XxxProvider` factory/access point is unique for the module and
  exposes both service and component contracts without implementing business behavior itself.
- The affected build succeeds; required negative, UI and runtime scenarios have explicit statuses.

## Fail-Closed Conditions

Stop and request an architecture decision when:

- the current project mandates a conflicting module/provider topology and no approved overlay
  resolves the conflict;
- the SDK/API baseline cannot support the required V2 behavior;
- external consumers already import business internals and changing that public dependency is
  outside scope;
- provider registration, factory lifecycle or component-builder conventions are unknown and a
  choice would create a new public contract;
- implementation requires an unapproved dependency, routing-framework change, signing change,
  production access or unrelated refactor; or
- the supplied network dependency, package entrypoint, symbol or implementation chain is
  unresolved and no suitable established exported project tool exists;
- proceeding would require a business-owned Transport, official-SDK adapter, authentication,
  certificate, retry, cache, response, service-environment, navigation, Toast, shared-infrastructure
  or sensitive-log policy; or
- a required resource qualifier, locked routing-framework version, compiler-plugin configuration,
  or public route contract cannot be established without guessing.

## Handoff

Return the module/provider file inventory, MVVM ownership map, request/response and other model
inventory, model dependency-direction review, API containment result, network-tool candidate map,
effective-dependency states, selection/rejection reasons, typed result/error and lifecycle contract,
redaction disposition, task-required negative-path results, route and
shell-delegate changes, provider interface-to-implementation map, public export changes, build and
scenario evidence, subordinate-capability map, composition conflicts, deviations, unresolved
decisions, resource-key and changed-literal review, Chinese-comment review, and rollback
instructions.
