#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"
python_bin="${HARNESS_PYTHON:-python3}"

required=(
  "README.md"
  "README-CH.md"
  "AGENTS.md"
  "registry/domains.json"
  "schemas/domain-pack.schema.json"
  "schemas/capability.schema.json"
  "schemas/route.schema.json"
  "schemas/registry.schema.json"
  "schemas/owners.schema.json"
  "domains/_template/domain.json"
  ".agents/skills/register-domain-pack/SKILL.md"
)

for path in "${required[@]}"; do
  test -e "$path" || { echo "ERROR: missing $path"; exit 1; }
done

if find . -path ./.git -prune -o -type f \( \
  -iname '*.pem' -o -iname '*.key' -o -iname '*credentials*' -o -iname '.env' \
\) -print | grep -q .; then
  echo "ERROR: suspicious secret-bearing filename found"
  exit 1
fi

non_english=()
while IFS= read -r -d '' generated_file; do
  if grep -Iq '[一-龥]' "$generated_file"; then
    non_english+=("$generated_file")
  fi
done < <(find . \
  -path ./.git -prune -o \
  -path ./README-CH.md -prune -o \
  -path './domains/*/README-CH.md' -prune -o \
  -path './changes' -prune -o \
  -path './.agents/skills/complete-domain-pack' -prune -o \
  -path './docs/GOVERNANCE.md' -prune -o \
  -path './AGENTS.md' -prune -o \
  -path './domains/engineering/harmonyos/skills/hmos-*' -prune -o \
  -type f \( \
  -name '*.md' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' \
\) -print0)
if ((${#non_english[@]})); then
  echo "ERROR: generated repository content must be English-first outside approved README-CH.md files"
  printf '  %s\n' "${non_english[@]}"
  exit 1
fi

"$python_bin" scripts/validate_registry.py
"$python_bin" scripts/validate_skills.py
"$python_bin" scripts/validate_agents.py
"$python_bin" -m unittest discover -s tests
