---
name: frontend
description: "Combined frontend workflow for inspecting a local project, building or improving responsive web interfaces with secure defaults, preserving project context, and verifying page quality with Lighthouse. Combines design, responsive layout, project memory, concise communication, and security-best-practices. Use when FrontEnd is requested or relevant frontend work calls for this workflow."
license: "Original FrontEnd material: MIT. Bundled references: MIT or Apache-2.0; see THIRD_PARTY_NOTICES.md."
---

# FrontEnd

One entry point for nine bundled workflows, including security-best-practices. Invoke as `$frontend` in Codex, `/frontend` in Claude Code, or through another Agent Skills client's supported invocation method.

When this skill is selected, apply only the guidance relevant to the actual task. Keep communication concise; workspace inspection, visual changes, and audits depend on task scope. Using FrontEnd as a standing workflow for every request is an optional user configuration. A preference-setting request does not itself start a redesign or audit.

## Agent portability

The workflow uses standard Markdown instructions and relative bundled resources. `agents/openai.yaml` is optional Codex UI metadata; the workflow does not require it. Use the host agent's available file, shell, browser, and validation tools, and adapt shell examples to the active environment. Do not assume a tool exists because a reference names it.

Product names or standalone slash commands in the source snapshots describe their original context. Read those references as guidance for the current agent, not as commands to launch another product or install another skill. Follow the project's host instructions, such as `AGENTS.md` or `CLAUDE.md`, where applicable.

## Load the relevant guidance

The complete source instructions are bundled below. Read relevant references before using their workflow, and reuse references already read in the current context. They are supporting documents, not separate skills that must be installed or invoked.

| Situation | Bundled guidance |
| --- | --- |
| Concise communication while using this workflow | [caveman](references/caveman.md) |
| Any work involving a local software project | [maintain-project-memory](references/maintain-project-memory.md), then [understand-workspace](references/understand-workspace.md) |
| Building or editing a web interface | [minimalist-ui](references/minimalist-ui.md) |
| Responsive layouts, fluid typography, container queries, adaptive navigation, images, or tables | [responsive-design](references/responsive-design/guide.md); follow its links for detailed patterns |
| Improving an existing interface | [redesign-existing-projects](references/redesign-existing-projects.md) |
| Landing pages, portfolios, marketing pages, and their redesigns | [design-taste-frontend](references/design-taste-frontend.md) |
| Page audits, frontend performance/accessibility/SEO work, or final page-quality verification | [lighthouse](references/lighthouse.md) |
| Secure defaults while writing supported code; requested security reviews or hardening | [security-best-practices](references/security-best-practices/SKILL.md), then only its matching language/framework references |

## Resolve overlapping instructions

- Follow the user's current request and project-specific requirements first. Preserve existing functionality, brand assets, routes, content, accessibility, and analytics unless changing them is part of the authorized task.
- Treat visual prescriptions as contextual design guidance. When the brief leaves visual direction open, use minimalist-ui's restrained, flat direction; its ban on gradients, heavy shadows, and glass effects takes precedence over optional decorative effects in the other references.
- Preserve established brand fonts, colors, icons, and component conventions rather than replacing them to satisfy a generic default. For new choices, use a consistent family and the task's design direction. Avoid conflicting font, icon, or component systems.
- Use design-taste-frontend's marketing guidance only on suitable surfaces. For dashboards, tables, and multi-step product flows, preserve usable density and established product patterns; continue the requested product work without imposing a marketing layout.
- Use responsive-design for layout mechanics across both marketing and product interfaces. Preserve established breakpoint conventions when they work; choose new breakpoints from actual content needs. Prefer mobile-first layouts, fluid sizing, logical properties for RTL, and container queries where component width drives behavior. Generic desktop composition rules must yield to readable, usable narrow-screen layouts.
- Accessibility, reduced-motion preferences, functional correctness, and measured performance take priority over animation or visual novelty. Do not add motion, images, dependencies, or theme switches solely to complete an unrelated checklist.
- Compress chat replies, not technical accuracy. Use complete language when compression risks ambiguity. Keep code, commits, PR descriptions, and product copy in normal language. Apply the communication reference within this workflow; persistent Caveman mode requires the user's preference. Honor later user requests to change communication style.
- Reference approval rules do not add a second confirmation when the user has already authorized the specific change. Preserve the actual task's authorization boundaries.
- Apply security guidance to relevant JavaScript/TypeScript, Python, and Go work. Load guidance for both frontend and backend when both are in scope. Dedicated PHP/Drupal and C# guidance is not bundled; disclose that limitation for reviews and consult authoritative stack-specific sources as needed.
- This bundle includes security-best-practices: use secure defaults for code being written and flag directly observed critical issues. Do not turn routine UI changes into a full security audit, active scan, penetration test, or unrelated hardening. Produce prioritized, code-referenced security reports when requested; implementation fixes follow the user's authorized scope.

