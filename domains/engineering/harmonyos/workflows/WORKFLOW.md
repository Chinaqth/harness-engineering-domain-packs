# HarmonyOS Engineering Delivery Workflow

Artifact iteration: 1  
Domain: `engineering.harmonyos`  
Lifecycle: `active`

## Purpose and Authority

This workflow turns an authorized HarmonyOS task into a reviewable architecture decision,
implementation or migration, and an evidence-bearing handoff. It covers authoritative knowledge
retrieval, ArkTS and ArkUI delivery, Stage-model and package design, deprecated-interface and
compatibility work, ArkUI state-management V1-to-V2 migration, and verification through verified
`devecocli` interfaces.

The workflow applies `engineering.harmonyos` rules. It does not select an organization's SDK or
API baseline, grant repository or device access, authorize dependency changes, handle signing
material, publish an application, approve risk, or activate this Domain. Project overlays supply
project commands, supported targets, quality thresholds, reviewers, and release procedures.

## Entry Gate

Open a delivery evidence record before making changes. Record the task ID, requester, current
revision, affected application and modules, evidence location, and accountable handoff owner.

| Required input | Entry evidence | If missing or contradictory |
| --- | --- | --- |
| Outcome and acceptance criteria | Expected behavior, material negative paths, exclusions, and acceptance authority | Stop dependent design choices and request a decision. |
| Project and architecture context | Project root, Stage-model structure, affected `UIAbility` or `ExtensionAbility`, navigation, lifecycle, context, concurrency, and module conventions | Limit work to confirmed surfaces; mark architecture decisions `needs-org-input`. |
| Version baseline | Compile SDK, compatible or minimum API, toolchain version, source and target versions for migration or compatibility work, and target devices or form factors | Do not make version-sensitive claims or changes. |
| ArkUI state model | Existing V1/V2 generation, observed data flow, ownership, initialization, persistence, reuse, and intentional mixed boundaries | Do not infer decorator conversions or change observation behavior. |
| Package intent | Product, modules, intended HAP/HAR/HSP boundaries, App Pack scope, reuse and runtime expectations | Do not redesign module topology or claim package suitability. |
| Authorized execution contract | Permitted reads and writes, verified `devecocli` availability and subcommands, project configuration, tests, device access, retry bound, and rollback procedure | Do not invent commands, install tools, mutate files, or cross the missing permission boundary. |
| Quality and handoff contract | Required lint, compatibility, build, unit, coverage, runtime, device, accessibility, security, performance, power, stability, signing, and release checks; named decision owners | Run only applicable authorized baseline checks and leave dependent claims unverified. |

**Entry output:** a scoped work record containing confirmed facts, assumptions, blockers,
authorized actions, changed-surface estimate, requirement-to-check mapping, and planned recovery
unit. Missing information remains visible; it is never converted into a default silently.

## Common Evidence Model

For every procedure, distinguish four evidence classes:

1. **Documented:** source ID, document ID or location, relevant section, stated version, retrieval
   context, and retrieval date.
2. **Observed:** exact command or inspection, working scope, tool and SDK versions, exit status,
   raw or linked output, and target identity.
3. **Assumed:** unresolved fact, reason it is provisionally usable, affected claim, and owner.
4. **Approved:** decision, approver or authoritative project source, scope, and date or revision.

A retrieved example is not compilation evidence. Lint is not build evidence. Build and packaging
are not install, runtime, device, signing, distribution, or release evidence. [HMOS-TESTING]

## Ordered Delivery Procedure

### 1. Baseline and route the task

1. Inventory affected `.ets` files, resources, configuration, modules, Stage components,
   navigation, state objects, persistence, package boundaries, and external interfaces.
2. Reproduce the current expected path and material negative paths in an authorized environment.
3. Record pre-existing diagnostics and unavailable checks without attributing them to the change.
4. Route the task to one or more procedure tracks below and identify dependencies between them.
5. Map every acceptance criterion to a target artifact and planned verification method.

**Output:** baseline inventory, route selection, dependency order, requirement-to-check map, and
explicit unchanged scope.

**Negative path:** if project identity, current behavior, or the affected boundary cannot be
established safely, stop mutation. Preserve the limitation and hand the missing fact to the
requester or architecture owner.

### 2. Retrieve authoritative, version-relevant guidance

Use this track before consequential API, language, decorator, migration, compatibility, or
package decisions.

1. Form a narrow question containing the construct, intended behavior, declared SDK/API baseline,
   and relevant Stage, ArkTS, ArkUI, or package context.
2. Confirm `devecocli docs` is available and authorized. Resolve its supported syntax from the
   installed interface; do not reuse flags from a cached Skill.
3. Search with `devecocli docs search <keywords...>`. Record query terms, returned document IDs,
   titles, version statements, and match rationale.
