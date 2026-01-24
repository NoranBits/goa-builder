# 12 Observability and Logs

## Telemetry Standard

This project adheres to the **Unified Log Philosophy** defined in `TELEMETRY.md` at the repository root.

**Key Invariant**: All runtime artifacts, telemetry, and session logs must settle into the `.logs/` root directory.

## Directory Structure (The "Spine")

| Directory | Domain | Definition | Retention |
| :--- | :--- | :--- | :--- |
| `.logs/ai/` | **Intelligence** | Prompts, completions, thoughts. | Ephemeral |
| `.logs/service/` | **Infrastructure** | Stdout/Stderr from daemons, DBs. | Ephemeral |
| `.logs/session/` | **Human Context** | Markdown summaries of dev sessions. | Ephemeral |
| `.logs/test/` | **QA** | Test reports (JSON), coverage. | Ephemeral |
| `.logs/client/` | **App** | Client-side logs. | Ephemeral |
| `.logs/changes/` | **Audit** | File modification history. | **Permanent** |
| `.logs/navigation/` | **Audit** | Traversal history. | **Permanent** |

## Integration

To add logging to a new component, do not create custom log folders. Configure your runner or logger to output to `.logs/<domain>/`.

See [TELEMETRY.md](../../../project-root/.logs/TELEMETRY.md) for detailed integration guidelines and multi-language examples.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
