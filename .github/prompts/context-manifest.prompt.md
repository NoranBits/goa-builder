# Context Manifest prompt

Purpose: Build a minimal list of files that the agent must read to complete a
single task. This enforces token efficiency and prevents scanning the repository.

Input:

- `goal`: short text
- `scope`: file paths or areas to consider (optional)

Output (JSON):
```text
{
  "manifest": [".canon/spec-A.md","templates/AGENTS.md","src/module/foo.py"],
  "justification": "These files define the API, agents, and code points"
}
```text

Instructions:

- Scan `.logs/decisions/` for any recent entries that affect the goal.
- List only the minimal files required (max 10).
- If unresolved conflicts are found, include both paths and set
  `requires_user_confirmation=true`.

<!-- md_autofix: processed -->
