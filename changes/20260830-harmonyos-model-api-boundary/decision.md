# Architecture Decision

## Decision

Adopt a mandatory pure-data `models/` boundary, restrict business `api/` to endpoint, repository and
HTTP-service responsibilities, and remove the feature-owned network-adapter fallback.

## Alternatives considered

1. **Keep 4.0.0 optional model placement and local adapter creation.** Rejected because runtime
   workflows can continue placing DTOs below `api/` and inventing a second network layer.
2. **Require model placement but retain `api/transport/`.** Rejected because the business module
   would still own infrastructure outside the approved four-part API structure.
3. **Require model placement and fail closed when no project tool exists.** Selected because it
   creates one observable dependency direction and leaves network-infrastructure decisions with the
   proper architecture owner.

## Compatibility

This is a major-version change from `4.0.0` to `5.0.0`. Existing projects can remain pinned to 4.x.
The 5.0.0 migration boundary is new or materially changed request/response models and their direct
API dependency chain; unrelated legacy files are not migrated implicitly.

## Distribution decision

This change updates only the authoritative Domain Pack. Kernel pinning, CLI bundle generation,
local Runtime installation and product-project migrations require later, separately authorized
work.
