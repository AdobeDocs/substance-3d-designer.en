---
name: generate-node-documentation
description: >
  How to author a Substance 3D Designer node-reference page so it matches the
  standard layout used across help/compositing-graphs/nodes-reference-for-com/node-library/.
  Use this skill whenever creating or editing a node page (a node's description,
  Inputs, Outputs, Parameters, or Examples) under that node-library tree — or the
  equivalent function-node / atomic-node reference pages. Covers the folder/TOC
  convention, minimal front matter, the icon/description table, the anchored
  Inputs/Outputs/Parameters tables, and the Examples gallery. For general Adobe
  Experience League Markdown rules (callouts, links, UICONTROL/DNL, images) use the
  write-experience-league-markdown skill; this skill only covers node-page structure.
  Canonical example: help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter-v2/shape-splatter-v2.md
---

# Generating node documentation

Every leaf node-reference page in this repo follows one consistent structure. This
skill is the spec for that structure. The canonical, fully-worked example is
`.../node-library/texture-generators/patterns/shape-splatter-v2/shape-splatter-v2.md` —
when in doubt, open it and mirror it.

This skill covers only node-page *structure*. For base Experience League Markdown
(note/alert blocks, relative-vs-absolute links, UICONTROL/DNL, image query params,
lint gotchas) follow the `write-experience-league-markdown` skill.

## Where a node page lives (folder / TOC convention)

* One folder per node, under the matching category/subcategory path, e.g.
  `.../node-library/<category>/<subcategory>/<node-name>/<node-name>.md`.
* The folder is named as the kebab-case node title; it contains **one** `.md` file
  named identically.
* All embedded media for the page (icon, example images, GIFs) live in a **sibling
  `<node-name>.resources/` folder** next to the `.md` and are referenced with a
  relative path (e.g. `<node-name>.resources/<file>.png`). Do not point node pages at
  the shared `help/assets/` folder — that is a legacy pattern being phased out; new and
  edited pages use their own `.resources` folder.
* Every page has a corresponding entry in `help/guide/TOC.md`. When adding or moving a
  page, update `TOC.md` and the folder layout together (see CLAUDE.md's Folder/TOC
  convention).

## Front matter

Node pages use the **minimal** block — only `title` and a breadcrumb-style
`description`. (This is distinct from the 11-field legacy block CLAUDE.md documents for
regular content pages.)

```yaml
---
title: "Shape splatter v2"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Generator > Pattern > Shape splatter v2"
---
```

## Body structure

Top to bottom, everything below the front matter:

### 1. H1 title

A single `# <Node title>` — exactly one H1 per page.

### 2. Icon / description table

One HTML table, one row, two cells. Left cell (`33.33%`) holds the icon then the
`In:` breadcrumb; right cell (`100.00%`) holds `## Description` and the prose.

```html
<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![<Node title> icon](<node-name>.resources/<node-name>.png "<Node title>")

<b>In:</b> <Category> &gt; <Subcategory>

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

<Description prose.>

</td>
</tr>
</table>
```

