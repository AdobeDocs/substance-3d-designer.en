---
name: write-experience-league-markdown
description: >
  Syntax rules, custom extensions, and gotchas for writing Markdown content
  published on Adobe Experience League. Use this skill whenever creating or
  editing any page under help/ in this repo (or any other Experience League
  content repo) — headings, links, images, tables, note/alert blocks,
  UICONTROL/DNL tags, video embeds, anchors, and known rendering pitfalls.
  Source: https://experienceleague.adobe.com/en/docs/contributor/contributor-guide/writing-essentials/markdown
---

# Writing Experience League Markdown

Experience League renders GitHub-flavored Markdown through a custom pipeline
with its own extensions and rendering quirks. Standard GFM mostly works, but
the items below are Experience League-specific — get them wrong and content
either fails lint/link-check CI or renders incorrectly on the live site.

## Headings

* `#` through `#####` (levels 1–5). The page's `title` front matter is
  effectively level 0; the first Markdown heading in the body should be a
  single `# Level 1` heading matching (or closely matching) the page title.
* Don't skip levels arbitrarily; the mini-TOC is generated from headings.

## Text formatting

* `**bold**`, `*italic*`, `***bold and italic***`.
* Escape literal special characters with a backslash (`\*`, `\_`, etc.).
* **Ampersands** in headings/titles must be written out (`and`) or encoded as
  `&amp;` — a raw `&` in a title can break parsing.
* **Angle brackets** used as literal text (not real HTML) must be encoded:
  `<placeholder>` → `&lt;placeholder&gt;`.
* **Smart quotes** pasted from word processors must be encoded, not left as
  literal curly characters: left double `&#8220;`, right double `&#8221;`,
  apostrophe/right single `&#8217;`.

## Lists

* Numbered lists: start every item with `1.` (or `1)`) — GitHub/Experience
  League auto-numbers regardless of the literal digits typed.
* Bulleted lists: use `*`, `-`, or `+`, but **do not mix bullet characters
  within the same list/document**.
* `TOC.md` list nesting uses `+` consistently — follow the existing file's
  bullet style rather than introducing a different one.

## Links

* Internal cross-references must be **relative** Markdown links to the
  target `.md` file: `[Overview](../../overview.md)`.
* External references must be **absolute** URLs.
* Anchors into another page's headings/spans: append `#anchor-id`, e.g.
  `[Mesh](../../glossary/glossary.md#mesh)`.
* In-page anchors are declared either as a heading (auto-slugged) or an
  explicit `<span id="anchor-id"></span>` immediately before the term —
  see `help/glossary/glossary.md` for the pattern used throughout this repo.
* `TOC.md` section anchors use `{#section-id}` syntax after a heading/list
  label, e.g. `Getting started{#getting-started}`.

## Images

* `![Alt text](path/to/image.png "Optional hover title")`.
* Optional sizing/optimization query params are supported:
  `![Adobe logo](assets/logo.png?width=750&format=png&optimize=medium)`.
* **Alt text must not contain underscores** — they don't render correctly;
  use hyphens or spaces instead.
* Page-specific images live in `<page-name>.resources/`; shared/app icons
  live in `help/assets/` (see CLAUDE.md).

## Tables

* Pipe-delimited, with a hyphen header-separator row:

  ```markdown
  | Header | Another header | Yet another header |
  |--- |--- |--- |
  | row 1 | column 2 | column 3 |
  | row 2 | row 2 column 2 | row 2 column 3 |
  ```

* A blank line must precede the table or it won't render as a table.
* Tables can't cleanly hold multi-paragraph or complex block content in a
  cell — where this repo needs images/lists inside a table cell (e.g.
  comparison tables in `overview.md`), it falls back to inline HTML
  (`<div>`, `<b>`, `<ul>`/`<li>`) with `data-preserve-html="true"` on each
  tag so the pipeline doesn't strip it. Follow that existing pattern rather
  than inventing new inline HTML unless necessary.

## Code

* Inline code: single backticks.
* Fenced blocks: triple backticks, with an optional language for syntax
  highlighting (` ```python `, ` ```javascript `, etc.).

## Note / alert blocks

Custom blockquote syntax, one type per block, blank blockquote line between
the tag and the body:

```markdown
>[!NOTE]
>
>This is a standard NOTE block.

>[!TIP]
>
>This is a standard TIP.

>[!IMPORTANT]
>
>This is an IMPORTANT note.
```

Supported types: `NOTE`, `TIP`, `IMPORTANT`, `CAUTION`, `WARNING`,
`ADMINISTRATION`, `AVAILABILITY`, `PREREQUISITES`, `ERROR`, `INFO`, `SUCCESS`.

## Video embeds

```markdown
>[!VIDEO](https://video.tv.adobe.com/v/29770/?quality=12)
```

## UICONTROL tag

Wraps UI element names (button labels, menu items, field names) inline so
the localization pipeline knows to check for a translated string and falls
back to the English label if none exists:

```markdown
Click [!UICONTROL Save] to apply changes.
Go to [!UICONTROL Tools] > [!UICONTROL Settings].
```

Use it for every literal UI label referenced in instructional text (menu
items, button names, dialog titles, panel names).

## DNL tag ("Do Not Localize")

Wraps product names, third-party feature names, or any phrase that must
never be machine-translated:

```markdown
Use [!DNL Adobe Analytics] to track metrics.
The [!DNL Target] implementation requires configuration.
```

In this repo, use it for product names like `[!DNL Substance 3D Designer]`,
`[!DNL Substance 3D Sampler]`, etc., on first/prominent mentions per page,
consistent with existing pages.

## Inline HTML

Raw HTML is allowed (this repo's `markdownlint_custom.json` disables MD033
specifically for this reason) but is only reliably preserved through the
pipeline when tags carry `data-preserve-html="true"`. Reserve inline HTML
for cases plain Markdown can't express (images/lists inside table cells,
`<span id="...">` anchors) rather than as a general substitute for Markdown.

## Front matter

See CLAUDE.md's "Page front matter" section for the exact block used by
regular content pages in this repo, and `metadata.md` for repo-level
inherited fields.