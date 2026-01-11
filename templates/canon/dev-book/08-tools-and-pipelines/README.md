# 08 Tools and Pipelines

## The Builder System (V3)

This repository is managed by a **Repo-Agnostic Builder** (`.builder/`). It is not just a script, but a lifecycle manager.

### Capabilities

- **Scaffolding**: Generates consistent `.canon/`, `.logs/`, and `.toolkit/` structures.
- **Pipeline Injection**: Automatically discovers package targets (e.g., `package.json`) and injects observability hooks.
- **Validation**: Enforces policies via `validate-kit`.

## Standard Commands (Placeholder)

- Generation: `python3 .builder/builder.py generate`
- Build: (Repo specific, e.g., `make build`, `npm run build`)
- Dev: (Repo specific, e.g., `npm run dev`)

## Legacy & Interop

See [Legacy System Interop](./legacy-system-interop.md) for details on migrating from older systems.