Description-cell prose conventions:
* Separate paragraphs with `<br><br>` (raw blank lines inside the cell are unreliable).
* Inline emphasis is `<b>…</b>` / `<i>…</i>`.
* Lead-in asides use `<i>Note:</i>` / `<i>Tip:</i>` at the start of the sentence.
* Use `&gt;` for the `>` in the `In:` line (it's inside HTML). Take the category /
  subcategory names from the node itself; don't invent them.

### 3. Optional callouts

`>[!INFO]`, `>[!TIP]`, `>[!NOTE]`, etc. go **after** the icon/description table (not
inside the cell). Syntax per the `write-experience-league-markdown` skill.

### 4. Inputs

Include only if the node has input pins. Precede the heading with an anchor.

```markdown
<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Background height</b> <i>Grayscale</i> | The base height map in which shapes are scattered.<br><br>The contribution is controlled by the <b>Background input opacity</b> parameter. |
```

* Two columns, empty header row, `|:---|:---|` alignment.
* One row per input: left cell `<b>Name</b> <i>Type</i>`, right cell the description.
* The type marker is HTML italics — `<i>Type</i>` — not markdown `*Type*`.

### 5. Outputs

Same shape as Inputs, with `<a name="outputs"></a>` + `## Outputs`. Include only if the
node documents distinct outputs (many nodes have a single implicit output and omit this
section — don't invent one).

For packed multi-channel outputs, break the channels out with `<br>` and indent
sub-points with `&nbsp;` (see the "Splatter UVW" / "Splatter data" rows in the
reference):

```markdown
| <b>Splatter UVW</b> | <b>R</b> - U component of the shapes' UVs.<br><b>G</b> - V component of the shapes' UVs.<br><b>B</b> - The shapes' height. (W)<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <i>Integer part:</i> The shapes' unique identifier. |
```

### 6. Parameters

Same table shape, with `<a name="parameters"></a>` + `## Parameters`. Omit the whole
section if the node has no parameters (never emit an empty table or a "No parameters."
line).

* **Grouped parameters**: emit a spanning label row with an empty right cell before the
  group's rows:

  ```markdown
  | <b>Positioning</b> |  |
  | <b>Project Input</b> <i>UV Position, World Space Position</i> | Choose whether the projection position is set in 2D/UV or in 3D/World space. |
  ```

* **Enum / multi-option values**: list the options inside the description cell as a
  `<br>`-separated dash list:

  ```markdown
  | <b>Position distribution mode</b> <i>Integer</i> | The method of distributing the shapes:<br><br>- <b>2D grid:</b> A simple uniform grid.<br>- <b>Poisson disc:</b> Randomly offsets grid cells to prevent overlaps.<br>- <b>Uniform:</b> An even distribution of a set number of shapes. |
  ```

### 7. Examples

Include only if there are example images/GIFs. Use an HTML gallery table; one `<td>`
per image with an optional caption; wrap to a new `<tr>` after 3 images. Media paths
point into the page's `.resources` folder.

```html
## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="./<node-name>.resources/<file>.gif" /><br><i>Caption</i>
        </td>
        <td style="border: 0; background: transparent">
            <img src="./<node-name>.resources/<file2>.jpg" /><br><i>Another caption</i>
        </td>
    </tr>
</table>
```

Leave trailing cells in a partially-filled final row empty (`<td …></td>`) rather than
reflowing. Omit captions if the source has none.

## Canonical type values

Reuse the node's own type wording; typical values: `Grayscale`, `Color`, `Integer`,
`Float`, `Float2`, `Float3`, `Float4`, `Integer2`, `Boolean`, `Grayscale Input`,
`Color Input`, `(Color value)`, `(Grayscale value)`. Don't invent or "normalize" a type
the node doesn't actually use.

## Table-cell rules

* No raw newlines inside a table cell — join lines with `<br>` (and `<br><br>` between
  paragraphs).
* Emphasis inside cells is `<b>`/`<i>`, and the type marker is always `<i>Type</i>`.
* Indent nested sub-points with `&nbsp;` sequences.

## Rules / don'ts

* **Don't fabricate** Inputs, Outputs, or Parameters the node doesn't have; omit the
  section instead. Don't reword, summarize, or drop existing technical content — only
  reformat it.
* **Keep links relative** to other `.md` pages; external links absolute.
* **Drop legacy cruft** when editing an old page into this format: difficulty tags
  (`**Simple**` / `**Intermediate**` / `**Complex**`), the redundant `## <Title>`
  sub-heading inside the icon cell, stub sentences like "There are no images attached to
  this page.", and any leftover empty navigation/wrapper tables from earlier migrations.
* **One H1** per page; sections use `##`, and the Inputs/Outputs/Parameters anchors
  (`inputs` / `outputs` / `parameters`) must precede their headings so cross-page
  `#inputs` links resolve.
* **Keep `TOC.md` in sync** when adding, renaming, or moving a page.
