#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"[validate:markdownlint] FAIL: {message}")


def repo_root() -> Path:
    return Path.cwd().resolve()


def _is_markdown_file(path: Path) -> bool:
    return path.is_file() and path.name.endswith((".md", ".mdc"))


def _walk_markdown_files(root: Path, start: Path) -> list[Path]:
    excluded_dirnames = {"node_modules", ".git", ".logs"}

    files: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(start):
        p = Path(dirpath)
        dirnames[:] = [d for d in dirnames if d not in excluded_dirnames]

        # Exclude upstream trees anywhere under docs/inspiration/projects/**/upstream/**
        if (
            "docs" in p.parts
            and "inspiration" in p.parts
            and "projects" in p.parts
            and "upstream" in p.parts
        ):
            dirnames[:] = []
            continue

        for name in filenames:
            if name.endswith((".md", ".mdc")):
                files.append(p / name)

    # Deduplicate + stable order
    return sorted(set(files))


def find_markdown_files(root: Path, *, rel_paths: list[str] | None) -> list[Path]:
    if not rel_paths:
        return _walk_markdown_files(root, root)

    files: list[Path] = []
    for rel in rel_paths:
        p = (root / rel).resolve()
        try:
            p.relative_to(root)
        except ValueError:
            fail(f"Path escapes repo root: {rel}")

        if _is_markdown_file(p):
            files.append(p)
            continue

        if p.exists() and p.is_dir():
            files.extend(_walk_markdown_files(root, p))

    return sorted(set(files))


def ensure_required_files(root: Path) -> None:
    required = ["markdown.md", ".markdownlint-cli2.cjs", ".markdownlint.json"]
    missing = [p for p in required if not (root / p).exists()]
    if missing:
        fail(f"Missing required file(s): {', '.join(missing)}")


def ensure_generated_scaffold(root: Path) -> None:
    required = [
        ".builder",
        ".canon",
        ".toolkit",
    ]
    missing = [p for p in required if not (root / p).exists()]
    if missing:
        fail(
            "Missing generated scaffold: "

            + ", ".join(missing)
            + ". Run `python3 .builder/builder.py generate`."
        )


def main() -> int:
    ap = argparse.ArgumentParser(prog="run_markdownlint.py")
    ap.add_argument(
        "--config",
        default=".markdownlint-cli2.cjs",
        help="Path to markdownlint-cli2 config file (relative to repo root).",
    )
    ap.add_argument(
        "--scope",
        choices=["generated", "repo", "paths"],
        default="generated",
        help=(
            "Lint scope: 'generated' lints only .builder + .canon + .toolkit + markdown.md; "
            "'repo' lints the whole repo; 'paths' lints only the provided --path entries."
        ),
    )
    ap.add_argument(
        "--path",
        action="append",
        default=[],
        help=(
            "Relative path to include when --scope=paths (repeatable). "
            "May be a file or directory."
        ),
    )
    args = ap.parse_args()

    root = repo_root()
    ensure_required_files(root)

    if args.scope == "generated":
        ensure_generated_scaffold(root)

    config_path = (root / args.config).resolve()
    if not config_path.exists():
        fail(f"Missing config: {config_path.relative_to(root)}")

    bin_path = root / "node_modules" / ".bin" / "markdownlint-cli2"
    if not bin_path.exists():
        npm = shutil.which("npm")
        hint = (
            "npm install && npm install --save-dev markdownlint-cli2"
            if npm
            else "install npm and run npm install --save-dev markdownlint-cli2"
        )
        fail(
            "markdownlint-cli2 is not installed locally (missing node_modules/.bin/markdownlint-cli2). "
            f"Run `{hint}`."
        )

    if args.scope == "repo":
        rel_paths: list[str] | None = None
    elif args.scope == "generated":
        rel_paths = [".builder", ".canon", ".toolkit", "markdown.md"]
    else:
        if not args.path:
            fail("--scope=paths requires at least one --path")
        rel_paths = list(args.path)

    files = find_markdown_files(root, rel_paths=rel_paths)
    if not files:
        print("[validate:markdownlint] OK (no markdown files found)")
        return 0

    cmd = [
        str(bin_path),
        "--config",
        str(config_path.relative_to(root)),
        *[str(p.relative_to(root)) for p in files],
    ]

    try:
        subprocess.check_call(cmd, cwd=root)
    except subprocess.CalledProcessError as e:
        fail(f"markdownlint failed (exit {e.returncode})")

    print("[validate:markdownlint] OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

<!-- md_autofix: processed -->
