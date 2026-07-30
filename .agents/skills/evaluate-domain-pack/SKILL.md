---
name: evaluate-domain-pack
description: Independently evaluate an assembled Domain Pack for source-traceable content completeness, structural consistency, cross-file references, routing behavior, lifecycle governance, and separate activation readiness. Use after all declared artifacts have current passing evaluations or when a final content-complete, needs-org-input, activation-ready, fail, or blocked verdict is required.
---

# Evaluate Domain Pack

Issue an independent final readiness verdict without repairing the Pack.

## Workflow

1. Read the change requirements, Generator-Evaluator contract, validated research ledger, session,
   artifact evaluations, repository rules, [activation-gates.md](references/activation-gates.md), and
   [routing-scenarios.md](references/routing-scenarios.md).
2. Confirm every required artifact evaluation is current and passing:

```bash
python3 .agents/skills/complete-domain-pack/scripts/validate_session.py \
  --root . \
  --session changes/<change-id>/session.json
```

3. Establish deterministic structural evidence:

```bash
python3 .agents/skills/evaluate-domain-pack/scripts/check_pack.py \
  --root . \
  --domain-id <domain-id> \
  --ledger changes/<change-id>/research/sources.json
```

4. Run `./scripts/domain-check.sh`.
5. Exercise representative positive, negative, ambiguous, disabled-capability, dependency, and
   version-mismatch routing scenarios without changing production data.
6. Independently score the complete Domain directory with `$evaluate-domain-artifact`, using
   Pack-level evidence and the same strict score and hard-gate policy. Return the raw evaluation
   payload to the Builder; do not write it from the read-only evaluator context. The Builder must
   normalize it with `--artifact-label .`.
7. Have the Builder persist and normalize the raw final evaluation, re-run session validation
   with `--require-final`, and persist the deterministic Pack check.
8. Confirm `content_state` and the final `state` from deterministic evidence: `content-complete`
   plus `needs-org-input` or `activation-ready`, or else `fail`/`blocked`.

## Activation Boundary

`content-complete` means the source-traceable public baseline passes. `needs-org-input` means
content passes but organization-specific activation facts remain. `activation-ready` still does
not mean `active`; require the named Domain Owner and required Reviewers to approve the lifecycle
change separately.

## Guardrails

- Remain read-only for Domain production artifacts.
- Do not accept passing unit tests as proof of routing or professional outcomes by themselves.
- Do not reuse the Author or Artifact Evaluator as final acceptance authority for G2 work.
- Treat stale artifact evaluations, unresolved references, missing negative-path evidence, and
  unavailable authority as blocking.
- Report findings before the score, with reproducible evidence and residual risks.
