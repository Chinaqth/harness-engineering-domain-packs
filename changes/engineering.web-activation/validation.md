# Engineering Web Activation Validation

## Classification

- Lifecycle: `active`
- `content_state=content-complete`
- `state=activation-ready`
- Independent G2 verdict: `Pass`
- Final normalized score: `98.30`

## Evidence

- `validate_research.py`: valid, 12 source IDs, no errors.
- `validate_session.py --require-final`: valid, no issues.
- `check_pack.py`: content and activation verdicts pass; no issues.
- `domain-check.sh`: registry, repository Skill, and Custom Agent validation pass; 43 tests pass.
- `git diff --check`: pass.
- The completed `20260802-domain-readme-ch` G1 dependency is required because the previous `main`
  language policy rejects the Web Domain's required Chinese inventory.
- Artifact gates: all 11 production artifacts have current passing evaluations.
- Critical journey: positive active routing, negative signal/task, deterministic ambiguity,
  disabled capability, missing dependency, version mismatch, draft-lifecycle fixture, and missing
  task-input fail-closed scenarios pass.

## Permission Boundary

Activation grants routing eligibility only. Project architecture, commands, matrices, targets,
security baselines, and operational permissions remain project/task inputs. Missing inputs block
dependent claims and actions with `needs-org-input`.

## Residual Risks

- Metadata scenarios do not prove a deployed resolver integration.
- Direct `main` publication depends on remote credentials and branch protection.
- Unrelated working-tree changes must remain outside both commits.

## Rollback

Revert the publication-evidence commit, then revert the scoped activation commit. The second revert
restores `draft` lifecycle and removes the reviewer/evidence activation bindings while preserving
the public professional baseline.
