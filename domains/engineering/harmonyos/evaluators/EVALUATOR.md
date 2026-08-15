# HarmonyOS Engineering Delivery Evaluator

## Purpose, Scope, and Independence

This evaluator determines whether an `engineering.harmonyos` outcome is supported by complete,
version-relevant, reproducible evidence. It evaluates only the requirements and HarmonyOS surfaces
declared by the authorized task contract. It does not grant architecture exceptions, select an
organization's supported SDK or device matrix, approve security or privacy risk, authorize signing
or distribution, accept a release, or change the Domain lifecycle.

The evaluator must be independent of the author of the evaluated outcome. It records evidence,
findings, and a verdict; it does not repair implementation artifacts, suppress diagnostics, change
test scope, or reinterpret missing evidence as success.

Project overlays or task contracts must supply project-specific commands, products, modules,
profiles, targets, quality thresholds, permissions, and acceptance authorities. The evaluator must
not invent them. A missing organization-owned fact is `needs-org-input` and prevents the dependent
claim. When the missing fact is required to execute or judge an applicable acceptance criterion,
that criterion is `blocked`.

## Evaluation Entry Gate

Bind the evaluation to all of the following before issuing a verdict:

- task identifier, accepted requirements, material positive and negative paths, and acceptance
  authority;
- immutable revision or artifact identity, changed-file and changed-module inventory, and baseline;
- HarmonyOS release, compile SDK, compatible or minimum API level, build toolchain and `devecocli`
  versions, target devices or form factors, and compatibility matrix supplied by the project;
- affected Stage components, modules, packages, ArkTS sources, ArkUI components, state-management
  generation, API uses, and behavior paths;
- authorized tools, subcommands, project scope, environments, devices, permissions, evidence
  locations, and retry limits;
- applicable project overlay, implementation handoff, known failures, exclusions, residual risks,
  and rollback expectations; and
- versions of `DOMAIN.md`, `rules/BASE.md`, `workflows/WORKFLOW.md`, and the validated research
  ledger used by the delivery.

Return `blocked` when the evaluated revision, accepted requirements, evidence provenance, or a
required version baseline cannot be established. Continue with criteria that remain decidable when
an optional organization input is absent, but never extend their conclusions to the dependent
compatibility, quality, runtime, device, signing, release, or activation claim.

## Required Evidence Contract

The evaluation record must contain an index with one entry for every applicable criterion. Each
entry must identify:

1. criterion ID, accepted requirement, and applicable Domain rule;
2. affected file, component, ability, module, package, API, state path, device, or user scenario;
3. evaluated revision, declared SDK/API/toolchain baseline, environment, and target identity;
4. authoritative source ID, document location, applicable version, and retrieval date or context;
5. exact authorized procedure or command actually executed, working scope, inputs, relevant
   configuration, tool version, exit status, and output location;
6. expected behavior, observed behavior, and criterion status;
7. positive and negative paths exercised, including skipped or unavailable paths;
8. retry count, variability, stale or conflicting results, and disposition;
9. stable location of raw or directly inspectable evidence, timestamp, and evidence producer;
10. sanitization applied to secrets or protected data, linked findings, residual risk, owner, and
    required handoff.

Permitted criterion statuses are `pass`, `fail`, `blocked`, `not-applicable`, and
`needs-org-input`. `not-applicable` requires an authoritative scope reason. A summary, screenshot,
generated snippet, local knowledge-index result, or claimed command is not a substitute for raw or
directly inspectable evidence. Failed, skipped, unavailable, flaky, and blocked results remain
visible. Evidence must distinguish documented claims from observed tool behavior and assumptions.

## Acceptance Criteria

### HMOS-EVAL-01 — Scope, version, and official-source traceability

**Pass conditions**

- Every claimed outcome maps to an accepted requirement, affected surface, evidence entry, and
  declared HarmonyOS, SDK, API, toolchain, and target baseline.
- Every consequential Stage, ArkTS, ArkUI, package, compatibility, deprecation, or migration claim
  cites version-relevant Huawei Developer documentation through a source ID and stable document
  location [HMOS-STAGE] [HMOS-ARKTS] [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]
  [HMOS-PACKAGES] [HMOS-TESTING].
- Local indexes, bundled Skill references, generated examples, and remembered APIs are reconciled
  with current official documentation and observed tool results before use.
- Claims do not exceed the exact revisions, configurations, modules, versions, or targets evaluated.

