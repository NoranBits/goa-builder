param(
  [string]$Root = "."
)

$ErrorActionPreference = "Stop"
$DateUtc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
$OutDir = Join-Path $Root ".logs/decisions"
$OutFile = Join-Path $OutDir "$DateUtc`__governance__gate.json"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $Root ".logs/test") | Out-Null
New-Item -ItemType Directory -Force -Path (Join-Path $Root ".logs/navigation") | Out-Null

$failCount = 0
$checks = @()

function Add-Check($id, $status, $msg) {
  $checks += [pscustomobject]@{ check_id = $id; status = $status; message = $msg }
}

function Require-Path($id, $p) {
  $full = Join-Path $Root $p
  if (Test-Path $full) {
    Add-Check $id "pass" "Found: $p"
  } else {
    Add-Check $id "fail" "Missing: $p"
    $script:failCount++
  }
}

Require-Path "GATE-02A" "AGENTS.md"
Require-Path "GATE-02B" ".canon/navigator/README.md"
Require-Path "GATE-02C" ".toolkit/scan/refresh_navigator.sh"
Require-Path "GATE-02D" ".toolkit/scan/refresh_navigator.ps1"

$scanLog = Join-Path $Root ".logs/navigation/$DateUtc`__scan__navigator.md"
if (Test-Path $scanLog) {
  Add-Check "GATE-01" "pass" "Navigator scan logged for today."
} else {
  Add-Check "GATE-01" "skip" "No navigator scan log for today (ok if not needed)."
}

try {
  python (Join-Path $Root ".builder/builder.py") validate --root $Root --scope generated
  Add-Check "GATE-03" "pass" "validate --scope generated passed."
} catch {
  Add-Check "GATE-03" "fail" "validate --scope generated failed."
  $failCount++
}

$hasTest = Get-ChildItem -Path (Join-Path $Root ".logs/test") -Filter "$DateUtc`__*.md" -ErrorAction SilentlyContinue
$hasSarif = Get-ChildItem -Path (Join-Path $Root ".logs/test") -Filter "$DateUtc`__*.sarif" -ErrorAction SilentlyContinue
if ($hasTest -or $hasSarif) {
  Add-Check "GATE-04" "pass" "Test/audit evidence present for today."
} else {
  Add-Check "GATE-04" "warn" "No test/audit evidence present for today."
}

$approved = $true
$nextActions = @()
if ($failCount -gt 0) {
  $approved = $false
  $nextActions = @("Fix failing gates; rerun governance_gate.ps1")
}

$data = @{
  generated_at = (Get-Date).ToUniversalTime().ToString("s") + "Z"
  approved = $approved
  checks = $checks
  required_next_actions = $nextActions
}

$data | ConvertTo-Json -Depth 6 | Out-File -FilePath $OutFile -Encoding utf8
Write-Host "[governance] Wrote gate decision: $OutFile"
if (-not $approved) { exit 2 }
