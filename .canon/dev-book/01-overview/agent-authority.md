# Agent Authority

## Purpose

Define how agents operate safely and consistently across the repository.

## Nearest gate wins

Agents MUST treat `AGENTS.md` files as hierarchical gates.

- The nearest `AGENTS.md` to the files being edited is authoritative.
- Subtree `AGENTS.md` files may add stricter rules.

## What `AGENTS.md` creates (behavior)

An `AGENTS.md` is not code generation. It creates:

- A deterministic workflow (read-before-change, decision cards, explicit approval).
- A logging contract (append-only change logs).
- A validation contract (stable tasks/validators).

## Recommended placement

- Root gate: `AGENTS.md` at repo root.
- Subtree gates: add `AGENTS.md` to any subtree that needs stricter rules (for example: `tools/`, `server/`, `infra/`).

## `.github/` structure (sample)

Use this as a reference layout. Do not copy blindly; adapt to repo needs.

```text
.github/
  agents/
    Orchestrator.agent.md
    Planner.agent.md
    Researcher.agent.md
    QA.agent.md
    LogHandler.agent.md
  instructions/
    docs.instructions.md
    tools.instructions.md
    vscode.instructions.md
  prompts/
    scan_repo.prompt.md
    validate_all.prompt.md
```

## `.cursor/` structure (sample)

```text
.cursor/
  rules/
    project.mdc
    markdown.mdc
    safety.mdc
```

## Minimal checklist for new subtrees

1. Add a subtree `AGENTS.md` if the area has unique risks.
2. Ensure validation is runnable.
3. Ensure changes are logged (append-only).

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
