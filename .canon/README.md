# Cognitive Repository (.canon) overview

This repository follows an OCS-inspired cognitive layout to make agent-driven automation safe, discoverable and auditable.

- Purpose: centralize canonical artifacts (policies, navigator, roles, agent manifests, project facts) so agents avoid arbitrary scanning and follow the Dedicated Navigation Path (DNP).
- Minimal layout: `architecture/`, `specifications/`, `standards/`, `navigator/`, `policies/`, `roles/` and guidance for adding new agent manifests under `.github/agents/`.
- Usage: automated agents should read `.canon/README.md` and `.canon/project_facts.json` first, then follow listed ENTRYPOINTS and policies before performing repo-wide operations.

## .canon (Canonical Knowledge Base)

This folder is the canonical knowledge base generated/maintained by the GOA Builder (Game Operational Agents Builder).

## What belongs here

- Policies, constraints, and operating procedures.
- The dev-book (structure-first, minimal content initially).
- Role playbooks under `roles/`.
- The audit spine under `logs/`.
- The repo map under `navigator/`.
- External project digests under `external/`.

## What does not belong here

- Runtime output logs (use `.logs/` and gitignore it).
- Vendored upstream code (if any, it must be stored under a dedicated upstream area and gitignored).

<!-- md_autofix: processed -->

<!-- md_autofix: processed by tools/md_autofix.py -->
