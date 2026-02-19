---
title: "Vector graphics (SVG) resource"
description: "Import and use SVG vector graphics as resources in Substance 3D Designer for procedural material creation."
helpx_description: Designer > Resources > Vector graphics (SVG) resource
helpx_url: "https://helpx.adobe.com/substance-3d-designer/resources/vector-graphics-svg-resource.html"
helpx_creative_field:
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - export
  - vector
  - save
---




# Vector graphics (SVG) resource

Substance 3D Designer supports a limited form of Vector Graphics, through the Scalable Vector graphics format. SVG files can be brought in as resources in different ways, to be used as resources for your graphs.

SVG files [can be created or edited through the atomic SVG node,](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/svg/svg.md) they can also be created by [the UV to SVG baker.](https://helpx.adobe.com/substance-3d-bake/bakers-settings/convert-uv-to-svg.html)

>[!NOTE]
>
> Adobe Illustrator (**.ai**) files are *not* currently supported.

## SVG storage

SVG storage depends on if they are Linked, or imported. Imported SVG files are embedded into the SBS file, requiring [no external files like Bitmaps](../bitmap-resource/bitmap-resource.md), and can be edited using the [Vector editing tools](vector-editing-tools/vector-editing-tools.md).

## SVG attributes

SVG Resources in a package have a number of attributes that you can customize. Most attributes don't have a major purpose and are for library filters, but a minority affects rendering quality.

| Attribute name | Purpose |
| --- | --- |
| Identifier | Used for referencing the SVG resource in a package, must be unique. |
| File path | The path on disk of the SVG file referenced by the resource. |
| Description | The description displayed in the [Explorer](../../interface/the-explorer-window/the-explorer-window.md) and [Library](../../interface/the-library/the-library.md) tooltips for this resource. |
| Category | Used for [sorting and curating the resource](../../interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../interface/the-library/the-library.md). |
| Label | Used for [sorting and curating the resource](../../interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../interface/the-library/the-library.md). |
| Author | Used for [sorting and curating the resource](../../interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../interface/the-library/the-library.md). |
| Author URL | Used for [sorting and curating the resource](../../interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../interface/the-library/the-library.md). |
| Tags | Used for [sorting and curating the resource](../../interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../interface/the-library/the-library.md). |
| User data | Optional extra data, not used on vector graphics. |
| Show in Library | Determines if the SVG resource should be hidden in [the Library view.](../../interface/the-library/the-library.md) |
| Vector graphics quality | Affects rendering quality. The range is not linear and best quality is achieved at 0.5. |

## SVG authoring

Because only a limited set of functionality is supported, authoring SVG's is constrained.

In general the following is true:

* Only simple primitive shapes and paths are guaranteed to draw correctly;
* Stroke is supported but only results in a 1 pixel wide stroke and stroke styling is ignored;
* Dashed line styles will definitely break;
* Text needs to be converted to paths/outline to be rendered;
* [Compound paths](https://helpx.adobe.com/ie/illustrator/using/combining-objects.html#compound_paths) are not supported;
* Advanced features like gradients are not supported;
* Style Elements for CSS properties are not supported.

## Recommended export options

Export options are slightly different for each applications:

### Adobe Illustrator

[Illustrator](https://www.adobe.com/products/illustrator.html) allows the most control over your SVG exports if you pay attention to the following options.

* Use only <b>Save As</b>, *not* Export As!
* <b>SVG Profile</b> does not matter much, though the Tiny profile will (mostly) default to settings that are definitely correct;
* <b>Fonts</b> must be set to <b>Convert to Outline</b> to work;
* <b>CSS Properties</b> should *not* be set to Style Elements, all other options will work;
* Uncheck <b>Preserve Illustrator Editing Capabilities</b>;
* Uncheck <b>Responsive</b>;
* Strokes will not work well, use <b>Object &gt; Path &gt; Outline Stroke</b> to get them to show up.

The image on the right demonstrates the recommended export options, click on it to display it in full size.

>[!IMPORTANT]
>
> Artboards can affect the result of the SVG file generated. Some Illustrator file templates introduce multiple Artboards.  
> Try to have only one, properly cropped artboard, and have it selected in the Artboard window when saving as SVG.

![Illustrator SVG export options](svg-export-options-ai.jpg "Illustrator SVG export options"){width="512px"}

### Inkscape

Inkscape saves natively as SVG, but with less control over the file format. Inkscape files will mostly work natively in the application, but with some limitations:

* Strokes only show as 1px wide in Substance 3D Designer, use <b>Path &gt; Stroke to Path</b> to get them to work,
* Text will not work, use <b>Path &gt; Object to Path</b> to get text to work.

### Adobe Photoshop

Photoshop has a very limited SVG exporter (<b>File &gt; Export &gt;Export As..</b>) that is currently unable to produce correct results for Substance 3D Designer. You can get your shape and path information, but Style is always saved as Elements, which is incompatible.

It can be used for simple black and white shape masks, where a solution is to extract the Alpha from the SVG using [Alpha Split](../../compositing-graphs/nodes-reference-for-com/node-library/filters/channels/alpha-split/alpha-split.md).

Alternatively a Photoshop-exported SVG can be [Imported](../importing-linking-and-new/importing-linking-and-new-resources.md), which lets you then [edit the style information natively inside the application.](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/svg/svg.md)
