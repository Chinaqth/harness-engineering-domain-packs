# Decision

Use current Huawei primary documentation and DevEco CLI evidence as the professional authority. Preserve the user-added Skills as implementation inputs, but replace unavailable CodeGenie assumptions with the available `devecocli` workflow and fail closed on SDK, API, device, permission, signing, or project uncertainty.

The user explicitly authorized a coarser evaluation granularity: treat each of the six top-level
Skill packages as one capability unit and preserve every bundled reference corpus unchanged. The
completion therefore resumes with one summary and evaluation per Skill package plus the normal
core Domain artifacts. This decision does not modify or weaken repository validators; if the
strict final session validator still requires every nested file, lifecycle finalization remains
blocked and must be reported precisely.

## Rollback

Restore only changed files under `domains/engineering/harmonyos/` and remove `changes/engineering.harmonyos-completion/`; preserve the registered draft entry and unrelated user work.
