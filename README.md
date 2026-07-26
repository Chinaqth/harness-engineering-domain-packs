# Harness Engineering Domain Packs

Private source of truth for enterprise Domain Packs consumed by the Harness Engineering control plane.

This repository contains reusable function-level capabilities such as Product, Design, iOS, Android, Web, Backend, QA, Security, and future departments. It starts with no concrete business functions. Instead, it provides the schemas, registry, templates, validation, ownership model, and registration Skill required to add them consistently.

## Boundary

| Repository | Owns |
| --- | --- |
| `harness-engineering-workstation` | Kernel rules, cross-domain workflow, routing protocol, task state, governance, autonomy, and integration evaluation |
| `harness-engineering-domain-packs` | Domain definitions, domain workflows, domain rules, capability metadata, domain evaluators, and domain-owned Skills |
| Product repositories | Project facts, architecture, commands, local overlays, and task execution records |

The authoritative Domain Pack source is this repository. Installed copies may live under `~/.harness/domains/`; globally discoverable Skills may be published to `~/.agents/skills/`. Installed copies are runtime material, not the source of truth.

## Repository Structure

```text
.
├── AGENTS.md
├── docs/
│   ├── ARCHITECTURE.md
│   └── GOVERNANCE.md
├── registry/
│   └── domains.json
├── schemas/
│   ├── capability.schema.json
│   ├── domain-pack.schema.json
│   ├── owners.schema.json
│   ├── registry.schema.json
│   └── route.schema.json
├── domains/
│   └── _template/
├── .agents/
│   └── skills/
│       └── register-domain-pack/
├── scripts/
│   ├── domain-check.sh
│   └── validate_registry.py
├── tests/
└── .github/
```

## Register a Function

Use the repository Skill:

```text
Use $register-domain-pack to register the iOS Engineering function.
```

The Skill collects the stable identity, owner, and purpose, then runs the deterministic registration script. Example:

```bash
python3 .agents/skills/register-domain-pack/scripts/register_domain_pack.py \
  --root . \
  --id engineering.ios \
  --display-name "iOS Engineering" \
  --owner "ios-platform-team" \
  --description "Owns iOS application delivery and evaluation."
```

Registration stages and validates `domains/engineering/ios/`, then commits the Domain directory and `registry/domains.json` through a rollback-safe operation. JSON-sensitive values are encoded structurally rather than substituted as raw text. A newly registered pack remains `draft` with empty routes and capabilities until its Domain Owner completes and reviews it.

## Validate

```bash
./scripts/domain-check.sh
```

The check validates every registered document against its repository JSON Schema, then enforces registry-to-directory consistency, lifecycle gates, dependency resolution, referenced files, Skill structure, English-first policy, suspicious secret filenames, and registration rollback tests.

## Current State

This is the foundation release. It intentionally contains no active department implementation. The first real Domain Pack should be registered only when a named owner is ready to define its workflows, rules, capabilities, tools, and evaluators.
