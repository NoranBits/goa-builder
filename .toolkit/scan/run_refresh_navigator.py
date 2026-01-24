#!/usr/bin/env python3
"""Cross-platform launcher for the navigator refresh.

Selects the appropriate platform-specific script and runs it.

Usage:
  python3 .toolkit/scan/run_refresh_navigator.py [--root /path/to/repo] [--step-id MM.SS.TT]

Behavior:

- On Windows: runs `refresh_navigator.ps1` via PowerShell (`pwsh` or `powershell`).
- On POSIX (Linux/macOS/Android-termux): runs `refresh_navigator.sh` via `bash`.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def repo_root(path: Path | None) -> Path:
    if path:
        return path.resolve()
    return Path.cwd().resolve()


def find_executable(names: list[str]) -> str | None:
    for n in names:
        p = shutil.which(n)
        if p:
            return p
    return None


def run_on_windows(tool_root: Path) -> int:
    # prefer pwsh, fallback to powershell
    pwsh = find_executable(["pwsh", "powershell"])
    if not pwsh:
        print("ERROR: PowerShell not found on PATH. Install PowerShell or use WSL.")
        return 2
    script = tool_root / "refresh_navigator.ps1"
    if not script.exists():
        print(f"ERROR: Missing {script}")
        return 2
    cmd = [pwsh, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", str(script)]
    return subprocess.run(cmd).returncode


def run_on_posix(tool_root: Path) -> int:
    bash = find_executable(["bash", "/bin/bash"])
    if not bash:
        print("ERROR: bash not found on PATH.")
        return 2
    script = tool_root / "refresh_navigator.sh"
    if not script.exists():
        print(f"ERROR: Missing {script}")
        return 2
    cmd = [bash, str(script)]
    return subprocess.run(cmd).returncode


def main() -> int:
    ap = argparse.ArgumentParser(prog="run_refresh_navigator.py")
    ap.add_argument("--root", type=Path, help="Repository root (defaults to CWD)")
    ap.add_argument("--step-id", type=str, help="Optional MM.SS.TT step id to include in logs")
    args = ap.parse_args()

    root = repo_root(args.root)
    tool_root = root / ".toolkit" / "scan"

    if sys.platform.startswith("win"):
        code = run_on_windows(tool_root)
    else:
        code = run_on_posix(tool_root)

    return code


if __name__ == "__main__":
    raise SystemExit(main())

<!-- md_autofix: processed -->
