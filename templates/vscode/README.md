# VS Code Templates

## Purpose

This folder contains editor configuration templates that the builder installs or merges into the target repo.

## What gets generated

- `.vscode/tasks.json` (merged): must include the stable `validate:markdownlint` task.
- `.vscode/extensions.json` (merged): recommended extensions for the workspace. The builder will merge `recommendations` with the repo's existing recommended extensions rather than overwrite them. Use `{{VSCODE_RECOMMENDED_EXTENSIONS}}` as a placeholder in templates.

## Adjustments

- If you add new tasks, keep existing task labels stable.
- Prefer tasks that call repo scripts (not long inline shell pipelines).

## Placeholders (adjust per repo)

- Primary validation tasks: `{{VSCODE_VALIDATE_TASKS}}`
- Recommended extensions placeholder: `{{VSCODE_RECOMMENDED_EXTENSIONS}}`

<!-- md_autofix: processed -->
