# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

# Substance 3D Designer documentation

This repository contains the documentation for Substance 3D Designer. There is no application code, build step, or test suite — the repository *is* the content, written in Markdown and published on [Adobe Experience League](https://experienceleague.adobe.com/docs/substance3d-designer.html?lang=en).

# Repository structure

* `help/` — all documentation content, organized to mirror the table of contents.
* `help/guide/TOC.md` — the table of contents. Every entry is a relative link (rooted at `/help/...`) to a page's Markdown file. `TOC.md` also carries page-tree metadata (`user-guide-title`, `breadcrumb-title`, `nudge`, section anchors like `{#section-id}`).
* `help/assets/` — shared, non-page-specific images (e.g. app icons reused across pages).
* `help/glossary/glossary.md` — a single large glossary page, organized alphabetically with anchor spans (`<span id="term"></span>`) used for cross-linking via `#term` fragments.
* `metadata.md` — repo-level front matter (cloud/solution/product IDs, `git-repo`, etc.) that is inherited by every `TOC.md`. Only edit this for repo-wide metadata changes; page-specific metadata belongs in the page's own front matter.
* `redirects.csv`, `linkcheckexclude.json`, `markdownlint_custom.json`, `pipeline.opts` — publishing-pipeline configuration (redirects, link-check exceptions, lint rule overrides, pipeline options).
* `fix-image-names.py` — one-off utility that renames `help/assets` images with parenthesized suffixes (e.g. `foo(1).png` → `foo_1.png`) and rewrites every Markdown reference to match. Not part of any regular workflow; run manually only when such filenames reappear.

## Folder/TOC convention

For every entry in `help/guide/TOC.md`:
* There is a corresponding folder under `help/`, following the same nesting as the TOC.
* That folder contains one Markdown file, named as the kebab-case version of the page title.
* If the page has bespoke media (images, GIFs, videos), it lives in a sibling subfolder named `<md-file-name>.resources`.

When adding or moving a page, update `TOC.md` and the folder layout together — they must stay in sync.

## Page front matter

Regular content pages use a front matter block like:

```yaml
---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/<section>/<page>.html"
breadcrumb-title: ""
description: <one/two sentence SEO description>
helpx_creative_field: ""
helpx_description: Designer > <Section> > <Page>
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: <Page title>
user-guide-description: ""
user-guide-title: ""
---
```

Keep `description` accurate and concise — it is used for SEO/search snippets.

# Content authoring rules

* English is the source of truth; all other languages are translated from it.
* All links to other documentation pages must be **relative** links; all links to external resources must be **absolute** links.
* Content is written in GitHub-flavored Markdown with Experience League's custom extensions/gotchas, documented [here](https://experienceleague.adobe.com/en/docs/contributor/contributor-guide/writing-essentials/markdown). Use the `write-experience-league-markdown` skill (if present) for the specifics.
* Every submitted change goes through automated lint checks and link validation in CI (see below) — check `markdownlint_custom.json` and `linkcheckexclude.json` before assuming a rule applies or a link needs fixing.

# Validation / CI

* `.github/workflows/validate-articles.yml` runs on PRs and pushes to `main` (and via a `retest` PR comment), calling the shared `Adobe-Enterprise-Docs/workflows` reusable workflow to lint Markdown and validate links. There is no local equivalent script in this repo — CI is the source of truth for pass/fail.
* `.github/workflows/mirror.yml` mirrors `main` to the public repo on push; it is infrastructure, not something content changes need to touch.
* `markdownlint_custom.json` extends the shared `markdownlint.json` ruleset and disables several rules (MD005, MD007, MD018, MD032, MD033, MD034, MD037, MD040) that conflict with Experience League's custom Markdown extensions (e.g. inline HTML, non-standard emphasis). Don't "fix" content to satisfy these disabled rules.
* `linkcheckexclude.json` whitelists link patterns (currently `example.com`/`example-end.com`) that the link checker should skip.

# Working conventions

* This is release-note-heavy documentation — release notes live under `help/release-notes/`, one folder per version (e.g. `version-16-0`), plus `all-changes` and `old-versions` aggregation pages. Follow the existing version folder as a template when adding a new release.
