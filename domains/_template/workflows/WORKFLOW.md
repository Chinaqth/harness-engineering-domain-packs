# Domain Workflow

Define repeatable stages, entry conditions, handoffs, outputs, failure recovery, and required evidence. Keep project-specific commands in project overlays.

For a capability that will mutate a target project, the workflow must have a professional planning
stage before its first mutating stage. That stage contributes concrete Domain-owned steps,
affected surfaces, checks, risks, and recovery to the target project's
`changes/<change-id>/task.md`. The complete integrated Markdown plan must then be presented to the
user and execution must pause. Resume only after the Kernel records explicit confirmation of the
current plan digest. If the user requests changes, revise the durable plan and present it completely
again. Read-only work may continue under the Kernel's risk-proportional policy.
