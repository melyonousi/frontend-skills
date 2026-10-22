# FrontEnd

One installable agent skill that brings together nine frontend and project workflows. Invoke **`$frontend`** in Codex to load the guidance relevant to your request.

FrontEnd combines interface design, responsive layout, workspace inspection, project memory, Lighthouse audits, concise communication, and secure coding guidance. Its entry point resolves overlapping advice and keeps work scoped to the user's request.

This repository contains a self-contained snapshot of the skill. It is a community bundle, not an official OpenAI product.

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

## Install in Codex

Copy the complete `skills/frontend` folder into your Codex skills directory. Keep the bundled notices and licenses with it. These commands run from this repository's root and stop if a skill named `frontend` already exists; back up or compare that installation before replacing it.

### Windows / PowerShell

```powershell
$codexSkillRoot = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME 'skills'
} else {
    Join-Path $env:USERPROFILE '.codex\skills'
}
$frontendTarget = Join-Path $codexSkillRoot 'frontend'
if (Test-Path -LiteralPath $frontendTarget) {
    throw "An existing frontend skill was found at $frontendTarget"
}
New-Item -ItemType Directory -Path $codexSkillRoot -Force | Out-Null
Copy-Item -LiteralPath '.\skills\frontend' -Destination $frontendTarget -Recurse
```

### macOS / Linux

```sh
codex_skill_root="${CODEX_HOME:-$HOME/.codex}/skills"
frontend_target="$codex_skill_root/frontend"
if [ -e "$frontend_target" ] || [ -L "$frontend_target" ]; then
  printf '%s\n' "An existing frontend skill was found at $frontend_target"
else
  mkdir -p "$codex_skill_root" && cp -R ./skills/frontend "$frontend_target"
fi
```

Restart Codex after installation so it discovers the skill. The package also follows the `SKILL.md` directory convention for other agents, but its UI metadata and the examples here target Codex.

## Use

```text
Use $frontend to make this product page responsive while preserving the existing design.
```

```text
Use $frontend to inspect this repository and fix the mobile navigation.
```

```text
Use $frontend to audit this local page with Lighthouse and address the main issues.
```

To make FrontEnd your standing workflow, optionally add this to your own `AGENTS.md`:

```markdown
Use $frontend as the standing workflow. Apply only guidance relevant to the
current task; keep communication concise and do not expand the requested scope.
For local software projects, initialize/read project memory before substantive
work and update it only when durable context changes. Keep memory out of Git
unless explicitly requested.
```

The skill does not edit global instructions during installation. Its project-memory helper creates `<project-root>/.codex`, or `.codex/project-memory.md` when `.codex` is already a directory, without overwriting existing content. Add `.codex` to a project's `.gitignore` when you want that context to stay local.

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
  agents/openai.yaml          Codex display metadata
  scripts/                    Project-memory helper
  references/                 Nine bundled guides and supporting references
  LICENSE                     License for original FrontEnd material
  THIRD_PARTY_NOTICES.md       Source attribution and licensing scope
  licenses/                   Third-party license and notice texts
```

## Updating the bundle

Bundled references are snapshots; they do not automatically track upstream changes. Review each source update, preserve its license and notices, and update [THIRD_PARTY_NOTICES.md](skills/frontend/THIRD_PARTY_NOTICES.md) when the scope changes. Keep personal paths, secrets, project memory, and generated audit files out of commits.

For Codex's skill validation, run its installed Skill Creator validator against `skills/frontend`. The validator needs PyYAML. Check relative links and exercise the memory helper in a temporary project if you modify it.

## Publish your local repository

Create an empty GitHub repository named `frontend-skills` with your chosen visibility, then run these commands here, replacing `YOUR_USERNAME`:

```sh
git remote add origin https://github.com/YOUR_USERNAME/frontend-skills.git
git push -u origin main
```

Use an empty remote without an initial README, license, or `.gitignore` so its history starts with this local repository.

## Credits and license

Original FrontEnd routing, packaging, and local workflow material use the [MIT license](LICENSE). Bundled third-party material retains its own MIT or Apache-2.0 terms; the root license does not replace them.

Credit to [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), [wshobson/agents](https://github.com/wshobson/agents), and [openai/skills](https://github.com/openai/skills). See the [file-level attribution and license notices](skills/frontend/THIRD_PARTY_NOTICES.md).
