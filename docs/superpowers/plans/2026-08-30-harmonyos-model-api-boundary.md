# HarmonyOS Business Model and API Boundary Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enforce `models/` as the only business-data boundary, restrict business `api/` to the approved four-part request structure, and remove the feature-owned transport fallback.

**Architecture:** Update every authoritative HarmonyOS Domain layer from the hard rule through workflow, Skills, references, evaluator, evidence and human-readable summaries. Record the breaking policy as Domain version `5.0.0`; defer Kernel, CLI bundle and product-project rollout.

**Tech Stack:** Markdown Domain contracts, JSON registry metadata, repository validation scripts.

**Spec:** `docs/plans/2026-08-30-harmonyos-model-api-boundary-design.md`

## Global Constraints

- Use `models/`, not a parallel singular `model/` directory.
- Request DTOs belong in `models/request/`; response DTOs, envelopes and response-error data belong in `models/response/`.
- Other entities, value objects, enums, state and pure data definitions belong below `models/`.
- Business `api/` contains `XxxApi.ets`, `XxxHttpService.ets`, `XxxHttpRepositoryImpl.ets` and `repository/IXxxHttpRepository.ets`.
- Business-module development must not create `api/transport/` or a feature-owned official-SDK adapter.
- No CatchPet or other product-project files are modified.
- Kernel pins, CLI bundle and local runtime rollout are out of scope.

---

### Task 1: Record the policy and version boundary

**Files:**
- Create: `changes/20260830-harmonyos-model-api-boundary/`
- Modify: `domains/engineering/harmonyos/domain.json`
- Modify: `registry/domains.json`

**Interfaces:**
- Consumes: the approved design document.
- Produces: an owner-requirement ledger, acceptance criteria and the `5.0.0` compatibility statement used by all later tasks.

- [ ] **Step 1:** Add the change task, requirements, contract, decision, research ledger, progress, validation and acceptance records with explicit Domain-only scope.
- [ ] **Step 2:** Change Domain and registry versions from `4.0.0` to `5.0.0` and describe the breaking model/API boundary and removed adapter fallback.
- [ ] **Step 3:** Validate both JSON files with `python -m json.tool`.

### Task 2: Update the hard rule and workflow

**Files:**
- Modify: `domains/engineering/harmonyos/rules/BASE.md`
- Modify: `domains/engineering/harmonyos/workflows/WORKFLOW.md`

**Interfaces:**
- Consumes: the `5.0.0` policy contract.
- Produces: mandatory placement, fail-closed behavior and evidence requirements for downstream Skills and evaluators.

- [ ] **Step 1:** Make `HMOS-RULE-11` require business DTOs under `models/request|response` and prohibit pure data declarations under `api/`.
- [ ] **Step 2:** Remove authorization to create a feature-owned transport or SDK adapter and require owner handoff when no verified project tool exists.
- [ ] **Step 3:** Update workflow decision tables, inventories and delivery evidence language to match the hard rule.
- [ ] **Step 4:** Search these files for stale `feature-owned adapter`, `api/transport` and optional-model wording.

### Task 3: Update orchestrating Skills and architecture references

**Files:**
- Modify: `domains/engineering/harmonyos/skills/harmonyos-engineering/SKILL.md`
- Modify: `domains/engineering/harmonyos/skills/hmos-business-module-development/SKILL.md`
- Modify: `domains/engineering/harmonyos/skills/hmos-business-module-development/references/business-module-architecture.md`
- Modify: `domains/engineering/harmonyos/skills/hmos-business-module-development/references/network-request-conventions.md`

**Interfaces:**
- Consumes: `HMOS-RULE-11` and the workflow contract.
- Produces: executable Skill instructions that cannot reintroduce Transport or relocate DTOs.

- [ ] **Step 1:** Replace optional model placement with mandatory `models/request|response` mapping and preserve unrelated legacy files.
- [ ] **Step 2:** Replace the network resolution ladder with supplied tool, project search and fail-closed handoff.
- [ ] **Step 3:** Replace the `api/transport/` example with the approved API and models trees.
- [ ] **Step 4:** Remove feature-owned adapter creation, verification and handoff clauses from both Skills.
- [ ] **Step 5:** Search all four files for contradictory ownership or fallback language.

### Task 4: Strengthen evaluation, evidence and summaries

**Files:**
- Modify: `domains/engineering/harmonyos/evaluators/EVALUATOR.md`
- Modify: `domains/engineering/harmonyos/templates/delivery-evidence.md`
- Modify: `domains/engineering/harmonyos/DOMAIN.md`
- Modify: `domains/engineering/harmonyos/README-CH.md`

**Interfaces:**
- Consumes: the final architecture and workflow wording.
- Produces: enforceable pass/fail criteria, handoff evidence and synchronized English/Chinese descriptions.

- [ ] **Step 1:** Fail new or materially changed business DTOs under `api/`, model-to-API reverse dependencies and business-owned Transport creation.
- [ ] **Step 2:** Record model inventories and directory/dependency checks instead of Transport implementation evidence.
- [ ] **Step 3:** Update Domain boundary and decision-table text, including the no-tool fail-closed outcome.
- [ ] **Step 4:** Update the Chinese inventory without making it an independent policy source.

### Task 5: Validate the authoritative Domain Pack

**Files:**
- Modify: `changes/20260830-harmonyos-model-api-boundary/validation.md`
- Modify: `changes/20260830-harmonyos-model-api-boundary/acceptance.json`
- Modify: `changes/20260830-harmonyos-model-api-boundary/progress.md`

**Interfaces:**
- Consumes: all changed Domain artifacts.
- Produces: reproducible validation and explicit deferred rollout status.

- [ ] **Step 1:** Run repository-wide searches for stale adapter fallback and DTO-under-API examples.
- [ ] **Step 2:** Run `bash scripts/domain-check.sh` from the Domain Pack repository.
- [ ] **Step 3:** Review `git diff --check`, the full diff and the exact changed-file inventory.
- [ ] **Step 4:** Record passing Domain checks and mark Kernel, CLI bundle, local runtime and product migration as deferred rather than complete.
