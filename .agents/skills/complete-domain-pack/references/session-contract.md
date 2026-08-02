# Development Session Contract

Store paths relative to the Domain directory and evaluation paths relative to the change
directory:

```json
{
  "schema_version": "1.0",
  "domain_id": "engineering.android",
  "research_ledger": "research/sources.json",
  "max_artifact_iterations": 5,
  "max_pack_iterations": 3,
  "artifacts": [
    {
      "path": "DOMAIN.md",
      "evaluations": [
        "evaluations/DOMAIN.1.evaluation.json"
      ]
    }
  ],
  "final_evaluations": [
    "evaluations/final.1.evaluation.json"
  ]
}
```

Append evaluation paths in iteration order. Do not replace failed evidence. The latest artifact
evaluation must pass and match the current artifact digest. A final evaluation must use artifact
label `.` and bind its digest to the complete Domain directory. Before final delivery, declare
every non-hidden production file in the Domain directory; `.gitkeep` files are not production
artifacts. `README-CH.md` is a required production artifact and must be evaluated against the
final file inventory before whole-Pack evaluation.
