# Per-Domain Chinese README Requirements

## Objective

Require every registered Domain Pack to contain `README-CH.md`, and require completed Packs to
use it as an accurate Chinese guide to every non-hidden production file and directory in that
Pack.

## Scope

- Add `README-CH.md` to the registration template and the existing Android draft.
- Make the file part of the required Domain contract and completion artifact order.
- Permit Chinese only in the repository-level and per-Domain `README-CH.md` files.
- Document the contract and add deterministic regression coverage.

## Non-goals

- Do not translate the authoritative production artifacts.
- Do not introduce professional rules or organization policy only in the Chinese guide.
- Do not activate any Domain or change the Kernel or CLI.

## Acceptance Criteria

1. Registration creates a token-resolved `README-CH.md` in every new Domain.
2. Repository validation rejects a registered Domain or template without `README-CH.md`.
3. Completion instructions require an exact Chinese inventory after all other production files.
4. Repository documentation describes the new artifact and the full integrity check passes.

## Risk

G1. This is an additive documentation contract with deterministic enforcement and no runtime
routing or lifecycle change.
