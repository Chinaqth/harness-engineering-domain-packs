---
name: hmos-init-business-module
description: Initialize a HarmonyOS business HAR module and its empty companion provider HAR using reusable skeletons, root build-profile registration, and a local provider dependency. Use when Codex is asked to create, scaffold, or initialize a HarmonyOS business module with standard source directories, resources, test stubs, and an `<module_id>provider` module under the root providers directory. Do not use for business implementation, application-specific routing, external dependencies, or runtime integration.
---

# Initialize a HarmonyOS Business Module

Create only the agreed project skeleton. Do not infer or generate business behavior.

## Required inputs

- Resolve the HarmonyOS project root containing `build-profile.json5` and the requested module directory.
- Obtain `module_id`. Require `^[a-z][a-z0-9_]*$`.
- Use `display_name` when supplied; otherwise use `module_id`.
- Use `modules_dir` when supplied; otherwise default to `features`. Require a relative directory
  that resolves inside the project root.

Do not ask for values already clear from the request or repository.

## Initialize

Run the bundled deterministic script:

```bash
python3 <skill-dir>/scripts/init_business_module.py \
  --project-root <harmonyos-project-root> \
  --module-id <module_id> \
  --display-name <display_name> \
  --modules-dir <modules_dir>
```

The script must:

1. Refuse invalid names, an existing business or provider target, a missing project manifest, or a duplicate module entry.
2. Create `<modules_dir>/<module_id>` from `assets/module-template`.
3. Create the standard empty source and resource directories.
4. Replace `__MODULE_ID__` and `__DISPLAY_NAME__` in text templates.
5. Ensure the project-root `providers/` directory exists and create
   `providers/<module_id>provider` from `assets/provider-template`.
6. Keep `providers/<module_id>provider/src/main/ets/` empty; do not generate provider interfaces,
   services, routers, or implementations.
7. Add both business and provider module entries to the root `build-profile.json5` modules array.
8. Add `<module_id>provider` to the business module's `oh-package.json5` as a relative local
   `file:` dependency.
9. Roll back both modules, the root manifest, and a newly created empty `providers/` directory if
   any step fails.

## Fixed structure

Create these source directories:

```text
src/main/ets/api/repository
src/main/ets/components
src/main/ets/dialogs
src/main/ets/models/request
src/main/ets/models/response
src/main/ets/pages
src/main/ets/router
src/main/ets/viewmodels
src/main/resources/base/element
src/main/resources/base/media
src/main/resources/rawfile
src/test
src/ohosTest/ets/test
```

Do not create any directories or files outside this declared skeleton.

Create the provider skeleton at `providers/<module_id>provider` with an empty
`src/main/ets/` directory, empty `Index.ets`, HAR manifests, empty base resources, and no test or
business implementation files.

## Boundaries

- Keep `Index.ets` as an export placeholder; do not invent public APIs.
- Add only the generated provider's local dependency to the business `oh-package.json5`; do not add
  external or unrelated dependencies.
- Do not create pages, components, models, APIs, routers, view models, provider implementations,
  delegates, icons, or other business-specific files.
- Do not create generated artifacts such as `oh-package-lock.json5`, `oh_modules/`, or `build/`.
- Do not modify application-global configuration, entry dependencies, runtime-only packages,
  routing configuration, or provider assembly outside the generated module pair.
- Do not build, sync, install dependencies, or run devices unless the user explicitly requests that evidence.

## Verify

After initialization:

1. Inspect the script summary and the exact changed paths.
2. Confirm the business manifests contain the requested module ID and its `oh-package.json5`
   contains exactly one `<module_id>provider` local dependency with the correct relative path.
3. Confirm the provider package and module manifests contain `<module_id>provider` and its
   `src/main/ets/` directory has no files.
4. Confirm the root `build-profile.json5` contains exactly one business entry and exactly one
   provider entry.
5. Confirm excluded directories and generated files were not created.
6. Report business files, provider files, dependency update, and root manifest update separately.
