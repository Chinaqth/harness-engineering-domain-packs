# HarmonyOS Engineering

## Purpose

`engineering.harmonyos` owns reusable professional practice for designing, implementing,
migrating, verifying, and handing off HarmonyOS applications. Its public baseline covers the
Stage application model, ArkTS, ArkUI, state-management migration, API compatibility, module and
package design, and evidence-bearing verification. The registered description is "Owns reusable
HarmonyOS application delivery practice and evaluation." [REPO-HARMONYOS-IDENTITY]

The Domain favors the Stage model as the long-term application model, with `UIAbility` for
user-facing components and the appropriate system-defined `ExtensionAbility` derivative for an
extension scenario. Architecture decisions must account for component lifecycle, context,
windows, pages, configuration, processes, threads, and concurrency boundaries rather than treating
an ArkUI screen as an isolated artifact. [HMOS-STAGE]

## Ownership and Lifecycle

- Domain ID: `engineering.harmonyos`
- Display name: `HarmonyOS Engineering`
- Primary owner: `platform-harmony`
- Version: `1.0.0`
- Lifecycle: `active`

These values are registered repository facts; this document does not assign additional reviewers,
decision rights, or permissions. Activation establishes routing eligibility only; it does not
grant operational permissions. [REPO-HARMONYOS-IDENTITY]

## In Scope

- Design and review Stage-model application structure, including `UIAbility`, applicable
  `ExtensionAbility` types, lifecycle handling, context use, window and page composition,
  configuration, process boundaries, and thread or concurrency decisions.
  [HMOS-STAGE]
- Implement and review ArkTS code with explicit attention to its stricter static type system,
  constrained dynamic features, null safety, declarations, modules and kits, interoperability,
  and documented concurrency rules. [HMOS-ARKTS]
- Develop and review declarative ArkUI interfaces and state-driven interactions while tracing
  version-sensitive API signatures and behavior to authoritative documentation rather than
  relying on recalled syntax. [HMOS-ARKTS]
- Plan, implement, and verify scenario-specific ArkUI state-management migration. In particular,
  migration of data-object observation from V1 patterns such as `Observed`, `ObjectLink`, and
  `Track` to V2 patterns such as `ObservedV2` and `Trace` must preserve data flow and observation
  behavior; it is not a mechanical decorator substitution. [HMOS-ARKUI-V2]
  [HMOS-ARKUI-MIGRATION]
- Detect deprecated, incompatible, or invalid ArkTS and HarmonyOS API use against a declared SDK
  and API baseline; identify a documented replacement or record the absence of one; and verify the
  change through static checks and relevant tests. [HMOS-ARKTS] [HMOS-TESTING]
- Select and review module boundaries using the distinct delivery and reuse semantics of HAP, HAR,
  and HSP artifacts, and account for the App Pack publication unit when release packaging is in
  scope. [HMOS-PACKAGES]
- Define and collect reproducible evidence from applicable code linting, unit testing, coverage,
  application or atomic-service self-inspection, and device-facing validation. Verification may
  address functionality, compatibility, performance, power consumption, security, and stability,
  but project-specific thresholds must be supplied by the project or organization.
  [HMOS-TESTING]
- Retrieve version-relevant HarmonyOS, ArkTS, ArkUI, SDK, API, and tooling guidance and retain the
  source identifier, document location, relevant version, and retrieval context for consequential
  implementation decisions. [HMOS-STAGE] [HMOS-ARKTS] [HMOS-ARKUI-V2]
  [HMOS-ARKUI-MIGRATION]

## Out of Scope

- Product requirements, business logic, visual identity, organization-specific design systems,
  private service architecture, authentication flows, data contracts, and customer or production
  data.
- Choosing an organization's supported SDK, API-level, DevEco Studio, device, screen-mode, or
  backward-compatibility matrix.
- Inventing repository commands, lint configuration, dependency policy, quality thresholds,
  accessibility targets, performance or power budgets, release gates, or rollback criteria.
- Granting permissions; accessing signing material or secrets; signing, publishing, distributing,
  rolling out, or operating a production application without an explicit project contract and
  authorization.
- Treating a successful static check or build as proof of runtime behavior, compatibility,
  usability, accessibility, security, performance, or release readiness.
- Treating a local knowledge index, generated snippet, Skill instruction, or remembered API as more
  authoritative than version-relevant platform documentation and observed tool evidence.
- Owning generic product management, UX approval, security approval, privacy approval, or release
  management. The Domain prepares evidence for those functions and hands decisions to their named
  owners.

## Stable Inputs

Work entering this Domain must identify, or explicitly mark as unknown:

1. The requested outcome, affected HarmonyOS application or module boundary, and acceptance
   criteria.
2. Relevant source files and configuration, plus the existing Stage-model, navigation,
   state-management, module, and package conventions that must be preserved.
3. The compile SDK, compatible or minimum API baseline, toolchain version, target device or form
   factors, and any required compatibility matrix.
