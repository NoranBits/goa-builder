param(
  [string]$Root = "."
)

$ErrorActionPreference = "Stop"
$DateUtc = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")
$LogDir = Join-Path $Root ".logs/navigation"
$LogFile = Join-Path $LogDir "$DateUtc`__scan__navigator.md"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

@"
# Navigator refresh ($DateUtc)

## Purpose

- Regenerate `.canon/navigator/**` using the approved bounded toolchain.

## Method

- Delete `.canon/navigator/` then run `python3 .builder/builder.py generate` (no overwrite).

## Preflight
"@ | Out-File -FilePath $LogFile -Encoding utf8

$builder = Join-Path $Root ".builder/builder.py"
if (-not (Test-Path $builder)) {
  Add-Content $LogFile "- FAIL: missing .builder/builder.py"
  throw "Missing .builder/builder.py"
}

Add-Content $LogFile "- OK: found .builder/builder.py"

$nav = Join-Path $Root ".canon/navigator"
if (Test-Path $nav) {
  Remove-Item -Recurse -Force $nav
  Add-Content $LogFile "- OK: removed existing .canon/navigator/"
} else {
  Add-Content $LogFile "- OK: .canon/navigator/ not present (fresh build)"
}

Add-Content $LogFile ""
Add-Content $LogFile "## Execution"
Add-Content $LogFile ""

python $builder generate --root $Root 2>&1 | Add-Content $LogFile
Add-Content $LogFile ""
Add-Content $LogFile "- OK: builder generate completed"

Add-Content $LogFile ""
Add-Content $LogFile "## Postchecks"
Add-Content $LogFile ""

$navReadme = Join-Path $Root ".canon/navigator/README.md"
if (Test-Path $navReadme) {
  Add-Content $LogFile "- PASS: .canon/navigator/README.md regenerated"
} else {
  Add-Content $LogFile "- FAIL: .canon/navigator/README.md missing after regeneration"
  throw "Navigator README missing after regeneration"
}

Write-Host "[navigator] OK: refreshed .canon/navigator (log: $LogFile)"
