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

    required_files = [
        "templates/project-root/AGENTS.md",
        "templates/project-root/README.md",
        "templates/project-root/.github/README.md",
        "templates/project-root/.github/agents/README.md",
        "templates/project-root/.github/instructions/README.md",
        "templates/project-root/.github/prompts/README.md",
        "templates/project-root/.vscode/README.md",
        "templates/project-root/.toolkit/README.md",
        "README.md",
        "builder.py",
        "tools/run_markdownlint.py",
        "spec/REQUIREMENTS.md",
        "spec/STRUCTURE.md",
        "spec/GENERATE_POLICY.md",
        "spec/VALIDATION.md",
        "templates/project-root/markdown.md",
        "templates/project-root/.markdownlint-cli2.cjs",
        "templates/project-root/.markdownlint.json",
        "templates/vscode/tasks.json",
        "templates/vscode/README.md",
        "templates/vscode/AGENTS.md",
        "templates/canon/README.md",
        "templates/canon/AGENTS.md",
        "templates/canon/logs/INDEX.md",
        "templates/canon/logs/AGENTS.md",
        "templates/canon/logs/navigation/README.md",
        "templates/canon/logs/navigation/INDEX.md",
        "templates/canon/logs/navigation/sessions/README.md",
        "templates/canon/dev-book/README.md",
        "templates/canon/dev-book/AGENTS.md",
        "templates/canon/dev-book/01-overview/README.md",
        "templates/canon/dev-book/01-overview/introduction.md",
        "templates/canon/dev-book/01-overview/tech-stack.md",
        "templates/canon/dev-book/01-overview/architecture.md",
        "templates/canon/dev-book/01-overview/features.md",
        "templates/canon/dev-book/01-overview/agent-authority.md",
        "templates/canon/dev-book/02-getting-started/installation-wizard.md",
        "templates/canon/roles/README.md",
        "templates/canon/roles/AGENTS.md",
        "templates/canon/navigator/README.md",
        "templates/canon/navigator/AGENTS.md",
        "templates/canon/external/README.md",
        "templates/canon/external/external_source.template.md",
        "templates/canon/external/linktree.template.md",
        "templates/toolkit/README.md",
        "templates/toolkit/AGENTS.md",
        "templates/toolkit/scan/README.md",
        "templates/toolkit/search/README.md",
        "templates/toolkit/validate/README.md",
        "templates/toolkit/test/README.md",
        "templates/toolkit/log/README.md",
        "templates/toolkit/build/README.md",
        "templates/toolkit/install/README.md",
        "templates/toolkit/package/README.md",
        "templates/toolkit/update/README.md",
        "templates/toolkit/scan/custom-tools/README.md",
        "templates/toolkit/search/custom-tools/README.md",
        "templates/toolkit/validate/custom-tools/README.md",
        "templates/toolkit/test/custom-tools/README.md",
        "templates/toolkit/log/custom-tools/README.md",
        "templates/toolkit/build/custom-tools/README.md",
        "templates/toolkit/install/custom-tools/README.md",
        "templates/toolkit/package/custom-tools/README.md",
        "templates/toolkit/update/custom-tools/README.md",
        "templates/canon/roles/GitAssistant.role.md",
        "templates/canon/roles/Maintainer.role.md",
    ]

    required_dirs = [
        "templates/canon/logs/changes",
        "templates/canon/logs/decisions",
        "templates/canon/logs/ingestion",
        "templates/canon/logs/navigation",
        "templates/canon/logs/navigation/sessions",
        "templates/canon/roles",
        "templates/canon/navigator",
        "templates/canon/external",
        "templates/toolkit",
        "templates/toolkit/scan/custom-tools",
        "templates/toolkit/search/custom-tools",
        "templates/toolkit/validate/custom-tools",
        "templates/toolkit/test/custom-tools",
        "templates/toolkit/log/custom-tools",
        "templates/toolkit/build/custom-tools",
        "templates/toolkit/install/custom-tools",
        "templates/toolkit/package/custom-tools",
        "templates/toolkit/update/custom-tools",
    ]

    for rel in required_files:
        _require_file(kit / rel, rel, problems)

    for rel in required_dirs:
        _require_dir(kit / rel, rel, problems)

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
