# validate

## Purpose

Validation tools enforce repo health and “definition of done”.

Common checks:

- Markdownlint
- Formatting
- Linting
- Typechecking
- Policy gates (for example: upstream not tracked)

## Works well with

- `scan/`: decide which validators apply.
- `test/`: run fast tests after the lowest-cost checks.
- `log/`: bundle outputs when a gate fails.

## Composition suggestions

- A `quality_gate` tool usually includes: markdown + lint + typecheck + fast tests.
- A `precommit` tool may include: formatting + lint + markdown.

## Suggested tools

- `validate_markdown.py`: run markdownlint with a scoped default.
- `validate_repo.py`: small, deterministic repo checks.
- `validate_assets.py`: detect missing or inconsistent asset outputs.

## Custom tools

Use `custom-tools/` for experimental validators.

## Safety

Validators should default to read-only.
If auto-fix exists, it should be explicit (for example: `--fix`).
