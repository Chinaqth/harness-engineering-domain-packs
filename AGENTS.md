# Domain Pack Repository Entry Point

This repository is the authoritative source for enterprise function-level capabilities. Keep Kernel policy and project-specific facts out of Domain Packs.

## Mandatory Rules

1. Write new repository content in English by default. `README-CH.md` is the explicitly maintained Chinese companion; keep other generated repository content in English unless the user explicitly requests an authoritative locale-specific source.
2. Register a new function through `$register-domain-pack`; do not hand-create an unregistered domain directory.
3. Every Domain Pack requires a stable ID, named owner, lifecycle status, version, purpose, and validation evidence.
4. Domain rules may specialize the Harness Kernel but may not weaken organization red lines.
5. Do not place credentials, production data, customer data, or project-specific secrets in a Domain Pack.
6. Capability, route, and Domain IDs are immutable after publication. Deprecate and replace instead of silently renaming.
7. Run `./scripts/domain-check.sh` before completing a change. Do not treat a non-empty route or capability list as activation evidence unless schema and lifecycle validation both pass.
8. Keep registry metadata and Domain Pack files consistent.

## Read on Demand

| Task | Required reading |
| --- | --- |
| Understand repository boundaries | `docs/ARCHITECTURE.md` |
| Register a function | `.agents/skills/register-domain-pack/SKILL.md` |
| Complete a registered draft | `.agents/skills/complete-domain-pack/SKILL.md`, `.codex/agents/` |
| Change ownership or lifecycle | `docs/GOVERNANCE.md` |
| Add a route or capability | Relevant JSON Schema in `schemas/` |
| Validate the repository | `scripts/domain-check.sh`, `scripts/validate_registry.py` |

## Definition of Done

- Registry validation passes.
- New or changed metadata conforms to the schemas.
- Domain ownership and lifecycle are explicit.
- Routes identify inputs, outputs, dependencies, and applicable task types.
- Capabilities identify workflows, Skills, tools, evaluators, and permission needs.
- Documentation and actual registry state agree.
- Autonomous completion cites a validated research ledger and keeps activation under human
  authority.
