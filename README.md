# The Builder Kit

This directory contains the **Repo-Agnostic Builder (V3)** kit. 
It is designed to be copied into the root of any repository to instantly provide:

1.  **Observability**: A unified `.logs/` spine with automated telemetry standards.
2.  **Governance**: A canonical knowledge base (`.canon/`) and governance policies (`AGENTS.md`).
3.  **Tooling**: A repository-agnostic tool surface (`.toolkit/`) for maintenance and validation.

## Usage

```bash
# 1. Copy .builder/ to your repo root.
cp -r /path/to/builder .builder

# 2. Run generation to scaffold the repository
python3 .builder/builder.py generate
```

## Component Structure

- **`builder.py`**: The single-file entry point for all operations.
- **`templates/`**: The physical schema of files to generate.
    - `project-root/`: Files that land in the repository root (e.g., `.logs/`, `AGENTS.md`).
    - `canon/`: The core documentation and knowledge base.
    - `toolkit/`: Scripts and placeholders for dev-tools.
- **`docs/`**: Documentation for the Builder itself (separate from the repo's docs).

## Updating the Kit

Modify the templates in `.builder/templates/`. The next time `builder.py generate` is run, changes will propagate to the generated files (unless marked preserved).