**Required evidence:** requirement-to-evidence map; baseline and changed-surface inventory;
`devecocli docs` query and result records when available and authorized; source IDs, document
locations, applicable versions, and retrieval context; conflicts and their disposition.

**Negative paths:** inspect an unknown version, stale local reference, ambiguous API signature, and
official-source/tool disagreement when present. An unresolved material version or source conflict is
`blocked`; selecting the favorable source or silently assuming the newest installed SDK is `fail`.

### HMOS-EVAL-02 — Stage architecture and lifecycle behavior

**Pass conditions**

- Affected `UIAbility` and applicable system-defined `ExtensionAbility` responsibilities, lifecycle,
  context, window, page, configuration, process, thread, and concurrency boundaries preserve the
  accepted architecture [HMOS-STAGE].
- Entry and feature module changes are consistent with the declared Stage model and do not introduce
  an unapproved architecture or navigation migration.
- Lifecycle and context-dependent behavior is exercised in the applicable states and targets.

**Required evidence:** architecture decision or preserved-convention record; affected component and
module map; inspectable configuration and implementation; lifecycle or state-transition traces;
relevant build and runtime observations; approved exception, when one exists.

**Negative paths:** exercise applicable creation, foreground/background transition, termination or
recreation, configuration change, missing context, unavailable window, and interrupted asynchronous
work. Static inspection alone cannot pass lifecycle behavior.

### HMOS-EVAL-03 — ArkTS static correctness, lint, and compilation distinction

**Pass conditions**

- Affected ArkTS code satisfies the declared language, type, module, kit, null-safety, concurrency,
  and project lint requirements for the selected baseline [HMOS-ARKTS].
- When available and authorized, `devecocli check lint <path>` is run at the resolved changed-file or
  project scope. Its result is reported as lint evidence only.
- Compilation or `devecocli build` results are reported separately. Neither lint success nor source
  inspection is represented as compilation, build, runtime, compatibility, or device evidence.
- Diagnostics retain file, location, rule or code, severity, exact invocation, configuration, and
  disposition; no ignore is broadened and no unrelated source is changed to force a pass.

**Required evidence:** changed ArkTS inventory; declared language and lint configuration; tool
availability and version record; exact lint and compile/build invocations, exit statuses, raw
diagnostics, report locations, retry counts, and unresolved findings.

**Negative paths:** include a representative invalid syntax or type case from the authorized test
scope, or preserve an observed failing diagnostic and its repair/rerun evidence. An unavailable lint
subcommand blocks the lint claim but does not imply compilation failure. A passing build never erases
an applicable lint failure.

### HMOS-EVAL-04 — ArkUI rendering, interaction, and state behavior

**Pass conditions**

- Affected ArkUI components render and behave according to the accepted state, data-flow,
  navigation, interaction, layout, lifecycle, and accessibility requirements on every declared
  target.
- API signatures, decorators, event contracts, and version support are traceable to the selected
  baseline; generated or cached snippets are independently checked before being called verified.
- New projects, new ArkUI components, and rewritten state-managed surfaces use State Management V2
  and introduce no V1 components, decorators, storage, or observation mechanisms.
- State changes produce the expected UI transitions without stale, lost, duplicated, or unintended
  updates. Existing V2 paradigms are preserved; affected V1 surfaces follow the migration criterion
  or remain an explicitly unchanged, bounded legacy dependency outside the authorized scope.

**Required evidence:** component and state-flow inventory; source-backed API record; inspectable
implementation; per-target render captures where assertions are insufficient; interaction and
state-transition tests; runtime logs; accessibility evidence required by the task contract.

**Negative paths:** exercise applicable empty, loading, error, disabled, repeated interaction,
interruption, invalid input, navigation recovery, configuration, and boundary-size states. A build
or snapshot without interaction evidence cannot establish ArkUI behavior.

### HMOS-EVAL-05 — Deprecation and API compatibility disposition

**Pass conditions**

- Every affected deprecated or compatibility-sensitive interface is evaluated against the declared
  SDK/API baseline and target matrix, using current official documentation [HMOS-ARKTS].
- When available and authorized, `devecocli check compat` is run with verified scope and inputs;
  compatibility findings are not inferred from lint codes.
- Each finding records location, affected targets, documented replacement or absence of one,
  behavioral and package impact, disposition, and post-change verification.
- No blind substitution, undocumented replacement, target removal, or compatibility-policy change is
  used to obtain a pass.

