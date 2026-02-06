---
title: "Font resource"
description: ""
helpx_description: "Designer > Resources > Font resource"
---

# Font resource

Font Resources are meant to be used together with the [atomic Text node](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/text/text.md). They allow you to use fonts that are not installed on your system, by referencing a font file anywhere on disk.

>[!NOTE]
>
> **Fonts in SBSAR**
> 
> Fonts are always embedded in an SBSAR, no matter if from a linked Resource, or by using a system-installed font. The advantage of this method is that there's no need to install, and when exporting an SBS file with dependencies, you can be sure the font files come along.

## Using custom font resources

* Right-click on a package, choose <b>Link &gt; Font</b>
* Select an .otf or .ttf file.
* Place a [Text node](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/text/text.md) in your [graph](../../compositing-graphs/substance-compositing-graphs.md).
* Under the <b>Font </b>property, any font resources will be found at the top of the list.

Note the font list does not automatically refresh with the properties open. You will have to switch to another property window and back to a Text node to see newly linked fonts.
