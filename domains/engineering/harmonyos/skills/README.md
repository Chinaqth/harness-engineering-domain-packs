# HarmonyOS Skill Capability Units

Artifact iteration: 1  
Domain: `engineering.harmonyos`  
Owner: `platform-harmony`  
Lifecycle: `active`

This inventory assembles the six user-supplied Skill packages as capability units. It does not modify, endorse, or make the bundled corpora authoritative. The original Skill files and references remain implementation inputs; current, version-specific Huawei documentation and project verification control whenever cached guidance conflicts with the selected SDK or API baseline. [REPO-HARMONYOS-IDENTITY] [HMOS-ARKTS] [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION] [HMOS-TESTING]

## Assembly Contract

Every invocation must receive the project root, applicable files or question, product/module scope when relevant, the current and target SDK/API baseline, and the requested output. Missing organizational standards, commands, permissions, devices, signing material, or release authority remain explicit gaps rather than inferred defaults. A local corpus result is evidence to inspect, not proof that an API is current. Tool output, commands, versions, diagnostics, changed files, artifacts, and unresolved failures must be reported. [HMOS-ARKTS] [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION] [HMOS-TESTING]

Domain assembly uses `devecocli` as the available execution boundary. This is an adapter, not a rewrite of the Skill corpora and not a claim that different tools produce identical diagnostics:

| Corpus assumption | Domain assembly mapping | Boundary |
| --- | --- | --- |
| `mcp_codegenie-mcp_harmonyos_knowledge_search`, `harmonyos_knowledge_search`, or an unspecified DevEco MCP documentation query | `devecocli docs search <keywords...>`, followed by `devecocli docs read <documentId>` when full context is required | Record document IDs and version statements. Treat unversioned or conflicting cached material as unresolved until checked against current official evidence. |
| `mcp_codegenie-mcp_check_ets_files` or `deveco-mcp_check_ets_files` used for general ArkTS/ETS diagnostics | `devecocli check lint <path>` with the project configuration; use JSON or a persisted report when evidence is required | Lint findings are not a successful compile. Do not translate diagnostic codes or severity labels as equivalent unless the output establishes that mapping. |
| Deprecated or target-version compatibility checking | `devecocli check compat`, after obtaining real version identifiers with `devecocli check compat versions` | Supply explicit source and target versions. Compatibility results require documented replacement review and follow-up verification. |
| `mcp_codegenie-mcp_build_project` or a generic DevEco MCP build | `devecocli build` with the project product, module, and build mode | A build passes only when the command exits successfully and its requested artifacts are located. Signing, installation, device execution, and release remain separate concerns. |
| Missing tool or unsupported operation | Stop the affected automated step, preserve partial evidence, and report `needs_input` or a manual-review fallback explicitly | Never represent a manual review, local-corpus search, lint pass, or compatibility scan as a compile, test, device, or release pass. |

## `hmos-arkts-knowledge-retriever`

- **Responsibility:** Retrieve traceable ArkTS language, library, concurrency, runtime, toolchain, and migration references from the package indexes for implementation, review, and debugging. ArkTS correctness includes stricter typing and restricted dynamic behavior. [HMOS-ARKTS]
- **Triggers:** Questions about ArkTS syntax, types, standard/common libraries, concurrency, runtime behavior, compilation tooling, TypeScript migration, examples, or the cause of a language-level diagnostic.
- **Inputs:** A query string; optional document scope and result limit; optionally a request to inspect a returned source document.
- **Outputs:** Ranked document paths, sections, match rationale, index-declared verification level, and optionally source excerpts or examples. `snippet_validated` is only the corpus index's assertion and must not be promoted to current-project verification.
- **Declared tool dependencies:** The package-local `scripts/search_docs.py` script, Python 3, and `doc_index.json`, `snippet_index.json`, `topic_aliases.json`, and the bundled ArkTS reference tree. No MCP dependency is declared.
- **Safety and version boundaries:** Read-only retrieval must preserve source paths. Cached results must be checked against current official documentation for API/version-sensitive conclusions; absence from the index is not evidence that an API does not exist. [HMOS-ARKTS]

