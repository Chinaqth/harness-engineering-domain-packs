# Domain Pack Governance

## Ownership

Each Domain Pack has:

- A primary Domain Owner accountable for professional correctness;
- Reviewers for material workflow, rule, capability, and evaluator changes;
- A lifecycle state and semantic version;
- Evidence that the pack remains routable and internally consistent.

The central Harness team owns schemas and registry protocol. Domain teams own their professional content. Product teams own project overlays.

## Lifecycle

Allowed Domain states:

| State | Meaning |
| --- | --- |
| `draft` | Registered but incomplete; Router must not select it for production work |
| `active` | Owned, validated, and available for routing |
| `deprecated` | Still resolvable for pinned consumers but not selected by default |
| `retired` | Unavailable for new routing; retained for audit and migration |

Activation requires at least one route, one capability, a named owner, validation evidence, and a compatibility statement.

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
