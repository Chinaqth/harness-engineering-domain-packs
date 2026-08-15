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
remain governed by [REPO-HARMONYOS-IDENTITY].
