# Requirements

## Functional policy

- **REQ-01:** `models/` owns request classes, response classes, response envelopes, response-error
  data, entities, value objects, enums, state and all other pure data definitions.
- **REQ-02:** Outbound business request payloads use `models/request/`; inbound response payloads,
  envelopes and response-error data use `models/response/`.
- **REQ-03:** Model code does not execute requests or depend on API, ViewModel or View code.
- **REQ-04:** Business `api/` contains endpoint declarations, repository contracts and
  implementations, request execution and HTTP-facing services only.
- **REQ-05:** The canonical API structure is `XxxApi.ets`, `XxxHttpService.ets`,
  `XxxHttpRepositoryImpl.ets` and `repository/IXxxHttpRepository.ets`.
- **REQ-06:** Business-module development does not create `api/transport/`, a feature-owned
  Transport abstraction, an official-SDK network adapter, a third-party network dependency or
  shared network infrastructure.
- **REQ-07:** When neither a supplied tool nor an established exported project capability is
  verifiable, dependent implementation stops and the candidate map is handed to the architecture
  owner.
- **REQ-08:** Existing deterministic typed result, lifecycle, negative-path and sensitive-data
  redaction requirements remain in force.

## Migration and evidence

- **REQ-09:** The new placement rule applies to new or materially changed request/response models
  and their direct API dependency chain; unrelated legacy models are not moved automatically.
- **REQ-10:** Evaluation fails in-scope business DTOs below `api/`, model-to-API reverse
  dependencies and business-owned network infrastructure.
- **REQ-11:** Handoffs record request/response/other-model inventories, dependency direction, API
  structure, selected network tool or no-tool decision, typed outcomes and negative paths.
- **REQ-12:** Domain and registry versions advance to `5.0.0`; Kernel, CLI and project rollout remain
  deferred.

## Quality gates

- **REQ-13:** All authoritative Domain layers use consistent ownership and fail-closed language.
- **REQ-14:** JSON parsing, Domain validation, Skill validation, Agent validation and repository
  tests pass.
- **REQ-15:** The final diff contains no stale business-module authorization for a minimal local
  adapter or DTO-under-API example.
