# HarmonyOS Business Module Architecture Contract

## Purpose

This contract defines the reusable structure for a HarmonyOS business HAR and its optional provider
HAR. Concrete directory aliases, framework decorators, service locators and module names remain
project facts, but the responsibility and dependency direction below must remain observable.

## Business HAR Responsibilities

| Surface | Required responsibility | Forbidden responsibility |
| --- | --- | --- |
| `pages/` | Navigable screen roots and composition | Direct network calls or provider contract declarations |
| `dialogs/` | Modal, sheet, popup or overlay presentation | Business orchestration or route registry ownership |
| `components/` | Reusable embedded UI | Cross-module service location or transport implementation |
| `viewmodels/` | Business actions, async orchestration and mutable presentation state | Declarative UI trees or provider API declarations |
| `models/` / `uistate/` | Domain values, request-independent models and UI-facing state shapes | Network execution |
| `api/` | Endpoints, repository contracts, request execution, network implementations and network-facing services | ArkUI page/component trees |
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
- Transport response objects are not made observable by default; map them into domain or UI-state
  objects when presentation behavior requires observation.
- V1 decorators are legacy migration inputs, not a target architecture.

## API Containment

All code that initiates a network request belongs under `api/`. A scalable internal split is:

```text
api/
├── XxxApi.ets
├── XxxHttpService.ets
├── XxxHttpRepositoryImpl.ets
└── repository/
    └── IXxxHttpRepository.ets
```

The names are illustrative. The invariant is that endpoint identity, repository abstraction,
request execution and network-facing service logic remain inside the API boundary. Request and
response data models may use the project's established `models/request` and `models/response`
locations. ViewModels call a service or repository abstraction; Views never call the network client
directly.

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
4. every network entry point and proof it resides below `api/`;
5. route and host-shell adaptation ownership;
6. provider interface declarations, business implementations and external imports; and
7. build plus task-required behavior evidence.

## Capability Precedence

For `harmonyos-business-module-development`, this architecture contract controls the cross-layer
composition. ArkUI delivery controls UI implementation correctness, ArkTS delivery controls source
correctness, Stage/package design controls package semantics, and verification controls evidence
collection. None of those subordinate concerns may independently redefine the accepted MVVM
ownership, API boundary, route/shell separation, provider dependency direction or public contract.

A broader Stage/package or public-interface decision from an authorized architecture owner may
supersede this contract only after the task scope and approval record are updated. A subordinate
Skill recommendation alone is not such a decision.

Source basis: `USER-BUSINESS-MODULE-CONTRACT`, `PROJECT-UGC-EXEMPLAR`, and
`HMOS-ARKUI-V2` in the change research ledger for `20260817-harmonyos-business-module-development`.
