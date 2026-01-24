# .toolkit

> **Context**: This directory contains the operational scripts and local automation tools that power the repository's daily maintenance. While `.github` handles CI/CD, `.toolkit` handles local developer tasks and "glue" code.

## Composition

- **`scripts/`**: Executable scripts (Bash, Python, Node.js) for tasks like setup, builds, or data processing.
- **`templates/`**: Scaffolding templates used by scripts to generate new files.
- **`manifests/`**: Configuration files or schemas used by the tools.

## Rules of the Road

1. **Idempotency**: All scripts must be safe to run multiple times without side effects (e.g., check if a resource exists before creating).
2. **Minimalism**: Prefer standard libraries (Python `sys`, `json`; Bash built-ins) to avoid complex dependency chains.
3. **Logging**: Scripts should output human-readable progress to stdout and detailed debug info to `.logs/` (gitignored).
4. **Error Handling**: Always exit with a non-zero status code on failure to block dependent tasks.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Bash Scripting Cheat Sheet**: [DevDocs Bash](https://devdocs.io/bash/) - Reference for shell script syntax.
- **Python 3 Documentation**: [Official Docs](https://docs.python.org/3/) - For Python-based automation.
- **Node.js Documentation**: [Node.js api](https://nodejs.org/en/docs/) - For JavaScript/TypeScript tooling context.
- **JSON Schema**: [Understanding JSON Schema](https://json-schema.org/understanding-json-schema/) - For validating configuration files.

## Safety

- Treat this folder as executable infrastructure. Validate inputs in scripts to prevent injection or corruption.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