4. For ArkUI work, the current state-management generation, component data flow, lifecycle
   expectations, interaction paths, and applicable UI or accessibility requirements.
5. For migration or deprecated-interface work, an inventory of affected constructs or diagnostics,
   the documented target behavior, and constraints that prevent immediate replacement.
6. Available authoritative documentation and its version or retrieval context, together with any
   local knowledge-index result whose provenance and freshness can be inspected.
7. The permitted tools and mutations, verification commands, test environment, device access,
   signing or release boundary, and rollback expectations.

Missing inputs that affect correctness, compatibility, authorization, or release safety are not to
be guessed. They become explicit assumptions, blockers, or organization-input requests.

## Use of Added Skills

The six added Skills provide owner-trusted operating procedures for ArkTS and ArkUI knowledge retrieval,
ArkUI implementation, syntax and build diagnostics, deprecated-interface analysis, and state
management migration. They may help inventory files, narrow a documentation query, structure a
migration batch, classify diagnostics, or bound a repair loop. Their embedded examples, local
indexes, commands, tool names, version statements, and severity labels are not independent
platform or organization policy.

Each Skill feeds specific registered capabilities as discovery and structuring input:

| Skill | Contributes to capabilities | Role |
| --- | --- | --- |
| `hmos-arkts-knowledge-retriever` | `harmonyos-authoritative-knowledge-retrieval`, `arkts-implementation-and-static-correctness`, `harmonyos-api-deprecation-and-compatibility` | Read-only ArkTS language, library, concurrency, runtime, toolchain, and TypeScript-migration retrieval through `scripts/search_docs.py` and its local indexes. |
| `hmos-arkui-knowledge-retriever` | `harmonyos-authoritative-knowledge-retrieval`, `arkui-interface-delivery`, `arkui-state-management-v1-to-v2-migration` | Read-only ArkUI retrieval across seventeen knowledge categories through `scripts/run.py`, including API signatures, V1/V2 distinctions, and error codes. |
| `hmos-arkui-develop-skill` | `arkui-interface-delivery` | ArkUI page and component creation, incremental modification, and diagnostic-driven repair using quick API references plus targeted retrieval, while preserving the existing state-management and navigation paradigm. |
| `hmos-arkui-statemgt-migration` | `arkui-state-management-v1-to-v2-migration` | V1-to-V2 decorator, application-storage, rendering-control, and reuse mappings plus dependency-ordered batch planning. |
| `hmos-arkts-deprecated-interface-checker` | `harmonyos-api-deprecation-and-compatibility` | Deprecated-API detection, P0/P1/P2 remediation classification, and documented replacement proposals. |
| `hmos-arkts-syntax-checker` | `arkts-implementation-and-static-correctness`, `harmonyos-build-and-runtime-verification` | A bounded diagnose-fix-build loop with retry limits and HAP/App artifact reporting. |

No added Skill covers Stage-model architecture or HAP/HAR/HSP topology design;
`stage-application-and-package-design` operates through the Domain wrapper and authoritative
documentation only.

Before using one of these procedures, the task must declare the applicable API and SDK baseline,
confirm that every required script or external tool is actually available, and identify which
mutations are authorized. Consequential API signatures, deprecation replacements, decorator
mixing rules, and version support must be reconciled with version-relevant primary documentation
and observed compiler or test evidence. [HMOS-ARKTS] [HMOS-ARKUI-V2]
[HMOS-ARKUI-MIGRATION]

When a Skill cannot run, its knowledge index is stale or ambiguous, or its recommendation conflicts
with authoritative documentation or tool output, the Domain must report that limitation and use an
available manual or documented verification path. It must not present an unexecuted Skill checklist,
generated snippet, or predicted build artifact as verified evidence.

## Evidence-Bearing Outputs

Depending on the task, the Domain produces one or more of the following:

- An architecture or implementation decision record that states the selected Stage components,
  module boundaries, lifecycle and concurrency implications, alternatives considered, and source
  IDs supporting the choice. [HMOS-STAGE]
- A scoped ArkTS or ArkUI change set with an affected-file inventory, preserved project
  conventions, API-signature evidence, and a concise explanation of user-visible and data-flow
  behavior. [HMOS-ARKTS]
- A migration plan and patch mapping each original state behavior to its intended V2 behavior,
  identifying mixed-mode boundaries and recording compilation and behavioral regression evidence.
  [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]
- A compatibility or deprecated-interface report containing the declared SDK/API baseline,
  diagnostics with locations and severities, authoritative replacement evidence, disposition for
  every finding, and post-change verification results. [HMOS-ARKTS] [HMOS-TESTING]
- A module and packaging decision that states why code belongs in an entry or feature HAP, a HAR,
  or an HSP, and records resulting publication, installation, runtime, and reuse implications.
  [HMOS-PACKAGES]
- A verification record listing the exact checks run, relevant configuration and environment,
  observed results, coverage or self-inspection artifacts where applicable, unresolved warnings,
  and checks not run. [HMOS-TESTING]
