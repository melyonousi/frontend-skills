#!/usr/bin/env python3
"""Create a project .codex context file without modifying existing content."""

from __future__ import annotations

import argparse
import subprocess
from datetime import date
from pathlib import Path


PROJECT_MARKERS = (
    ".git",
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    "go.mod",
    "composer.json",
    "Gemfile",
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",
    ".sln",
)


def git_root(start: Path) -> Path | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(start), "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None

    value = result.stdout.strip()
    return Path(value).resolve() if value else None


def has_project_marker(directory: Path) -> bool:
    for marker in PROJECT_MARKERS:
        if marker == ".sln":
            if any(directory.glob("*.sln")):
                return True
        elif (directory / marker).exists():
            return True
    return False


def resolve_project_root(explicit_root: str | None) -> Path:
    start = Path(explicit_root).expanduser().resolve() if explicit_root else Path.cwd().resolve()
    if not start.is_dir():
        raise SystemExit(f"Project root is not a directory: {start}")

    root = start if explicit_root else git_root(start)
    if root is None:
        root = next((candidate for candidate in (start, *start.parents) if has_project_marker(candidate)), start)

    home = Path.home().resolve()
    if root == home or root == Path(root.anchor):
        raise SystemExit(f"Refusing unsafe project root: {root}")
    return root


def template(project_name: str) -> str:
    today = date.today().isoformat()
    return f"""# {project_name} — project context for coding agents

Read this file before substantive project work. Keep durable facts current after material changes.
Never store secrets, raw transcripts, or unverified claims here.

Last updated: {today}

## Project snapshot

- Purpose: Unknown
- Stack: Unknown
- Important entry points: Unknown

## Working rules

- Treat current code, configuration, and fresh command output as authoritative.
- Never claim a build or test passed unless it was actually executed.

## Architecture

- None recorded.

## Confirmed commands

- None recorded.

## Durable decisions and conventions

- None recorded.

## Current handoff

- Active goal: Unknown
- Completed: None recorded.
- Next: Unknown

## Verification

- None recorded.

## Known issues

- None recorded.

"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", help="Explicit project root; otherwise detect from the current directory")
    args = parser.parse_args()

    root = resolve_project_root(args.root)
    codex_path = root / ".codex"
    target = codex_path / "project-memory.md" if codex_path.is_dir() else codex_path

    if target.exists():
        print(f"EXISTS {target}")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(template(root.name), encoding="utf-8", newline="\n")
    print(f"CREATED {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
