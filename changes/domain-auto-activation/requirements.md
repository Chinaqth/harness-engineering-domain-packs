# Domain Auto-Activation Requirements

- Risk: G2
- Status: done

## Objective

Automatically activate a registered draft after `$complete-domain-pack` produces and validates its
role and capabilities, without a separate reviewer, approval-evidence, or activation transaction.

## Acceptance Criteria

1. Registration remains draft-only.
2. Content-complete Packs are eligible for automatic activation without reviewers or activation
   evidence.
3. A deterministic command updates registry and manifest status atomically and refuses incomplete
   or non-draft Packs.
4. Active Packs still require an owner, applicability, routes, capabilities, compatibility,
   evaluator coverage, and resolvable references.
5. Organization-specific task inputs remain non-blocking for Domain lifecycle and fail-closed for
   dependent task actions and claims.
6. Skills, agent instructions, documentation, and tests agree.

## Risks

- Automation makes routing eligibility depend more heavily on machine checks.
- Older integrations may expect non-empty reviewer or activation-evidence fields.
- Publication remains a separate Git authorization and is not performed by finalization.
