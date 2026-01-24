# Game Creator Agent System (The Builder Kit)

> **The Builder** is the bootstrapping mechanism that manifests the **GameOps Agents (GOA)** within your repository. It implants a team of specialized AI agents, memory structures, and governance protocols to automate game development.

**License**: [MPL-2.0](LICENSE)

---

## 🧠 What is the GOA?

The **Game Operational Agents (GOA)** is an context framework that embeds a team of specialized AI agents and memory structures into a game development project. It aims to automate and optimize all aspects of game development – from coding and testing to documentation and maintenance – while collaborating with human developers.

### Purpose and Goals

The primary goal of the system is to act as an autonomous project co-developer.

* **Automate Development Tasks**: Delegates labor-intensive tasks (coding, reviewing, testing) to AI agents, allowing humans to focus on creative decisions.
* **Goal-Driven Collaboration**: Works towards high-level goals specified by the user throughout the lifecycle.
* **Project-Agnostic Integration**: The Builder is repo-agnostic. It can be copied into any game project to adapt and learn the local structure.
* **Perfection through Iteration**: Strives for high-quality code and up-to-date documentation by continually refining its knowledge of the project.

---

## 🏗️ Architecture Overview

The system architecture is modular – defined as an "octopus" that grasps every aspect of the repository through dedicated agents and tools.

### 1. Multi-Agent Team

A collection of AI agents working under a defined hierarchy (Orchestrator, Planner, Developer, etc.).

### 2. Governance & Knowledge Base (`.canon/`)

The **Single Source of Truth**. A directory containing design docs, specs, and agent guidelines (`AGENTS.md`) that ensure all agents share the same context and abide by the same rules.

### 3. Observability (`.logs/`)

A unified telemetry spine that captures agent outputs, decisions, and metrics. This ensures transparency and allows for auditing the "thought process" of the system.

### 4. Automation Toolkit (`.toolkit/`)

A suite of scripts (build, test, scan) that agents can invoke to interact with the codebase and environment in a consistent way.

---

## 🤖 Multi-Agent Roles

The system mimics a well-functioning development team with specialized roles:

| Role | Responsibility |
| :--- | :--- |
| **Orchestrator** | **Project Manager**. Coordinates the multi-step build process, enforces stage gates, and ensures quality checks pass. |
| **Planner** | **Architect**. Turns user requirements into ordered action plans and questionnaires. Analyzes the project state. |
| **Researcher** | **Analyst**. Read-only agent that gathers facts, scans codebase structure, and summarizes context without altering files. |
| **Developer** | **Builder**. Executes the plan by writing code, refactoring, and updating documentation alongside the Orchestrator. |
| **QA** | **Quality Assurance**. Validates artifacts, runs tests, performs static analysis, and flags discrepancies. |
| **Log Handler** | **Auditor**. Maintains the audit trail (`.logs`) and ensures validation tools run properly. |
| **Git Assistant** | **Version Control**. Manages branches, creates clean commits/PRs, and ensures history remains reviewable. |
| **Maintainer** | **Gardener**. Keeps the repo healthy (dependencies, linters, structure) and prevents entropy over time. |

---

## ⚖️ Orchestration & Governance

Having multiple agents requires strong coordination to prevent chaos (the "telephone game").

* **Context Management**: All agents access a shared knowledge base (`.canon`) and logs (`.logs`). If the Planner decides on an architecture, that decision is recorded and visible to the Developer and QA agents.
* **Read-Only Safety**: Agents like the **Researcher** operate in a read-only capacity to gather information without risk of unintended modification.
* **Sequential Pipeline**: The Orchestrator sequences activities (Plan -> Research -> Build -> QA) to avoid parallel conflicts.
* **Policy Enforcement**: `AGENTS.md` files act as operational gates, defining authority and permissions at every directory level.

---

## 🛠️ Usage (The Builder)

This repository contains **The Builder** – the tool that installs the system.

### Installation

1. **Embed**: Copy this `.builder/` folder into your project root.

    ```bash
    cp -r /path/to/root .builder
    ```

1. **Manifest**: Run the generation script to implant the system (Agents, Canon, Toolkit) into your repo.

    ```bash
    python3 .builder/builder.py generate
    ```

1. **Validate**: Verify the system integrity.

    ```bash
    python3 .builder/builder.py validate-kit
    ```

### Activation & Safety

The Builder-Orchestrator and the internal `.builder` payload include
    non-repo-agnostic tools and instruction files. To prevent accidental
    modifications in a target repository, explicit human activation is required
    before running any Builder operations that change repository structure or
    canonical docs.

Enable the Builder for non-agnostic operations by either:

    - creating a marker file in the project root: `.builder/ALLOW_AUTOINVOKE`, or
    - setting the environment variable: `GOA_BUILDER_ACTIVATE=1`.

    Scripts and agents should verify activation before performing non-agnostic
    work by running:

    ```bash
    python3 tools/require_activation.py || { echo "Enable builder first"; exit 1; }
    ```

    Example (human-approved flow):

    ```bash
    # human confirms
    touch .builder/ALLOW_AUTOINVOKE
    # validate activation then run consolidation
    python3 tools/require_activation.py && python3 .builder/tools/consolidate_memory.py .
    ```

    This ensures generated agents and automated flows do not automatically invoke
    the Builder-Orchestrator without explicit operator consent.

### Directory Layout

The following shows the layout of this Builder kit (what lives inside the `.builder` folder) and the primary artifacts it generates when installed into a project.

Kit (this repository) — `.builder/`

```text
.builder/                  # Builder kit: installer, templates, tools, and specs
├── builder.py             # CLI / entrypoint used to generate and validate the kit
├── templates/             # Templates used to scaffold a project (canon, vscode, project-root, etc.)
│   ├── project-root/      # Templates that are copied into a target project's root
│   │   └── .logs/         # Template for telemetry, decisions, sessions, etc.
│   ├── canon/             # Canon templates (AGENTS.md, dev-book, roles, external sources)
│   └── vscode/            # VS Code workspace templates (extensions, tasks)
├── scripts/               # Helper scripts (installers, packaging helpers)
│   └── install-builder.sh
├── tools/                 # Local developer tools used by the kit (linting, validation)
├── spec/                  # Specs and validation rules (structure, generate policy)
├── docs/                  # Kit documentation and guidance
└── RELEASE_NOTES.md
```

Generated into a target repo (what the Builder creates)

```text
/.canon/                   # Generated: single source of truth (AGENTS.md, docs, roles)
.logs/                     # Generated: telemetry, session memory, decisions, changes, tests
.toolkit/                  # Generated: agent-invokable scripts and custom tools
AGENTS.md                  # Top-level governance and policy produced by the kit
```

Notes:

- The authoritative telemetry guidance for generated projects is provided in `templates/project-root/.logs/TELEMETRY.md`.
- `.gitignore` in this kit already recommends ignoring runtime `.logs/` in projects; tracked template `.logs/` content (the guidance files) remains in `templates/` so they are installed into generated projects.

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
