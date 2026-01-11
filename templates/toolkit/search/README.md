# search

## Purpose

Search tools make codebase navigation fast and repeatable.

## Suggested tools

- `rg_wrap.py`: opinionated ripgrep wrapper (paths, excludes, formatting).
- `symbols_index.py`: build a lightweight symbol index.
- `find_entrypoints.py`: locate important bootstrap and routing files.

## Works well with

- `scan/`: turn scan results into targeted queries.
- `log/`: match log errors to file paths and symbols.
- `validate/`: locate config files that drive validation.

## Custom tools

Use `custom-tools/` for one-off searches and investigations.

## Safety

Search tools should be read-only.
