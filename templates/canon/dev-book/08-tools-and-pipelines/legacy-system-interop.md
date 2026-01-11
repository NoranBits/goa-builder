# Legacy System Interop

## Purpose

Provide a game-project-agnostic way to “understand how it worked” in a legacy repository without assuming any specific engine or language.

This document is about process and artifacts: what to scan, what to record into `.canon/**`, and how to grow `.toolkit/**` safely.

## What counts as legacy

A “legacy system” is anything that exists before the builder kit is introduced:

- Existing CI workflows and task runners.
- Existing linting/formatting conventions.
- Existing documentation authority model.
- Existing log and telemetry sinks.

## Read-only discovery checklist

1. **Structure**

   - List top-level folders and packages.
   - Identify entry points: executables, services, apps.

2. **Build**

   - Find the build command(s) and their required environment.
   - Identify cache directories and generated outputs.

3. **Test**

   - Find the smallest fast test suite.
   - Identify slow/integration suites and how to run them selectively.

4. **Validation**

   - Identify formatting and linting tools already enforced by CI.
   - Prefer reusing existing validators instead of replacing them.

5. **Logging**

   - Identify runtime log locations (local files, cloud services, structured logs).
   - Capture sample log lines and where they’re emitted.

## Recording into `.canon/**`

- Add only facts you can verify from the repo.
- Prefer short bullets over essays.
- Link to entry points and commands.

## Extending `.toolkit/**`

- Start in `custom-tools/`.
- Compose primitives into a few high-signal workflows.
- Add explicit “write mode” flags for any tool that mutates the repo.

## When to stop

Stop and request human input when:

- Governance rules conflict.
- The legacy system’s “source of truth” disagrees with the new scaffold.
- A change would affect CI, release, or licensing.
