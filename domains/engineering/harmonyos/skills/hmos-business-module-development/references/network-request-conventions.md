# HarmonyOS Network Request Discovery and Delivery Contract

## Purpose and Authority

This contract defines how a HarmonyOS business-module change discovers, selects and verifies an
existing network-request capability without assuming that a dependency or remembered tool symbol
exists. It also fixes the business module's model and API responsibility boundaries. The structure
observed in `PROJECT-DRILL-UGC-NETWORK-EXEMPLAR` remains evidence only. Its package names, exported
symbols, response envelope, authentication, routing, user messaging, base URLs, singleton assembly,
interceptors and network implementation are not HarmonyOS requirements.

Version-sensitive platform APIs must be reconciled under `HMOS-RULE-01` and `HMOS-RULE-02` for the
declared SDK/API baseline. The task or project owns product endpoints, authentication, certificates,
retry and cache policy, backend response semantics, dependency approval and service environments.
Business-module development does not create network infrastructure when the project does not expose
a suitable capability.

## Responsibility Contract

The exact filenames are project facts, but the responsibilities and dependency direction below are
mandatory for new or materially changed business-module request surfaces:

| Responsibility | Required location | Owns | Must not own |
| --- | --- | --- | --- |
| Request models | `models/request/` | Typed outbound business request payloads | Request execution, UI observation or dependencies on API/ViewModel/View code |
| Response models | `models/response/` | Typed inbound payloads, response envelopes and response-error data | Request execution, presentation behavior or dependencies on API/ViewModel/View code |
| Other models | `models/` or recorded model subdirectories | Entities, value objects, enums, state and other pure data definitions | Network side effects or dependencies on API/ViewModel/View code |
| Endpoint contract | `api/XxxApi.ets` | Stable endpoint identity, method and protocol constants | Base environment selection, UI text or request execution |
| Repository contract | `api/repository/IXxxHttpRepository.ets` | Typed business-facing data-access operations using model types | Concrete network-client calls or presentation behavior |
| Repository implementation | `api/XxxHttpRepositoryImpl.ets` | Endpoint selection, request mapping and invocation of one verified project network tool | View state, navigation or business DTO declarations |
| HTTP service | `api/XxxHttpService.ets` | Business pre/post-processing and network-result-to-domain mapping | Direct UI rendering, Toasts, route changes or business DTO declarations |
| ViewModel | `viewmodels/` | Async sequencing and domain-result-to-UI-state mapping | Concrete network-client calls |
| View | `pages/`, `dialogs/` or `components/` | State rendering and user-intent forwarding | Network execution or async business orchestration |

The canonical business-module split is:

```text
src/main/ets/
├── api/
│   ├── XxxApi.ets
│   ├── XxxHttpService.ets
│   ├── XxxHttpRepositoryImpl.ets
│   └── repository/
│       └── IXxxHttpRepository.ets
└── models/
    ├── request/
    │   └── XxxRequest.ets
    ├── response/
    │   └── XxxResponse.ets
    └── entities, value objects, enums, state and other pure data definitions
```

Create `models/request/` or `models/response/` when an authorized module needs the corresponding
model category. An established project-equivalent model or API directory may be preserved only when
its mapping is explicit and maintains the same responsibilities and dependency direction. Do not
create duplicate abstractions merely to match illustrative filenames. Do not create
`api/transport/` or declare business request, response or other pure data classes below `api/`.

## Network Tool Resolution Ladder

Before generating imports or request code, evaluate candidates in this order:

1. **Task-supplied or module-declared tool.** Verify the exact dependency and requested symbol.
2. **Established project network capability.** Search manifests, package entrypoints, source and
   existing repository implementations for a compatible exported abstraction.
3. **Fail-closed handoff.** When neither candidate class yields a suitable tool, stop the dependent
   implementation and hand the candidate map and discovery evidence to the architecture owner.

Do not skip directly to a new implementation because an expected class name is absent. Conversely,
do not force a discovered utility into the change merely because a similarly named file exists.
Select a candidate only when its responsibility, compatibility, dependency direction, error
contract, sensitive-data boundary and authorized scope fit the task. Business-module development
must not create an official-SDK adapter, install a third-party dependency, introduce a feature-owned
or shared network module, or migrate unrelated callers.

## Effective Dependency Evidence

A dependency advances through these evidence states:

```text
declared -> target-resolved -> symbol-exported -> implementation-complete -> build-verified
```

- **declared:** the affected module manifest directly declares the package or an authoritative
  project contract explicitly supplies it;
- **target-resolved:** a local target and its package entrypoint exist, or the lock/resolver evidence
  identifies the exact installed package version and entrypoint;
- **symbol-exported:** the requested tool and required public types are exported through the package
  interface available to the affected module;
