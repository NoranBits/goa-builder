#!/usr/bin/env python3
"""Require explicit activation before running non-repo-agnostic Builder actions.

Checks for either:

- repository root file: .builder/ALLOW_AUTOINVOKE
- environment variable: GOA_BUILDER_ACTIVATE=1

Exit code 0 when allowed, non-zero otherwise.
"""
import os
from pathlib import Path


def is_allowed(repo_root: Path) -> bool:
    env = os.environ.get("GOA_BUILDER_ACTIVATE")
    if env is not None and env.strip() == "1":
        return True
    marker = repo_root / ".builder" / "ALLOW_AUTOINVOKE"
    return marker.exists()


def main():
    repo = Path(os.getcwd()).resolve()
    # climb until we find a .git or stop at filesystem root
    root = repo
    for _ in range(10):
        if (root / ".git").exists() or (root / "package.json").exists() or (root / "README.md").exists():
            break
        if root.parent == root:
            break
        root = root.parent

    allowed = is_allowed(root)
    if allowed:
        print("Activation check: ALLOWED")
        return 0
    print("Activation check: DENIED. Create .builder/ALLOW_AUTOINVOKE or set GOA_BUILDER_ACTIVATE=1 to proceed.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
