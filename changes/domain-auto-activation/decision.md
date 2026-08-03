# Decision: Complete and Activate in One Workflow

## Decision

Keep registration as a draft-only identity transaction. Make successful autonomous completion the
single activation boundary: after all automated content and routing checks and independent Pack
evaluation pass, atomically synchronize registry and manifest to `active`.

Reviewers and activation evidence remain compatible optional metadata but are not lifecycle gates.
Organization gaps are reported for downstream project and task contracts, not used to suppress the
reusable Domain role.

Non-breaking registration and completion is G1 by default. Permission, security-boundary,
breaking-compatibility, or production-configuration changes still use the higher Kernel risk level.

## Rollback

Revert this change. For any Pack activated by the new finalizer, synchronously restore registry and
manifest status to `draft` before using the previous completion workflow.
