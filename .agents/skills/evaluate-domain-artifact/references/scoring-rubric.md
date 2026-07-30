# Artifact Scoring Rubric

Score each dimension from 0 to 100 using observable evidence:

| Dimension | Weight | Evidence |
| --- | ---: | --- |
| `contract` | 20 | Schema, required sections, declared artifact contract |
| `professional` | 20 | Correct, complete, source-backed professional practice |
| `boundaries` | 15 | Ownership, exclusions, handoffs, project/Domain separation |
| `executability` | 15 | Actionable sequence, inputs, outputs, failure handling |
| `verifiability` | 15 | Measurable criteria, evidence, negative paths |
| `architecture` | 10 | Kernel compatibility, dependencies, cross-file consistency |
| `maintainability` | 5 | Clarity, stable identifiers, focused content |

The normalized score is the weighted average. Passing requires a score strictly greater than 90.

Set all hard gates:

- `schema_passed`
- `references_resolved`
- `professional_sources_traceable`
- `no_invented_authority`
- `kernel_constraints_preserved`
- `owner_facts_authoritative`

Any false hard gate, P0/P1 finding, or blocked reason prevents a pass regardless of score.
