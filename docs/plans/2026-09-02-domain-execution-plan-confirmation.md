# Domain Execution Plan Confirmation Migration

## Scope

This migration applies to `engineering.harmonyos` 6.0.0 and `engineering.web` 1.0.0. It changes
the transition between Domain professional planning and mutating implementation. It does not
change Domain IDs, route IDs, capability IDs, tool permissions, release authority, or the Domain
Pack JSON contract.

## Required Kernel

Adopters must use Harness Kernel protocol 3.0 and Routing Plan 4.0. Earlier Kernel versions do not
bind the target-project `task.md` digest or require evidence that the complete plan was shown to
the user.

## Producer Migration

For a Domain-augmented mutating task:

1. Run only authorized read-only baseline, diagnosis and professional planning after routing.
2. Integrate every selected Domain contribution into the target project's
   `changes/<change-id>/task.md`.
3. Bind that artifact through the Routing Plan `execution_plan` object.
4. Display the complete current Markdown to the user and pause.
5. Record a decision only with matching `presented_execution_plan` artifact, digest and evidence.
6. If the plan changes, regenerate the Routing Plan and repeat presentation and confirmation.

Read-only Domain work remains risk-proportional. Model-native tasks continue under Kernel approval
without a Domain-specific execution-plan requirement.

## Compatibility and Rollback

Projects pinned to HarmonyOS 5.x or Web 0.x retain their prior Domain workflow. Do not relabel an
old Pack as the new major version. To roll back before release, restore the earlier Domain version
and Kernel compatibility pin together. After adoption, a project may pin the earlier major only if
its Kernel and project overlay still declare that tuple as supported; never discard an already
recorded plan or approval audit trail.
