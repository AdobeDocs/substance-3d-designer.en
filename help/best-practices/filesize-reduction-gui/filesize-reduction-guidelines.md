---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/best-practices/filesize-reduction-guidelines.html"
breadcrumb-title: ""
description: Learn guidelines for reducing Substance graph file sizes to optimize performance and storage requirements.
helpx_creative_field: ""
helpx_description: Designer > Best Practices > Filesize Reduction Guidelines
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Filesize Reduction Guidelines
user-guide-description: ""
user-guide-title: ""
---


# Overview

In some cases the total filesize of [Substance 3D assets (SBSAR)](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) can be an important factor. This page covers a few critical areas and settings to keep in mind when trying to reduce filesize.

Filesize is mostly determined by [embedded bitmaps.](../../help/resources/bitmap-resource/bitmap-resource.md) They are files that are linked, embedded or baked and added to the  [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) file (SBS) as a resource. Only bitmaps that are used in a graph i.e. connected to an output either directly or through the node chain are published in the Substance 3D asset. In an Substance 3D file, bitmaps have no impact on filesize, as all bitmap resources are still stored outside of the file.

>[!IMPORTANT]
>
> Make sure the [Output size](../../help/compositing-graphs/output-size/output-size.md) property of all [Bitmap](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md) nodes are set to the *Absolute* [inheritance method](../../help/compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md). If that is not the case, their referenced [Bitmap resource](../../help/resources/bitmap-resource/bitmap-resource.md) will be saved at the default 256\*256 resolution in the published Substance 3D asset file, which will *impact the quality* of one or more outputs.

## Filesize Factors

There are a few different factors affecting total filesize of the [SBSAR](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html). They are listed below with an short explanation.

+++Resolution
Obviously has a large effect. Use the smallest resolution possible, keeping mind that you might also want your Substance file to work in large resolutions. You can use standard resolution-masking tricks to make smaller Bitmaps seem larger.

*Found in: external software, or import/re-export bitmap in Designer.*

+++

+++File color mode
Set in your Image Editor before export, the color mode also has an effect on filesize when using Raw bitmap format. Grayscale only bitmaps are smaller than RGB(A) images.

*Found in: external software, or import/re-export bitmap in Designer while setting up [Output nodes](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md) correctly.*

+++

+++File format
The file format of your images makes a difference, though it can be ignored in some cases. A program like Photoshop allows for slightly more control over JPG compression and can sometimes offer a decent middle road.

*Found in: external software, or import/re-export bitmap in Designer.*

+++

+++Usage in graph
What mode you set the Bitmap node to also has an effect on how Designer will compress the file, using a Grayscale mode file as a color bitmap in the graph will result in larger files. Make sure to set these correctly!

*Found in:[ Bitmap Node properties.](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md)*

+++

+++Bitmap format in package
On the Resource properties you can choose between "Raw" and "Jpeg" compression. This can have considerable effect on the final result.

*Found in: Bitmap Resource [Properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html), through [Explorer window.](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html)*

+++

+++Bitmap compression quality in package
When using "Jpeg" Bitmap format, the slider below can affect quality and filesize. This slider does not behave very predictable, but 1 tends to correspond to the highest quality JPG compression, and 0.5 tends to give the smallest size.

*Found in: Bitmap Resource [Properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html), through [Explorer window.](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html)*

+++

+++Compression mode on publish
When publishing to SBSAR, you have a choice between "Auto", "Best" and "None" for compressing, these can make a considerable difference if you are using the "Raw" bitmap format. Also has a large impact on export speed. Generally not recommended to use "none as it offers no quality increase.

*Found in: final publishing settings for an SBSAR package.*

+++

## Filesize comparison

The table below shows the influence of all settings on each other. Bitmap used is a 4096x4096 image of generated noise, exported from Photoshop as either 24-bit TGA or JPG at quality 8. TGA's were also exported as Grayscale and RGBA mode.

The Graph just places a single Bitmap Node connected to a single output. Bitmap mode is set according to source file mode.

While the table on the right is not fully conclusive, the following can be learned when comparing visual results and file sizes:

* Raw Bitmap + Compression Best gives the best quality with an acceptable filesize.
* Pre-compressed source files can give reduced filesizes in most cases, but at a quality cost.
* Smallest filesizes, but worst quality is obtained with JPG package format at quality 0.5.
* Grayscale is not always smaller in filesize, but will have higher quality than color at similar settings.

>[!NOTE]
>
> **Jpeg Bitmap Format**
> 
> It's important to note that special maps that require high accuracy such as Normal maps, Vector Maps and others should probably not be set to Jpeg compression, as this will lead to much more visible artifacts!

| Source image | Color TGA | Color JPG | Grayscale TGA | Grayscale JPG |
| --- | --- | --- | --- | --- |
| <b>Raw Bitmap Format</b> Compression mode: *None* | 48 MB | 48 MB | 16 MB | 16 MB |
| <b>Raw Bitmap Format</b> Compression mode: *Best* | 9.11 MB | 3.37 MB | 5.06 MB | 4.75 MB |
| <b>Jpeg Bitmap Format</b> Compression quality: *1* | 5.09 MB | 1.94 MB | 6.30 MB | 2.49 MB |
| <b>Jpeg Bitmap Format</b> Compression quality: *0.5* | 231 KB | 230 KB | 626 KB | 569 KB |
| <b>Jpeg Bitmap Format</b> Compression quality: *0* | 407 KB | 433 KB | 990 KB | 808 KB |
