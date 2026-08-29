# HarmonyOS Network Request Discovery and Delivery Contract

## Purpose and Authority

This contract defines how a HarmonyOS business-module change discovers, selects, creates, and
verifies network-request infrastructure without assuming that a dependency or remembered tool
symbol exists. It preserves the reusable responsibility split observed in
`PROJECT-DRILL-UGC-NETWORK-EXEMPLAR`, but that project remains structural evidence only. Its package
names, exported symbols, response envelope, authentication, routing, user messaging, base URLs,
singleton assembly, interceptors, and transport implementation are not HarmonyOS requirements.

Version-sensitive platform APIs must be reconciled under `HMOS-RULE-01` and `HMOS-RULE-02` for the
declared SDK/API baseline. The task or project owns product endpoints, authentication, certificates,
retry and cache policy, backend response semantics, dependency approval, and service environments.

## Responsibility Contract

The exact filenames are project facts, but the responsibilities must remain observable:

| Responsibility | Owns | Must not own |
| --- | --- | --- |
| Endpoint contract | Stable endpoint identity, method and protocol constants | Base environment selection, UI text or request execution |
| Request/response models | Typed transport input and output shapes | UI observation or network side effects by default |
| Repository contract | Typed business-facing data-access operations | Concrete SDK calls or presentation behavior |
| Repository implementation | Endpoint selection, request mapping and network-client invocation | View state or navigation |
| Service | Business pre/post-processing and transport-to-domain result mapping | Direct UI rendering, Toasts or route changes |
| Transport abstraction | Request configuration, deterministic success/failure completion and cancellation contract | Product endpoint catalogs or screen behavior |
| Transport implementation | One verified project tool or official HarmonyOS network interface | Product policy, global architecture migration or unapproved dependency installation |
| ViewModel | Async sequencing and domain-result-to-UI-state mapping | Concrete transport SDK calls |
| View | State rendering and user-intent forwarding | Network execution or async business orchestration |

For an established project, preserve its equivalent boundaries when they keep the same dependency
direction. Do not create duplicate abstractions merely to match the illustrative names.

## Network Tool Resolution Ladder

Before generating imports or request code, evaluate candidates in this order:

1. **Task-supplied or module-declared tool.** Verify the exact dependency and requested symbol.
2. **Established project network capability.** Search manifests, package entrypoints, source and
   existing repository implementations for a compatible exported abstraction.
3. **Verified official HarmonyOS interface.** Use only an interface supported by the declared
   SDK/API baseline and current authoritative documentation.
4. **Minimal local adapter.** Create the smallest feature-owned transport abstraction and official
   SDK adapter needed by the accepted vertical slice.

Do not skip directly to a new implementation because an expected class name is absent. Conversely,
do not force a discovered utility into the change merely because a similarly named file exists.
Select a candidate only when its responsibility, compatibility, dependency direction, error
contract, sensitive-data boundary, and authorized scope fit the task.

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
unsupported platform kit, or a utility with missing configuration is not an effective tool.

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

## Minimal Creation Boundary

When no suitable project tool exists, create a feature-local adapter under `api/` or the recorded
project-equivalent network boundary. A typical optional split is:

```text
api/
├── XxxApi.ets
├── XxxHttpService.ets
├── XxxHttpRepositoryImpl.ets
├── repository/
│   └── IXxxHttpRepository.ets
└── transport/
    ├── INetworkClient.ets
    ├── HarmonyNetworkClient.ets
    ├── NetworkRequest.ets
    ├── NetworkResult.ets
    └── NetworkError.ets
```

Create only the artifacts required by the accepted slice. Use a verified official HarmonyOS
networking interface already available in the project SDK. Do not install a third-party dependency,
create a global shared module, migrate unrelated callers, or invent authentication, retry, cache,
certificate, response-envelope, Toast or navigation policy without separate authority. Promote a
feature-local adapter to shared infrastructure only after real multi-module consumers and an
approved dependency-direction decision exist.

## Deterministic Result and Lifecycle Contract

Every request path must settle exactly once with a typed success or failure outcome. Network
unavailability, invalid configuration, non-success protocol status, business rejection, decoding
failure, timeout, cancellation and SDK exception must not leave a pending Promise or collapse into
an indistinguishable empty value.

Define which layer maps:

- transport and connectivity failures;
- protocol status and response-shape failures;
- backend business failures;
- authentication/authorization decisions;
- cancellation and stale-result suppression; and
- presentation messages and retry affordances.

Transport and Service code return typed outcomes. ViewModels decide UI state and presentation;
network infrastructure must not directly navigate, mutate View state, or display a Toast unless an
explicit existing project contract assigns that side effect and the task preserves it deliberately.
For lifecycle-sensitive or overlapping requests, define cancellation, last-result-wins,
deduplication or idempotency behavior as applicable rather than letting stale results overwrite
current state.

## Sensitive Data and Observability

Logs and evidence must redact credentials, authorization headers, cookies, tokens, personal data,
request/response bodies, file contents and service details whose disclosure is not authorized.
Prefer structured metadata such as operation ID, sanitized endpoint identity, status class,
duration, retry/cancel state and redacted error category. Verbose tracing is not enabled merely
because a transport supports it.

Authentication, certificate validation, cleartext transport, proxy, production host and protected
log access remain security or project decisions. Preserve an established policy and stop when a new
choice would be required outside the authorized task.

## Verification and Handoff

Record separately:

1. dependency declaration and target resolution;
2. package entrypoint and exported symbol inspection;
3. implementation dependency and SDK/API reconciliation;
4. selected tool and rejected candidates;
5. endpoint/repository/service/transport/ViewModel responsibility map;
6. typed result and error mapping;
7. successful affected-module build; and
8. task-required success, business-failure, protocol-failure, offline, timeout, decode-error,
   cancellation, lifecycle re-entry and overlapping-request observations.

Static discovery cannot pass compilation or runtime behavior. Build success cannot prove a service
response, cancellation, retry, authentication, privacy or production-readiness claim. When a
required dependency, platform interface, permission, service environment or behavior target is
unavailable, preserve the exact discovery record and mark only the dependent claim blocked.

Source basis: `OWNER-HMOS-NETWORK-REQUEST-CONTRACT` and
`PROJECT-DRILL-UGC-NETWORK-EXEMPLAR` in
`changes/20260829-harmonyos-network-request-policy/research/sources.json`, plus `HMOS-ARKTS` and
`REPO-HARMONYOS-IDENTITY` through their existing validated ledger references.
