# Responsibility Boundaries

## Owns

HarmonyOS Engineering owns reusable guidance, workflows, checks, and evaluation for ArkTS and ArkUI implementation; Stage-model application structure and lifecycle; V1-to-V2 state migration; deprecated or incompatible API remediation; HAP/HAR/HSP module decisions; and reproducible lint, build, test, packaging, and device-verification evidence. [HMOS-ARKTS] [HMOS-STAGE] [HMOS-ARKUI-MIGRATION] [HMOS-PACKAGES] [HMOS-TESTING]

It may use the added Skills as operational procedures, but official version-specific evidence controls when Skill content conflicts with current platform documentation. In particular, V2 observation and migration must respect API support, traced-property behavior, and V1/V2 mixing constraints. [HMOS-ARKUI-V2] [HMOS-ARKUI-MIGRATION]

## Does not own

The Domain does not invent product requirements, private architecture, organization design standards, supported SDK/device matrices, security or privacy acceptance, signing identities, credentials, store accounts, release approval, production access, or rollback authority. It does not claim a build passed when required tools, SDKs, dependencies, devices, or project commands are unavailable.

## Handoffs

- Product and design owners decide requirements, interaction intent, visual standards, and supported form factors.
- Architecture owners approve private module, navigation, state, data, service, and observability choices.
- Security/privacy owners assess permissions, data handling, dependencies, signing, and risk acceptance.
- Release owners control certificates, profiles, distribution channels, rollout, and rollback.
- Project teams supply supported API/SDK/DevEco/device matrices and authoritative commands.

All unknown organizational facts remain downstream gaps, not reusable Domain policy. The owner is `platform-harmony`; activation evidence must demonstrate that routes, capabilities, Skills, workflows, rules, and evaluators agree with these boundaries. [REPO-HARMONYOS-IDENTITY]
