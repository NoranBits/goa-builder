# Builder Kit Requirements (Hardcoded)

This document is the **requirements contract** for the `.builder/` starter kit.

## Required artifacts

The kit MUST ensure the following exist in any target repository:

- `markdown.md` (root-level)
- `.markdownlint-cli2.cjs` (root-level)
- `.markdownlint.json` (root-level)
- `.vscode/tasks.json` contains a task with label `validate:markdownlint`
- `.canon/README.md`
- `.logs/INDEX.md`
- `.canon/roles/` (core role playbooks)
- `.canon/dev-book/` (01–15 structure-first chapters)
- `.toolkit/` (repo-agnostic tool composition scaffold)

The kit MUST also provide a self-validation command:

- `python3 .builder/builder.py validate-kit`

If a `.git/` directory exists, the kit MUST ensure:

- `.gitignore` contains `.logs/`

## Mandatory validation

- Markdown must be validated using `markdownlint-cli2`.
- Validation must be runnable as a VS Code task.
- The kit MUST assume install via npm:

```bash
npm install --save-dev markdownlint-cli2
```

## Lint scope

- By default, validate Markdown in **generated scope** (the kit surface):
  - `.builder/**`
  - `.canon/**`
  - `.toolkit/**`
  - `markdown.md`

- Optionally, validate Markdown across the **entire repo** (recommended in CI), excluding:
  - `node_modules/**`
  - `.git/**`
  - `.logs/**`
  - `docs/inspiration/projects/**/upstream/**`

## Canon overview entry points

The generated `.canon/dev-book/01-overview/` MUST include:

- `introduction.md`
- `tech-stack.md`
- `architecture.md`
- `features.md`
