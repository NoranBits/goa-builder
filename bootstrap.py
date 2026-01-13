#!/usr/bin/env python3
"""Simple hydrator: copy the .builder payload into a target project.

Usage: python3 bootstrap.py /path/to/target
"""
import sys
import shutil
from pathlib import Path


def copy_payload(target: Path):
    here = Path(__file__).resolve().parent
    payload_dirs = ["agents", "prompts", "tools", "templates"]
    target_builder = target / ".builder"
    target_builder.mkdir(parents=True, exist_ok=True)
    for d in payload_dirs:
        src = here / d
        if not src.exists():
            continue
        dst = target_builder / d
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    print(f"Hydrated .builder payload into: {target_builder}")


def main():
    if len(sys.argv) < 2:
        print("Usage: bootstrap.py /path/to/target")
        sys.exit(2)
    target = Path(sys.argv[1]).resolve()
    if not target.exists():
        print(f"Target does not exist: {target}")
        sys.exit(1)
    copy_payload(target)


if __name__ == "__main__":
    main()
