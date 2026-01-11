# Session Logs Governance

## Access Policy

- **Read**: Allowed for context restoration.
- **Write**: Allowed for session summaries.
- **Delete**: Automated pruning only.

## Structure

- Store files as `YYYY-MM-DD-session-id.md`
- Do not commit to git (should be gitignored).
