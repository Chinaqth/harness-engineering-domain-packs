---
name: author-domain-artifact
description: Create or revise exactly one declared Domain Pack artifact from authoritative professional inputs and existing dependencies. Use during draft Pack development for DOMAIN.md, manifests, ownership, rules, workflows, evaluators, templates, Skills, capabilities, routes, or activation evidence; do not use to evaluate or activate the Pack.
---

# Author Domain Artifact

Author one evidence-ready artifact without scoring it.

## Workflow

1. Confirm the registered Domain ID, target artifact path, artifact type, iteration, validated
   research ledger, approved source IDs, dependencies, and acceptance contract.
2. Read the repository rules, relevant JSON schema, [artifact-contracts.md](references/artifact-contracts.md),
   and [content-boundaries.md](references/content-boundaries.md).
3. Inspect only the dependencies required for the target artifact. Do not preload unrelated
   Domain bodies.
4. Establish the current baseline and preserve any failing validation evidence.
5. Create or revise only the declared artifact and directly required references.
6. Run the narrowest relevant deterministic checks, then the repository validator when the
   artifact changes registered references.
7. Return changed paths, source IDs used, assumptions, validation evidence, organization-specific
   gaps, and the exact artifact ready for independent evaluation.

## Artifact Rules

- Write `DOMAIN.md`, ownership, rules, workflows, evaluators, templates, and Skills before
  assembling capabilities and routes.
- Reference only files and capability IDs that already exist.
- Keep professional rules reusable across products; move local paths, commands, and constraints
  to project overlays.
- Define measurable outputs and evidence, not aspirational prose.
- Keep generated repository content in English unless preserving an authoritative localized
  source.

## Stop Conditions

Return `needs_input` without writing speculative content when:

- the Domain owner or required reviewer is unknown;
- professional behavior lacks an authoritative source;
- a tool, permission, dependency, or compatibility claim cannot be verified;
- the requested content would weaken Kernel rules;
- the artifact requires a project-specific fact.

Do not stop public baseline authoring merely because a reviewer, internal permission, private
architecture, or unpublished policy is unknown. Preserve it as `needs-org-input` and continue
where the validated research ledger supports content.

## Guardrails

- Do not evaluate or score your own artifact.
- Do not write evaluation records.
- Do not change the Domain to `active`.
- Do not broaden scope in response to evaluator feedback; return scope changes to the
  Orchestrator.
- Do not hide validation failures or delete evidence to improve a later score.
