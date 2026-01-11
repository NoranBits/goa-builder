# install

## Purpose

Install tools bootstrap a dev environment and dependencies.

## Suggested tools

- `install_deps.py`: install dependencies using the repo’s package manager.
- `doctor.py`: verify prerequisites and print actionable fixes.

## Works well with

- `build/`: ensure toolchain and dependencies exist.
- `validate/`: install missing validators or linters.
- `test/`: set up the environment for reliable test runs.

## Custom tools

Use `custom-tools/` for local-only helpers.

## Safety

Install tools should be explicit about what they change.
