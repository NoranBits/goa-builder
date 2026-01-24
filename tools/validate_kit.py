#!/usr/bin/env python3
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Problem:
    message: str


def _kit_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _require_file(path: Path, rel: str, problems: list[Problem]) -> None:
    if not path.exists():
        problems.append(Problem(f"Missing required file: {rel}"))
        return
    if not path.is_file():
        problems.append(Problem(f"Expected file but found non-file: {rel}"))


def _require_dir(path: Path, rel: str, problems: list[Problem]) -> None:
    if not path.exists():
        problems.append(Problem(f"Missing required directory: {rel}"))
        return
    if not path.is_dir():
        problems.append(Problem(f"Expected directory but found non-dir: {rel}"))


def _load_json(path: Path, rel: str, problems: list[Problem]) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        problems.append(Problem(f"Missing required JSON file: {rel}"))
        return None
    except json.JSONDecodeError as e:
        problems.append(
            Problem(f"Invalid JSON in {rel}: {e.msg} (line {e.lineno}, col {e.colno})")
        )
        return None


def _validate_tasks_template(kit: Path, problems: list[Problem]) -> None:
    rel = "templates/vscode/tasks.json"
    tasks_path = kit / rel
    data = _load_json(tasks_path, rel, problems)
    if data is None:
        return

    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        problems.append(Problem(f"{rel}: expected 'tasks' to be a list"))
        return

    required_label = "validate:markdownlint"
    required_command = "python3"
    required_args = [".builder/tools/run_markdownlint.py"]

    match = None
    for t in tasks:
        if isinstance(t, dict) and t.get("label") == required_label:
            match = t
            break

    if match is None:
        problems.append(Problem(f"{rel}: missing task with label '{required_label}'"))
        return

    if match.get("command") != required_command:
        problems.append(
            Problem(
                f"{rel}: task '{required_label}' must use command '{required_command}'"
            )
        )

    args = match.get("args")
    if args != required_args:
        problems.append(
            Problem(f"{rel}: task '{required_label}' must use args {required_args!r}")
        )


def validate_kit(kit: Path) -> list[Problem]:
    problems: list[Problem] = []
    # A compact, flexible set of required files/dirs aligned with the
    # current builder templates. Keep checks conservative to reduce
    # noise while still enforcing the key governance and tooling artifacts.
    required_files = [
           "templates/canon/AGENTS.md",
           "templates/canon/README.md",
           "builder.py",
           "package.json",
           "tools/validate_kit.py",
    ]

    required_dirs = [
        "templates/canon",
        "templates/toolkit/scan",
        "templates/canon/dev-book",
        "templates/canon/navigator",
        "templates/canon/roles",
        "templates/canon/external",
    ]

    for rel in required_files:
        _require_file(kit / rel, rel, problems)

    for rel in required_dirs:
        _require_dir(kit / rel, rel, problems)

    # Ensure a navigator script exists either in templates or in the repo toolkit
        nav_template = kit / "templates/toolkit/scan/refresh_navigator.sh"
        nav_toolkit = kit / ".toolkit/scan/refresh_navigator.sh"
        if not nav_template.exists() and not nav_toolkit.exists():
            problems.append(
                Problem(
                    "Missing required navigator script: templates/toolkit/scan/refresh_navigator.sh or .toolkit/scan/refresh_navigator.sh"
                )
            )

    _validate_tasks_template(kit, problems)

    return problems


def main() -> int:
    kit = _kit_root()
    problems = validate_kit(kit)

    if problems:
        print("[builder] validate-kit: FAIL")
        for p in problems:
            print(f"- {p.message}")
        return 1

    print("[builder] validate-kit: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

<!-- md_autofix: processed -->
