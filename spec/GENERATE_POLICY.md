# Generate Policy (Deterministic)

This document defines the deterministic behavior of `python3 .builder/builder.py generate`.

## Primary goals

- Ensure required Markdown enforcement artifacts exist.
- Ensure the canonical knowledge base scaffold exists.
- Ensure the repo-agnostic tool scaffold exists.
- Ensure validation is runnable as a VS Code task.
- Ensure `.gitignore` contains `.logs/` if applicable.
- Ensure repeatable, conflict-averse generation.

## Rules

- The generator MUST be conflict-averse:
  - If a file exists and `--overwrite` is not provided, the generator MUST NOT overwrite it.
  - The generator MAY patch `/.vscode/tasks.json` to add missing required tasks.
- The generator MUST create or extend `/.vscode/tasks.json` with `validate:markdownlint`.
- The generator MUST generate `.canon/**` from templates.
- The generator MUST generate `.toolkit/**` from templates.
- If the target repo contains `.git/`, the generator MUST append `.logs/` to `/.gitignore`.

## Hardcoded tasks

The task label is a stable contract:

- `validate:markdownlint`

The task MUST run:

- `python3 .builder/tools/run_markdownlint.py`

<!-- md_autofix: processed -->
