# .github

> **Context**: This folder acts as the interface between the Game Creator Agent System (GCAS) and the external GitHub platform. It houses both the "Cognitive Layer" (AI configuration) and the "Mechanical Layer" (CI/CD automation).

## Cognitive Layer (AI Context)

Files here dictate how AI agents perceive and interact with the repository.

- **`agents/`**: Defined personas (e.g., `RepoManager`, `Architect`) with specific capabilities and constraints.
- **`instructions/`**: Scoped directives for specific tasks or domains.
- **`prompts/`**: Reusable prompt fragments for standardizing AI outputs.
- **`copilot-instructions.md`**: Global "Constitution" for Copilot within this repo.

## Mechanical Layer (Automation)

The physical execution of tasks defined by human or AI agents.

- **`workflows/`**: GitHub Actions definitions (YAML) that run on triggers.

## External Context (For Generators)

> **Note**: These links are just examples. Upon scanning the repository and digesting the stack, this section should be updated with accurate external context matching the project.

Use these resources to understand the underlying schemas and capabilities available in this environment.

- **GitHub Actions Schema**: [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions) - For generating valid YAML workflows.
- **GitHub REST API**: [API Documentation](https://docs.github.com/en/rest) - For understanding scriptable capabilities.
- **GitHub Copilot**: [Best Practices](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot) - For optimizing agent instructions.
- **Mermaid.js**: [Diagram Syntax](https://mermaid.js.org/intro/) - For generating architectural diagrams in markdown.

## Safety & Invariants

- **Do not** modify `.github/workflows` without verifying permissions in `AGENTS.md`.
- **Do not** commit secrets; use `${{ secrets.VAR }}` substitution.
