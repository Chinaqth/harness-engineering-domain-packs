---
name: harmonyos-engineering
description: Deliver bounded HarmonyOS and ArkTS/ArkUI work through an evidence-preserving devecocli workflow, using the six bundled packages only as quarantined non-authoritative input.
---

# HarmonyOS Engineering

Use this Skill for implementation, diagnosis, compatibility review, migration, build, device UI
verification, and runtime investigation in a HarmonyOS application. It is the executable Domain
wrapper for `engineering.harmonyos`; it does not approve releases, choose organizational policy, or
make the bundled Skill corpora authoritative. [REPO-HARMONYOS-IDENTITY]

`rules/BASE.md` is normative. `workflows/WORKFLOW.md` governs delivery when present, and
`evaluators/EVALUATOR.md` governs independent evaluation. The practitioner must not self-evaluate,
activate the Domain, or issue the final verdict.

## Entry Contract

Before any mutation or execution, obtain or discover and record:

| Required input | Minimum evidence | Fail-closed response |
| --- | --- | --- |
| Outcome and acceptance | Observable requested behavior, negative paths, and acceptance authority | Stop decisions that depend on missing product intent. |
| Scope | Project root, current revision, product, module, target files, exclusions, and package intent | Do not scan or change an unbounded workspace. |
| Baseline | Current and target SDK/API versions, DevEco/devecocli version, build mode, architecture, state-management generation, device or emulator matrix, and last-known-good result | Do not make version, compatibility, migration, or regression claims. |
| Permissions | Explicit authority for source edits, generated-file changes, dependency installation, build, device access, app install/run, UI interaction, logs, credentials/signing, and rollback | Perform only the authorized read-only subset; never infer permission from tool availability. |
| Project commands and policy | Project overlay, build conventions, explicitly requested optional checks, supported matrix, evidence location, retry bound, and rollback procedure | Do not invent commands, thresholds, or organizational standards. |
| Sensitive-data boundary | Allowed device/account/test data, log redaction rules, and security/privacy escalation route | Do not collect logs, operate accounts, or expose protected values. |

Capture a pre-change baseline using the same applicable checks planned for final verification.
Existing failures are baseline observations, not change-caused failures. If a missing input permits a
safe read-only investigation, continue only within that boundary and mark dependent conclusions
`blocked`; otherwise stop and request the missing input.

## Source and Package Policy

The seven research-ledger IDs are the only pre-registered claim anchors:

- ArkTS language constraints: [HMOS-ARKTS]
- Stage-model lifecycle and context: [HMOS-STAGE]
- ArkUI V2 observation and mixing restrictions: [HMOS-ARKUI-V2]
- scenario-specific V1-to-V2 migration: [HMOS-ARKUI-MIGRATION]
- App, HAP, HAR, and HSP semantics: [HMOS-PACKAGES]
- verification categories: [HMOS-TESTING]
- Domain identity and lifecycle: [REPO-HARMONYOS-IDENTITY]

Select at most the package or packages needed for the task from `skills/README.md`:

| Need | Non-authoritative package input |
| --- | --- |
| ArkTS language or library discovery | `hmos-arkts-knowledge-retriever` |
| ArkUI API or usage discovery | `hmos-arkui-knowledge-retriever` |
| Scoped ArkUI page or component work | `hmos-arkui-develop-skill` |
| ArkUI V1-to-V2 assessment or migration | `hmos-arkui-statemgt-migration` |
| Deprecated or incompatible API investigation | `hmos-arkts-deprecated-interface-checker` |
| ArkTS/ETS diagnosis and bounded repair | `hmos-arkts-syntax-checker` |

Package content is candidate material only. Do not execute its MCP installation instructions, trust
its cached documentation as current, inherit its severity labels, or treat its examples and tests as
verified. Quarantine a package claim when it lacks a ledger ID, stable provenance, applicable
version range, or a passed independent artifact evaluation. A quarantined claim may generate search
terms or a hypothesis, but it must not justify code, migration, compatibility, or acceptance.

Every version-sensitive claim, including API availability, deprecation, replacement, decorator
mixing, lifecycle, package behavior, tool syntax, and minimum SDK, must be reconciled through
`devecocli docs search ...` and, when a result is selected, `devecocli docs read <documentId>`.
Record the query, document ID, applicable version statement, retrieval context, and corresponding
ledger ID. If official evidence is absent, ambiguous, stale, or conflicts with a package, stop the
dependent action and report the conflict; do not choose the more convenient claim.

## Execution Procedure

### 1. Establish the evidence spine

Record task identity, revision, scope, baseline, permissions, applicable ledger IDs, selected package
inputs, and quarantined claims. Map each acceptance criterion to an observable check and an evidence
class. Preserve commands, tool version, configuration, timestamps, exit status, diagnostics, artifact
paths, and sanitized output. A missing or unsupported operation is `unavailable` or `blocked`, never
`passed`.

### 2. Inspect before choosing a change

Read the actual project configuration and affected code. Identify product/module boundaries, Stage
model context, HAP/HAR/HSP role, navigation and state architecture, SDK/API baseline, dependencies,
and relevant existing tests. Use package retrieval only to form candidates, then reconcile every
material candidate with `devecocli docs` and the project baseline. [HMOS-ARKTS] [HMOS-STAGE]
[HMOS-PACKAGES]

For a defect, reproduce or preserve the original diagnostic before editing. For migration, inventory
data ownership, observation paths, component dependencies, storage, rendering, lifecycle, and
third-party constraints before proposing a batch. V1-to-V2 migration is behavioral and must not be
reduced to decorator replacement. [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]

