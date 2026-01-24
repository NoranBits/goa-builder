# log

> **Context**: Helpers for structured logging, telemetry ingestion, and local log hygiene.

## Purpose

Log tools help manage the `.logs/` directory and ensure logs are readable.

## Suggested Tools

- **`normalize_logs.py`**: Convert messy stdout files to JSON-JSON-Lines.
- **`rotate_logs.sh`**: Archive old logs to save space.
- **`tail_session.sh`**: Watch the current active session log.

## Works Well With

- **`.logs/`**: The destination for all outputs.
- **`scan/`**: Scanners often generate large logs that need management.

## Custom Tools

Use `custom-tools/` for bespoke parsers (e.g., parsing a specific game engine's crash dump).

## Safety

- Do not upload logs automatically unless strictly configured.
- Ensure PII (Personal Identifiable Information) scrubbing if logs are shared.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

- **JSON Lines**: [Format](https://jsonlines.org/) - Standard for structured logging.
- **ELK Stack**: [Elastic](https://www.elastic.co/what-is/elk-stack) - Concepts of log aggregation.
- **OpenTelemetry**: [Concepts](https://opentelemetry.io/docs/concepts/) - Modern observability standards.

<!-- md_autofix: processed -->
