<!-- Navigation / Scan Log template (TEMPLATE__scan-log__v1.md) -->
# Navigation Scan Log — Template v1

Generated At: {{generated_at}}

Repository: {{repo}}

Navigator Version: {{navigator_version}}

Summary: |
  Brief human summary of the scan results.

Entries:

- timestamp: "2026-01-17T00:00:00Z"
  path: "path/to/file/or/folder"
  source: "scanner-name or tool"
  summary: "One-line summary of finding"
  severity: "info|warn|error"
  tags: ["navigation","docs","policy"]
  evidence:
    - "short evidence line 1"
    - "short evidence line 2"

Example JSON payload:

```json
{
  "generated_at": "2026-01-17T00:00:00Z",
  "repo": "owner/repo",
  "navigator_version": "v1",
  "summary": "Found 3 navigation issues, 1 critical",
  "entries": [
    {
      "timestamp": "2026-01-17T00:00:00Z",
      "path": "src/handlers/main.py",
      "source": "context-indexer",
      "summary": "Missing entry in navigator for module handlers",
      "severity": "warn",
      "tags": ["navigation","missing-index"],
      "evidence": ["no README in handlers/", "no navigator link to handlers/"]
    }
  ]
}
```

Notes:
- Keep entries short and link to the source file/path.
- Use `severity: error` for policy-blocking issues that should fail CI.
- This template is intended to be both human-readable and easily converted to JSON for schema validation.
