#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

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

if find . \
  -path ./.git -prune -o \
  -path ./README-CH.md -prune -o \
  -type f \( \
  -name '*.md' -o -name '*.json' -o -name '*.yaml' -o -name '*.yml' \
\) -print0 | xargs -0 grep -Il '[一-龥]' | grep -q .; then
  echo "ERROR: generated repository content must be English-first outside README-CH.md"
  exit 1
fi

python3 scripts/validate_registry.py
python3 scripts/validate_skills.py
python3 scripts/validate_agents.py
python3 -m unittest discover -s tests
