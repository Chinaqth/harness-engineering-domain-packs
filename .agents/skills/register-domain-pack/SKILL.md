---
name: register-domain-pack
description: Register a new enterprise function as a draft Domain Pack by creating the standard directory contract and updating the central registry. Use when a new department, discipline, platform team, or reusable professional capability must become discoverable through the Harness routing protocol.
---

# Register Domain Pack

Register the identity and empty contract of a new function without inventing its professional
content. Keep the empty result in `draft`; `$complete-domain-pack` automatically activates it after
the role, capabilities, and automated evidence are complete.

## Workflow

1. Locate the Domain Pack repository by finding `registry/domains.json` and `domains/_template/`.
2. Read `registry/domains.json` and confirm that the proposed function is not already registered under the same or a confusingly similar identity.
3. Collect four facts from the user or an authoritative source:
   - A stable dotted ID such as `engineering.ios`;
   - A human-readable display name;
   - A named team or role that owns the Domain Pack;
   - A concise, durable description of its responsibility.
4. Read `references/registration-contract.md` before choosing the ID or owner.
5. Preview the registration:

```bash
python3 .agents/skills/register-domain-pack/scripts/register_domain_pack.py \
  --root . \
  --id engineering.ios \
  --display-name "iOS Engineering" \
  --owner "ios-platform-team" \
  --description "Owns reusable iOS delivery practice and evaluation." \
  --dry-run
```

6. If the preview is correct, run the same command without `--dry-run`.
7. Run `./scripts/domain-check.sh`. Treat a failed check as a failed registration and report it immediately.
8. Report the created path, registry entry, lifecycle state, and the next command:
   `Use $complete-domain-pack to complete <domain-id> from its registered identity.`

## Guardrails

- Do not hand-create a Domain directory or edit the registry as a substitute for the script.
- Do not invent an owner. Ask for one if no authoritative owner can be found.
- Do not register project names, temporary initiatives, or individual tasks as enterprise Domains.
- Do not copy project-specific architecture, credentials, customer data, or environment values into a Domain Pack.
- Do not mark the empty newly registered Pack `active`; automatic activation belongs to the
  completion workflow.
- Do not add routes or capabilities merely to make validation pass; the Domain Owner must define meaningful content.
- Treat a published Domain ID as immutable. Deprecate and replace it instead of renaming it.
- Do not bypass the staged registration script with raw token replacement. JSON values must be encoded structurally, and a failed registry update must roll back the Domain directory.

## Expected Result

The script stages `domains/<id segments>/`, encodes JSON values structurally, and commits the
Domain directory and sorted registry entry as one rollback-safe operation. The result uses version
`0.1.0` and status `draft`. A dry run makes no changes, and invalid or duplicate registrations are
rejected. Completion remains a separate rollback-safe transaction handled by
`$complete-domain-pack`, which automatically activates a passing Pack.