- **implementation-complete:** the symbol's implementation dependencies, platform kits,
  configuration, permissions and required collaborators resolve for the declared baseline; and
- **build-verified:** the affected configured module build resolves the imports and compiles the
  selected integration.

Static inspection may establish only the first four states. Never report a dependency as verified
by build when the build did not execute successfully against the affected module. A source file that
is not exported, an undeclared transitive package, an unresolved local path, a type-only shell, an
unsupported platform kit or a utility with missing configuration is not an effective tool.

## Project Search Procedure

When the supplied candidate is ineffective, search only the authorized project scope for:

- module and root package manifests, lock files and package entrypoints;
- exported clients, interfaces and request functions such as `NetworkClient`, `HttpClient`,
  `ICall`, `request`, `fetch`, `get` and `post`;
- imports of current or legacy HarmonyOS networking interfaces;
- endpoint/base-address managers, request configuration, response envelopes and typed errors;
- interceptors or middleware for authentication, headers, serialization and observability; and
- existing repository implementations and their ViewModel consumers.

Record each credible candidate, its owning module, public import path, declared and resolved
dependency, implementation backend, applicable SDK/API baseline, consumers, error contract,
sensitive-data behavior, and selection or rejection reason. Do not copy private implementation
paths when the package exposes a public entrypoint.

## No-Tool Boundary

When no suitable supplied or project tool exists, preserve the discovery record and stop the
dependent business-module implementation. Do not create a local network client, official-SDK
adapter, external dependency, shared infrastructure or project policy as a fallback. A separate
architecture capability and explicit authority must establish any new network infrastructure,
including SDK selection, dependency direction, public exports, configuration, permissions,
authentication, certificates, response semantics, retry/cache behavior and rollback.

Unrelated business-module work may continue when it does not depend on the missing network tool.
Mark only the dependent implementation and behavior claims blocked.

## Deterministic Result and Lifecycle Contract

Every request path must settle exactly once with a typed success or failure outcome. Network
unavailability, invalid configuration, non-success protocol status, business rejection, decoding
failure, timeout, cancellation and SDK exception must not leave a pending Promise or collapse into
an indistinguishable empty value.

Define which layer maps:

- network-client and connectivity failures;
- protocol status and response-shape failures;
- backend business failures;
- authentication/authorization decisions;
- cancellation and stale-result suppression; and
- presentation messages and retry affordances.

Repository and Service code return typed outcomes. ViewModels decide UI state and presentation;
network-facing code must not directly navigate, mutate View state or display a Toast unless an
explicit existing project contract assigns that side effect and the task preserves it deliberately.
For lifecycle-sensitive or overlapping requests, define cancellation, last-result-wins,
deduplication or idempotency behavior as applicable rather than letting stale results overwrite
current state.

## Sensitive Data and Observability

Logs and evidence must redact credentials, authorization headers, cookies, tokens, personal data,
request/response bodies, file contents and service details whose disclosure is not authorized.
Prefer structured metadata such as operation ID, sanitized endpoint identity, status class,
duration, retry/cancel state and redacted error category. Verbose tracing is not enabled merely
because a network client supports it.

Authentication, certificate validation, cleartext network use, proxy, production host and protected
log access remain security or project decisions. Preserve an established policy and stop when a new
choice would be required outside the authorized task.

## Verification and Handoff

Record separately:

1. dependency declaration and target resolution;
2. package entrypoint and exported symbol inspection;
3. implementation dependency and SDK/API reconciliation;
4. selected tool and rejected candidates, or the no-tool owner handoff;
5. request, response and other model inventory plus model dependency-direction review;
6. endpoint/repository/service/ViewModel responsibility map and API-directory review;
7. typed result and error mapping;
8. successful affected-module build; and
9. task-required success, business-failure, protocol-failure, offline, timeout, decode-error,
   cancellation, lifecycle re-entry and overlapping-request observations.

Static discovery cannot pass compilation or runtime behavior. Build success cannot prove a service
response, cancellation, retry, authentication, privacy or production-readiness claim. A new or
materially changed business DTO below `api/`, model-to-API reverse dependency, business-owned
network infrastructure, unresolved tool, pending request path, collapsed material error or
protected-data log fails the affected criterion. When a required dependency, permission, service
environment or behavior target is unavailable, preserve the exact discovery record and mark only
the dependent claim blocked.

Source basis: `OWNER-HMOS-MODEL-API-BOUNDARY`, `OWNER-HMOS-NETWORK-REQUEST-CONTRACT` and
`PROJECT-DRILL-UGC-NETWORK-EXEMPLAR` in their respective change research ledgers, plus `HMOS-ARKTS`
and `REPO-HARMONYOS-IDENTITY` through their existing validated ledger references.
