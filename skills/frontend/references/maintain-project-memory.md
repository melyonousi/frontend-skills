---
name: maintain-project-memory
description: Create, read, and maintain the `.codex` project-context file at the active project root, with `.codex/project-memory.md` as a compatibility fallback when `.codex` is already a directory. Use at the start and end of every project-related request that reads, changes, diagnoses, plans, or reviews a local codebase; use whenever durable facts, decisions, conventions, progress, verification results, or unresolved issues should persist across Codex tasks. Skip casual conversation and requests with no project context.
---

# Maintain Project Memory

Keep a trustworthy project context and handoff file that survives across Codex tasks without becoming a transcript.

## Workflow

1. Resolve the active project root. Prefer the Git top level. Otherwise use the nearest directory containing a recognized project marker, then the current workspace root. Never choose the filesystem root or the user's home directory.
2. Run `scripts/ensure_project_memory.py --root <project-root>` with an available Python runtime. The script prints the exact target path:
   - Prefer `<project-root>/.codex` when it is absent or already a file.
   - Use `<project-root>/.codex/project-memory.md` when `.codex` is already a directory.
3. Read the printed target before substantive project work. When it is an existing detailed instruction file, read it as a whole and follow its project-specific routing to other required files.
4. Treat repository instructions, source code, configuration, and fresh command output as authoritative. Treat the memory as a secondary handoff. Correct stale entries when evidence disagrees.
5. Before the final response, update the memory only if the request produced material, reusable project context.

## What to Record

Record concise facts that will improve a later task:

- Project purpose, architecture, important entry points, and stable stack details.
- Commands that were actually confirmed for setup, development, build, lint, test, or deployment.
- User-approved decisions, project conventions, constraints, and project-specific preferences.
- The current goal, completed work, next useful step, and durable blockers.
- Verification performed and its result, including important failures that remain unresolved.
- Known issues whose impact extends beyond the current turn.

Do not record:

- Secrets, tokens, passwords, credentials, private keys, or sensitive personal data.
- Raw logs, large diffs, chat transcripts, or information already obvious from a single nearby file.
- Temporary debugging observations, abandoned hypotheses, or speculation presented as fact.
- Routine no-op requests that produce no durable information.

## Editing Rules

- Patch the existing file minimally. Preserve its structure, user-authored notes, requirements, and unknown sections. Never replace a mature `.codex` file with the starter template.
- Put new facts in the most relevant existing section. If no suitable mutable section exists, add or update a concise `Current handoff` section.
- Maintain canonical current state instead of appending a diary. Replace stale entries and remove resolved blockers.
- Keep newly created files concise. Existing authoritative files may be longer when their project rules require it.
- If the file uses a dated handoff or recent-changes section, keep it bounded and add an ISO date only for an actual material change.
- Use `Unknown` rather than inventing information. Delete placeholder bullets once real information exists.
- Never stage or commit the memory file unless the user explicitly requests it.
- Do not interrupt the user merely to update memory. If the target cannot be written, continue the main task when safe and mention the issue only if it affects continuity.

## Completion Check

Before responding, verify that the memory reflects the final state, not the plan from the start of the request. A failed or partially completed task may still require an update to `Current state`, `Verification`, or `Known issues`.
