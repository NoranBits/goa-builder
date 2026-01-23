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
