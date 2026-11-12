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
  explicit `<span id="anchor-id"></span>` (HTML) / `{: #anchor-id}` (Markdown) immediately before the term —
  see `help/glossary/glossary.md` for the pattern used throughout this repo.
* `TOC.md` section anchors use `{#section-id}` syntax after a heading/list
  label, e.g. `Getting started{#getting-started}`.

## Images

Use Markdown image syntax whenever possible:

```markdown
![Alt text](path/to/image.png "Optional hover text")
```

* The `![...]` text is required accessible alt text. Keep it concise and do
  not use underscores; use spaces or hyphens instead.
* The image path may be relative to the Markdown file or root-relative, such
  as `/help/assets/shared-image.png`. Page-specific images belong in the
  sibling `<page-name>.resources/` folder (for example,
  `<page-name>.resources/image.png`). `help/assets/` is a legacy shared folder;
  do not add new page-specific images there.
* Optional image query parameters can control CDN processing:
  `?width=750&format=png&optimize=medium`. Keep these parameters on the image
  URL, before any property block.
* Add image properties immediately after the closing `)`:
  `![Alt text](image.png "Hover text"){width="300" align="center"}`.
  `width` is a pixel value or percentage of the view area; images scale
  proportionally. Supported alignment values are `center` and `right`.
  `valign` is not supported.
* Use `modal="regular"` or `zoomable="yes"` to make an image click-to-zoom:
  `![Alt text](image.png){width="100" zoomable="yes"}`. Do not combine
  click-to-zoom with an image link; the hyperlink takes precedence.
* To make an image link to another page, wrap the image in a Markdown link:
  `[![Alt text](image.png)](../target/target.md)`.
* For large images, provide at least 640 pixels of source width when practical,
  use no more than about 2000 pixels unless needed, and keep image files under
  5 MB where possible. The pipeline accepts files up to 100 MB, but files over
  20 MB fail validation and articles should generally contain no more than
  100 images (some older guidance says 200; use the stricter limit).

Use HTML only when Markdown cannot express the required layout, such as a
special table or a custom inline presentation. The supported HTML image form
is:

```html
<img src="image.png" alt="Alt text" />
```

* Always provide a meaningful `alt` attribute, and use a relative or
  root-relative `src` consistent with Markdown images.
* For HTML images inside preserved inline HTML, add
  `data-preserve-html="true"` to the containing tags when required by the
  surrounding markup. For example:

  ```html
  <div data-preserve-html="true" align="center">
    <img src="my-page.resources/preview.gif" alt="Preview" />
  </div>
  ```

* To enable click-to-zoom for an HTML image, use
  `class="modal-image"` on the `<img>` tag.
* Do not use unsupported HTML attributes or rely on `valign`; prefer Markdown
  properties for width and alignment.

## Tables

Prefer native Markdown tables for ordinary tabular content:

  ```markdown
  | Header | Another header | Yet another header |
  |--- |--- |--- |
  | row 1 | column 2 | column 3 |
  | row 2 | row 2 column 2 | row 2 column 3 |
  ```

* Put a blank line before the table. Markdown tables require at least one
  header row and one body row; use an HTML table for a one-row or headerless
  table.
* Use at least three hyphens in every header separator cell, and keep the same
  number of pipe characters in every row. Escape a literal pipe as `\|` or
  `&vert;`.
* Use alignment markers in the separator row when needed:
  `|---|:---:|---:|` for left, center, and right alignment.
* Inline HTML is supported in Markdown table cells for paragraph breaks and
  basic lists. Use `<p>` for separate paragraphs, `<br>` for line breaks, and
  `<ul>`/`<ol>` with `<li>` items for lists. Add
  `data-preserve-html="true"` to inline HTML elements when required by the
  surrounding repository markup.

  ```markdown
  | Header | Details |
  |---|---|
  | Text | First paragraph.<p>Second paragraph.<br>New line.<ul><li>Item</li></ul> |
  ```

* Avoid very wide and very tall tables; they are difficult to navigate.
  Be cautious with inline code in tables because long code can force
  disproportionate column widths.
* To choose the table layout for a Markdown table, add the property after the
  table, separated by a blank line:

  ```markdown
  {style="table-layout:fixed"}
  ```

  Use `table-layout:auto` (the default) when long text or code needs flexible
  column widths. Use `fixed` for balanced columns, such as tables containing
  similarly sized images.

Use an HTML table when Markdown cannot express the required structure, such as
omitting headers, combining cells with spans, balancing columns, or aligning
content within cells:

```html
<table style="table-layout:fixed">
  <tr>
    <th>Property</th>
    <th>Value</th>
  </tr>
  <tr>
    <td align="center">Example</td>
    <td>Details</td>
  </tr>
</table>
```

* Supported table elements include `<table>`, `<tbody>`, `<thead>`, `<tfoot>`,
  `<tr>`, `<th>`, `<td>`, `<col>`, and `<colgroup>`, along with supported
  inline elements such as `<p>`, `<br>`, `<b>`, `<i>`, `<ul>`, `<ol>`, and
  `<li>`.
* Do not use Markdown syntax inside an HTML table. For example, Markdown
  notes, images, and links may render literally; use HTML syntax instead.
  `UICONTROL` and `DNL` localization tags are exceptions.
* Use `align="left"`, `align="center"`, or `align="right"` on a cell when
  needed. HTML tables cannot contain nested tables.
* Set the HTML table layout on the opening tag:
  `<table style="table-layout:auto">` or
  `<table style="table-layout:fixed">`.
* For a borderless one-row HTML table, use
  `<tr style="border: 0;">`.

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

Experience League does not support direct MP4 or YouTube video embeds in `[!VIDEO]` blocks. If you need an animated preview, use a GIF in the page's sibling `.resources` folder instead and center it with inline HTML if needed.

```markdown
<div data-preserve-html="true" align="center">
  <img src="my-page.resources/my-preview.gif" alt="My preview" />
</div>
```

Do not use `[!VIDEO]` for local MP4 files, remote MP4 files, or YouTube URLs — the publish pipeline rejects them and CI fails.

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

See AGENTS.md's "Page front matter" section for the exact block used by
regular content pages in this repo, and `metadata.md` for repo-level
inherited fields.