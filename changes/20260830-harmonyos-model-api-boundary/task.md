# HarmonyOS Business Model and API Boundary Task

## Objective

Revise the active HarmonyOS Domain so business-module request, response and other pure data
definitions have one mandatory `models/` boundary, the business `api/` directory has one bounded
request-layer structure, and business-module development no longer creates local network
infrastructure when no verified project tool exists.

## Scope

- Update authoritative HarmonyOS Domain rules, workflow, capabilities, Skills, references,
  evaluator, evidence template and English/Chinese inventories.
- Advance `engineering.harmonyos` from `4.0.0` to `5.0.0` because the fallback and acceptance
  behavior changes incompatibly.
- Apply the migration rule only to new or materially changed request/response models and their
  direct API dependency chain.
- Record the Domain owner requirement and the inspected CatchPet account-module structure as
  separate authority classes.

## Exclusions

- No CatchPet or other product-project migration.
- No Kernel Domain-pin update.
- No CLI bundle rebuild or local Runtime installation.
- No new network client, SDK adapter, third-party dependency or shared network infrastructure.
- No remote push, PR, publication or deployment.

## Completion boundary

The task completes when the authoritative Domain is internally consistent, version metadata is
synchronized, deterministic repository checks pass and deferred distribution/project work is
recorded explicitly.
