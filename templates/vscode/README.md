# VS Code Templates

## Purpose

This folder contains editor configuration templates that the builder installs or merges into the target repo.

## What gets generated

- `.vscode/tasks.json` (merged): must include the stable `validate:markdownlint` task.

## Adjustments

- If you add new tasks, keep existing task labels stable.
- Prefer tasks that call repo scripts (not long inline shell pipelines).

## Placeholders (adjust per repo)

- Primary validation tasks: `{{VSCODE_VALIDATE_TASKS}}`
