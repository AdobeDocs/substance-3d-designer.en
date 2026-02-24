---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/tiling/make-it-tile-photo.html"
breadcrumb-title: ""
description: Use the Make It Tile Photo node to convert photographs into seamless tiling textures for material creation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Tiling > Make It Tile Photo
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Make It Tile Photo
user-guide-description: ""
user-guide-title: ""
---


# Make It Tile Photo

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](make-it-tile-photo.png)

![](make-it-tile-photo-grayscale.png)

## Make It Tile Photo (Grayscale)

**In:** *Filters/Tiling*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

This node provides edge-fixup functionality for any image that might not tile due to non-continuous edges. It does not affect anything other than the input image's edges. If you want to adjust scale or tile in different ways, look at [Make It Tile Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/tiling/make-it-tile-patch/make-it-tile-patch.md).

## Parameters

* **Mask Warping H**: *-100.0 - 100.0*Introduces warping on the horizontal axis, to avoid undefined transitions.
* **Mask Warping V**: *-100.0 - 100.0*Introduces warping on the vertical axis, to avoid undefined transitions.
* **Mask Size H**: *0.0 - 1.0*Sets how far the transition edge reaches horizontally.
* **Mask Size V**: *0.0 - 1.0*Sets how far the transition edge reaches vertically.
* **Mask Precision H**: *0.0 - 1.0*Sets how smooth the transition is horizontally.
* **Mask Precision V**: *0.0 - 1.0*Sets how smooth the transition is vertically.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="mit-photo-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
