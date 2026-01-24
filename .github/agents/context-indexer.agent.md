# Context Indexer — Agent Manifest

Role: Create and maintain content indices (semantic + syntactic) for fast retrieval by other agents.

Responsibilities

- Index `.canon/`, `README.md`, `docs/`, and other canonical content listed in `.canon/navigator/ENTRYPOINTS.md`.
- Emit machine-readable indices to `.logs/index/` and append navigation logs.

Authority and boundaries

- Read-only across repo by default; writes only to `.logs/` and `.canon/00_Index/`.
- Must not alter source files.

Inputs: `.canon/` and files under ENTRYPOINTS.
Outputs: index files, index manifests, and index metadata in `.logs/index/`.
---
name: context-indexer
description: Builds and refreshes the deterministic repository navigation surfaces.
tools: [read_file, list_files, run_task]
---

## Mission

Maintain an accurate, bounded navigation surface for the repo.

## DNP

Follow root AGENTS.md and POLICY__dedicated-navigation-path__v1.md.

## Allowed actions

- Run `.toolkit/scan/refresh_navigator.*`
- Write only to: `.canon/navigator/**` and `.logs/navigation/**`

## Output

- Update `.canon/navigator/README.md` and folder READMEs.
- Write an append-only log entry under `.logs/navigation/`.
- If emitting a structured report, use `SCHEMA__repository-map__v1.json`.

<!-- md_autofix: processed -->
