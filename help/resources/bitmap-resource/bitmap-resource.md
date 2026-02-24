---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/resources/bitmap-resource.html"
breadcrumb-title: ""
description: Learn how to import, create, and use bitmap resources in Substance 3D Designer for texture-based material creation.
helpx_creative_field: ""
helpx_description: Designer > Resources > Bitmap resource
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Bitmap resource
user-guide-description: ""
user-guide-title: ""
---


# Bitmap resource

A bitmap resource is a resource in a Substance Package. It is different from the [atomic bitmap node. The atomic Bitmap node](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md) is a specific representation of that bitmap inside[ a Substance graph](../../help/compositing-graphs/substance-compositing-graphs.md).

Bitmaps are some of the most common non-Graph resources in Substance 3D Designer, usually their usage falls in one of the following categories:

* A baked map, either [baked internally by Designer](../../help/bakers/bakers.md), or externally by another application.
* A helper texture, like a pattern, grunge map or decal.
* A simple grayscale mask for blending, either created internally using [the bitmap node](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md), or with an external app.

## Bitmap storage

Bitmaps are usually the largest resource that Designer deals with. That's why it's good you understand how Designer handles these files with its two main filetypes.

### In Substance 3D files (SBS)

How bitmaps are stored in SBS depends on if you [Link or Import them, make sure you are familiar with the concept first.](../../help/resources/importing-linking-and-new/importing-linking-and-new-resources.md) Imported bitmaps can be edited using the [Bitmap painting tools](../../help/resources/bitmap-resource/bitmap-painting-tools/bitmap-painting-tools.md).

Unlike SVG (Vector Graphics) Resources, Bitmaps are always stored externally, even when created as a new resource, or imported. For new Substance Packages, they are kept in memory, until the .SBS file is saved to disk. Once saved to disk, bitmaps are stored in a */resources* folder next to the SBS file.

### In Substance 3D assets (SBSAR)

In [SBSAR files](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html), Bitmaps are embedded, meaning they have a large impact on the final SBSAR filesize. You can read more about the impact on filesize further on this page. When [SBSAR files are published,](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) only bitmaps that are used to compute an output of a graph are embedded. Any unused bitmaps are optimized and excluded from the final SBSAR package, with no effect on the filesize.

## File type, color mode and resolution

Substance 3D Designer can easily edit and re-arrange data from bitmaps, but it is best to keep the following in mind:

* Set your resolutions to be power of 2 compliant, that means follow standard realtime texture size like <b>256, 512, 1024 ,2048,</b> etc. Designer will rescale textures outside of this range to the closest matching resolution. Note that they don't have to be in square proportions.
* Many filetypes are supported, but choose one that is best for your usecase. <b>Lossless compression or even uncompressed</b> filetypes like PNG or TGA give better quality than JPG or DDS.
* Make sure to <b>set up your color mode correctly</b>, depending on whether you need color, grayscale or an alpha channel.

## Bitmap attributes

Bitmap Resources in a package have a number of attributes that you can customize. Most attributes don't have a major purpose and are for library filters, though a minority affects filesize..

| Attribute name | Purpose |
| --- | --- |
| Identifier | Used for referencing the bitmap resource in a package, must be unique. |
| File path | The path on disk of the bitmap referenced by the resource. |
| Description | The description displayed in the [Explorer](../../help/interface/the-explorer-window/the-explorer-window.md) and [Library](../../help/interface/the-library/the-library.md) tooltips for this resource. |
| Category | Used for [sorting and curating the resource](../../help/interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../help/interface/the-library/the-library.md). |
| Label | Used for [sorting and curating the resource](../../help/interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../help/interface/the-library/the-library.md). |
| Author | Used for [sorting and curating the resource](../../help/interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../help/interface/the-library/the-library.md). |
| Author URL | Used for [sorting and curating the resource](../../help/interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../help/interface/the-library/the-library.md). |
| Tags | Used for [sorting and curating the resource](../../help/interface/the-library/managing-custom-content/managing-custom-content-and-filters.md) in the [Library](../../help/interface/the-library/the-library.md). |
| User data | Optional extra data, not used on bitmaps. |
| Show in Library | Determines if bitmap should be hidden in [the Library view.](../../help/interface/the-library/the-library.md) |
| Bitmap format | Either Raw or Jpeg, has great effect on SBSAR filesize. See our [filesize reduction guidelines](../../help/best-practices/filesize-reduction-gui/filesize-reduction-guidelines.md) to learn more. |
| Bitmap compression quality | Only has an affect with Jpeg compression, determines quality/filesize balance. |

## Filesize reduction

See the [Filesize reduction guidelines](../../help/best-practices/filesize-reduction-gui/filesize-reduction-guidelines.md) page in the [Best practices](../../help/best-practices/best-practices.md) section for our recommendations regarding minizing the filesize of bitmaps embedded into [published Substance 3D assets](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) (SBSAR).