## `hmos-arkui-knowledge-retriever`

- **Responsibility:** Retrieve ArkUI API signatures, component and decorator guidance, error material, V1/V2 distinctions, navigation, rendering, accessibility, and performance references without generating or modifying code. ArkUI use must remain aligned with the selected API baseline and Stage-model context. [HMOS-STAGE] [HMOS-ARKUI-V2]
- **Triggers:** ArkUI API or parameter questions, usage validation, compiler/runtime error investigation, V1-versus-V2 comparison, or a targeted evidence request from another Skill.
- **Inputs:** A query; optional category filters, result count, context limits, code inclusion, and compact/full-content controls.
- **Outputs:** A direct answer assembled from retrieved documents, API signatures, examples, source paths, and confidence/version caveats.
- **Declared tool dependencies:** Python 3 and the package-local `scripts/run.py`, `document_loader.py`, and `retriever.py`, backed by `references/knowledges/`. No code-writing tool is declared.
- **Safety and version boundaries:** Keep the operation read-only. A document with an explicit API version or deprecation marker has stronger local evidence; an unversioned result remains uncertain. Official version-specific evidence controls conflicts. [HMOS-ARKUI-V2]

## `hmos-arkui-develop-skill`

- **Responsibility:** Design, generate, incrementally modify, or repair ArkUI `.ets` pages and components after targeted API retrieval, while preserving the existing state-management and navigation architecture. Stage-model lifecycle and context boundaries apply to UI delivery. [HMOS-STAGE] [HMOS-ARKUI-V2]
- **Triggers:** Requests to create an ArkUI page/component, change an existing `.ets` feature, repair ArkUI code from diagnostics or screenshots, or implement state, layout, navigation, or interaction behavior.
- **Inputs:** Requirements; for existing work, the actual target files and project conventions; selected API baseline; current V1/V2 and navigation approach; intended regression path.
- **Outputs:** A design and uncertainty list, evidence-linked API decisions, scoped code or patch, lint diagnostics, up to three bounded repair iterations, and at least one stated regression path for incremental work.
- **Declared tool dependencies:** The sibling `hmos-arkui-knowledge-retriever`; local quick API, quick rule, style, search-strategy, common-mistake, and checklist references; plus corpus references to `deveco-mcp_check_ets_files` and documentation search. The front matter also mentions `hmos-arkui-mvvm-pattern`, which is not one of the six assembled packages and is therefore an optional unavailable collaborator, not a required Domain capability.
- **Safety and version boundaries:** Do not overwrite business logic, replace V1/V2 state management, change navigation architecture, or refactor unrelated modules without authorization. Never invent an API signature. Map documentation queries to `devecocli docs`; map changed-file diagnostics to `devecocli check lint`, then use the project build when compile evidence is required. A manual checklist fallback must be labeled manual and cannot establish compilation success. [HMOS-ARKUI-V2] [HMOS-TESTING]

## `hmos-arkui-statemgt-migration`

- **Responsibility:** Inventory and plan dependency-aware ArkUI state-management V1-to-V2 migration across component state, observed objects, cross-component state, application storage, rendering controls, reuse, and special cases. Migration is behavioral, not mechanical decorator replacement. [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]
- **Triggers:** A V1-to-V2 upgrade; decorator, LocalStorage/AppStorage/PersistentStorage/Environment, ForEach/LazyForEach, nested-observation, `animateTo`, or V1/V2 mixing questions.
- **Inputs:** Project files; current and target API/SDK versions; V1 usage inventory; component/data-flow dependencies; third-party compatibility; functional, performance, and regression expectations.
- **Outputs:** A migration inventory, dependency/risk-ordered batches, scenario-specific code changes, compatibility findings, and compile/functional/performance/regression evidence or explicit unresolved items.
- **Declared tool dependencies:** Shell/text scanning implied by the workflow and the package's migration references and test cases. The Skill declares no named build or lint tool.
- **Safety and version boundaries:** V2 guidance in this corpus assumes API 12 or later, but the actual target must be verified. Respect traced-property behavior and documented V1/V2 mixing restrictions; retain rollback capability and do not migrate by global token substitution. Use `devecocli docs` for version-sensitive confirmation, `devecocli check compat` for explicit source/target compatibility evidence, `devecocli check lint` for static findings, and `devecocli build` for compile evidence. [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION] [HMOS-TESTING]