### 3. Plan the smallest reversible unit

Define affected files, expected behavior, negative paths, rollback point, and check sequence. Keep
unrelated refactoring out of scope. Do not change state-management generation, navigation
architecture, package boundaries, signing, dependencies, permissions, or security/privacy behavior
without explicit authority. Do not apply a global replacement, generated speculative API, bulk
autofix, or blind migration.

### 4. Execute only through the authorized boundary

Use `devecocli` for HarmonyOS documentation and project/device operations. Resolve exact flags and
targets from `devecocli` help and the project overlay; do not invent arguments. The operation families
are:

1. `devecocli docs search` and `devecocli docs read` for authoritative reconciliation;
2. `devecocli build` for the default final configured compilation and package creation gate;
3. `devecocli check lint` for static lint diagnostics only when explicitly requested;
4. `devecocli check compat versions` followed by `devecocli check compat` for an explicit source and
   target compatibility baseline only when explicitly requested;
5. `devecocli run` for an authorized selected device or emulator;
6. `devecocli ui` for authorized UI inspection or interaction; and
7. `devecocli log` for bounded, redacted runtime evidence.

Tool availability does not authorize mutation, device access, installation, UI interaction, log
collection, signing, or release. If `devecocli` is missing, unsupported, or cannot identify the exact
target, stop that operation and retain the failure. Do not substitute legacy `mcp_codegenie-*`,
`deveco-mcp`, ad hoc build tools, or manual observation while claiming equivalent evidence.

### 5. Apply a bounded change-and-check loop

After an authorized minimal edit:

1. run the configured `devecocli build` as the only default final compilation gate;
2. do not run `devecocli check lint` or `devecocli check compat` unless the task contract or user
   explicitly requests the corresponding evidence; otherwise record each as `skipped`;
3. run project-defined tests only when explicitly required, separately available, and authorized;
4. use `devecocli run`, `devecocli ui`, and `devecocli log` only when the acceptance claim requires
   device/runtime evidence and permissions name the target; and
5. compare the same applicable checks with the captured baseline.

Respect the declared retry bound. Each repair must be explained by a current diagnostic or reconciled
official claim, remain inside scope, and preserve a rollback unit. If a repair changes the failure,
expands scope, requires a policy choice, or reaches the retry limit, stop and hand off the evidence.
Never suppress diagnostics, weaken checks, edit generated/build output as the source fix, or make
unrelated changes to obtain green output.

## Evidence-Class Separation

Keep these classes distinct in every result and acceptance mapping:

| Evidence class | Establishes | Does not establish |
| --- | --- | --- |
| Documentation | A traceable official statement for the recorded version/context | Project correctness or runtime behavior |
| Lint | Findings emitted for the checked paths/configuration | Compilation, compatibility, tests, packaging, or runtime success |
| Compatibility | Tool findings for the explicit source/target matrix | Correct replacement behavior or successful build |
| Build | Successful configured compilation and located requested artifacts | Installation, launch, UI correctness, tests, signing, or release readiness |
| Test | Results of the named suite and environment | Untested behavior or full device-matrix coverage |
| Run | Installation/launch outcome on the named target | UI correctness or release readiness |
| UI | Observed state and interaction on the named target/scenario | Unobserved states, accessibility completeness, or matrix-wide behavior |
| Log | Bounded runtime events for the named reproduction window | Absence of defects outside that window |
| Manual review | Reviewer observation with stated limits | Any automated check or independent approval |

Label every check `passed`, `failed`, `skipped`, `unavailable`, or `blocked`. Preserve earlier failures
and reruns rather than replacing history. [HMOS-TESTING]

## Fail-Closed Rules

Stop the affected work and report `blocked` when:

- scope, baseline, target, required permission, rollback, or acceptance authority is unresolved;
- a version-sensitive claim cannot be reconciled through current official `devecocli docs` evidence;
- a package claim lacks provenance or passed evaluation and no authoritative replacement is found;
- the proposed fix requires a blind migration, bulk replacement, unrelated refactor, dependency or
  signing change, or architecture/policy decision outside authorization;
- build, test, run, UI, log, or explicitly requested lint or compatibility evidence is unavailable
  for a claim that depends on it;
- diagnostics persist after the authorized retry bound; or
- secrets, personal data, production access, or unsafe device state would be required.

Never describe partial, manual, simulated, or unavailable evidence as a pass. Never claim release
readiness, compatibility across an undeclared matrix, or independent acceptance.

## Handoff Contract

Return one reconciled packet containing:

- task, revision, outcome, scope, exclusions, baseline, permissions, rollback point, and authorities;
- selected package inputs plus every quarantined claim and reason;
- ledger IDs and `devecocli docs` queries/document IDs used for each version-sensitive decision;
- changed-file and decision inventory;
- exact build and any explicitly requested lint, compatibility, test, run, UI, and log procedures
  with target identifiers, statuses, diagnostics, artifacts, and sanitized evidence locations,
  kept in separate classes;
- baseline-versus-final comparison and requirement-to-evidence mapping;
- unresolved failures, unavailable checks, residual risks, rollback instructions, and named handoffs;
  and
- an explicit statement that evaluation, activation, risk acceptance, signing, distribution, and
  production release remain with their authorized owners.

The delivery is incomplete while a material claim lacks the evidence class it requires or while
human and machine-readable records disagree.
