# Domain Pack Governance

## Ownership

Each Domain Pack has:

- A primary Domain Owner accountable for professional correctness;
- Optional reviewers for material workflow, rule, capability, and evaluator consultation;
- A lifecycle state and semantic version;
- Evidence that the pack remains routable and internally consistent.

The central Harness team owns schemas and registry protocol. Domain teams own their professional content. Product teams own project overlays.

## Lifecycle

Allowed Domain states:

| State | Meaning |
| --- | --- |
| `draft` | Registered but incomplete; a future resolver must not select it for production work |
| `active` | Owned, validated, and available for routing |
| `deprecated` | Still resolvable for pinned consumers but not selected by default |
| `retired` | Unavailable for new routing; retained for audit and migration |

Completion automatically activates a Pack when it has at least one meaningful route, one
capability with workflow and evaluator coverage, a named owner, a compatibility statement,
resolvable references and dependencies, and passing automated evaluation. Reviewer presence and a
separate activation-evidence transaction are not lifecycle prerequisites.

## Completion and Activation Modes

Two modes govern how a registered draft becomes `active`:

| Mode | Trigger | Flow |
| --- | --- | --- |
| Default mode (默认模式) | No explicit user direction; the normal path | Full completion workflow: validated research ledger, per-artifact authoring with independent evaluation, final Pack evaluation, and automatic activation through `finalize_domain_pack.py` |
| Intervention mode (介入模式) | The user explicitly directs it, acting as the Domain owner and naming the stages to skip | Owner-directed flow: the direction and waived stages are recorded, deterministic gates still run, and lifecycle is synchronized manually |

Intervention mode requirements:

- It is never inferred or defaulted. The user must explicitly direct it, and the direction,
  claimed authority, and date are recorded verbatim in the change record.
- Waivable stages: per-artifact scoring evaluations, evaluation granularity, iteration budgets,
  and the final independent Pack evaluation.
- Never waivable: schema and registry validation (`scripts/validate_registry.py`,
  `./scripts/domain-check.sh`), route, capability, and reference integrity, documentation and
  registry consistency, Kernel policy, capability permission clauses, fail-closed behavior, and
  the non-authoritative status of bundled corpora.
- Activation in intervention mode is a manual, rollback-safe synchronization of
  `registry/domains.json` and the manifest, with `activation.evidence` pointing at an
  intervention record under `changes/<domain-id>-activation/` that states the authority, waived
  gates, retained gate results, and rollback path.
- The user-facing completion report must name every waived gate. An intervention-mode activation
  must never be reported as passing the automated evaluation gates.

A non-breaking registration and completion that changes only reusable routing metadata is G1 by
default. Round up under Kernel governance when permissions, security boundaries, compatibility, or
production configuration change.

Automatic activation grants routing eligibility only. Git publication, deployment, release,
production access, exceptions, and task-specific permissions remain separate authorities.

## Change Rules

- Stable IDs do not change after activation.
- Breaking input, output, routing, or evaluator changes require a major version.
- Ownership changes require acknowledgment by the incoming owner.
- Deprecation identifies a replacement or explains why none exists.
- A Domain Pack cannot loosen Kernel security, privacy, authorization, or evidence rules.
- Project-specific facts stay in project overlays.

## Registry Review

A registry change must demonstrate:

- Unique and valid IDs;
- A matching Domain directory and manifest;
- Valid owner and lifecycle state;
- No unregistered capability references;
- No missing workflow, Skill, evaluator, or template path;
- A migration note for breaking changes.
