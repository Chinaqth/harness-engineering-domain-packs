# Routing Evaluation Scenarios

Exercise at least:

1. Positive match: supported task type and a discriminating repository signal.
2. Negative signal: supported task type without Domain evidence.
3. Negative task: Domain signal with an unsupported task type.
4. Ambiguity: signals matching multiple routes; verify deterministic priority.
5. Disabled capability: verify the route fails closed instead of silently omitting required work.
6. Missing dependency: verify unresolved capabilities fail closed.
7. Version mismatch: verify a project pin different from the registry version is unroutable.
8. Draft lifecycle: verify a draft Pack is never selected for production routing.

Record input, expected result, actual result, command or method, revision, environment, and
limitations for every scenario.

