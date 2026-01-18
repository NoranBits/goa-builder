#!/usr/bin/env bash
# Minimal refresh_navigator script for templates
set -euo pipefail

ROOT_DIR="${1:-.}"
OUT_INDEX="$ROOT_DIR/navigator/context-index.json"

echo "[refresh_navigator] Scanning repository at: $ROOT_DIR"
mkdir -p "$(dirname "$OUT_INDEX")"

# Naive indexer: list top-level directories and README files
jq -n --arg generated_at "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --arg repo "$(basename "$(pwd)")" \
  '{generated_at: $generated_at, repo: $repo, entries: []}' > "$OUT_INDEX"

echo "[refresh_navigator] Wrote minimal index to $OUT_INDEX"
exit 0