## Working sequence

1. For local project work, resolve the project root and initialize/read its memory before substantive work. Inspect Git state and the relevant project structure, preserving existing uncommitted work. Scope the inspection to the request.
2. For interface work, inspect current code and, when available, the rendered interface. Establish the brief, existing design tokens, and whether the task is a targeted change, preservation-focused redesign, or an authorized overhaul. Use the design read from design-taste-frontend only when that route applies.
3. Make focused changes within the existing stack. Verify dependencies before importing them. Apply matching security-best-practices guidance to code being written, without expanding the task. Resolve visual conflicts using the rules above rather than mixing incompatible recommendations. For layout changes, apply responsive-design to typography, spacing, media, navigation, and component sizing as relevant.
4. Verify behavior and rendering at relevant viewport sizes, languages, and supported themes, including intermediate widths where content breaks. Check overflow, long labels, touch targets, keyboard/focus behavior, and affected loading, empty, and error states. Distinguish browser emulation from real-device testing. Run project checks appropriate to the change.
5. Use Lighthouse when page quality is in scope or a completed page needs verification. Prefer a production build and repeat comparable modes after performance changes. Report actual measurements with URL, build mode, device mode, and run count; do not claim improvement from unavailable or inconclusive evidence. If no runnable target is available, finish independent work and identify the missing target.
6. Update project memory only when durable context changed. Report the result, meaningful verification, and remaining limitations concisely, distinguishing local work from deployed or production-verified behavior.

## Bundled project-memory helper

Use [scripts/ensure_project_memory.py](scripts/ensure_project_memory.py). Resolve its absolute path from this skill's installation directory, not from the repository or the references directory:

```text
python <absolute-skill-directory>/scripts/ensure_project_memory.py --root <absolute-project-root>
```

Read the target printed by the helper: `<project-root>/.codex`, or `.codex/project-memory.md` when `.codex` is a directory. This is an ordinary Markdown context file used by this workflow across agents; it does not require Codex or replace the host's instruction files. Preserve existing content; never store secrets or raw transcripts, and do not stage or commit memory unless requested.

## Reference provenance

The original eight guide documents, responsive-design's supporting references, and project-memory helper were assembled from installed skills on 2026-10-07. This bundle's entry point and UI metadata identify **FrontEnd**. Bundled copies are self-contained snapshots and do not automatically follow later edits to the originals. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source attribution and licensing scope.

Security Best Practices was sourced from `openai/skills`, path `skills/.curated/security-best-practices`, on 2026-10-07 and bundled with its complete reference directory under `references/security-best-practices/`. This ninth component is a snapshot; refresh it explicitly when updating the bundle. No standalone installation is required.

In the project-memory reference, `scripts/ensure_project_memory.py` means the helper bundled above. The design-taste reference's illustrative `skills/taste-skill/blocks/` tree describes a proposed block library, not resources shipped here. Do not assume those blocks exist.