**Required evidence:** interface inventory; official deprecation and replacement references with
versions; exact compatibility invocation and raw results; before/after diagnostics; per-target
disposition; exception or owner decision where replacement is unavailable.

**Negative paths:** assess unavailable replacement, replacement unsupported on a target, behavior
change, transitive use, and mixed-version dependency when applicable. A deprecated interface without
a verified safe disposition is `fail`; an absent required baseline, tool, or decision is `blocked`.

### HMOS-EVAL-06 — ArkUI V2 architecture and V1-to-V2 behavioral migration

**Pass conditions**

- The evaluated architecture identifies State Management V2 as the only target for new projects,
  new components, and rewritten state-managed surfaces. V1 appears only as inventoried legacy
  migration input or an unchanged boundary outside the authorized scope.
- Migration maps each original V1 state owner, initialization rule, observation boundary, parent-child
  flow, bidirectional update, application storage behavior, monitor, render loop, reuse lifecycle, and
  animation behavior to an explicit intended V2 behavior [HMOS-ARKUI-V2]
  [HMOS-ARKUI-MIGRATION].
- The change is evaluated by scenario and data-flow behavior, not by decorator-name substitution.
- Mixed V1/V2 boundaries are inventoried and either proven compatible for the declared baseline or
  retained behind an approved staged boundary.
- Each migration batch independently passes applicable static, build, and behavioral regression
  checks before dependent batches are accepted.

**Required evidence:** architecture-generation decision; changed-surface scan for V1 constructs;
before/after state and data-flow map; V1 construct inventory; V2 mapping and official references;
mixed-mode boundary record; out-of-scope legacy boundary and handoff record; batch identities;
compile/build results; runtime state-transition and regression results; rollback unit for each batch.

**Negative paths:** exercise nested mutation, parent-to-child and child-to-parent updates,
reinitialization, repeated rendering, storage reconnect or restoration, reuse, and animation timing
when applicable. Lost observation, changed ownership, unintended update, or unverified mixed-mode
behavior is `fail`, even when compilation succeeds. Any newly introduced V1 state-management usage
is `fail`; a baseline that cannot support required V2 behavior is `blocked`, not a V1 exception.

### HMOS-EVAL-07 — Module, HAP/HAR/HSP, and App Pack integrity

**Pass conditions**

- Entry and feature HAP, HAR, HSP, and App Pack choices match the accepted delivery, installation,
  runtime, reuse, and publication requirements [HMOS-PACKAGES].
- Module dependencies, package metadata, products, profiles, build modes, and artifacts correspond to
  the declared project configuration and do not rely on invented paths or flags.
- `devecocli build`, when available and authorized, succeeds for every required product/module/mode
  combination, and located artifacts are tied to the exact invocation and revision.
- Packaging success is not represented as installability, signature validity, runtime success,
  device compatibility, publication authorization, or release readiness.

**Required evidence:** module and dependency map; package decision; relevant configuration;
`devecocli build` availability, version, invocation, exit status, raw diagnostics, and artifact
inventory with identity or digest; required matrix results; signing and release status kept separate.

**Negative paths:** inspect missing dependency, invalid or unavailable configuration, absent expected
artifact, wrong module boundary, and failed required build combination when applicable. A missing
artifact after a zero exit status is `fail`; unavailable signing permission leaves signing unverified
and must not trigger a bypass.

### HMOS-EVAL-08 — Runtime, emulator, and physical-device evidence

**Pass conditions**

- Every runtime or device claim is supported by execution on the exact declared emulator or physical
  device target, with OS/API level, model or profile, configuration, scenario, and result recorded.
- Required application or atomic-service self-inspection, unit, coverage, runtime, accessibility,
  security, performance, power, and stability checks remain distinct evidence classes
  [HMOS-TESTING].
- Material expected, failure, recovery, lifecycle, and interaction paths are exercised on the targets
  required by the task contract.
- Simulator or emulator results are not generalized to physical devices, and one device result is not
  generalized to an unevaluated matrix.

**Required evidence:** target matrix; environment and target identity; installation and launch record
when authorized; exact test procedures; raw logs, reports, traces, and captures; expected and observed
behavior; per-target results; skipped and unavailable targets.

**Negative paths:** exercise applicable launch failure, permission denial, interruption, background
and resume, constrained resource, configuration or form-factor change, and recovery behavior. If a
required device or permission is unavailable, the dependent criterion is `blocked`; build success
cannot substitute for it.

### HMOS-EVAL-09 — Tool integrity, permissions, and fail-closed execution

