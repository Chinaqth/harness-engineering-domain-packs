# HarmonyOS Page, Dialog, Resource, and Comment Conventions

## Purpose and Authority

This contract defines reusable delivery outcomes for ArkUI pages, Dialog pages, embedded
components, route declarations, UI resources, and explanatory comments. It applies whether the
project uses HMRouter or another approved navigation mechanism. HMRouter-specific clauses apply
only when the project already selects and pins HMRouter; they do not make a third-party framework
part of the HarmonyOS platform contract.

The contract is supported by the Domain Owner requirement `OWNER-UI-RESOURCE-COMMENT-CONTRACT`,
the corrected CatchElf sample `PROJECT-CATCHELF-SAMPLE`, and HMRouter upstream documentation
`HMROUTER-UPSTREAM`. The sample is structural project evidence, not platform authority. Any
version-sensitive HMRouter behavior must be reconciled with the project's locked dependency and
an actual build.

## UI Artifact Classification

| Artifact | Required location | Required responsibility | Forbidden responsibility |
| --- | --- | --- | --- |
| Page | `src/main/ets/pages/` | Navigable screen root and composition | Direct network execution or scattered route identity |
| Dialog page | `src/main/ets/dialogs/` | Modal, Dialog, sheet, popup, or overlay presentation | Business orchestration or ordinary-page classification |
| Component | `src/main/ets/components/` | Reusable embedded UI | Independent route registration unless explicitly designed as a destination |
| Route contract | `src/main/ets/router/` | Route identifiers, page metadata, and route parameters | UI tree, network execution, or host-shell behavior |

An established project-equivalent location may be preserved when it is explicit and does not
collapse these responsibilities. Record the mapping instead of creating a duplicate directory.

## HMRouter Contract

When HMRouter is selected by the project:

- declare an ordinary page with `@HMRouter({ pageUrl: XxxPath.XxxPage })`;
- declare a Dialog page with `@HMRouter({ pageUrl: XxxPath.XxxDialog, dialog: true })`;
- use the project's approved state-management generation; new components remain subject to
  `HMOS-RULE-05` and therefore use State Management V2;
- declare route protocol strings once as named constants under `router/`, and pass those constants
  to both annotations and navigation calls;
- keep page metadata and parameter contracts under `router/` rather than duplicating them in Views;
- verify the exact HMRouter core and compiler-plugin versions, required build configuration, and
  generated route integration for the affected HAR, HSP, or HAP; and
- treat framework documentation as proof of its declared interface only. Compilation proves the
  configured source and generated integration, while navigation and Dialog behavior require the
  corresponding runtime or UI evidence.

A core/compiler-plugin version difference or generated API-level warning is a compatibility
finding, not direct proof of functional failure. Record it, identify the affected compatibility
claim, and retain it as warning/residual risk when the configured build and task-required behavior
checks pass. Fail only after an observed build or required runtime failure, or when an explicit
project hard gate requires equality or forbids the warned API. Block only a task-required
compatibility claim whose necessary target evidence is unavailable; do not block unrelated UI
structure, resource, or comment delivery.

Route protocol strings such as `page://SamplePage` are program identifiers, not localizable UI
content. They remain named ArkTS constants and must not be moved to `string.json`.

## Resource Contract

For new or materially changed ArkUI:

- declare user-visible text in `src/main/resources/base/element/string.json` and reference it with
  `$r('app.string.<name>')`;
- declare application-owned colors in `color.json` and reference them with
  `$r('app.color.<name>')`;
- declare reusable dimensions, font sizes, spacing, corner radii, and similar UI measurements in
  `float.json` and reference them with `$r('app.float.<name>')`;
- prefer an applicable system resource or an established project token instead of duplicating a
  local value;
- use stable semantic resource names that describe purpose rather than the current literal value;
- keep locale- or qualifier-specific variants aligned with the base resource key when the task
  affects those configurations; and
- remove a resource only after proving that no supported source, qualifier, or generated consumer
  still references it.

Do not classify every string literal as a UI resource. Route IDs, log formats, regular expressions,
serialization keys, endpoint fragments, and enum discriminators use named ArkTS constants or the
project's typed contract. Dynamic user-visible messages must still be assembled from localizable
resources rather than embedded prose.

## Chinese Comment Contract

New or materially changed classes, structs, ArkUI components, ViewModels, public methods, and
non-obvious business methods must include meaningful Chinese comments. A sufficient comment
explains at least one relevant concern: responsibility, intent, input/output contract, state
transition, side effect, failure handling, lifecycle dependency, or why a non-obvious choice is
necessary.

Comments must remain synchronized with behavior. Line-by-line narration, translated syntax,
comments that merely repeat an identifier, and filler added only to satisfy comment presence do
not pass. Trivial accessors and self-evident local expressions do not need individual comments
unless they enforce a material contract.

This language requirement is an explicit Domain Owner policy, not a claim about HarmonyOS or ArkTS.
A future language-policy change requires an owner decision and migration record.

## Ordered Implementation Checkpoints

### Before implementation

1. Inventory affected pages, Dialog pages, components, route declarations, resource files, locale
   or qualifier variants, and existing comment conventions.
2. Record the selected navigation framework and locked version. When HMRouter is used, inspect its
   project configuration and an applicable conforming project reference.
3. Classify each new UI artifact and map each accepted UI state to resources and observable checks.

### During implementation

1. Create or reuse semantic resource keys before adding user-visible text, color, or reusable UI
   measurements to ArkUI source.
2. Add or update route constants and metadata together with the destination; do not leave anonymous
   route literals in the View or caller.
3. Add Chinese responsibility and logic comments while implementing the class or method so that
   the explanation reflects the actual design.
4. Keep Views declarative and delegate business actions and asynchronous orchestration to the
   ViewModel.

### Before build and handoff

1. Inspect changed `.ets` files for new visible-text, color, repeated-dimension, and route literals.
2. Verify that every referenced resource key exists in the base file and every affected qualifier.
3. Verify page/Dialog/component location, route uniqueness, metadata ownership, and public exports.
4. Review comment meaning and freshness, not only comment presence.
5. Run the configured build, then separately record any required navigation, Dialog open/close,
   repeated-interaction, dismissal, failure, and recovery evidence.

## Evidence and Failure Handling

Required evidence includes the UI artifact inventory, navigation-framework/version record, route
map, resource-key diff, changed-literal review, Chinese-comment review, build result, required UI
scenarios, deviations, and rollback unit.

Fail the affected criterion when a new or materially changed surface contains an unexplained UI
magic literal, a missing resource, an incorrectly classified page/Dialog/component, a duplicated or
anonymous route ID, or a required Chinese comment that is absent, stale, or meaningless. Mark the
dependent criterion blocked only when a task-required generated integration, qualifier, build
target, compatibility claim, or runtime target cannot be established. Version differences and API
warnings alone remain warning evidence unless an explicit hard gate or observed failure elevates
them. Do not use a successful build to waive a structural, resource, comment-quality, or
observed-behavior failure, and do not use a warning to invent an unobserved functional failure.

Source basis: `OWNER-UI-RESOURCE-COMMENT-CONTRACT`, `PROJECT-CATCHELF-SAMPLE`,
`HMROUTER-UPSTREAM`, and `HMOS-ARKUI-V2` in
`changes/20260828-harmonyos-ui-resource-comment-policy/research/sources.json`.
