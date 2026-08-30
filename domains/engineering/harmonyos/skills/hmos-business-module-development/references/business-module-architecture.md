# HarmonyOS Business Module Architecture Contract

## Purpose

This contract defines the reusable structure for a HarmonyOS business HAR and its optional provider
HAR. Concrete directory aliases, framework decorators, service locators and module names remain
project facts, but the responsibility and dependency direction below must remain observable.

Read [ui-page-dialog-conventions.md](ui-page-dialog-conventions.md) for the companion contract on
page/Dialog route declarations, UI resource use, and Chinese responsibility comments. Read
[network-request-conventions.md](network-request-conventions.md) whenever the task adds or materially
changes an endpoint, request/response model, repository, service, network dependency, or request lifecycle.

## Business HAR Responsibilities

| Surface | Required responsibility | Forbidden responsibility |
| --- | --- | --- |
| `pages/` | Navigable screen roots and composition | Direct network calls or provider contract declarations |
| `dialogs/` | Modal, sheet, popup or overlay presentation | Business orchestration or route registry ownership |
| `components/` | Reusable embedded UI | Cross-module service location or network execution |
| `viewmodels/` | Business actions, async orchestration and mutable presentation state | Declarative UI trees or provider API declarations |
| `models/` / `uistate/` | Request/response DTOs, entities, value objects, enums, state and other pure data shapes | Network execution or dependencies on API, ViewModel or View code |
| `api/` | Endpoints, repository contracts and implementations, request execution and HTTP-facing services | Business request/response or other pure data declarations, ArkUI trees, or feature-owned Transport/SDK adapters |
| `router/` | Route paths, page metadata, route parameters and module navigation contracts | Network or unrelated shell behavior |
| `hmdelegate/` | Host-shell adapters and delegated builders | Canonical business state, networking or route definitions |

An existing project may map `hmdelegate/` to a stable equivalent directory. Record that mapping;
do not create a duplicate directory merely to satisfy a spelling convention.

## MVVM and State Ownership

- Views comprise `pages/`, `dialogs/` and `components/`. They render state and forward user events.
- ViewModels own business decisions, asynchronous sequencing, error-to-presentation mapping and
  mutable data consumed by Views.
- New or rewritten ViewModels and mutable UI-facing model objects use `@ObservedV2`.
- A property is decorated with `@Trace` when its mutation must trigger dependent UI refresh.
- Request and response DTOs are not made observable by default; map them into domain or UI-state
  objects when presentation behavior requires observation.
- V1 decorators are legacy migration inputs, not a target architecture.

## API Containment

All code that initiates a network request belongs under `api/`. Before selecting an implementation,
prove the supplied dependency and tool through declaration, target resolution, exported symbol,
complete implementation dependencies, and the affected configured build. When that candidate is
ineffective, search the project for an established compatible exported network abstraction. When no
suitable supplied or project tool exists, stop dependent implementation and hand the discovery
evidence to the architecture owner. Business-module development does not create a feature-owned
Transport, official-SDK adapter or `api/transport/` directory. The required internal split is:

```text
api/
├── XxxApi.ets
├── XxxHttpService.ets
├── XxxHttpRepositoryImpl.ets
└── repository/
    └── IXxxHttpRepository.ets

models/
├── request/
│   └── XxxRequest.ets
├── response/
│   └── XxxResponse.ets
└── entities, value objects, enums, state and other pure data definitions
```

The names are illustrative. The invariant is that endpoint identity, repository abstraction,
request execution and HTTP-facing service logic remain inside the API boundary, while business
request/response and other pure data definitions remain inside the model boundary. Request payloads
use `models/request/`; response payloads, envelopes and response-error data use `models/response/`;
other entities, value objects, enums and state remain below `models/` or an explicitly recorded
project equivalent. Models do not depend on API, ViewModel or View code. ViewModels call a service
or repository abstraction; Views never call the network client directly. Every request path settles
with a typed success or failure result; offline, non-success status, decode, timeout, cancellation,
and SDK-exception paths cannot leave a pending Promise or be silently collapsed into an
indistinguishable empty value. Repository and Service code do not copy project-specific
authentication, routing, Toast, response-envelope, URL, retry, cache or logging policy.

## Provider Bridge

When `<module>provider` exists, dependency direction is:

```text
external consumer -> <module>provider contracts <- <module> implementations
```

The provider HAR declares:

- `XxxServiceProvider`: callable business capabilities;
- `XxxComponentProvider`: externally embeddable UI builders or component contracts; and
- one `XxxProvider` singleton factory/access point that exposes those interfaces through the
  project's approved registration or construction mechanism.

The business HAR implements both interfaces and performs the actual work. The provider HAR must not
import business implementation internals or accumulate business logic. External consumers must not
import internal ViewModels, repositories, pages or implementation classes from the business HAR.

A provider-only module state is inconsistent with this dependency direction because the declared
contracts have no owned business implementation. Preserve that state for diagnosis and block
development until an authorized owner selects recovery or business-only reconstruction; do not
delete, overwrite or reinterpret the existing provider implicitly.

If only one contract category is currently required, retain the named split and omit the unused
implementation until there is a real consumer; do not invent placeholder behavior. Adding a new
public method requires explicit consumer semantics and compatibility review.

## Structural Evidence

For each delivery, record:

1. the directory-to-responsibility inventory;
2. View-to-ViewModel event and state dependencies;
3. each mutable UI property and why it is traced or intentionally untraced;
4. every request/response and other model definition, its directory, and proof that models do not
   depend on API, ViewModel or View code;
5. every network entry point and proof it resides below `api/` without business DTO or Transport
   declarations;
6. network-tool candidates, effective-dependency state, selection or rejection rationale, typed
   result/error mapping, redaction behavior, and deterministic completion paths;
7. route and host-shell adaptation ownership;
8. provider interface declarations, business implementations and external imports; and
9. build plus task-required behavior evidence; and
10. page/Dialog/component classification, route ownership, resource-key changes, magic-literal
   review, and Chinese-comment review for every new or materially changed UI surface.

## Capability Precedence

For `harmonyos-business-module-development`, this architecture contract controls the cross-layer
composition. ArkUI delivery controls UI implementation correctness, ArkTS delivery controls source
correctness, Stage/package design controls package semantics, and verification controls evidence
collection. None of those subordinate concerns may independently redefine the accepted MVVM
ownership, API boundary, route/shell separation, provider dependency direction or public contract.

A broader Stage/package or public-interface decision from an authorized architecture owner may
supersede this contract only after the task scope and approval record are updated. A subordinate
Skill recommendation alone is not such a decision.

Source basis: `USER-BUSINESS-MODULE-CONTRACT`, `PROJECT-UGC-EXEMPLAR`, and `HMOS-ARKUI-V2` in the
change research ledger for `20260817-harmonyos-business-module-development`, plus
`OWNER-HMOS-MODEL-API-BOUNDARY` and `PROJECT-CATCHELF-ACCOUNT-API-EXEMPLAR` in the ledger for
`20260830-harmonyos-model-api-boundary`.
