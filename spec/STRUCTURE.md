# Builder Kit Structure

This document describes the **required directory layout** of the `.builder/` starter kit and the **generated outputs**.

## Kit layout (`.builder/`)

```text
.builder/
  README.md
  builder.py
  context/
    session_summary.md
  spec/
    REQUIREMENTS.md
    STRUCTURE.md
    GENERATE_POLICY.md
    VALIDATION.md
  templates/
    project-root/
      AGENTS.md
      README.md
      markdown.md
      .markdownlint-cli2.cjs
      .markdownlint.json
      .github/
        README.md
        agents/README.md
        chatmodes/README.md
        instructions/README.md
        prompts/README.md
      .vscode/README.md
      .toolkit/README.md
    vscode/
      tasks.json
      README.md
      AGENTS.md
    canon/
      README.md
      AGENTS.md
      logs/
        INDEX.md
        AGENTS.md
        changes/
          README.md
        decisions/
          README.md
        ingestion/
          README.md
        navigation/
          README.md
          INDEX.md
          sessions/
            README.md
      roles/
        Orchestrator.role.md
        Researcher.role.md
        Planner.role.md
        QA.role.md
        LogHandler.role.md
        GitAssistant.role.md
        Maintainer.role.md
      dev-book/
        README.md
        AGENTS.md
        01-overview/README.md
        ...
        15-appendix/README.md
      navigator/
        README.md
        AGENTS.md
      external/
        README.md
        external_source.template.md
        linktree.template.md
    toolkit/
      README.md
      AGENTS.md
      scan/
        README.md
        custom-tools/README.md
      search/
        README.md
        custom-tools/README.md
      validate/
        README.md
        custom-tools/README.md
      test/
        README.md
        custom-tools/README.md
      log/
        README.md
        custom-tools/README.md
      build/
        README.md
        custom-tools/README.md
      install/
        README.md
        custom-tools/README.md
      package/
        README.md
        custom-tools/README.md
      update/
        README.md
        custom-tools/README.md
  tools/
    run_markdownlint.py
    validate_kit.py
```text

## Generated outputs (target repo)

The kit generates the following into the target repo root:

- `markdown.md`
- `.markdownlint-cli2.cjs`
- `.markdownlint.json`
- `.vscode/tasks.json` (created or patched)
- `.canon/**`
- `.toolkit/**`

If `.git/` exists, it also ensures:

- `.gitignore` contains `.logs/`

<!-- md_autofix: processed -->
