# Accepted Contract

## Directory ownership

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
    └── entities, value objects, enums, state and other pure data definitions
```

`api/` depends on `models/`. `models/` does not depend on `api/`, ViewModels or Views. Request and
response directories are created when an authorized change needs the corresponding category. An
existing equivalent directory is allowed only when its mapping is explicit and preserves the same
responsibilities.

## Network capability decision

The business-module workflow verifies a task-supplied or module-declared tool, then searches the
authorized project for an established exported capability. If both fail, the dependent
implementation is blocked. Creation of new network infrastructure is a separate architecture task,
not a fallback owned by business-module development.

## Acceptance semantics

A successful build does not waive incorrect DTO placement, a model reverse dependency or
business-owned network infrastructure. A missing project network tool blocks only dependent
implementation and behavior claims; unrelated module work may continue.
