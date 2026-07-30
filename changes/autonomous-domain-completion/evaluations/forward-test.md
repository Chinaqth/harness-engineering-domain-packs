# Isolated Android Completion Forward Test

## Result

The minimum real workflow slice passed in
`/tmp/domain-completion-test.nf41HJ` without changing the authoritative checkout.
The only business input was the registered draft Domain ID `engineering.android`.

## Journey

1. A delegated Researcher inspected the registered identity and current authoritative public
   sources.
2. The Builder persisted a research ledger, capability map, and responsibility boundaries.
3. Research validation passed with 11 authoritative professional Web sources and one repository
   identity source.
4. A separate Author completed `DOMAIN.md`.
5. A fresh read-only Evaluator returned raw evaluation JSON.
6. The Builder persisted and normalized that payload with artifact label `DOMAIN.md`.
7. Session validation and the isolated repository check passed.
8. The whole-Pack check failed closed because the deliberately limited fixture did not complete
   the remaining production artifacts or final evaluation.

## Evidence

| Evidence | Result | SHA-256 |
| --- | --- | --- |
| Research ledger | Valid, 12 source IDs | `04728ecd277cd10858614d0bce166c0bfe623a79bf1869fe3f68513df3188212` |
| Completed `DOMAIN.md` | Authored by isolated Author | `7d7f978d792a59d3ef85cdfd9a0b38dc455fe5840b683b345a4d85a18512da5c` |
| Raw independent evaluation | Complete source-bound payload | `8556637417ddb745df482275fe51a4cb1f401f5a743a2631570d989f975333f6` |
| Normalized evaluation | `pass`, score `97.45` | `26b1ed0cfe04b15264898397234d6c0d3d410bef52b2d2052ee72312f1c379ad` |
| Session | Valid, no issues | `3301f00b59c77f45c3071ce00a676381f19beffffa354f1bc33f631d90f1a969` |
| Invalid-label negative fixture | Rejected by session validation | `3e41099c8984f4610486e0deafa396b3448d60a3254a6bd3c1bc49f4ac00190a` |

All six hard gates passed, including `professional_sources_traceable`. The artifact digest in the
normalized evaluation exactly matched the completed `DOMAIN.md`. The isolated repository check
passed its registry, Skill, Agent, and 33-test suite.

## Findings and Corrections

The forward test found two workflow defects:

1. The Researcher handoff did not originally guarantee three machine-persistable outputs. The
   production contract now requires `sources_json`, `capability_map_markdown`, and
   `responsibility_boundaries_markdown`; the Builder may only persist them mechanically.
2. The normalization example originally omitted the session artifact label. The production
   workflow now requires `--artifact-label`, the CLI rejects an omitted label, and whole-Pack
   evaluation uses label `.`.

## Limitation

This fixture intentionally proved research plus one artifact's Author-Evaluator loop and the
Pack's fail-closed behavior. A future full Android completion test should exercise every artifact,
the complete routing scenario matrix, and the final Pack evaluation in one session.
