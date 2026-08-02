# Engineering Web Routing Scenarios

## Method

- Revision: `a5e87f54e1ee0a2cca6215eed771639721f1a1dc`
- Date: 2026-08-02
- Environment: local authoritative Domain Packs checkout, Python 3
- Inputs: current `domain.json`, `routes.json`, and `capabilities.json`
- Matching: require the task type and at least one exact declared signal substring; sort candidates
  by descending numeric priority and then route ID; resolve capability state, dependencies, pinned
  version, and lifecycle fail-closed.
- Mutation: none. Disabled capability and missing dependency were injected only into the in-memory
  scenario state.

| Scenario | Input | Expected | Actual | Result |
| --- | --- | --- | --- | --- |
| Positive match | `web-frontend-implementation` plus exact HTML semantics signal | Select `semantic-web-interface-engineering` as a content candidate | Selected that route and capability | Pass |
| Negative signal | Supported task plus database/queue-only evidence | No match | `no-route-match` | Pass |
| Negative task | Native iOS task plus exact HTML signal | No match | `no-route-match` | Pass |
| Ambiguity | `web-frontend-review` plus exact ECMAScript and HTML signals | Deterministically select higher-priority ECMAScript route | Selected `ecmascript-browser-application-behavior` at priority 450 over semantic route at 400 | Pass |
| Disabled capability | Exact CSP route input with its capability disabled in memory | Reject | `capability-disabled` | Pass |
| Missing dependency | Exact HTTP route input with a synthetic unresolved dependency | Reject | `missing-dependency` | Pass |
| Version mismatch | Exact accessibility input pinned to `0.2.0` while registry version is `0.1.0` | Reject | `version-mismatch` | Pass |
| Draft lifecycle | Positive HTML input requested for production routing | Reject because lifecycle is `draft` | `draft-lifecycle` | Pass |

## Limitations

This repository provides contracts and metadata, not a production routing runtime. The scenario
harness therefore exercises the declared matching and fail-closed semantics directly against the
JSON documents. It does not claim that an external resolver implementation exists or is activated.
