# AGENTS.md (.toolkit Subtree Gate)

This gate applies to files under `.toolkit/**`.

## Rules

- Tools must be safe-by-default and idempotent.
- Prefer read-only behavior unless a write flag is explicit.
- Clear exit codes: non-zero on failure.
- Document inputs, outputs, and failure modes in the nearest `README.md`.

## Promotion policy

- New scripts start in `custom-tools/`.
- Promote to the category root only after explicit confirmation.

## Placeholders (adjust per repo)

- Tool owners: `{{TOOLKIT_OWNERS}}`
- Log directory: `{{TOOLKIT_LOG_DIR}}`

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
