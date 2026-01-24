Logging usage for intent pipeline

Overview
- The intent pipeline produces short, redacted snippets of user intent and writes them to `.logs/ingestion/`.
- This document explains how to generate entries (manual and automated), how to consume them, and how agents should react.

How to generate
- Automated (recommended): use `.toolkit/agents/intent_pipeline.py --user <name> --message "..."`.
- Manual: create an NDJSON line in `.logs/ingestion/user-intents.ndjson` using the schema below, then add a markdown note `YYYYMMDDTHHMMSSZ-intent.md`.

NDJSON schema (required fields)
- `ts` — ISO8601 UTC timestamp (string)
- `task_id` — MM.SS.TT identifier when applicable (string)
- `user_hash` — short hash of the user (string)
- `snippet` — short, non-specific summary (string)

Agent behavior
- Agents must not load raw markdown notes into working prompt context; they may read `snippet` values only.
- If an agent intends to act on a snippet, it must: (1) create a plan with a new MM.SS.TT id, (2) append a decision log under `.logs/decisions/`, and (3) proceed through the normal remediation workflow (tools, validation, CI).

Retention and corrections
- Do not edit existing NDJSON lines. To correct a mis-logged intent, append a new NDJSON entry referencing the correction and include `correction_of` with the original `change_id`.

Examples
- Minimal NDJSON line:

  {"ts":"2026-01-24T12:00:00Z","task_id":"00.01.01","user_hash":"a1b2c3d4","snippet":"Fix CI config and lint errors"}

Consumption examples
- Python: `json.loads` line-by-line and aggregate by `task_id`.

Policy
- All generated files and notes must be in English.
