# AGENTS

This repository uses the GOA builder governance model. Agents must follow the Dedicated Navigation Path (DNP) and respect the procedural, semantic and episodic memory separation defined in .canon/ and .logs/.

## Dedicated Navigation Path (DNP)

Purpose: Prevent uncontrolled repo-wide searching and stabilize agent behavior in sessions.

### The only allowed navigation order (read in sequence)
1) `AGENTS.md` (this file)
2) `.canon/navigator/README.md` (repo map index)
3) `.canon/navigator/ENTRYPOINTS.md` (what files to open first per subsystem)
4) `.canon/policies/POLICY__dedicated-navigation-path__v1.md` (the rules)
5) `.canon/modules/engine/` (engine-specific rules, if the task touches engine code)
6) `.canon/policies/` and `.canon/roles/` (if role/policy constraints are relevant)

### Scanning rule (hard stop)
Agents must NOT scan the repository arbitrarily.

The only permitted scan action is running the repo-approved script:
- `.toolkit/scan/refresh_navigator.*`

Any other scanning must be treated as out-of-policy and stopped.

### Logging rule
Any navigation or scan must be logged (append-only) in:
- `.logs/navigation/`

### Acceptance
- Agents must read this file first and follow DNP before taking actions that read or write repository files.
