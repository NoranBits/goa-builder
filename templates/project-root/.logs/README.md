# .logs

> **Context**: Stores execution records, decision logs, and runtime telemetry. This folder is the "Black Box" of the GOA Builder airplane.

## Contents

- **`sessions/`**: Full transcripts of AI coding sessions (Markdown).
- **`decisions/`**: Architecture Decision Records (ADRs) or lightweight decision snippets.
- **`TELEMETRY.md`** defines the unified logging philosophy and structure.

## Retention

- This directory is generally **gitignored** (except for `README.md` and specific decision records), as logs can be large and ephemeral.
- **Do not commit** sensitive tokens or massive debug dumps here if they risk being pushed.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **ISO 8601**: [Date and Time Format](https://en.wikipedia.org/wiki/ISO_8601) - Standard timestamp format (YYYY-MM-DDTHH:MM:SSZ) used in log filenames.
- **Keep a Changelog**: [Guiding Principles](https://keepachangelog.com/en/1.0.0/) - For structuring human-readable history (though automated logs differ, principles apply).

<!-- md_autofix: processed -->
