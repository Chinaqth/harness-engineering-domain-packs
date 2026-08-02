# Engineering Web Activation Decision

## Decision

Activate the reusable public Web Frontend Engineering baseline with `platform-web` acting as both
the accountable owner and the authorized reviewer.

Project architecture, commands, browser and assistive-technology matrices, quality targets,
security baselines, and operational permissions are project/task inputs. Their absence does not
block global Domain registration from becoming active, but it must block every dependent task
claim or action. Activation grants routing eligibility only.

## Authority

On 2026-08-02, the user explicitly stated that they are the reviewer, represent `platform-web`,
authorize activation, and approve proceeding. This record preserves that attestation without
claiming a personal identity not supplied by the approver.

## Consequences

- A resolver may consider the Domain for matching tasks.
- Capability permission clauses and task contracts remain authoritative and fail closed.
- Deployment, production access, release approval, exceptions, legal claims, and risk acceptance
  continue to require separate explicit authority.
- The completed G1 per-Domain Chinese README prerequisite is published in the same batch so the
  exact `main` tree accepts and validates the required Web Domain inventory.

## Rollback

Revert the scoped activation commit. This restores lifecycle `draft`, removes the activation
evidence reference and reviewer entry, and preserves the completed public baseline.