4. Read the selected source with `devecocli docs read <documentId>` when full context is needed.
5. Cross-check consequential signatures, lifecycle behavior, deprecation replacements, decorator
   mixing rules, and version support against version-relevant primary guidance. [HMOS-ARKTS]
   [HMOS-STAGE] [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]
6. Label cached Skill-corpus results as provisional. Record conflicts and prefer current primary
   guidance and observed compiler evidence; absence from a local index proves nothing.

**Output and evidence:** question, query record, source locations and versions, selected guidance,
conflicts, confidence, and the implementation decision it supports.

**Bounded retry:** refine a failed or noisy query at most twice after the initial search. Each
refinement must narrow the construct, version, or scenario. After three total searches, stop and
hand off the unresolved documentation question rather than cycling synonyms.

**Negative paths:** when `devecocli docs` is unavailable, use an authorized manual primary-source
path and label it manual. If no version-relevant source or verified signature is found, do not
invent an API or proceed with the dependent change.

### 3. Design Stage components and package boundaries

1. Identify the required application behavior and select `UIAbility` or the applicable
   system-defined `ExtensionAbility` type from authoritative scenario guidance. [HMOS-STAGE]
2. Describe lifecycle, context, window, page, configuration, process, thread, and concurrency
   implications. Record ownership and cleanup at every boundary.
3. Partition entry or feature HAP, HAR, and HSP responsibilities using their distinct publication,
   installation, runtime, and reuse semantics; identify App Pack implications when applicable.
   [HMOS-PACKAGES]
4. Compare alternatives and preserve existing project topology unless an authorized requirement
   justifies change.
5. Define the smallest reversible architecture unit and the checks needed to validate it.

**Output and evidence:** decision record containing selected components and package types,
alternatives, lifecycle and concurrency model, dependency direction, versioned sources, affected
configuration, recovery boundary, and unresolved organization decisions.

**Negative paths:** do not treat a HAR as an installable application, infer HSP suitability from
code reuse alone, choose an extension type by name similarity, or change module topology without
architecture authority. Hand unresolved cross-application reuse, process, package, or publication
decisions to the named platform or architecture owner.

### 4. Implement ArkTS and ArkUI behavior

1. Confirm the target files, accepted UI states, current navigation and state-management model,
   project conventions, and permissions to edit.
2. Retrieve exact version-relevant APIs before use. Account for ArkTS static typing, null safety,
   restricted dynamic behavior, module and kit declarations, interoperability, and concurrency
   constraints. [HMOS-ARKTS]
3. Define state ownership and data flow for loading, empty, success, invalid input, failure,
   retry, lifecycle re-entry, and other material expected or negative paths.
4. For a new project, new component, or rewritten state-managed surface, use State Management V2
   and introduce no V1 decorators, storage, or observation mechanisms. [HMOS-ARKUI-V2]
5. Inventory V1 usage in the affected surface. When authorized work touches V1, route the affected
   state flow through the V1-to-V2 migration track. If migration is outside scope, keep the smallest
   existing V1 boundary unchanged, add no V1 usage, and record the migration handoff.
6. Make the smallest scoped change. Preserve business logic, navigation architecture, lifecycle
   contracts, and unrelated modules unless explicitly authorized.
7. Inspect changed files. Run lint only when the task contract or user explicitly requires lint
   evidence; repair only findings caused by or blocking the scoped change.
8. Exercise at least one accepted regression path for an incremental change and record any path
   that cannot be executed.

**Output and evidence:** scoped patch, changed-file inventory, API decision references, state-flow
description, requested check results, expected and negative-path observations, known limitations,
and rollback guidance.

**Bounded retry:** when lint is explicitly requested, permit no more than three
diagnose-fix-lint iterations, including the first repair attempt. A task contract may lower this
bound. Every iteration records diagnostics, edits, and result; it may not widen scope or weaken
checks.

**Negative paths:** if an API signature is uncertain, state behavior changes unexpectedly, or the
repair loop fails to converge, stop. Revert or isolate the unsafe batch when authorized, retain
diagnostics, and hand off root-cause or design questions. A manual checklist never becomes a lint
or compile pass.

### 5. Analyze deprecation and compatibility

1. Declare source and target SDK/API versions, supported matrix, file scope, exclusions, and
   remediation authority.
2. Only when the task contract or user explicitly requires compatibility evidence, confirm the
   compatibility interface and obtain valid identifiers with `devecocli check compat versions`
   when available.
3. Run `devecocli check compat` with explicit, verified source and target identifiers and exact
   project scope. Persist the report when evidence is required.
4. Reconcile findings with `devecocli check lint` diagnostics and authoritative documentation.
   Classify each finding by location, affected target, behavioral risk, and disposition.
5. For every proposed replacement, record documented semantics, minimum-version implications,
   lifecycle or state effects, and required regression coverage.
