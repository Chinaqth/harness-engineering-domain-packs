# Autonomous Domain Completion Requirements

## Problem

Registration creates a safe but empty draft. A user who recognizes a durable enterprise function
may not know enough professional detail to author its rules, workflows, evaluators, Skills,
capabilities, and routes. Requiring that user to supply the professional corpus defeats the value
of assisted Domain registration.

## Objective

Accept a registered Domain ID as the only required input, research a source-traceable public
professional baseline, fill the complete Domain Pack structure, independently evaluate each
artifact, revise within bounded budgets, and evaluate the assembled Pack.

## Scope

- Add one public completion Skill and project-scoped Custom Agents for research, authoring,
  artifact evaluation, Pack evaluation, and orchestration.
- Add a deterministic research ledger and source-coverage gate.
- Distinguish content completeness from organization-specific activation readiness.
- Preserve all scoring, digest, containment, history, convergence, and lifecycle safeguards.
- Make registration recommend the completion workflow without coupling the two transactions.

## Non-goals

- Do not infer internal reviewers, permissions, architecture, commands, or unpublished policy.
- Do not treat public professional practice as organization approval.
- Do not automatically change a Domain lifecycle to `active`.
- Do not modify the Harness Kernel or CLI source.
- Do not require the registering user to author professional content.

## Acceptance Criteria

1. `$complete-domain-pack` requires only a registered Domain ID.
2. A read-only Researcher Agent creates a validated source ledger from authoritative public and
   repository sources.
3. Separate Author, Artifact Evaluator, and Pack Evaluator Agent contexts are project-configured.
4. Every normalized evaluation cites source IDs and passes a source-traceability hard gate.
5. Content-complete and activation-ready checks are reported separately.
6. Missing organization-specific facts produce `needs-org-input` without blocking public baseline
   completion.
7. Existing registration, scoring, session, path, history, and repository gates remain compatible.
8. The workflow is forward-tested in an isolated repository and independently evaluated.

## Risks

- Research may use low-authority or stale sources.
- Generated content may be plausible but unsupported.
- Agent recursion may lose evaluator independence or exceed budgets.
- A public baseline may be mistaken for organization policy.
- Custom Agent configuration may drift from the Skill contract.

