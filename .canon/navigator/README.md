# navigator

> **Context**: The `navigator` is a generated map of the repository structure. It allows agents to "look around" without expensive file reads or shell commands.

## Purpose

`navigator/` is an agent-facing map of the repository generated from a scan.

It is designed to be:

- **High-signal**: Small summaries, stable ordering.
- **Incremental**: Easy to regenerate, easy to refine.
- **Safe**: Does not modify source folders.

## What Gets Generated

- **`README.md`**: Entry point index for the repo map.
- **Per-folder `README.md`**: Pages mirroring the repo’s folder structure.

## How Agents Should Use It

1. Start at `navigator/README.md`.
2. Follow links deeper until you reach the target subsystem.
3. Use `.toolkit/scan` and `.toolkit/search` to confirm details.

## Navigation History (Append-only)

After a scan session, record what you inspected (and why) under:

- `.logs/navigation/**`

This reduces repeated discovery work and creates reliable “quicksteps” for future sessions.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **Abstract Syntax Trees (AST)**: [Explorer](https://astexplorer.net/) - Understanding how code structures are parsed.
- **Language Server Protocol (LSP)**: [Specification](https://microsoft.github.io/language-server-protocol/) - How modern editors "understand" code navigation.
- **Tags (ctags)**: [Universal Ctags](https://github.com/universal-ctags/ctags) - Classic definition of code indexing.

## Generated index

Start here, then follow links deeper until you reach the target subsystem.

- [.builder](.builder/README.md)
- [.github](.github/README.md)
- [.toolkit](.toolkit/README.md)
- [.vscode](.vscode/README.md)
- [context](context/README.md)
- [docs](docs/README.md)
- [reports](reports/README.md)
- [spec](spec/README.md)
- [templates](templates/README.md)
- [tools](tools/README.md)

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