6. Apply only authorized, independently reviewable remediations, then rerun the affected
   compatibility and verification checks.

**Output and evidence:** baseline and command record, complete finding ledger, documented
replacement or explicit absence, remediation patch, before/after diagnostics, unresolved risks,
and supported-matrix impact.

**Bounded retry:** one initial remediation plus at most two corrective iterations. Repeated or
expanding failures stop the automated loop and require owner review.

**Negative paths:** a deprecation is not automatically a defect, and a matching symbol name is not
a verified replacement. If versions are invalid, the tool is unavailable, a replacement cannot be
verified, or compatibility results conflict with compilation or runtime evidence, retain all
evidence and block the dependent compatibility claim.

### 6. Migrate ArkUI state management from V1 to V2

1. Confirm that V2 is supported by the declared target baseline; do not rely solely on the Skill
   corpus assumption that V2 guidance targets API 12 or later. [HMOS-ARKUI-V2]
2. Inventory V1 decorators and state mechanisms, observed objects, nested properties,
   parent-child data flow, storage, persistence, rendering controls, reuse, initialization,
   `ForEach` or `LazyForEach`, animation, and third-party boundaries.
3. Map each original read, write, observation, refresh, initialization, persistence, and ownership
   behavior to its intended V2 behavior using scenario-specific migration guidance.
   [HMOS-ARKUI-MIGRATION]
4. Identify unsupported or unverified V1/V2 mixing boundaries. Order migration batches by data-flow
   dependency and risk; define a rollback point for every batch.
5. Migrate one bounded batch. Avoid global token or decorator substitution.
6. Run the configured build check. Run lint only when explicitly required, then exercise reads,
   writes, nested changes, parent-child propagation, refresh, initialization, persistence, reuse,
   and material performance or regression paths for that batch.
7. Compare observations with the baseline before continuing to the next batch.

**Output and evidence:** V1 inventory, V1-to-V2 behavior map, dependency-ordered batch plan,
documented mixing constraints, per-batch patch and rollback point, compile and behavioral results,
and remaining migration scope.

**Bounded retry:** each batch allows one implementation and at most two corrective iterations.
Only a verified batch may unlock its dependents. A failed batch is isolated or reverted before
other dependent batches proceed.

**Negative paths:** stale UI, missing or excess refresh, nested-observation failure, initialization
error, persistence change, performance regression, or unsupported mixing blocks the batch. Preserve
the reproduction and hand unresolved semantics to the ArkUI or architecture owner.

### 7. Run final compilation verification through `devecocli`

1. Confirm the installed `devecocli` version, authorization, project identity, and availability of
   `devecocli build`. Resolve exact syntax from the tool; project overlays supply product, module,
   profile, mode, and output expectations.
2. Run `devecocli build` as the only default final compilation gate, using verified project,
   product, module, and build-mode inputs. Record
   invocation, environment, exit status, diagnostics, and located artifacts.
3. Do not run `devecocli check lint` or `devecocli check compat` by default. Run either only when
   the task contract or user explicitly requests its distinct evidence; otherwise record it as
   `skipped`, not `passed`.
4. Run project-defined unit, coverage, self-inspection, emulator, physical-device, accessibility,
   security, performance, power, and stability checks required by the task contract.
5. Exercise material expected and negative paths on declared targets. Keep static, compile, build,
   package, install, runtime, device, signing, and release results separate. [HMOS-TESTING]

**Output and evidence:** command ledger, environment and target identities, raw or linked reports,
artifact inventory, acceptance-to-result mapping, skipped and unavailable checks, and residual
failures.

**Bounded retry:** for repairable source diagnostics, use at most three diagnose-fix-rerun
iterations across the affected check. Do not reset the counter by switching commands. Environment,
permission, signing, or device failures are not source-repair attempts and must be handed off
without speculative edits.

**Negative paths:** an unavailable subcommand, unresolved scope, failing command, missing artifact,
or absent target remains failed or unverified. Never invent flags or output paths, suppress a
diagnostic, loosen configuration, delete a test, broaden an ignore, alter signing, or change an
unrelated file to obtain a pass.

### 8. Reconcile evidence and hand off

1. Rerun the narrow checks affected by the final remediation, then the full authorized check set
   required by the task contract.
2. Index each criterion to changed artifacts, exact method, observed result, and evidence location.
   Label results `passed`, `failed`, `skipped`, `unavailable`, or `blocked`.
3. Review the changed scope for unintended architecture, dependency, permission, signing, data,
   or release effects.
4. Record unchanged scope, assumptions, warnings, residual risks, rollback guidance, approvals
   still required, and the recipient for every unresolved decision.
5. Transfer the candidate source or artifact and evidence to the authorized reviewers and release
   owner. A successful build does not authorize signing, installation, distribution, or rollout.

