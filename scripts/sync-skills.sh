#!/usr/bin/env bash
# Usage: bash scripts/sync-skills.sh [--verify]
# Mirrors canonical .agents/skills/ -> .claude/skills/ additively (never deletes extras).
# Generated Python bytecode is local state, not skill content.
# --verify compares SHA-256 of each canonical file against its mirror; exit 1 on drift/missing, 0 when clean.

set -euo pipefail

# Resolve the repo root (parent of scripts/) so the script works from any CWD.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE="$REPO_ROOT/.agents/skills"
MIRROR="$REPO_ROOT/.claude/skills"

sha256() {
    if command -v sha256sum >/dev/null 2>&1; then
        sha256sum "$1" | awk '{print toupper($1)}'
    elif command -v shasum >/dev/null 2>&1; then
        shasum -a 256 "$1" | awk '{print toupper($1)}'
    else
        echo "ERROR: no SHA-256 tool found (need sha256sum or shasum)" >&2
        exit 2
    fi
}

if [ ! -d "$SOURCE" ]; then
    echo "ERROR: canonical skills directory not found: $SOURCE" >&2
    exit 1
fi

canonical_files() {
    find "$SOURCE" -type d -name __pycache__ -prune -o -type f ! -name '*.pyc' -print0
}

if [ "${1:-}" = "--verify" ]; then
    problems=0
    while IFS= read -r -d '' file; do
        relative="${file#"$SOURCE"/}"
        mirror_file="$MIRROR/$relative"
        if [ ! -f "$mirror_file" ]; then
            echo "MISSING: $relative"
            problems=$((problems + 1))
            continue
        fi
        if [ "$(sha256 "$file")" != "$(sha256 "$mirror_file")" ]; then
            echo "DRIFT:   $relative"
            problems=$((problems + 1))
        fi
    done < <(canonical_files)
    if [ "$problems" -gt 0 ]; then
        echo "Skill mirror drift detected: $problems problem(s)."
        exit 1
    fi
    echo "Skill mirror clean."
    exit 0
fi

mkdir -p "$MIRROR"
copied=0
skipped=0
while IFS= read -r -d '' file; do
    relative="${file#"$SOURCE"/}"
    destination="$MIRROR/$relative"
    if [ -f "$destination" ] && [ "$(sha256 "$file")" = "$(sha256 "$destination")" ]; then
        skipped=$((skipped + 1))
        continue
    fi
    mkdir -p "$(dirname "$destination")"
    cp "$file" "$destination"
    copied=$((copied + 1))
done < <(canonical_files)

echo "Skill sync complete: $copied copied, $skipped unchanged (skipped). Extras in .claude/skills left untouched."
exit 0
