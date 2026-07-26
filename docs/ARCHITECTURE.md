# Domain Pack Architecture

## Purpose

A Domain Pack converts a business function into a discoverable, versioned capability surface. It tells the enterprise Router when the function applies, what it owns, which workflows and Skills it provides, which tools it needs, and how its output is evaluated.

## Layering

```text
Harness Kernel
  -> Global Domain Pack
       -> Project Domain Overlay
            -> Task Contract
```

- The Kernel defines cross-domain invariants and task state.
- A Domain Pack defines reusable professional practice.
- A project overlay adds product architecture, commands, design systems, and local constraints.
- A task contract adds the current objective, scope, evidence, and temporary limits.

Professional behavior becomes more specific closer to the task. Safety constraints use the strictest applicable rule and cannot be weakened by a lower layer.

## Domain Pack Contract

```text
domains/<domain-path>/
├── DOMAIN.md
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
| `domain.json` | Stable identity, lifecycle, ownership, inheritance, and applicability |
| `routes.json` | Conditions that make the Router consider this Domain |
| `capabilities.json` | Workflows, Skills, tools, evaluators, permissions, and dependencies |
| `owners.json` | Primary owner and required reviewers |
| `rules/` | Domain invariants that specialize but do not weaken the Kernel |
| `workflows/` | Repeatable domain delivery sequences |
| `evaluators/` | Domain-specific acceptance and evidence contracts |
| `templates/` | Reusable domain artifacts |
| `skills/` | Domain-owned Skill source |

## Discovery and Routing

The Harness Router reads `registry/domains.json`, then loads only candidate manifests and route metadata. It does not load every Domain Pack body into context.

```text
Task Envelope
  -> Domain registry candidates
  -> route condition evaluation
  -> capability dependency resolution
  -> policy and permission filtering
  -> routing plan
  -> selected workflows, Skills, tools, and evaluators
```

The registry is the fact source. Model reasoning may interpret ambiguous intent and compose work packages, but it must not invent unregistered capabilities.

All registered JSON documents are checked against the schemas in `schemas/`. Lifecycle validation adds semantic gates that JSON Schema alone cannot express: an active Pack must have review ownership, meaningful routes and capabilities, evaluator coverage, activation evidence, a compatibility statement, and resolvable dependencies.

## Distribution

The Git repository is authoritative. An installer may publish versioned Domain Packs to `~/.harness/domains/` and selected Skills to `~/.agents/skills/`. Projects may optionally declare versions and overlays without copying the complete Pack.
