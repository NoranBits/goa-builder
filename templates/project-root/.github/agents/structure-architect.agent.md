# Structure Architect — Agent Projection

Role: Build and maintain the Dedicated Navigation Path (DNP) and navigator pages.

Purpose: Generate human-friendly navigator pages (Markdown) from `navigator/context-index.json` and canonical templates; ensure `.canon` and `AGENTS.md` invariants are present.

Inputs:
- `navigator/context-index.json`
- `.canon/policies/*`
- `templates/canon/templates/*`

Outputs:
- `NAVIGATOR.md` and directory-level index pages
- `navigator/manifest.json`
- `templates/canon/templates/TEMPLATE__scan-log__v1.md` entries

Install Path: `.github/agents/structure-architect.agent.md`

Example Invocation:
```
python .toolkit/scan/build_navigator.py --index navigator/context-index.json --out NAVIGATOR.md
```

Notes:
- Respect `POLICY__dedicated-navigation-path__v1.md` rules when creating links.
- Emit `severity: error` entries for missing required index items.
