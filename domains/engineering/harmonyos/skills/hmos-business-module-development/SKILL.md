---
name: hmos-business-module-development
description: Develop or revise a HarmonyOS business HAR after scaffolding using a bounded MVVM, State Management V2, API, UI-classification, routing, shell-delegate, and optional provider-bridge contract. Use for complete business-module feature work; do not use for scaffold-only initialization or generic ArkUI component work outside a business module.
---

# HarmonyOS Business Module Development

Deliver one bounded business-module change without collapsing UI, mutable presentation state,
network access, routing, shell integration, or external contracts into one layer.

## Required Inputs

Confirm before editing:

- project root, business HAR path and module name;
- whether a companion `<module>provider` HAR exists or is required;
- declared SDK/API and State Management V2 baseline;
- requested pages, dialogs, components, service behavior and external consumers;
- existing navigation, network, dependency-injection or service-registration conventions;
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

Read [business-module-architecture.md](references/business-module-architecture.md) before planning
or editing. Apply `HMOS-RULE-05`: new or rewritten state-managed surfaces use State Management V2.
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
   calls, UI artifacts, tests and build target. Record deviations from the architecture contract.
2. Record the selected subordinate capabilities and the architecture decisions they are forbidden
   to change. Define the smallest vertical slice and map each file to View, ViewModel, model/UI-state, API,
   router, shell-delegate or provider responsibility. Do not move unrelated legacy code.
3. Keep pages, dialogs and components declarative. They render state, forward user intent and own
   only ephemeral view-local state; business decisions, asynchronous orchestration and mutable
   presentation data belong to the ViewModel.
4. Implement ViewModels and mutable UI-facing model objects with `@ObservedV2`; annotate each
   property whose mutation must refresh the UI with `@Trace`. Keep untraced internal fields private
   when practical and do not introduce V1 decorators.
5. Put endpoint declarations, repository contracts, repository implementations, request execution
   and network-facing services under `src/main/ets/api/` or its subdirectories. Request/response
   data models may remain in the project's established `models/` boundary. View code must not call
   the network client directly.
6. Classify reusable embedded UI under `components/`, modal or overlay UI under `dialogs/`, and
   navigable screen roots under `pages/`. Keep business route paths, page metadata and route
   parameters under `router/`.
7. Keep shell-project adaptation under `hmdelegate/` (or the explicitly mapped project-equivalent
   directory). It may adapt the business module to host-shell contracts but must not become a
   second location for business state, network access or route definitions.
8. When `<module>provider` exists, keep it as the sole external compile-time bridge. Declare
   `XxxServiceProvider` and `XxxComponentProvider` contracts plus the single `XxxProvider`
   factory/access point in the provider HAR; implement the contracts in the business HAR. External
   consumers depend on the provider contract, not business implementation paths.
9. Update public exports deliberately. Export only required pages, route contracts, shell delegates
   or provider contracts; do not expose ViewModel internals, repositories or network clients by
   convenience.
10. Run the configured build for the affected module and every explicitly required lint, test or
    device scenario. Record structure and dependency-direction checks separately from compilation
    and runtime evidence.

## Verification Checklist

- UI artifacts are in exactly one of `components/`, `dialogs/` or `pages/` according to behavior.
- UI code renders state and delegates actions; ViewModels own business/presentation behavior.
- Mutable UI-facing classes use `@ObservedV2` and refresh-driving fields use `@Trace`.
- Network requests and their contracts/implementations are contained by `api/`.
- `router/` contains module route paths, page metadata and route parameter contracts.
- `hmdelegate/` contains only host-shell adaptation.
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
  choice would create a new public contract; or
- implementation requires an unapproved dependency, routing-framework change, signing change,
  production access or unrelated refactor.

## Handoff

Return the module/provider file inventory, MVVM ownership map, API containment result, route and
shell-delegate changes, provider interface-to-implementation map, public export changes, build and
scenario evidence, subordinate-capability map, composition conflicts, deviations, unresolved
decisions and rollback instructions.
