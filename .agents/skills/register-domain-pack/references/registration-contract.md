# Domain Registration Contract

## What Qualifies as a Domain

A Domain represents a durable enterprise function with a distinct professional practice, owner, workflow, capability surface, and acceptance model. Examples include Product Management, Product Design, iOS Engineering, Web Engineering, Quality Engineering, and Security.

A project, feature, ticket, release, customer, or temporary initiative is not a Domain. Those belong in project overlays or task contracts.

## Identity Rules

- Use a lowercase dotted ID with two or more segments.
- Use durable organizational or capability concepts, not current reporting lines.
- Prefer `discipline.specialization`, for example `engineering.ios`.
- Allowed characters inside each segment are lowercase letters, digits, and hyphens.
- Treat the ID as immutable after it is published.

The dotted ID maps directly to a directory:

```text
engineering.ios -> domains/engineering/ios/
```

## Ownership Rules

The owner must be a stable team or role that accepts responsibility for correctness, lifecycle, compatibility, and review. Do not use an AI agent as the owner. A person may be named when no durable team exists, but the governance record should later migrate to a stable role.

## Initial State

Registration is intentionally conservative:

- Version: `0.1.0`
- Status: `draft`
- Routes: empty
- Capabilities: empty
- Reviewers: empty

Registration makes a function visible to maintainers. It does not make the function selectable by a future production resolver; activation is a separate governed change.
