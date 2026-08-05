# Harness Engineering Domain Packs

The private source of truth for reusable enterprise function capabilities consumed through the Harness Engineering routing protocol.

[Chinese README](README-CH.md)

## Project Overview

This repository turns durable organizational functions—such as Product, Design, iOS, Android, Web, Backend, Quality, Security, and Operations—into versioned and governable Domain Packs.

A Domain Pack defines when a function applies, what capabilities it owns, which workflows and Skills it provides, which tools and permissions it needs, and how its output is evaluated. It allows professional practice to evolve independently from the Harness Kernel and from any one product repository.

The repository begins with no concrete business function. It provides the registry, schemas, templates, governance, validation, and registration workflow required to add functions without inventing or silently activating them.

### What this repository is

- The authoritative catalog of enterprise function identities and lifecycle state;
- A reusable source of professional workflows, rules, Skills, tools, templates, and evaluators;
- A versioned contract between Domain Owners, the Harness Kernel, and adopting projects;
- A controlled distribution source for user-level Domain runtime projections.

### What this repository is not

- The Harness Kernel or an organization-wide policy repository;
- A product repository or a place for project-specific architecture, commands, or secrets;
- A production Router;
- A collection of unowned prompts;
- Permission to execute task-level operational actions merely because a Domain is active.

## Kernel, Domain Packs, and Projects

Enterprise behavior is divided into three versioned scopes:

| Scope | Source of truth | Responsibility |
| --- | --- | --- |
| Harness Kernel | `harness-engineering-workstation` | Cross-domain workflow, risk, authorization, routing protocol, evidence, and governance |
| Domain Packs | This repository | Function identity, routes, capabilities, professional workflows, rules, Skills, tools, and evaluators |
| Product project | Each product repository | Architecture, commands, local ownership, enabled Pack versions, stricter constraints, and task records |

Context becomes more specific toward the task:

```text
Harness Kernel
  -> Domain Pack
       -> Project Domain Overlay
            -> Task Envelope and Routing Plan
```

A Domain Pack or project overlay may specialize the layer above it, but it cannot weaken Kernel security, privacy, authorization, evidence, or approval constraints.

See [Domain Pack Architecture](docs/ARCHITECTURE.md) and [Domain Pack Governance](docs/GOVERNANCE.md).

## Domain Pack Engineering Principles

### 1. Identity is stable

Published Domain, route, and capability IDs are immutable. Breaking semantic changes require versioning, deprecation, and migration rather than silent renaming.

### 2. Ownership precedes activation

Registration establishes a draft identity and named owner. Completion automatically activates the
Pack after its role, capabilities, references, compatibility, and automated evaluation pass.

### 3. Discovery stays lightweight

Routing begins with the registry and route metadata. Full workflows, Skills, rules, and evaluators load only after a capability is selected.

### 4. Professional knowledge stays reusable

Domain Packs contain function-level practice. Product-specific paths, commands, architecture, and exceptions remain in project overlays.

### 5. Activation is completion-backed

An `active` Pack must be schema-valid and demonstrate meaningful routes, capabilities, workflow and
evaluator coverage, ownership, compatibility, and resolvable dependencies. Reviewer metadata and
separate activation evidence are optional and do not block automatic activation.

### 6. Missing capability is an explicit result

Neither an agent nor a future resolver may invent an unregistered function or capability to force a route.

## Lifecycle and Operating Model

| State | Meaning | Routing behavior |
| --- | --- | --- |
| `draft` | Registered but incomplete | Visible to maintainers; unavailable for production routing |
| `active` | Owned and automatically validated | Available when a project enables the exact compatible version |
| `deprecated` | Supported only for migration | Resolved only by explicitly pinned consumers |
| `retired` | No longer available | Retained for audit and migration history |

The standard lifecycle is:

```text
Need for a reusable function
  -> register stable identity and owner
  -> complete routes and capabilities
  -> add workflows, Skills, tools, and evaluators
  -> record compatibility and automated evaluation
  -> run deterministic validation
  -> automatically activate
  -> publish when separately authorized
  -> monitor, version, deprecate, or retire
```

Registration always starts in `draft`. Successful completion automatically activates the Pack in
the same completion transaction.

## Repository and File Responsibilities

### Entry, architecture, and governance

| Path | Responsibility | Read or update when |
| --- | --- | --- |
| `README.md` | English project overview and operating guide | A contributor first enters the repository |
| `README-CH.md` | Chinese project overview and operating guide | A Chinese-speaking contributor first enters the repository |
| `AGENTS.md` | Mandatory repository rules and task routing index | Every agent begins Domain work |
| `docs/ARCHITECTURE.md` | Layer boundaries, Pack contract, routing, and distribution | Changing structure or integration behavior |
| `docs/GOVERNANCE.md` | Ownership, lifecycle, activation, versioning, and registry review | Registering, activating, or changing a Pack |
| `changes/README.md` | Domain repository change-record guidance | Planning a material repository change |

