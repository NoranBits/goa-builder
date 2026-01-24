# Conftest policy scan — top 3 failures

1. Rule: `unknown` — Path: `unknown`

- Message: {"file": ".github/agents/bad_agent_disallowed_tool.agent.md", "frontmatter": {"name": "bad-agent", "description": "Requests disallowed tool", "tools": "['web','read']"}}

1. Rule: `unknown` — Path: `unknown`

- Message: {"file": ".github/agents/bad_agent_missing_name.agent.md", "frontmatter": {"description": "Missing name frontmatter", "tools": "['read','execute']"}}

1. Rule: `unknown` — Path: `unknown`

- Message: {"file": ".github/agents/good_agent.agent.md", "frontmatter": {"name": "good-agent", "description": "Well-formed agent", "tools": "['read','execute']"}}

<!-- md_autofix: processed -->
