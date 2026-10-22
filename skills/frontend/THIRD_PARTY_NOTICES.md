# Sources and third-party notices

FrontEnd combines original routing and local workflow material with bundled third-party instructions. Each third-party work retains its copyright and license. Including it here does not imply endorsement by its authors.

The public bundle was prepared on 2026-10-22 from the installed FrontEnd snapshot. Its existing provenance records the guide collection on 2026-10-07. Exact upstream commit identifiers were not retained for that installation; this package does not claim to be a checkout of the latest upstream versions. Source repository links identify attribution, not a verified byte-for-byte release tag.

## Third-party material

Paths below are relative to this skill directory.

| Bundled files | Source | License text |
| --- | --- | --- |
| `references/design-taste-frontend.md`, `references/minimalist-ui.md`, `references/redesign-existing-projects.md` | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill), Copyright (c) 2026 Leonxlnx | [MIT](licenses/Leonxlnx-taste-skill.txt) |
| `references/caveman.md` | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman), Copyright (c) 2026 Julius Brussee | [Historical MIT text](licenses/JuliusBrussee-caveman-MIT.txt), [current Apache-2.0 text](licenses/JuliusBrussee-caveman.txt), [upstream NOTICE](licenses/JuliusBrussee-caveman-NOTICE.txt); see version scope below |
| `references/responsive-design/guide.md` and `references/responsive-design/references/*` | [wshobson/agents](https://github.com/wshobson/agents), `plugins/ui-design/skills/responsive-design`, Copyright (c) 2024 Seth Hobson | [MIT](licenses/wshobson-agents.txt) |
| `references/security-best-practices/SKILL.md` and `references/security-best-practices/references/*` | [openai/skills](https://github.com/openai/skills/tree/main/skills/.curated/security-best-practices), `skills/.curated/security-best-practices` | [Apache-2.0](licenses/openai-skills.txt) |

The bundled reference contents were preserved from the local snapshot during public packaging. Some source entry points had already been relocated or renamed when assembled into FrontEnd; for example, the Responsive Design entry point is `guide.md`. The FrontEnd entry point documents how to resolve bundled helper paths and which illustrative resources are not shipped.

License texts for Taste Skill, Caveman, and Agents, and Caveman's root NOTICE, were obtained from their source repositories on 2026-10-22. The Security Best Practices license was retained from its installed source skill. Preserve these notices when redistributing or installing the bundled material. When changing third-party references, identify the modifications and continue to preserve applicable upstream notices.

Caveman's [licensing guide](https://github.com/JuliusBrussee/caveman/blob/main/LICENSING.md) states that its skill was MIT before version 3.0.0 and Apache-2.0 from 3.0.0 onward; earlier releases retain their original terms. The exact version of the installed text snapshot is unavailable, so both published license texts and the upstream copyright notice are retained. This does not relicense an earlier snapshot. Only the skill instructions are bundled here: the runtime, fonts, browser, CLI, and other products described in the unmodified upstream NOTICE are not included.

## Original FrontEnd material

The FrontEnd entry point, Codex UI metadata, project-memory helper, Lighthouse guide, Understand Workspace guide, Maintain Project Memory guide, and repository packaging are local workflow material supplied with this bundle. They use the [FrontEnd MIT license](LICENSE).

For public packaging, the entry point was made independent of the original user's personal setup: applying the skill on every request is an opt-in configuration, source attribution is explicit, and machine-local memory is excluded. The entry point also explains invocation and tool adaptation for Codex, Claude Code, and other Agent Skills clients. The bundled reference instructions remain subject to the entry point's scope and conflict-resolution rules.
