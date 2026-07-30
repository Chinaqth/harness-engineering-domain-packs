---
name: evaluate-domain-artifact
description: Independently assess one Domain Pack artifact against its schema, professional contract, boundaries, dependencies, evidence quality, and Kernel constraints. Use after an Author produces or revises a Domain artifact and a normalized score, findings, hard gates, digest, and pass, fail, or blocked verdict are required.
---

# Evaluate Domain Artifact

Evaluate the artifact, not the Generator's confidence. Remain read-only for production content.

## Workflow

1. Confirm evaluator independence. Do not accept the Author's score or verdict.
2. Read the raw artifact, declared requirements, validated research ledger, authoritative
   sources, required dependencies, relevant schema,
   [scoring-rubric.md](references/scoring-rubric.md), and
   [evaluation-record.md](references/evaluation-record.md).
3. Reproduce applicable schema, reference, policy, and narrow behavior checks.
4. Score every rubric dimension from observable evidence. Record findings with severity,
   concrete evidence, and source IDs present in the ledger.
5. Set every hard gate explicitly. Use `blocked_reasons` when required authority, source,
   environment, or evidence is unavailable.
6. Return the complete raw evaluation JSON to the Builder. A read-only evaluator must not write
   process evidence. The Builder persists that exact payload and normalizes it deterministically:

```bash
python3 .agents/skills/evaluate-domain-artifact/scripts/score_evaluation.py \
  --artifact domains/<domain-path>/<artifact> \
  --artifact-label <artifact-relative-path> \
  --input /path/to/raw-evaluation.json \
  --output changes/<change-id>/evaluations/<artifact>.evaluation.json
```

`--artifact-label` must exactly match the path declared in `session.json` (for example
`DOMAIN.md`). Use `.` for the whole-Pack evaluation.

7. Re-read the normalized record supplied by the Builder and confirm the verdict and findings. Do
   not repair the artifact.

## Verdict Policy

`pass` requires all of the following:

- computed weighted score is strictly greater than 90;
- every hard gate is `true`;
- every cited source ID exists in the validated research ledger;
- no P0 or P1 finding exists;
- no blocked reason exists.

Otherwise return `fail` or `blocked`. A high score never overrides a hard-gate or severity
failure.

## Guardrails

- Do not modify Domain production artifacts during evaluation.
- Do not weaken a criterion or omit a finding to cross the threshold.
- Do not infer professional correctness from schema validity alone.
- Do not fabricate sources, execution, independence, or evidence.
- Bind every verdict to the artifact digest so later edits invalidate the evaluation.
