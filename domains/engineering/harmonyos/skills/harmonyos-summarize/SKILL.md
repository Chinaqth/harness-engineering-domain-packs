---
name: harmonyos-summarize
description: Implement the summarize lifecycle stage for HarmonyOS tasks dispatched by Harness Kernel 4.0.
---

# HarmonyOS Summarize

Execute only when the Kernel dispatches this Domain stage. Preserve the dispatch context_id and invocation ID in the receipt. The host calls the Skill; the Kernel supplies no professional implementation.

Read actual stage results and issues. Return a user-facing summary and checklist of delivered artifacts, performed checks, failed/unverified work, assumptions/alternatives and user next actions. Do not modify professional artifacts or upgrade unverified claims. Summarize solved routine issues compactly and retain material unresolved findings.

Return status completed, partial, unavailable or error. Preserve actual evidence and platform/user authority. Ordinary quality failures are recorded and do not prevent lifecycle evaluation and summary.