**Pass conditions**

- Before any tool claim, evidence confirms that `devecocli`, the required subcommand (`docs`,
  `check lint`, `check compat`, or `build`), project identity, scope, environment, and permission are
  available and applicable.
- Exact syntax is resolved from the installed tool or authoritative interface; flags, products,
  modules, profiles, output paths, and credentials are never inferred from cached Skill examples.
- Automated source-repair attempts stop after at most three diagnose-fix-rerun iterations across the
  affected check. Switching commands does not reset the counter.
- Environment, dependency, device, signing, or permission failures are handed off without speculative
  source changes or control bypass.

**Required evidence:** availability and authorization checks; installed tool and subcommand versions;
resolved project scope; exact commands and exit statuses; raw outputs; changed-file inventory; common
retry ledger; unavailable dependency and permission record; reproducible handoff.

**Negative paths:** required subcommand absent, authentication or permission denied, project not
recognized, dependency unavailable, malformed scope, environment failure, and retry exhaustion. Any
claim whose only evidence path is unavailable is `blocked`. Fabricated execution, suppressed output,
weakened configuration, deleted tests, broadened ignores, unauthorized access, or unrelated mutation
is `fail` and may be severity `P0` or `P1` according to impact.

### HMOS-EVAL-10 — Completion, recovery, and handoff integrity

**Pass conditions**

- The handoff includes evaluated revision, changed and unchanged scope, evidence index, source IDs,
  exact executed checks, failed and unavailable checks, assumptions, residual risks, required
  approvals, and named receiving authorities when known.
- Completion claims are limited to criteria that passed; lint, compatibility, build, package,
  runtime, device, signing, release, and activation states are reported separately.
- Recovery guidance identifies the smallest reversible batch or artifact and uses a project-approved
  rollback procedure, or marks it `needs-org-input`.
- No successful engineering result is represented as signing permission, distribution authority,
  risk acceptance, release approval, or Domain activation.

**Required evidence:** delivery handoff; criterion-to-evidence map; finding and decision logs; residual
risk register; recovery or rollback reference; approval state; unresolved organization gaps; last
known good revision or artifact where supplied.

**Negative paths:** review unavailable reviewer, permission, device, signing asset, rollback procedure,
release authority, or evidence store. Silence, an empty reviewer list, a successful build, or a
generated package never constitutes approval.

## Cross-Criterion Evidence Rules

### Freshness and version relevance

Evidence is current only when bound to the evaluated revision and the declared SDK, API, toolchain,
configuration, dependency, and target baseline. Earlier evidence may be reused only when the record
proves that neither the affected implementation nor any material input changed. A change in official
documentation, API level, SDK, dependency, toolchain, module configuration, device image, or target
matrix makes dependent evidence stale until reconciled or rerun. Stale evidence cannot pass.

### Reproducibility and raw results

An independent qualified reviewer must be able to identify the revision, reconstruct the authorized
scope and environment, execute the recorded procedure, locate raw outputs, and compare expected with
observed behavior. Protected infrastructure may use an authorized execution record with a named access
owner, but unavailable access is `blocked` when it prevents a trustworthy decision. Secrets,
credentials, signing material, production data, and protected user data must be sanitized without
destroying reproducibility.

### Evidence-class separation

Maintain distinct entries for documentation retrieval, lint, compatibility analysis, compilation,
build, package creation, unit tests, coverage, self-inspection, emulator execution, physical-device
execution, accessibility, security, performance, power, stability, signing, publication, release,
and rollback. A success in one class proves only that class. An unexecuted command, predicted artifact,
or generated report is not evidence.

### Conflicting, flaky, and negative evidence

Contradictory current results remain visible. The affected criterion is `fail` when an applicable
requirement is contradicted, or `blocked` when the evidence shows that a required target could not be
evaluated. Reruns do not erase failures; record root cause, scope, variability, and disposition. Never
select a favorable run, target, or source to conceal uncertainty.

## Severity Classification

Apply a stricter approved organization policy when available. Otherwise use this impact model:

| Severity | Classification |
| --- | --- |
| `P0` | Active or readily exploitable critical trust-boundary loss; exposed signing credentials or protected data; destructive corruption; unauthorized production, signing, or distribution action; or immediate widespread danger requiring authorized emergency response. |
| `P1` | Required primary behavior is unusable without acceptable recovery; a supported target cannot perform it; an architecture, lifecycle, state, compatibility, packaging, security, integrity, or release-blocking requirement is materially violated. |
| `P2` | A material secondary behavior, negative path, compatibility case, device target, accessibility behavior, quality objective, or evidence requirement is unmet, but impact is bounded and the primary path retains a documented recovery. |
| `P3` | Low-impact defect, documentation or evidence weakness, or maintainability issue that does not invalidate the applicable outcome but requires tracked correction. |