**Output:** reviewable change set, architecture or migration record where applicable, evidence
index, finding dispositions, verification summary, residual-risk register, recovery note, and
handoff status.

**Negative path:** do not declare completion or release readiness when a required check fails,
evidence is missing, the supported matrix was not exercised, or an accountable authority has not
decided a blocker. Preserve the last known good state and reproducible failure.

## Consolidated Negative-Path Controls

| Condition | Required response | Effect |
| --- | --- | --- |
| SDK/API baseline is unknown | Stop version-sensitive retrieval conclusions and mutations; request the baseline. | Dependent architecture, implementation, migration, and compatibility claims are blocked. |
| Local Skill corpus conflicts with primary guidance or observed diagnostics | Retain both, prefer version-relevant primary guidance and observations, and escalate unresolved conflict. | The local result remains provisional. |
| Required API signature or replacement is unverified | Do not invent or substitute it. | Dependent change is blocked. |
| State migration changes data flow or observation | Stop, isolate or revert the batch, and preserve reproduction evidence. | Batch and dependents remain failed. |
| Tool, command, project scope, permission, device, or environment is unavailable | Do not guess or bypass it; provide a reproducible manual or owner handoff. | Corresponding evidence class is unavailable or blocked. |
| Lint or compatibility was not explicitly requested | Record the check as `skipped`; do not run it as a default gate. | Lint or compatibility claims remain unverified. |
| Build succeeds but artifact cannot be located | Preserve command output and investigate only within the retry bound. | Packaging claim remains unverified. |
| Automated repair reaches its bound | Stop mutation, retain every iteration and the last known good state. | Hand remaining diagnosis to the accountable engineer. |
| Signing, distribution, or production action is requested without explicit authority | Stop before the controlled action. | Hand the verified candidate to the authorized release owner. |
| Secrets, customer data, or private production architecture would enter evidence | Refuse that path and request sanitized inputs or a controlled environment. | Affected verification remains blocked. |

## Permissions and Handoffs

- Read-only documentation retrieval and local inspection still require access to the supplied
  project and sources. Network, private repository, or protected documentation access is not
  inferred.
- Source, configuration, dependency, module-topology, generated-file, and test changes require
  explicit task authorization for their stated scope.
- Emulator and physical-device use, protected data, signing material, application-market access,
  distribution, production operation, and rollback execution require distinct authorization.
- Product and design owners receive unresolved behavior, visual, content, interaction, and
  accessibility decisions with expected and negative-path evidence.
- Platform or architecture owners receive SDK/API baseline selection, Stage exceptions, process
  and concurrency questions, module-topology changes, cross-application reuse, and unresolved
  V1/V2 boundaries.
- Security and privacy owners receive permission, authentication, storage, sensitive-data, and
  trust-boundary findings without secrets in the record.
- Test, compatibility, performance, power, and stability owners receive matrix gaps, failed or
  unavailable environments, threshold questions, and reproducible results.
- Release owners receive build artifacts, signing and publication prerequisites, approval state,
  residual risks, and rollback requirements. The workflow never performs or authorizes release by
  implication.

Every handoff states the decision requested, affected requirements and modules, options, impact,
sanitized evidence, last known good state, urgency if supplied, receiving authority, and required
return information.

## Recovery and Completion Boundary

Before handoff, document the smallest reversible unit, dependency order, configuration and state
effects, generated or packaged artifacts, and the method for verifying restored behavior. Execute
only an organization-approved rollback. If none is supplied, mark rollback `needs-org-input`.

Completion requires evidence and actual behavior to agree, every acceptance criterion to have a
disposition, no known in-scope P0 or P1 issue, all skipped or blocked checks to remain visible, and
the receiving owner to have enough context to continue without chat history. It does not imply
Domain activation, signing approval, market acceptance, production readiness, or release.

## Organization Inputs Still Required

This reusable workflow intentionally does not define supported SDK/API/toolchain/device matrices,
project structure, architecture exceptions, commands and flags, reviewer roles, test environments,
quality or coverage thresholds, accessibility targets, security and privacy policy, signing and
distribution controls, release blockers, evidence retention, or rollback procedures. Until an
authoritative overlay or task contract supplies them, dependent outcomes remain `needs-org-input`.

## Source and Capability Basis

This iteration uses the validated `engineering.harmonyos` research ledger: ArkTS constraints
[HMOS-ARKTS], Stage architecture [HMOS-STAGE], ArkUI V2 observation [HMOS-ARKUI-V2], V1-to-V2
migration [HMOS-ARKUI-MIGRATION], package semantics [HMOS-PACKAGES], testing services
[HMOS-TESTING], and registered identity [REPO-HARMONYOS-IDENTITY]. It also composes the six
user-supplied capability units summarized in `skills/README.md` as provisional workflow input;
their bundled corpora, tool names, examples, and version claims are not independently promoted to
authority by this document.
