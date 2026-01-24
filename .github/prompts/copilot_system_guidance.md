# Copilot / VS Code system guidance (condensed)

Sourced: official VS Code and GitHub Copilot docs (fetched on run).

Key points for prompt engineering and agent design

- Use short, structured prompt files (see `planning.prompt.md`).
- Provide `custom-instructions` style snippets for project conventions; place

  these in `.github/prompts/` so Copilot/agents can apply them consistently.

- Prefer replicable templates and require structured outputs (JSON/YAML).
- Use MCP/tool integrations only when necessary; declare allowed tools per

  generated-agent manifest.

- For autonomous tasks, always include: goal, constraints, verification steps,

  and rollback instructions.

Integration notes

- The Builder-Orchestrator should reference these guidelines and include a

  short citation (URL) when generating prompts that will run in editor agents.

- When adapting to Copilot Chat or VS Code Agents, include `applyTo` or

  `custom-instructions` snippets so editor-side tooling can pick up project
  conventions.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
