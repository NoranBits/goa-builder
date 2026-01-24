# Session Summary (Source Context)

This file captures the requirements and intent accumulated during the session that introduced this `.builder/` kit.

## Primary intent

- Create a **repo-agnostic** “GOA Builder” bootstrap kit.
- The kit lives in `.builder/` and can be dropped into any repo.
- The kit generates a canonical knowledge base under `.canon/`.

## Mandatory audit/logging

- `.logs/**` is the mandatory, append-only audit spine.
- `.logs/**` is runtime/ephemeral and should be gitignored.

## Strict Markdown enforcement

- A root-level `markdown.md` is required.
- `markdownlint-cli2` is required, installed via npm.
- VS Code tasks MUST include a stable `validate:markdownlint` task.

## Output expectations

- `.canon/dev-book/` is generated with minimal content (structure first).
- `.canon/roles/` contains the playbooks for the core agent roles.
- `.logs/INDEX.md` is the audit spine index.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
