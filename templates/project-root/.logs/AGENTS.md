# AGENTS.md (Canon Logs Gate)

This gate applies to files under `.logs/**`.

## Rules

- Append-only: never edit or delete previous entries.
- Each entry must be timestamped.
- Prefer small, frequent entries over large, ambiguous ones.

## Placeholders (adjust per repo)

- Timestamp format: `{{LOG_TIMESTAMP_FORMAT}}`
- Actor IDs: `{{LOG_ACTOR_IDS}}`

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
