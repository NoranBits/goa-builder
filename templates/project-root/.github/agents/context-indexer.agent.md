# Context Indexer — Agent Projection

Role: Build a repository-level context index for navigator consumption.

Purpose: Scan source folders and documentation to produce a structured context index (JSON) mapping topics → locations to seed the Dedicated Navigation Path.

Inputs:
- repository root filesystem
- `.canon` policy files
- `templates/` navigator hints

Outputs:
- `navigator/context-index.json` (schema: repository-map)
- `templates/canon/templates/TEMPLATE__scan-log__v1.md` entry

Install Path: `.github/agents/context-indexer.agent.md`

Example Invocation:
```
python .toolkit/scan/context_indexer.py --out navigator/context-index.json
```

Notes:
- Should be idempotent and append-only for logs.
- Use `SCHEMA__repository-map__v1.json` for validation.
