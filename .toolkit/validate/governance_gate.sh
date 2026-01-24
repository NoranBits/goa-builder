#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
DATE_UTC="$(date -u +%Y-%m-%d)"
OUT_DIR="$ROOT/.logs/decisions"
OUT_FILE="$OUT_DIR/${DATE_UTC}__governance__gate.json"

mkdir -p "$OUT_DIR" "$ROOT/.logs/test" "$ROOT/.logs/navigation"

fail_count=0
checks_json="[]"

add_check () {
  local id="$1"
  local status="$2"
  local msg="$3"
  checks_json="$(python3 - <<PY
import json
arr=json.loads('''$checks_json''')
arr.append({"check_id":"$id","status":"$status","message":"$msg"})
print(json.dumps(arr))
PY
)"
}

require_path () {
  local id="$1"
  local p="$2"
  if [[ -e "$ROOT/$p" ]]; then
    add_check "$id" "pass" "Found: $p"
  else
    add_check "$id" "fail" "Missing: $p"
    fail_count=$((fail_count+1))
  fi
}

# GATE-02: required artifacts

require_path "GATE-02A" "AGENTS.md"
require_path "GATE-02B" ".canon/navigator/README.md"
require_path "GATE-02C" ".toolkit/scan/refresh_navigator.sh"
require_path "GATE-02D" ".toolkit/scan/refresh_navigator.ps1"

## GATE-01: navigation refresh evidence (optional, but if scan happened today it must be logged)

if compgen -G "$ROOT/.logs/navigation/${DATE_UTC}__scan__navigator.md" > /dev/null; then
  add_check "GATE-01" "pass" "Navigator scan logged for today."
else
  add_check "GATE-01" "skip" "No navigator scan log for today (ok if not needed)."
fi

## GATE-03: validate generated surfaces

if python3 "$ROOT/.builder/builder.py" validate --root "$ROOT" --scope generated; then
  add_check "GATE-03" "pass" "validate --scope generated passed."
else
  add_check "GATE-03" "fail" "validate --scope generated failed."
  fail_count=$((fail_count+1))
fi

## GATE-04: test evidence (soft requirement; promote to hard if desired)

if compgen -G "$ROOT/.logs/test/${DATE_UTC}__*.md" > /dev/null || compgen -G "$ROOT/.logs/test/${DATE_UTC}__*.sarif" > /dev/null; then
  add_check "GATE-04" "pass" "Test/audit evidence present for today."
else
  add_check "GATE-04" "warn" "No test/audit evidence present for today."
fi

approved="True"
required_next_actions="[]"
if [[ "$fail_count" -gt 0 ]]; then
  approved="False"
  required_next_actions='["Fix failing gates; rerun governance_gate.sh"]'
fi

python3 - <<PY > "$OUT_FILE"
import json, datetime
data = {
  "generated_at": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
  "approved": $approved,
  "checks": json.loads('''$checks_json'''),
  "required_next_actions": json.loads('''$required_next_actions''')
}
print(json.dumps(data, indent=2))
PY

echo "[governance] Wrote gate decision: $OUT_FILE"
if [[ "$approved" != "True" ]]; then
  echo "[governance] NOT APPROVED"
  exit 2
fi
echo "[governance] APPROVED"

<!-- md_autofix: processed -->
