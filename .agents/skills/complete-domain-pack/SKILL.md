---
name: complete-domain-pack
description: Autonomously research, author, independently evaluate, complete, and activate a registered draft Domain Pack from its Domain ID alone. Use immediately after $register-domain-pack when the user wants the function role and capabilities made available without a separate lifecycle approval step.
---

# Complete Domain Pack

From the authoritative Domain Packs checkout, accept one registered Domain ID and complete its
public professional baseline through isolated Researcher, Author, Artifact Evaluator, and Pack
Evaluator contexts. Do not run against the installed read-only runtime copy or a product project.

## Required Input

Require only the registered Domain ID, for example `engineering.android`. Read display name,
description, owner, version, status, and path from the registry and manifest. Do not require the
user to provide professional scope, capabilities, sources, or non-goals.

## Completion Modes

This workflow runs in one of two modes defined in `docs/GOVERNANCE.md`:

- **Default mode (默认模式)**: the normal path below, with per-artifact independent evaluation,
  the final Pack evaluation, and automatic activation through `finalize_domain_pack.py`.
- **Intervention mode (介入模式)**: only when the user explicitly directs it as the Domain owner
  and names the stages to skip (for example, waiving per-Skill scoring for owner-trusted Skill
  packages in their familiar profession). In intervention mode:
  1. Record the direction, claimed authority, and date verbatim in
     `changes/<domain-id>-completion/decision.md` before skipping anything.
  2. Run only the mandatory deterministic gates in
     [lifecycle-gates.md](references/lifecycle-gates.md): `scripts/validate_registry.py`,
     `./scripts/domain-check.sh`, `check_pack.py` with the validated ledger, and
     documentation-registry consistency.
  3. Synchronize `registry/domains.json` and the manifest to `active` manually and write the
     intervention record under `changes/<domain-id>-activation/` naming every waived gate,
     retained gate results, and the rollback path.
  4. Report the result as an owner-directed intervention-mode activation and name every waived
     gate. Never report it as passing the automated evaluation gates.
  5. Never waive Kernel policy, evaluator independence for artifacts still being evaluated,
     capability permission clauses, fail-closed behavior, or the non-authoritative status of
     bundled corpora.

## Workflow

1. Locate the authoritative checkout containing `registry/domains.json`, `domains/_template/`,
   and `.codex/agents/`. Refuse an unregistered ID or a Pack outside `draft`.
2. Read repository rules, Domain architecture and governance, relevant schemas,
   [research-contract.md](references/research-contract.md), and
   [lifecycle-gates.md](references/lifecycle-gates.md).
3. Create or resume `changes/<domain-id>-completion/` with requirements, tasks, contract,
   decision, progress, acceptance, `session.json`, `research/`, and `evaluations/`.
4. Delegate research to a fresh `domain_profession_researcher` custom agent. Give it only the
   Domain ID, registered identity facts, repository research contract, and output paths.
5. Require the Researcher to discover current primary, standards-body, or professional-body
   sources; record repository identity facts; infer a source-supported responsibility boundary
   and capability hypotheses; and record organization-specific gaps without inventing answers.
   Require the exact three-part handoff envelope in
   [research-contract.md](references/research-contract.md). Persist it mechanically; the Builder
   must not supply missing professional claims.
6. Validate the ledger:

```bash
python3 .agents/skills/complete-domain-pack/scripts/validate_research.py \
  --root . \
  --domain-id <domain-id> \
  --ledger changes/<domain-id>-completion/research/sources.json
```

7. Build the production artifact plan in
   [artifact-order.md](references/artifact-order.md). Declare every production file and the
   research ledger in `session.json` using
   [session-contract.md](references/session-contract.md).
8. For one artifact at a time, delegate authoring to a fresh `domain_artifact_author` agent using
   `$author-domain-artifact`. Pass only the validated ledger, relevant source IDs, prior
   dependencies, and artifact contract.
9. Run deterministic schema and reference checks. Preserve failures before revision.
10. Delegate evaluation to a fresh read-only `domain_artifact_evaluator` agent using
    `$evaluate-domain-artifact`. Do not pass Author confidence or an intended verdict.
11. Normalize the evaluation. Require score greater than 90, all hard gates including
    `professional_sources_traceable`, no P0/P1 finding, and source IDs present in the ledger.
12. If evaluation fails, return findings to a fresh Author iteration. Stop after five iterations
    or two consecutive improvements below two points and report `blocked`.
13. After all English production artifacts stabilize, author and independently evaluate the
    required `README-CH.md` as the final production artifact. Require it to enumerate every
    non-hidden production file and directory in Chinese, explain both responsibility and actual
    behavior, and remain a faithful guide rather than an independent policy source.
14. After all artifacts pass, delegate final evaluation to a fresh read-only
    `domain_pack_evaluator` agent using `$evaluate-domain-pack`. Allow at most three Pack
    iterations.
15. Run research validation, session validation with `--require-final`,
    `evaluate-domain-pack/scripts/check_pack.py`, and `./scripts/domain-check.sh`.
16. Require `content_state=content-complete`, `state=activation-ready`, and a current passing final
    evaluation. Organization-specific gaps remain downstream project or task inputs and do not
    block reusable Domain lifecycle.
17. Finalize the Pack in the same workflow:

```bash
python3 .agents/skills/complete-domain-pack/scripts/finalize_domain_pack.py \
  --root . \
  --domain-id <domain-id> \
  --ledger changes/<domain-id>-completion/research/sources.json \
  --session changes/<domain-id>-completion/session.json
```

18. Re-run `check_pack.py` and `./scripts/domain-check.sh`; require synchronized `active` status in
    the registry and manifest. Report `active`, `blocked`, or `fail` as the user-facing result.

## Custom Agent Contract

Run this workflow through the project `domain_pack_builder` custom agent. It must dispatch:

- `domain_profession_researcher`: read-only research and source ledger;
- `domain_artifact_author`: one production artifact, workspace-write;
- `domain_artifact_evaluator`: one digest- and source-bound read-only evaluation;
- `domain_pack_evaluator`: final read-only Pack evaluation.

If named custom agents or fresh evaluator contexts are unavailable, report `blocked`. Do not
collapse G2 authoring and final evaluation into one context.

## Public Baseline Boundary

Use current authoritative public practice to create reusable professional content. Treat internal
reviewers, organization permissions, private architecture, project commands, local paths, and
unpublished policy as downstream project or task inputs. Their absence does not block reusable
Domain completion or activation, but every dependent task action and claim must fail closed.

## Guardrails

- Do not use model memory as the only professional source.
- Do not cite search-result pages, unsourced summaries, or low-authority aggregators as primary
  evidence.
- Do not convert common industry practice into organization policy.
- Do not place research or evaluation evidence inside the production Domain directory.
- Do not create content merely to cross the score threshold.
- Do not weaken Kernel policy, scoring, hard gates, evaluator independence, or iteration budgets.
- Do not enter intervention mode without an explicit user direction recorded before any stage is
  skipped, and do not waive deterministic validation, Kernel policy, or fail-closed behavior in
  any mode.
