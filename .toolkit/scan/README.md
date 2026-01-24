# scan

> **Context**: Discovery tools that read the repository state to help agents understand the lay of the land.

## Purpose

Scan tools are read-only analyzers that produce summaries or maps of the codebase.

## Suggested Tools

- **`map_repo.py`**: updates `.canon/navigator` with a fresh map.
- **`list_entrypoints.py`**: identify main files, routes, and public APIs.
- **`find_large_files.sh`**: detect binary blobs or asset clusters.

## Works Well With

- **`.canon/navigator`**: The primary output destination.
- **`search/`**: Scan is high-level; search is specific query.

## Custom Tools

Use `custom-tools/` for deep AST analysis of specific languages.

## Safety

- Scanners must be **read-only**.
- Avoid scanning `node_modules` or `.git` to prevent performance kills.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Tree Command**: [Man Page](https://linux.die.net/man/1/tree) - The classic directory visualizer.
- **Cloc**: [Count Lines of Code](https://github.com/AlDanial/cloc) - Metrics for codebase size.
- **Graphviz**: [DOT Language](https://graphviz.org/doc/info/lang.html) - For generating dependency graphs.

<!-- md_autofix: processed -->