Severity describes impact and never grants risk-acceptance authority. If impact depends on a missing
organization policy, target population, or release classification, record a provisional severity,
`needs-org-input`, and the required decision authority. Never lower severity because a fix, reviewer,
device, or permission is unavailable.

## Criterion and Overall Verdict Semantics

- `pass`: every applicable pass condition is supported by fresh, reproducible evidence, required
  negative paths were exercised, and no unresolved contradictory result exists.
- `fail`: observed behavior contradicts an applicable requirement, or required available evidence or
  a material authorized path was omitted.
- `blocked`: a required input, source, dependency, artifact, environment, tool, subcommand, permission,
  target, or trustworthy evidence path is unavailable, so the criterion cannot be determined.
- `not-applicable`: an authoritative scope source demonstrates that the criterion does not apply.
- `needs-org-input`: baseline evaluation can continue, but a missing organization-owned matrix,
  threshold, command, policy, reviewer, permission, or authority prevents the dependent claim.

The overall verdict is:

- `pass` only when every applicable criterion is `pass`, no unresolved `P0` or `P1` exists, all
  required evidence is fresh and reproducible, and no approval or permission is inferred;
- `fail` when any applicable criterion is `fail`; or
- `blocked` when no criterion fails but at least one required criterion is `blocked`.

Record `needs-org-input` separately from the behavioral verdict. A reusable professional baseline
may pass while organization acceptance, signing, release, or activation remains unavailable. If the
task entry contract requires the missing organization input, the overall verdict is `blocked`.

## Required Evaluation Output

Return an evaluation record containing:

- task, revision, scope, exclusions, evaluator identity, evaluation time, baseline, environment, and
  target matrix;
- applied Domain, rule, workflow, overlay, toolchain, and source-ledger versions;
- criterion-by-criterion status, requirement mapping, evidence links, and positive/negative paths;
- separate results for every applicable evidence class, including exact `devecocli` commands;
- findings with severity, affected requirement and target, reproduction, disposition, and owner;
- stale, conflicting, flaky, skipped, unavailable, and sanitized evidence notes;
- retry ledger, residual risks, recovery implications, handoffs, and required approvals;
- organization-specific gaps and the exact claims each prevents; and
- overall `pass`, `fail`, or `blocked` verdict plus a separate organization-readiness statement.

The record must never claim that the evaluator approved an exception, accepted risk, authorized a
controlled operation, approved a release, or activated `engineering.harmonyos`.

## Organization-Specific Gaps

The following remain `needs-org-input` until supplied authoritatively:

- reviewer roles and decision rights for HarmonyOS engineering, architecture, UX, accessibility,
  security, privacy, testing, signing, distribution, and release;
- supported HarmonyOS, SDK, API, DevEco Studio, `devecocli`, dependency, emulator, physical-device,
  form-factor, and screen-mode matrices;
- repository, dependency, device, signing, distribution, production, recovery, and rollback
  permissions;
- project Stage architecture, module topology, navigation and state-management conventions, design
  system, accessibility policy, dependency policy, and compatibility policy;
- authoritative project commands and evidence formats for install, lint, compatibility, compile,
  build, test, coverage, self-inspection, package, sign, launch, inspect, publish, and rollback; and
- thresholds for coverage, static analysis, compatibility, accessibility, security, stability,
  performance, power, quality, and release blocking.

These gaps prevent dependent organization acceptance, release, and activation claims. They do not
authorize weakened evidence, fabricated defaults, or bypassed controls.

## Source Basis

This evaluator uses the validated `engineering.harmonyos` research ledger at
`changes/engineering.harmonyos-completion/research/sources.json`: Domain identity
[REPO-HARMONYOS-IDENTITY], ArkTS language and API behavior [HMOS-ARKTS], Stage application model
[HMOS-STAGE], ArkUI state management V2 [HMOS-ARKUI-V2], V1-to-V2 migration guidance
[HMOS-ARKUI-MIGRATION], HarmonyOS package semantics [HMOS-PACKAGES], and testing and verification
guidance [HMOS-TESTING]. Source IDs resolve through that ledger; this artifact introduces no new
source authority.
