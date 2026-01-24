Custom tools directory

Purpose: host sandboxed remediation tools created by agents. Tools placed here must include a `tool.spec.yml`, `tool.py` (or equivalent entrypoint), `README.md`, and tests/.

Promotion: When a tool is reviewed and promoted, it may be moved to `.toolkit/tools/` and registered in `.toolkit/registry/index.yml`.