- A handoff summary containing changed and unchanged scope, assumptions, residual risks, rollback
  guidance, required approvals, and traceable documentation references.
- For knowledge-retrieval work, a query record identifying the question, search scope, returned
  document location, relevant API or SDK version, retrieval date or context, match rationale, and
  whether any cited snippet was independently compiled or tested.

Outputs must distinguish documented claims from tool observations and assumptions. A code snippet
or recommendation is not marked verified unless the recorded check actually exercised it.

## Handoffs

- Hand off product ambiguity, UX behavior, content, and accessibility acceptance to the named
  product, design, or accessibility owner, attaching UI behavior and validation evidence.
- Hand off security, privacy, authentication, storage, permission, and sensitive-data decisions to
  the applicable control owner before implementation or release when their policy is not already
  part of the task contract.
- Hand off SDK/API baseline selection, architecture exceptions, module-topology changes, and
  cross-application reuse decisions to the named platform or architecture authority when they
  exceed the supplied project contract.
- Hand off signing, application-market metadata, distribution, rollout, production operation, and
  rollback execution to authorized release owners; never infer authority from successful packaging.
- Hand off unresolved compiler, linter, emulator, device, or toolchain failures with reproduction
  inputs, raw diagnostics, attempted remediations, and the last known good state.
- Accept a handoff back only when the needed decision, permission, environment, or acceptance
  criterion is explicit enough to produce reproducible evidence.

## Failure Modes and Required Response

| Failure mode | Required response |
| --- | --- |
| SDK/API or documentation version is unknown | Stop version-sensitive claims and changes; record the missing baseline and request it. |
| Local knowledge conflicts with current official documentation or compiler evidence | Preserve both references, prefer version-relevant primary documentation and observed diagnostics, and escalate any unresolved conflict. |
| A proposed ArkTS or ArkUI API signature cannot be verified | Do not invent parameters or behavior; retrieve authoritative documentation or mark the implementation blocked. |
| Static analysis or compilation fails | Report exact diagnostics and affected files, make only scoped fixes, rerun the check, and preserve remaining failures. |
| A deprecated API has no verified replacement | Do not perform a blind substitution; document impact, compatibility constraints, alternatives, and required owner decision. |
| State-management migration changes observation or data flow | Revert or isolate the unsafe batch, document the behavioral mismatch, and redesign from the scenario-specific migration rules. |
| Build or packaging succeeds but runtime evidence is absent | Report build success only; keep runtime, device compatibility, and release readiness unverified. |
| Required tool, device, permission, signing material, or release authority is unavailable | Do not bypass the control; produce a reproducible handoff and mark the affected verification or operation not run. |
| Repeated automated repair does not converge | Stop at a declared retry bound, retain diagnostics and changes, and hand off the remaining root-cause analysis rather than looping indefinitely. |
| Requested work would expose secrets, production data, or private architecture | Refuse that handling path and request a sanitized, authorized input or an appropriate controlled environment. |

## Maturity and Organization Inputs

This Domain is an active source-supported professional baseline at version `1.0.0`. Activation
establishes routing eligibility only; per-Skill artifact scoring was waived by explicit owner
direction and the six added Skills remain non-authoritative discovery aids under the quarantine
policy. [REPO-HARMONYOS-IDENTITY]

The following are `needs-org-input` and must be supplied through project overlays, task contracts,
or authoritative organization policy as appropriate:

- Reviewer roles and decision rights across HarmonyOS engineering, architecture, UX,
  accessibility, security, privacy, testing, and release.
- Permissions for repository and dependency changes, device access, signing, distribution,
  production operation, and rollback.
- Internal ArkTS and ArkUI conventions, architecture rules, design-system requirements,
  accessibility policy, lint configuration, and dependency policy.
- Supported HarmonyOS, API, SDK, DevEco Studio, emulator, physical-device, and screen-mode matrix.
- Reproducible project commands and evidence formats for install, lint, compatibility analysis,
  build, test, package, sign, launch, inspect, publish, and rollback.
- Coverage, static-analysis, compatibility, stability, performance, power, security, accessibility,
  and release-blocking thresholds.
- Provenance, supported versions, tool dependencies, and independent validation evidence for the
  user-added HarmonyOS Skills before their local knowledge or automation is treated as authoritative.

These gaps do not prevent routing or use of the cited public baseline. They do prevent the
Domain from silently claiming organization-specific compatibility, permission, quality, or release
assurance.

## Source Register

The validated research ledger is
`changes/engineering.harmonyos-completion/research/sources.json`. This iteration uses all approved
source IDs:

- `REPO-HARMONYOS-IDENTITY`
- `HMOS-ARKTS`
- `HMOS-STAGE`
- `HMOS-ARKUI-V2`
- `HMOS-ARKUI-MIGRATION`
- `HMOS-PACKAGES`
- `HMOS-TESTING`
