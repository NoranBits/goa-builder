#!/usr/bin/env python3
"""Create a single CONTEXT_MAP.md by concatenating key docs.

Usage: python3 consolidate_memory.py /path/to/project
"""
import sys
from pathlib import Path


def read_if_exists(p: Path):
    if p.exists():
        return p.read_text(encoding='utf-8')
    return ""


def main():
    if len(sys.argv) < 2:
        print("Usage: consolidate_memory.py /path/to/project")
        return 2
    project = Path(sys.argv[1]).resolve()
    out = project / "CONTEXT_MAP.md"
    parts = []
    # order matters: agents, canonical, decisions index
    parts.append("# CONTEXT MAP\n\n")
    parts.append("## AGENTS.md\n\n")
    parts.append(read_if_exists(project / "AGENTS.md"))
    parts.append("\n\n## .canon/README.md\n\n")
    parts.append(read_if_exists(project / ".canon/README.md"))
    parts.append("\n\n## .logs/decisions/INDEX.md\n\n")
    parts.append(read_if_exists(project / ".logs/decisions/INDEX.md"))
    # write
    out.write_text("\n".join(parts), encoding='utf-8')
    print(f"Wrote CONTEXT_MAP.md -> {out}")


if __name__ == "__main__":
    raise SystemExit(main())

