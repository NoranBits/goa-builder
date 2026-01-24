# Policy: Task Identification & Numbering Standards

## 1. Objective
To ensure all agent plans, logs, commit messages, and QA reports utilize a unified, sortable, and machine-parsable identifier system.

## 2. Standard Syntax: MM.SS.TT
All task identifiers must follow the Hierarchical Dot Notation with Zero-Padding.

Format: `MM.SS.TT`
- `MM` (Milestone): High-level deliverable or phase (00-99).
- `SS` (Step): Distinct workflow stage within the milestone (00-99).
- `TT` (Task): Atomic action or execution unit (00-99).

Example:
- `01.02.03` (Correct)
- `1.2.3` (Incorrect)

## 3. Rules of Usage

### 3.1. Stability
- IDs are permanent. Once an ID is assigned, it must not be reused or renumbered.
- Insertion: Use additional task numbers rather than renumbering existing IDs.

### 3.2. Sorting & Scope
- Zero-padding allows lexicographical sort to match intended order.
- Wildcards allowed for scope e.g., `01.02.*`.

### 3.3. Implementation in Artifacts
- Plan files: every roadmap item must have an ID.
- Logs: every entry in `.logs/` must reference the active Task ID.
- Commits: The Git Assistant must prefix commit messages with the Task ID (e.g., `[01.04.02] Add validation logic`).

## 4. Automation Contract
Plans should be parseable as structured data (YAML/JSON) where possible.

YAML example:

```yaml
id: "01.02.03"
title: "Implement User Login"
owner: "Developer"
status: "todo"
depends_on: ["01.02.02"]
```

## 5. Governance
- The CSO (Contextual Systems Orchestrator) enforces this policy. Validators under `.toolkit/` must include regex checks to ensure compliance.

## 6. Phase 00 Initialization
- Current phase: `00.01.00` (Initialization). All initial plans must use MM.SS.TT IDs starting with `00`.
# POLICY: Step ID and Task Numbering

**Location:** .canon/policies/POLICY__step-id-and-task-numbering.md
**Status:** Draft (seeded by CSO agent)
**Owner:** CSO

## 1. Core Convention

All plans, logs, and agent handoffs must use the Hierarchical Dot Notation with zero-padding.
**Format:** `MM.SS.TT`

- **MM (Milestone):** High-level deliverable (01-99).
- **SS (Step):** Workflow stage or logical grouping (01-99).
- **TT (Task):** Atomic executable action (01-99).

## 2. Rules

1. **Zero-Padding:** Use two digits (`01`, not `1`).
2. **Stability:** Once assigned and logged, IDs must not change. Use inserted sub-tasks `MM.SS.TT` as needed.
3. **Usage:** Reference IDs in plan files, commit messages, and logs.

## 3. Automation Contract

For machine-readable files, use an `id` field as the primary key and ensure it follows `MM.SS.TT`.

---
Seeded by builder-orchestrator on 2026-01-24.

<!-- md_autofix: processed -->
