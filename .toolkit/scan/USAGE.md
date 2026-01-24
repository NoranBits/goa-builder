# Navigator Scan — Cross-Platform Usage

This document explains how to run the repository navigator scan on common platforms (Linux, macOS, Windows, Android/Termux).

Recommended (single command)

```bash
python3 .toolkit/scan/run_refresh_navigator.py [--root /path/to/repo] [--step-id MM.SS.TT]
```text

- `--root`: optional repo root (defaults to CWD).
- `--step-id`: optional MM.SS.TT identifier for logging and session metadata.

Platform details

- Linux / macOS / Android (Termux): the wrapper executes `refresh_navigator.sh` via `bash`.
- Windows: the wrapper executes `refresh_navigator.ps1` via PowerShell (`pwsh` preferred, falls back to `powershell`).

Direct invocation

- Linux/macOS/Termux:

```bash
bash .toolkit/scan/refresh_navigator.sh
```text

- Windows (PowerShell):

```powershell
powershell -NoProfile -NonInteractive -ExecutionPolicy Bypass -File .toolkit/scan/refresh_navigator.ps1
```text

Notes for Android/Termux

- Install packages: `pkg install python bash`.
- Use `python3 .toolkit/scan/run_refresh_navigator.py` as above.

Logging & Step IDs

When present, the `--step-id` should follow the policy in `.canon/policies/POLICY__step-id-and-task-numbering.md` (format `MM.SS.TT`, zero-padded). Tools should write structured metadata into `.logs/validation/` and append an entry to `.logs/sessions/` for auditability.

<!-- md_autofix: processed -->