### Registry, schemas, and Domain content

| Path | Responsibility |
| --- | --- |
| `registry/domains.json` | Authoritative, sorted catalog of Domain identity, version, status, owner, and path |
| `schemas/domain-pack.schema.json` | Domain identity, applicability, compatibility, lifecycle, and activation contract |
| `schemas/route.schema.json` | Route task types, signals, priority, and capability references |
| `schemas/capability.schema.json` | Capability workflows, Skills, tools, evaluators, permissions, and dependencies |
| `schemas/owners.schema.json` | Primary owner and reviewer contract |
| `schemas/registry.schema.json` | Registry entry contract |
| `domains/_template/` | Standard draft Pack skeleton |
| `domains/<domain-path>/` | Versioned source for one registered professional function |

### Registration, validation, and delivery

| Path | Responsibility |
| --- | --- |
| `.agents/skills/register-domain-pack/` | Guided, rollback-safe registration of a new draft Domain |
| `.agents/skills/complete-domain-pack/` | Autonomous research, authoring, scoring, and completion from a Domain ID |
| `.codex/agents/` | Project-scoped Builder, Researcher, Author, and independent Evaluator roles |
| `scripts/validate_registry.py` | Schema, lifecycle, reference, identity, ownership, and dependency validation |
| `scripts/domain-check.sh` | Complete repository integrity gate |
| `tests/test_registration.py` | Registration encoding, idempotency, staging, and rollback behavior |
| `tests/test_registry_validation.py` | Registry, schema, lifecycle, evidence, and dependency rejection paths |
| `.github/workflows/domain-check.yml` | Run the integrity gate on pushes and pull requests |
| `.github/pull_request_template.md` | Require ownership, lifecycle, compatibility, evidence, and rollback context |

## Domain Pack Contract

Every registered function uses:

```text
domains/<domain-path>/
├── DOMAIN.md
├── README-CH.md
├── domain.json
├── routes.json
├── capabilities.json
├── owners.json
├── rules/
├── workflows/
├── evaluators/
├── templates/
└── skills/
```

| Artifact | Responsibility |
| --- | --- |
| `DOMAIN.md` | Human-readable purpose, boundaries, inputs, outputs, and maturity |
| `README-CH.md` | Chinese inventory explaining the responsibility and behavior of every production file and directory |
| `domain.json` | Stable identity, version, lifecycle, owner, applicability, compatibility, and activation evidence |
| `routes.json` | Task types, repository signals, priority, and candidate capabilities |
| `capabilities.json` | Workflows, Skills, tools, evaluators, permissions, and dependencies |
| `owners.json` | Primary owner and optional reviewers |
| `rules/` | Professional invariants that specialize but do not weaken the Kernel |
| `workflows/` | Repeatable professional delivery sequences |
| `evaluators/` | Domain-specific acceptance and evidence contracts |
| `templates/` | Reusable function-level artifacts |
| `skills/` | Domain-owned Skill source |

## Quick Start

### 1. Read the entry rules

Read [AGENTS.md](AGENTS.md), [Architecture](docs/ARCHITECTURE.md), and [Governance](docs/GOVERNANCE.md).

### 2. Register a draft function

Invoke the repository Skill:

```text
Use $register-domain-pack to register the iOS Engineering function.
```

Or preview the deterministic script:

```bash
python3 .agents/skills/register-domain-pack/scripts/register_domain_pack.py \
  --root . \
  --id engineering.ios \
  --display-name "iOS Engineering" \
  --owner "ios-platform-team" \
  --description "Owns reusable iOS application delivery and evaluation." \
  --dry-run
```

Remove `--dry-run` only after confirming the identity and owner. Registration creates a
schema-valid `draft`; completion supplies the professional content and automatically activates it.

### 3. Complete the Pack

Delegate completion when the user knows the registered function but not its professional content:

```text
Spawn the domain_pack_builder subagent and use $complete-domain-pack
to complete and activate engineering.ios from its registered identity.
```

Run this authoring workflow from the authoritative Domain Packs checkout. Its Custom Agents are
project-scoped under `.codex/agents/`; they are not runtime capabilities projected into product
repositories by the Harness CLI.

The Domain ID is the only required input. A read-only Researcher discovers current authoritative
public sources and records organization-specific gaps. Separate Author, Artifact Evaluator, and
Pack Evaluator agents then build and evaluate every production artifact. Every artifact must
receive a current source-bound score greater than 90, pass all hard gates, and contain no P0 or P1
finding.

The supporting Skills are:

