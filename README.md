# FrontEnd

One portable **Agent Skill** that brings together nine frontend and project workflows for **Codex, Claude Code, and other compatible agents**. Invoke **`$frontend`** in Codex or **`/frontend`** in Claude Code.

FrontEnd combines interface design, responsive layout, workspace inspection, project memory, Lighthouse audits, concise communication, and secure coding guidance. Its entry point resolves overlapping advice and keeps work scoped to the user's request.

This repository contains a self-contained snapshot of the skill. It is a community bundle, not an official OpenAI or Anthropic product.

## Included guidance

| Component | Purpose |
| --- | --- |
| Lighthouse | Repeatable performance, accessibility, best-practices, and SEO audits |
| Redesign Existing Projects | Improve existing interfaces while preserving their behavior |
| Minimalist UI | Restrained typography, color, and layout defaults |
| Design Taste Frontend | Visual direction for landing pages, portfolios, and marketing pages |
| Responsive Design | Fluid sizing, container queries, and layouts across screen sizes |
| Understand Workspace | Inspect the relevant code, architecture, and Git state |
| Maintain Project Memory | Preserve useful project context in a local `.codex` file |
| Caveman | Keep chat replies concise without compressing code or product copy |
| Security Best Practices | Secure defaults and requested reviews for JavaScript/TypeScript, Python, and Go |

The guides live in `skills/frontend/references/` and are loaded as needed. They do not need separate installations. A request to fix a button does not automatically trigger a redesign, a full audit, or unrelated hardening.

## Agent compatibility

