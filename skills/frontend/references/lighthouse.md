---
name: lighthouse
description: Run, interpret, and act on Google Lighthouse audits for web pages and web apps. Use when Codex needs to measure or improve Lighthouse performance, accessibility, best-practices, SEO, PWA, Core Web Vitals-related signals, local page quality, Lighthouse CI setup, audit reports, or before/after web optimization results.
---

# Lighthouse

## Purpose

Use Lighthouse as an evidence-gathering tool, not just a score generator. Run the audit in a repeatable way, inspect the report, connect findings to code, fix practical issues, then rerun enough to confirm direction.

## Audit Setup

1. Identify the target.
   - Use the URL the user provides.
   - For a local app, inspect package scripts and project docs to find the correct dev or production server command.
   - If no URL or runnable local target can be inferred, ask one concise question before proceeding.

2. Check prerequisites.
   - Confirm Node and Chrome or Chromium are available before running CLI audits.
   - Prefer a project-local Lighthouse package when present. Otherwise use `npx --yes lighthouse@latest` for one-off audits.
   - Use Lighthouse CI (`lhci`) when the user asks for CI, thresholds, regression prevention, or multi-URL repeatability.

3. Choose audit mode.
   - For broad page quality, run the default mobile Lighthouse audit first.
   - Add `--preset=desktop` when desktop behavior matters or when comparing responsive experiences.
   - Run against production builds when assessing deploy readiness. Use dev builds only for debugging local behavior.
   - For authenticated flows, prefer a browser/DevTools workflow or a controlled Chrome profile. Do not hardcode credentials into commands or reports.

## Command Patterns

Use these as adaptable patterns:

```powershell
npx --yes lighthouse@latest https://example.com --quiet --chrome-flags="--headless" --output=json --output-path="$env:TEMP\lighthouse-report.json"
npx --yes lighthouse@latest https://example.com --quiet --chrome-flags="--headless" --preset=desktop --output=json --output-path="$env:TEMP\lighthouse-desktop.json"
npx --yes @lhci/cli@latest autorun --collect.url=https://example.com --collect.numberOfRuns=3 --upload.target=filesystem --upload.outputDir="$env:TEMP\lhci"
```

When keeping reports in the workspace, use an ignored or clearly named artifact folder already used by the project. Otherwise prefer a temp directory and summarize the important findings.

## Reading Results

1. Start with failures and diagnostics, not only category scores.
   - Check `categories.performance.score`, `accessibility`, `best-practices`, `seo`, and any PWA category present.
   - For performance, inspect LCP, CLS, TBT, FCP, Speed Index, render-blocking requests, unused JavaScript/CSS, image sizing, caching, font loading, and main-thread work.
   - For accessibility, prioritize keyboard access, names/labels, contrast, landmarks, headings, form labels, and ARIA misuse.
   - For SEO, prioritize crawlability, titles/descriptions, canonical metadata, robots rules, status codes, links, and structured data when applicable.

2. Treat scores as sampled measurements.
   - Mention run count, target URL, mobile/desktop mode, build mode, and any throttling or Chrome flags used.
   - Avoid claiming small score changes are conclusive from a single run.
   - Prefer concrete audit findings and before/after metric direction over score-only reporting.

## Fix Workflow

1. Map report items to code ownership.
   - Search for route files, page components, metadata, image usage, font imports, scripts, analytics tags, CSS, and server/cache headers relevant to each finding.
   - Prefer existing framework primitives: framework image components, metadata APIs, route headers, code splitting, font loaders, and build configuration.

2. Fix high-impact issues first.
   - Performance: image dimensions and formats, LCP resource priority, excessive client JavaScript, hydration cost, render-blocking CSS/scripts, font display strategy, cache headers.
   - Accessibility: semantic controls, labels, focus order, alt text, contrast, heading order, visible focus, ARIA correctness.
   - SEO: unique titles/descriptions, canonical URLs, indexability, valid links, status codes, structured data correctness.

3. Verify.
   - Run project tests, lint, or type checks when relevant.
   - Rerun the same Lighthouse mode after changes. For performance-sensitive work, run multiple times or use LHCI with `collect.numberOfRuns`.
   - Report what changed, what improved, what did not move, and any remaining risks.

## Lighthouse CI

Use LHCI when repeatability matters:

```powershell
npx --yes @lhci/cli@latest healthcheck
npx --yes @lhci/cli@latest autorun --collect.url=http://localhost:3000 --collect.numberOfRuns=3 --upload.target=filesystem
```

Add or update `lighthouserc.*` only when the user wants CI or persistent thresholds. Keep thresholds realistic and project-specific; avoid failing builds on volatile performance scores without team intent.

## Boundaries

- Do not run destructive commands, publish reports publicly, or upload to a remote LHCI server unless the user asks.
- Do not commit generated reports unless the user asks or the repository already tracks them.
- Do not read or expose secrets while configuring authenticated audits.
- Do not optimize purely for Lighthouse if it harms real user experience, accessibility, correctness, or maintainability.
