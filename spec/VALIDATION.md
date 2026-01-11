# Validation Policy

## Markdownlint

All Markdown enforcement in this kit is based on:

- `markdownlint-cli2`
- `.markdownlint-cli2.cjs` as the primary config file

## Installation requirement

The target repo MUST install markdownlint via npm:

```bash
npm install --save-dev markdownlint-cli2
```

## How validation runs

- CLI:

```bash
python3 .builder/tools/run_markdownlint.py
```

By default, Markdownlint runs in **generated scope**:

- `.builder/**`
- `.canon/**`
- `.toolkit/**`
- `markdown.md`

To lint the entire repository (optional):

```bash
python3 .builder/builder.py validate --scope repo
```

## Kit self-validation

The kit includes a lightweight self-check that validates `.builder/` integrity:

```bash
python3 .builder/builder.py validate-kit
```

It checks:

- Required `.builder/` files exist (runner, specs, templates, tools)
- Template expectations (including `.canon/dev-book/01-overview` entry points)
- VS Code task template contains the required `validate:markdownlint` task

- VS Code:

Run task:

- `validate:markdownlint`

## Exclusions

Validation excludes these directories by default:

- `node_modules/**`
- `.git/**`
- `.logs/**`
- `docs/inspiration/projects/**/upstream/**`
