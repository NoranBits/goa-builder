# log

## Purpose

Log tools collect, normalize, and analyze runtime logs.

## Conventions

- Write runtime logs under `.logs/`.
- Keep tracked audit logs under `.logs/**`.

## Suggested tools

- `collect_logs.py`: gather logs for a run into a timestamped folder.
- `summarize_logs.py`: produce a concise error summary.
- `redact_logs.py`: remove secrets and personal data.

## Works well with

- `test/`: bundle failing test output and artifacts.
- `validate/`: gather validation output into a single digest.
- `search/`: map stack traces and errors back to code.

## Custom tools

Use `custom-tools/` for targeted log analyzers.

## Safety

Log tools should be read-only by default.
