#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"

echo "[validate-repo] root=$ROOT"

# 1) Validate generated surfaces (markdown policy)

echo "[validate-repo] builder validate --scope generated"
python3 "$ROOT/.builder/builder.py" validate --root "$ROOT" --scope generated

## 2) Refresh navigator only if explicitly requested

## (Default is NO scanning; DNP compliance means you only scan when necessary.)

if [[ "${GOA_REFRESH_NAVIGATOR:-0}" == "1" ]]; then
  echo "[validate-repo] GOA_REFRESH_NAVIGATOR=1; refreshing navigator"
  chmod +x "$ROOT/.toolkit/scan/refresh_navigator.sh"
  "$ROOT/.toolkit/scan/refresh_navigator.sh" "$ROOT"
fi

## 3) Engine tests if present

if [[ -x "$ROOT/.toolkit/modules/engine/run_tests.sh" ]]; then
  echo "[validate-repo] engine tests: .toolkit/modules/engine/run_tests.sh"
  "$ROOT/.toolkit/modules/engine/run_tests.sh" "$ROOT"
else
  echo "[validate-repo] engine tests: skipped (missing .toolkit/modules/engine/run_tests.sh)"
fi

## 4) Governance gate (hard stop on failure)

echo "[validate-repo] governance gate"
chmod +x "$ROOT/.toolkit/validate/governance_gate.sh"
"$ROOT/.toolkit/validate/governance_gate.sh" "$ROOT"

echo "[validate-repo] OK"