FrontEnd uses the open [Agent Skills format](https://agentskills.io/specification): a `SKILL.md` entry point, supporting references, and an optional Python helper. Compatibility depends on the **agent application**, its skill loader, and its available tools, rather than the model name alone.

| Agent | Personal installation | Project installation | Explicit invocation |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/frontend/` | `<project>/.agents/skills/frontend/` | `$frontend` |
| Claude Code | `~/.claude/skills/frontend/` | `<project>/.claude/skills/frontend/` | `/frontend` |
| Other Agent Skills clients | Use the client's documented skill directory | Use the client's documented skill directory | Use its skill picker or invocation syntax |

The paths and invocation examples follow the official [Codex skills documentation](https://developers.openai.com/codex/skills) and [Claude Code skills documentation](https://code.claude.com/docs/en/skills). On Windows, `~` refers to your user profile directory.

`agents/openai.yaml` is optional Codex UI metadata. It does not make the Markdown instructions depend on OpenAI. No Claude-specific hooks, subagents, or plugin manifest are required for the direct skill-folder installation described here.

The bundle has passed local structure, link, and helper checks. The Claude Code installation instructions were checked against its documentation; the complete workflow has not been tested in a Claude Code session. Other clients may need different installation paths or tool substitutions.

## Install

Clone or download the repository. For a new clone:

```sh
git clone https://github.com/melyonousi/frontend-skills.git
cd frontend-skills
```

Copy the **complete** `skills/frontend` folder into your agent's skills directory, including references, notices, and licenses. Run the commands below from this repository's root. They stop if `frontend` already exists; compare or back up that installation before replacing it.

### Codex

Windows / PowerShell:

```powershell
$codexSkillRoot = Join-Path $env:USERPROFILE '.agents\skills'
$frontendTarget = Join-Path $codexSkillRoot 'frontend'
if (Test-Path -LiteralPath $frontendTarget) {
    throw "An existing frontend skill was found at $frontendTarget"
}
New-Item -ItemType Directory -Path $codexSkillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\frontend' -Destination $frontendTarget -Recurse
```

macOS / Linux:

```sh
codex_skill_root="$HOME/.agents/skills"
frontend_target="$codex_skill_root/frontend"
if [ -e "$frontend_target" ] || [ -L "$frontend_target" ]; then
  printf '%s\n' "An existing frontend skill was found at $frontend_target"
else
  mkdir -p "$codex_skill_root" && cp -R ./skills/frontend "$frontend_target"
fi
```

Codex detects skill changes automatically; restart it if the skill does not appear. If your existing Codex setup or skill installer already manages `frontend` in `$CODEX_HOME/skills` or `~/.codex/skills`, maintain that copy instead of adding another skill with the same name.

### Claude Code

Windows / PowerShell:

```powershell
$claudeSkillRoot = Join-Path $env:USERPROFILE '.claude\skills'
$frontendTarget = Join-Path $claudeSkillRoot 'frontend'
if (Test-Path -LiteralPath $frontendTarget) {
    throw "An existing frontend skill was found at $frontendTarget"
}
New-Item -ItemType Directory -Path $claudeSkillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\frontend' -Destination $frontendTarget -Recurse
```

macOS / Linux:

```sh
claude_skill_root="$HOME/.claude/skills"
frontend_target="$claude_skill_root/frontend"
if [ -e "$frontend_target" ] || [ -L "$frontend_target" ]; then
  printf '%s\n' "An existing frontend skill was found at $frontend_target"
else
  mkdir -p "$claude_skill_root" && cp -R ./skills/frontend "$frontend_target"
fi
```

Start Claude Code in your project and invoke `/frontend`. If it is already running and the skill does not appear, run `/reload-skills` or restart the session.

### Project-only or other agent installations

For a project-only installation, copy `skills/frontend` into the corresponding project directory from the compatibility table. A client must be able to read the bundled references and run local tools to carry out the full workflow. A plain chat model without those capabilities can use supplied instructions, but cannot perform the filesystem, browser, or audit steps by itself.

## Use

Codex:

```text
Use $frontend to make this product page responsive while preserving the existing design.
```

Claude Code:

```text
/frontend Make this product page responsive while preserving the existing design.
```

For either agent, follow up with the concrete task, such as:

```text
Inspect this repository and fix the mobile navigation.
Audit this local page with Lighthouse and address the main issues.
```

To make FrontEnd your standing workflow, optionally add this to `AGENTS.md` for Codex or `CLAUDE.md` for Claude Code:

```markdown
Use the installed FrontEnd skill as the standing workflow. Apply only guidance relevant to the
current task; keep communication concise and do not expand the requested scope.
For local software projects, initialize/read project memory before substantive
work and update it only when durable context changes. Keep memory out of Git
unless explicitly requested.
```

The skill does not edit global instructions during installation. Its project-memory helper creates `<project-root>/.codex`, or `.codex/project-memory.md` when `.codex` is already a directory, without overwriting existing content. This is an ordinary Markdown context file explicitly read by the workflow, not a dependency on the Codex application. It does not replace `AGENTS.md` or `CLAUDE.md`. Add `.codex` to a project's `.gitignore` when you want that context to stay local.

## Requirements and boundaries

- The instructions themselves require no package installation or API key.
- The project-memory helper requires Python 3.10 or newer and uses the standard library.
- Lighthouse work requires Node.js and Chrome or Chromium, plus Lighthouse when an audit is actually run.
- Design and security references are guidance; verification still depends on the project's stack and available tools.
- The security bundle covers JavaScript/TypeScript, Python, and Go. It does not include dedicated PHP/Drupal or C# guidance.
- The illustrative block-library tree in Design Taste is an example; those component assets are not included.

## Repository layout

```text
skills/frontend/
  SKILL.md                    Skill entry point and routing
  agents/openai.yaml          Optional Codex display metadata
  scripts/                    Project-memory helper
  references/                 Nine bundled guides and supporting references
  LICENSE                     License for original FrontEnd material
  THIRD_PARTY_NOTICES.md       Source attribution and licensing scope
  licenses/                   Third-party license and notice texts
```

## Updating the bundle

Bundled references are snapshots; they do not automatically track upstream changes. Review each source update, preserve its license and notices, and update [THIRD_PARTY_NOTICES.md](skills/frontend/THIRD_PARTY_NOTICES.md) when the scope changes. Keep personal paths, secrets, project memory, and generated audit files out of commits.

Validate `skills/frontend` with an Agent Skills format validator, check relative links, and exercise the memory helper in a temporary project if you modify it. Codex's installed Skill Creator validator is one option and requires PyYAML. Verify discovery and invocation in each agent before claiming runtime compatibility.

## Credits and license

Original FrontEnd routing, packaging, and local workflow material use the [MIT license](LICENSE). Bundled third-party material retains its own MIT or Apache-2.0 terms; the root license does not replace them.

Credit to [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), [wshobson/agents](https://github.com/wshobson/agents), and [openai/skills](https://github.com/openai/skills). See the [file-level attribution and license notices](skills/frontend/THIRD_PARTY_NOTICES.md).
