# Engineering Web Activation Requirements

## Objective

Activate `engineering.web@0.1.0` after an authorized `platform-web` reviewer approved the
source-traceable public baseline, then publish the scoped activation change to `main`.

## Scope

- Record the reviewer and approval as durable repository evidence.
- Reclassify organization-specific project facts as task/project-overlay entry requirements rather
  than global Domain activation blockers.
- Synchronize the Domain manifest and registry lifecycle to `active`.
- Update lifecycle statements in production documentation.
- Publish the completed `changes/20260802-domain-readme-ch/` G1 prerequisite and its declared
  files because the Web Pack's required `README-CH.md` is invalid against the prior `main` policy.
- Independently verify activation readiness, active routing, fail-closed permission behavior, and
  rollback.
- Commit and push only the activation, `engineering.web` completion, and declared per-Domain
  README prerequisite scope.

## Non-goals

- Grant deployment, production, dependency, security-exception, release, or risk-acceptance
  permissions.
- Invent a project framework, architecture, command set, browser matrix, quality threshold, or
  security policy.
- Include pre-existing working-tree changes outside the completed per-Domain README prerequisite.

## Acceptance Criteria

1. `platform-web` is recorded as owner and reviewer, with explicit activation approval evidence.
2. Pack evaluation reports `content_state=content-complete` and `state=activation-ready`.
3. Registry and manifest both report `active`; lifecycle and reference validation pass.
4. A representative Web frontend task is routable while missing task-specific authority remains
   fail-closed.
5. An independent evaluator returns `Pass` with no P0/P1 finding.
6. The scoped commit is pushed to `origin/main` without unrelated working-tree changes.

## Risks

- Direct publication to `main` is externally visible and may be constrained by branch protection.
- The repository validates routing metadata rather than a deployed resolver.
- Activation makes the Domain selectable but does not make an underspecified task executable.
