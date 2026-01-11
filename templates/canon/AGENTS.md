# AGENTS.md (Canon Subtree Gate)

This gate applies to files under `.canon/**`.

## Authority (nearest wins)

When multiple `AGENTS.md` files exist, the **nearest** one is authoritative.

## Read-before-change

- Read `.canon/README.md` for system entry points.
- Read `.logs/INDEX.md` for how to write append-only logs.
- Read the nearest `AGENTS.md` before editing any files.

## Logging

- Write append-only records under `.logs/**`.
- Do not rewrite history; only add new entries.
- Use `.logs/navigation/**` to record how you navigated the repo (what you checked and why).

## Safety defaults

- Prefer read-only work unless a write mode is explicit.
- Keep changes minimal and localized.

## Placeholders (adjust per repo)

- Owner team: `{{CANON_OWNER_TEAM}}`
- Validation command/task: `{{CANON_VALIDATE_TASK}}`
