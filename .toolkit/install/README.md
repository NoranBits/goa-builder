# install

> **Context**: Tools for bootstrapping the development environment and managing dependencies.

## Purpose

Install tools ensure that the local machine is ready for development.

## Suggested Tools

- **`setup.sh`**: The "One Script" to rule them all (calls others).
- **`install_deps.py`**: Idempontent dependency installer (pip, npm, cargo).
- **`check_env.py`**: Verify python version, available memory, etc.

## Works Well With

- **`update/`**: Use update tools to change versions; use install to sync them.
- **`build/`**: Install often feeds into build.

## Custom Tools

Use `custom-tools/` for one-off environment patches.

## Safety

- Prefer virtual environments (venv, node_modules) over global installs.
- Warn the user before modifying shell profiles (`.bashrc`).

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Python Virtual Environments**: [venv](https://docs.python.org/3/library/venv.html) - Python isolation.
- **NPM**: [CLI Commands](https://docs.npmjs.com/cli/v8/commands/npm-install) - Node package management.
- **Cargo**: [The Book](https://doc.rust-lang.org/cargo/) - Rust package manager.
