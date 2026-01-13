# Validation prompt template

Target: |
  <Files, tests, or commands to run>

Commands: |
  - <shell command to run, e.g. `pytest -q`>

Checks: |
  - Lint
  - Tests
  - Build

OutputFormat: json

Example:
```
{
  "results": {"lint": "passed","tests": {"passed": 24, "failed": 0}},
  "logs": "<link or short excerpt>"
}
```
