param(
  [string]$Root = "."
)

$ErrorActionPreference = "Stop"
Write-Host "[validate-repo] root=$Root"

Write-Host "[validate-repo] builder validate --scope generated"
python (Join-Path $Root ".builder/builder.py") validate --root $Root --scope generated

if ($env:GOA_REFRESH_NAVIGATOR -eq "1") {
  Write-Host "[validate-repo] GOA_REFRESH_NAVIGATOR=1; refreshing navigator"
  powershell -ExecutionPolicy Bypass -File (Join-Path $Root ".toolkit/scan/refresh_navigator.ps1") -Root $Root
}

$engineTests = Join-Path $Root ".toolkit/modules/engine/run_tests.ps1"
if (Test-Path $engineTests) {
  Write-Host "[validate-repo] engine tests: run_tests.ps1"
  powershell -ExecutionPolicy Bypass -File $engineTests -Root $Root
} else {
  Write-Host "[validate-repo] engine tests: skipped (missing run_tests.ps1)"
}

Write-Host "[validate-repo] governance gate"
powershell -ExecutionPolicy Bypass -File (Join-Path $Root ".toolkit/validate/governance_gate.ps1") -Root $Root

Write-Host "[validate-repo] OK"
