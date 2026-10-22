---
name: understand-workspace
description: Build a working mental map of a repository or workspace before acting. Use when the user asks Codex to understand, inspect, onboard to, summarize, or get the whole idea of a workspace, including files, folders, projects, Git branches, Git status, history, architecture, or context needed for follow-up coding requests.
---

# Understand Workspace

## Purpose

Orient in the workspace before making changes. Prefer direct evidence from files, project manifests, and Git over assumptions. Keep the scan bounded enough to stay useful, but broad enough to avoid missing the project shape.

## Workflow

1. Establish the workspace boundary.
   - Confirm the current directory and Git root.
   - Check whether the workspace is a single project, monorepo, nested Git repo, or non-Git folder.
   - Note sandbox, network, and approval constraints from the active environment context.

2. Inspect Git state before reading deeply.
   - Run `git status --short --branch`.
   - Identify the current branch, upstream, remotes, and worktrees when available.
   - Review recent history with a bounded log such as `git log --oneline --decorate -n 20` and, when useful, `git log --stat -n 5`.
   - Inspect uncommitted change scope with `git diff --stat`, `git diff --name-only`, and `git diff --cached --stat`.
   - Treat dirty files as user or generated work unless proven otherwise. Do not revert unrelated changes.

3. Map the file and project layout.
   - Use `rg --files` first for file discovery. Exclude obvious generated or dependency folders such as `node_modules`, `.next`, `dist`, `build`, `coverage`, `.git`, `.venv`, and `vendor`.
   - Read top-level directory names and project-defining files: `README*`, `package.json`, lockfiles, `turbo.json`, `nx.json`, `pyproject.toml`, `requirements*.txt`, `Cargo.toml`, `go.mod`, `.sln`, `Dockerfile`, `compose*.yml`, `.github/workflows/*`, `.openai/hosting.json`, and similar local equivalents.
   - In monorepos, identify apps, packages, shared libraries, tooling packages, and boundaries between them.

4. Learn the runtime and architecture.
   - Read manifests and scripts to identify package manager, build commands, test commands, lint commands, framework, language versions, and deployment targets.
   - Inspect routing, entrypoints, API handlers, data access, auth/session code, state management, shared UI components, configuration, and environment examples.
   - For user-facing apps, note the primary screens and paths. For backend projects, note service boundaries, request entrypoints, jobs, queues, storage, and external integrations.

5. Focus on the next request.
   - Search for terms from the user's request after the broad map is clear.
   - Prefer targeted reads around likely ownership boundaries instead of opening large files wholesale.
   - Use parallel tool calls for independent reads and searches.

6. Build and carry forward a compact working model.
   - Know the stack, package manager, main projects, important folders, current Git branch/state, recent history themes, likely commands, and areas relevant to the task.
   - Track uncertainties explicitly. Resolve them with local evidence when cheap; otherwise mention them before relying on them.
   - Share a concise orientation summary before editing when the scan reveals meaningful risks, ambiguous ownership, or broad architecture context the user should know.

## Command Patterns

Prefer PowerShell-friendly commands in this environment:

```powershell
Get-Location
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git worktree list
git branch --all --verbose --no-abbrev
git log --oneline --decorate -n 20
git log --stat -n 5
git diff --stat
git diff --cached --stat
rg --files -g "!node_modules/**" -g "!.next/**" -g "!dist/**" -g "!build/**" -g "!coverage/**" -g "!.git/**"
```

Use these as patterns, not a mandatory script. Skip commands that do not apply, and add targeted searches based on the repository's language and the user's request.

## Boundaries

- Do not run installs, migrations, destructive Git commands, or network-dependent workflows during orientation unless the user specifically asks.
- Do not open secrets or private key material. For `.env*` files, usually note existence and read only safe examples such as `.env.example`.
- Do not produce a long inventory dump. The goal is a useful mental model, not a file listing.
- If the workspace is very large, sample top-level structure, project manifests, and recent Git context first, then narrow based on the task.
