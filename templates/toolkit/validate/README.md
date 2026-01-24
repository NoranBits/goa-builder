# validate

> **Context**: Static analysis and policy enforcement gates.

## Purpose

Validate tools ensure code quality without running the code (mostly). They are the first line of defense.

## Suggested Tools

- **`lint.sh`**: Run all linters (flake8, eslint, clippy).
- **`typecheck.sh`**: Run static type checkers (mypy, tsc).
- **`check_format.sh`**: Verify code formatting (black, prettier).
- **`check_leaks.sh`**: Scan for secrets or PII.

## Works Well With

- **`.vscode/tasks.json`**: Validation should be a default task on save/commit.
- **`.github/workflows`**: validation is the cheapest CI step.

## Custom Tools

Use `custom-tools/` for architecture compliance checks (e.g., dependency direction).

## Safety

- Validators should be **read-only** (use `format.sh` which lives in `update/` or `custom-tools` for fixing).

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **ESLint**: [Rules](https://eslint.org/docs/latest/rules/) - JavaScript linting standards.
- **Ruff**: [Docs](https://docs.astral.sh/ruff/) - Fast Python linter.
- **Prettier**: [Options](https://prettier.io/docs/en/options.html) - Opinionated code formatting.
- **MyPy**: [Cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html) - Python static typing.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
