# Decision: Run Completion as a Project-Scoped Custom Agent Workflow

## Decision

Keep reusable procedures under `.agents/skills/` and define actual runtime roles under
`.codex/agents/`. Use a Builder custom agent as the single delegated workflow entry and allow it
to dispatch fresh Researcher, Author, Artifact Evaluator, and Pack Evaluator contexts.

## Rationale

The workflow can derive its public baseline from the registered identity and authoritative
sources. Running it as a subagent keeps research and iteration output out of the user's primary
context. Project-scoped Agent files provide explicit role, permission, and independence boundaries
while Domain-owned Skills keep portable workflow and deterministic scripts.

These Custom Agents are an authoring control plane for the authoritative Domain Packs checkout,
not a routed product-project capability. The Harness CLI and installed runtime remain unchanged;
published Domain content continues through the existing bundle path after review.

## Compatibility

Registration remains a separate atomic draft operation. Existing artifact and Pack evaluation
Skills remain internal dependencies. The previous uncommitted `$develop-domain-pack` entry is
replaced by `$complete-domain-pack` before publication.

## Rollback

Remove `$complete-domain-pack`, the five project Agent files and Agent validator, research
validation, source-bound scoring additions, completion documentation, and this change record.
Return to the registration-only baseline; the replaced development-loop prototype was never a
published compatibility contract. Do not remove the existing registration Skill or registered
Domain content.
