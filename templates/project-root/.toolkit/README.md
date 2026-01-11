# .toolkit

## Purpose

Repo-local automation scripts.

## Rules

- Idempotent and safe to re-run.
- Prefer standard library and minimal dependencies.
- Exit non-zero on failures.
- Write large runtime logs under `.logs/` (gitignored).

## Placeholders (adjust per repo)

- Tools owner: `{{TOOLS_OWNER}}`
- Primary validators: `{{TOOLS_VALIDATORS}}`