## `hmos-arkts-deprecated-interface-checker`

- **Responsibility:** Detect deprecated or incompatible SDK use, classify remediation risk, retrieve documented replacements, and propose or verify migrations against an explicit supported baseline. [HMOS-ARKTS] [HMOS-TESTING]
- **Triggers:** SDK/API upgrades, deprecated-symbol warnings, release-readiness review, technical-debt cleanup, or static-quality inspection.
- **Inputs:** Project root and `.ets` scope; exclusions; current compile SDK, compatible SDK, and minimum supported API; diagnostics; remediation and testing constraints.
- **Outputs:** An evidence-bearing finding list with locations, severity/priority, documented replacement, minimum-version implications, proposed change, validation plan, and unresolved cases.
- **Declared tool dependencies:** Corpus references to `mcp_codegenie-mcp_check_ets_files`, optional `mcp_codegenie-mcp_harmonyos_knowledge_search`, and a build tool in its command reference; local deprecated-API and configuration references.
- **Safety and version boundaries:** Do not infer that every deprecation is a defect or apply an unreviewed substitution. Map general diagnostics to `devecocli check lint`, version compatibility to `devecocli check compat`, replacement research to `devecocli docs`, and post-change compilation to `devecocli build`. Require the supported API matrix and verify behavior after migration. [HMOS-ARKTS] [HMOS-TESTING]

## `hmos-arkts-syntax-checker`

- **Responsibility:** Run a bounded diagnose-fix-verify-build loop for ArkTS/ETS projects and report the resulting HAP/App build evidence without hiding failures. Package semantics distinguish publication, installation/runtime, and shared-package units. [HMOS-PACKAGES] [HMOS-TESTING]
- **Triggers:** Compilation, syntax-error repair, first build, post-upgrade build, CI-oriented verification, or a request to locate a HAP/App artifact.
- **Inputs:** Project root; `.ets` files; product, modules, target/package intent, and build mode; SDK/API baseline; retry limit; permission to change source or install dependencies where applicable.
- **Outputs:** Classified diagnostics, scoped fixes, per-iteration results, final build command and exit status, artifact paths when produced, and a failure report after the bounded retry limit.
- **Declared tool dependencies:** Corpus references to `mcp_codegenie-mcp_check_ets_files`, `mcp_codegenie-mcp_build_project`, optional `mcp_codegenie-mcp_harmonyos_knowledge_search`, plus file discovery/read/write operations and local error/output references.
- **Safety and version boundaries:** File edits and dependency changes require task authorization; signing and credential changes are outside this unit. Map static checks to `devecocli check lint`, compatibility questions to `devecocli check compat`, documentation lookup to `devecocli docs`, and compilation to `devecocli build`. Stop after the configured retry bound, preserve diagnostics, and never call a lint-only result a successful build. [HMOS-PACKAGES] [HMOS-TESTING]

## Composition and Handoffs

Knowledge retrieval feeds implementation, migration, deprecated-interface remediation, and build diagnosis. Implementation and migration feed lint and compatibility checks; only a successful configured build can supply compile/package evidence. Stage architecture, HAP/HAR/HSP design, device verification, signing, distribution, security/privacy approval, and production rollout require their owning capability or organizational handoff and must not be inferred from these six packages. [HMOS-STAGE] [HMOS-PACKAGES] [HMOS-TESTING]

The six units are owner-trusted inputs whose per-Skill artifact scoring was waived by explicit owner direction at Pack activation. They remain non-authoritative discovery aids under the assembly contract above; this inventory neither evaluates them nor changes Domain lifecycle state. [REPO-HARMONYOS-IDENTITY]
