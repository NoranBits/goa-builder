# Builder Documentation

This directory contains internal documentation for the Builder V3 system itself.

## Architecture

The Builder is a self-contained Python script (`builder.py`) that operates on a "Template + Stamping" model.

- **Templates**: Located in `templates/`. These are the "source of truth" for the generated files.
- **Generator**: The `generate` command recursively copies templates to the target, preserving governance files.
- **Pipelines**: The Builder proactively scans `package.json` files to inject `test:report` scripts, ensuring observability.

## Key Invariants

1. **Agnostic**: The Builder does not import project code. It inspects files (JSON/YAML) and structure.
2. **Safe**: It defaults to `overwrite=False` for sensitive files (`create_only_paths`).
3. **Audit**: It enforces the existence of `.logs/` and `AGENTS.md`.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