- `$author-domain-artifact` for one declared artifact;
- `$evaluate-domain-artifact` for a digest-bound independent evaluation;
- `$evaluate-domain-pack` for final content and activation-readiness evaluation.

The result requires `content_state=content-complete` and `state=activation-ready`, then atomically
sets the registry and manifest to `active`. Internal reviewers, permissions, and unpublished
project policy remain downstream task inputs; their absence does not block reusable lifecycle but
does block every dependent task action or claim.

### 4. Validate

```bash
./scripts/domain-check.sh
```

### 5. Publish or adopt

Completion has already synchronized the lifecycle to `active`. Publish the immutable revision only
with the repository's applicable Git authority, then enable the Pack in a project overlay.

## Scenario Playbooks

### Scenario A: Register a New Department or Discipline

| Stage | What happens | Files involved |
| --- | --- | --- |
| Establish need | Confirm the function is durable and reusable across projects | `docs/ARCHITECTURE.md`, proposed ownership |
| Choose identity | Select a stable dotted ID, display name, owner, and durable purpose | Registration contract and registry search |
| Register | Stage the standard Pack and registry entry atomically | `$register-domain-pack`, `domains/_template/`, `registry/domains.json` |
| Verify draft | Confirm schema, structure, ownership, and rollback behavior | `scripts/domain-check.sh` |
| Complete and activate | Build the role and capabilities, evaluate them, and automatically set `active` | `$complete-domain-pack` |

### Scenario B: Add a Capability to an Existing Domain

| Stage | What happens | Files involved |
| --- | --- | --- |
| Define professional outcome | Specify inputs, outputs, supported task types, and evidence | `DOMAIN.md`, change record |
| Model routing | Add route signals and capability references without broadening unrelated routes | `routes.json`, `capabilities.json` |
| Add execution content | Supply workflows, Skills, tools, templates, and permission needs | `workflows/`, `skills/`, `templates/` |
| Add evaluation | Define how a qualified evaluator proves the outcome | `evaluators/`, `capabilities.json` |
| Validate and version | Resolve dependencies and choose compatible semantic version impact | Schemas, governance, `domain-check.sh` |

### Scenario C: Change an Active Workflow

| Stage | What happens | Files involved |
| --- | --- | --- |
| Assess compatibility | Determine whether behavior, inputs, outputs, permissions, or evidence change | `docs/GOVERNANCE.md`, current manifest |
| Preserve intent | Record rationale, migration needs, and rollback | Change record and decision evidence |
| Update bounded content | Modify only the affected workflow, Skill, rule, or evaluator | Selected Domain files |
| Re-evaluate | Run deterministic checks and reproduce representative Domain journeys | Tests, evaluator contract, activation evidence |
| Publish | Increment the correct version and keep registry and manifest synchronized | `domain.json`, `registry/domains.json` |

### Scenario D: Deprecate or Retire a Capability

| Stage | What happens | Files involved |
| --- | --- | --- |
| Find consumers | Identify pinned projects and dependent capabilities | Registry, dependency references, project overlays |
| Define migration | Name the replacement or explain why none exists | Domain documentation and change record |
| Change lifecycle | Deprecate before retirement when migration time is required | Registry and manifest |
| Verify safety | Confirm active routes no longer select unavailable capabilities | Routes, capabilities, tests |
| Retain evidence | Preserve history for audit and recovery | Git history and durable change record |

### Scenario E: Adopt a Domain in a Product Project

| Stage | What happens | Source of truth |
| --- | --- | --- |
| Publish | Domain Owner releases an immutable active Pack revision | This repository |
| Enable | Product Owner pins the approved Pack version and local owner | Product `.harness/domains.json` |
| Specialize | Project adds paths, commands, signals, disabled optional capabilities, and stricter constraints | Product overlay |
| Route | Harness combines the Task Envelope, registry revision, and overlay | Harness CLI or future conforming resolver |
| Execute and evaluate | Only selected content loads; project and Domain evidence remain traceable | Routing Plan, Pack workflows, project tests |

## Validation

Run the complete gate:

```bash
./scripts/domain-check.sh
```

The gate validates:

- English-first repository policy;
- Suspicious credential-bearing filenames;
- JSON Schema conformance;
- Registry ordering, identity, directory, owner, version, and lifecycle consistency;
- Route and capability uniqueness and references;
- Workflow, Skill, evaluator, template, and dependency existence;
- Active-Pack ownership, compatibility, evaluator, route, capability, and reference requirements;
- Registration encoding, staging, idempotency, and rollback behavior.

## Current State and Next Step

The repository foundation is complete and its validation suite passes. It intentionally contains no registered or active business Domain.

The next production milestone is to register one owner-backed draft—recommended:
`engineering.ios`—complete and automatically activate its professional content, publish an
immutable version, and enable it in a pilot product overlay.
