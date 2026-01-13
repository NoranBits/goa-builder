# Planning prompt template

Goal: |
  <Clear, single-sentence statement of the goal>

Constraints: |
  - <List constraints: time, resources, engine-agnostic, do-not-touch-remote>

Context: |
  - Short context bullets or reference to `.docs/*` or `.canon/*` (max 200 words)

Steps: |
  1. <Step 1 — explicit action, owner: `Planner`/`Developer`/`QA`>
  2. <Step 2 — expected artifact, acceptance criteria>

AcceptanceCriteria: |
  - <List of pass conditions; tests, docs, or formats>

OutputFormat: json

Example:
```
{
  "steps": [
    {"id":1,"owner":"Developer","task":"create .github/roles/Planner.role.md","acceptance":"file exists and README references it"}
  ]
}
```
