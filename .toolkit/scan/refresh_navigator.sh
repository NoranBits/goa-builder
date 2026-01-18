#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
DATE_UTC="$(date -u +%Y-%m-%d)"
LOG_DIR="$ROOT/.logs/navigation"
LOG_FILE="$LOG_DIR/${DATE_UTC}__scan__navigator.md"

mkdir -p "$LOG_DIR"

echo "# Navigator refresh ($DATE_UTC)" > "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "## Purpose" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "- Regenerate `.canon/navigator/**` using the approved bounded toolchain." >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "## Method" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "- Delete `.canon/navigator/` then run `python3 .builder/builder.py generate` (no overwrite)." >> "$LOG_FILE"
echo "" >> "$LOG_FILE"
echo "## Preflight" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

if [[ ! -f "$ROOT/.builder/builder.py" ]]; then
  echo "- FAIL: missing .builder/builder.py" >> "$LOG_FILE"
  echo "[navigator] FAIL: missing .builder/builder.py"
  exit 2
fi

echo "- OK: found .builder/builder.py" >> "$LOG_FILE"

# Delete navigator surface to force clean regeneration without global overwrite
if [[ -d "$ROOT/.canon/navigator" ]]; then
  rm -rf "$ROOT/.canon/navigator"
  echo "- OK: removed existing .canon/navigator/" >> "$LOG_FILE"
else
  echo "- OK: .canon/navigator/ not present (fresh build)" >> "$LOG_FILE"
fi

echo "" >> "$LOG_FILE"
echo "## Execution" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

python3 "$ROOT/.builder/builder.py" generate --root "$ROOT" >> "$LOG_FILE" 2>&1

echo "" >> "$LOG_FILE"
echo "- OK: builder generate completed" >> "$LOG_FILE"

echo "" >> "$LOG_FILE"
echo "## Postchecks" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

if [[ -f "$ROOT/.canon/navigator/README.md" ]]; then
  echo "- PASS: .canon/navigator/README.md regenerated" >> "$LOG_FILE"
else
  echo "- FAIL: .canon/navigator/README.md missing after regeneration" >> "$LOG_FILE"
  echo "[navigator] FAIL: navigator README missing after regeneration"
  exit 3
fi

echo "[navigator] OK: refreshed .canon/navigator (log: $LOG_FILE)"
