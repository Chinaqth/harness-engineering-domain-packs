# Profession Research Contract

## Inputs

Use only the registered Domain ID and identity facts from the registry and manifest.

## Source Priority

1. Official platform, language, framework, regulator, or standards-body documentation.
2. Recognized professional-body guidance.
3. Repository identity and schema facts.

Do not use model memory, search-result pages, marketing summaries, forums, or generic tutorials as
the sole support for a professional claim.

## Required Outputs

Create:

```text
changes/<domain-id>-completion/research/
├── sources.json
├── capability-map.md
└── responsibility-boundaries.md
```

The ledger must include at least two distinct authoritative web sources, repository identity facts,
source-supported capability hypotheses, and organization-specific gaps. Record exact URLs,
publishers, retrieval timestamps, claims, and stable source IDs.

The read-only Researcher must return one handoff envelope:

```json
{
  "sources_json": {},
  "capability_map_markdown": "# Capability Map\n...",
  "responsibility_boundaries_markdown": "# Responsibility Boundaries\n..."
}
```

`sources_json` is the complete `sources.json` object, not a path. Both Markdown strings must be
non-empty and cite stable source IDs inline. The Builder writes these three values to the required
paths without adding, deleting, or reinterpreting professional claims. A malformed or incomplete
envelope is `blocked`; it is not permission for the Builder to supply missing research.

## Organizational Gaps

Record unknown reviewers, permissions, internal standards, private architecture, product commands,
and approval evidence as downstream task or project gaps. Do not ask for them before generating the
public baseline and do not invent values. Retain the `required_for_activation` boolean for schema
compatibility and set it to `false` for new research because these facts no longer gate reusable
Domain lifecycle.

## Failure

Return `blocked` when authoritative sources cannot be accessed or do not support a responsible
baseline. Preserve the attempted queries and unavailable evidence.
