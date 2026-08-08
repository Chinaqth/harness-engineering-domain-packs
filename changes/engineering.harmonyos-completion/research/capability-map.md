# Capability Map

The Domain should expose eight reusable capabilities derived from the added Skills and official platform evidence:

1. **Authoritative knowledge retrieval** — answer ArkTS, ArkUI, SDK, API-version, error, and migration questions with traceable evidence; never treat a cached Skill reference as newer than official documentation. [HMOS-ARKTS] [HMOS-ARKUI-V2]
2. **ArkTS implementation and review** — generate, inspect, and correct `.ets` code under documented typing, syntax, module, interoperability, and concurrency constraints. [HMOS-ARKTS]
3. **ArkUI application delivery** — implement declarative screens, components, navigation, interaction, state-driven rendering, accessibility, and device adaptation while preserving project conventions. [HMOS-STAGE] [HMOS-ARKUI-V2]
4. **State-management migration** — inventory V1 usage, plan dependency-aware batches, migrate behavior to V2, and verify nested observation and mixing constraints. Mechanical decorator replacement is insufficient. [HMOS-ARKUI-MIGRATION] [HMOS-ARKUI-V2]
5. **Deprecated and incompatible API maintenance** — identify SDK warnings against the selected API baseline, retrieve documented replacements, prioritize risk, and validate each change. [HMOS-ARKTS] [HMOS-TESTING]
6. **Stage-model architecture** — review UIAbility lifecycle, contexts, extensions, process/thread concerns, and ArkUI page composition. [HMOS-STAGE]
7. **Module and package design** — select HAP, HAR, and HSP boundaries based on install, publication, and reuse semantics. [HMOS-PACKAGES]
8. **Build and verification** — run configured lint/static checks, compile, test, coverage, packaging, and relevant device checks; report commands, versions, diagnostics, artifacts, and unresolved failures. [HMOS-TESTING]

These capabilities align with the six added Skills, but tool names mentioned inside a Skill are dependencies to detect, not guaranteed platform capabilities. Each route must accept the project/API baseline and return evidence-bearing outputs.
