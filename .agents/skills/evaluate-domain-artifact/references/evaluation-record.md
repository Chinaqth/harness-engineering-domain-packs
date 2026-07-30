# Evaluation Record Contract

Provide a raw JSON object with:

```json
{
  "schema_version": "1.0",
  "evaluator": "independent-agent-id",
  "iteration": 1,
  "evaluated_at": "2026-01-01T00:00:00Z",
  "source_ids": [
    "android-app-architecture"
  ],
  "dimensions": {
    "contract": 92,
    "professional": 92,
    "boundaries": 92,
    "executability": 92,
    "verifiability": 92,
    "architecture": 92,
    "maintainability": 92
  },
  "hard_gates": {
    "schema_passed": true,
    "references_resolved": true,
    "professional_sources_traceable": true,
    "no_invented_authority": true,
    "kernel_constraints_preserved": true,
    "owner_facts_authoritative": true
  },
  "findings": [],
  "blocked_reasons": []
}
```

Each finding requires `severity` (`p0`, `p1`, `p2`, or `p3`), `summary`, and `evidence`.
Every `source_ids` value must exist in the validated research ledger. The scoring script adds the
artifact path, SHA-256 digest, weighted score, and derived verdict.
