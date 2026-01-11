# Runtime Log: AI Trace Gate

This gate applies to files under `.logs/ai/**`.

## Policies

1. **Ephemeral**: Trace logs are not authoritative.
2. **Privacy**: Do not commit secrets/keys in trace logs.
3. **Retention**: These logs can be deleted at any time.
