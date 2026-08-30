# HarmonyOS Business Model and API Boundary Design

## Goal

Make the HarmonyOS business-module boundary deterministic: `models/` owns pure data definitions,
including request and response DTOs, while `api/` owns only endpoint declarations, repository
contracts and implementations, and HTTP-facing services. Remove the business-module-owned
transport fallback.

## Approved contract

The canonical business-module structure is:

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
    ├── response/
    └── other entities, value objects, enums, state and pure data definitions
```

`models/request/` owns outbound business request payload classes. `models/response/` owns inbound
response payloads, response envelopes and response-error data. Other entities, value objects,
enums and pure data shapes remain below `models/`. Model code must not execute requests or depend
on repositories, services, network clients, ViewModels or Views.

`api/` owns endpoint identity, the repository contract, the repository implementation that invokes
an already approved project network tool, and the HTTP service that performs business pre/post
processing and typed result mapping. It must not declare business request, response or other pure
data classes.

## Network-tool behavior

The business-module workflow resolves network tools in this order:

1. verify the task-supplied or module-declared tool;
2. search the authorized project for an established exported network capability; and
3. stop the dependent implementation and hand evidence to the architecture owner when neither is
   usable.

The workflow no longer creates a feature-owned transport abstraction, an official-SDK adapter, an
`api/transport/` directory, or `NetworkRequest`, `NetworkResult` and `NetworkError` types below
`api/`. Creating shared or platform network infrastructure requires a separately authorized
architecture capability outside business-module development.

## Compatibility and scope

This is a breaking policy change because it removes an implementation fallback and turns model
placement into a mandatory acceptance condition. The Domain version advances from `4.0.0` to
`5.0.0`. The migration rule applies to new or materially changed business request/response models
and their direct API dependency chain; unrelated legacy files are not moved automatically.

The authoritative Domain Pack is updated in this change. Kernel pins, CLI bundle contents, local
runtime installation and product-project migrations are explicitly deferred.

## Verification

Verification must prove that:

- every normative layer uses the same `models/` and `api/` responsibility language;
- no normative business-module path still authorizes a feature-owned transport or SDK adapter;
- the evaluator fails new or materially changed DTOs declared below `api/`;
- the initializer's existing `models/request` and `models/response` scaffold remains aligned;
- registry and Domain metadata both report `5.0.0`; and
- the repository Domain validation succeeds.
