---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/shape-drop-shadow.html"
breadcrumb-title: ""
description: Use the Shape Drop Shadow node to add drop shadow effects to shapes for creating depth and dimension in textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Shape Drop Shadow
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Shape Drop Shadow
user-guide-description: ""
user-guide-title: ""
---


# Shape Drop Shadow

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shape-dropshadow-grayscale.png){width="128px"}

![](shape-dropshadow.png){width="128px"}

## Shape Drop Shadow (Grayscale)

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Performs the well-known "Drop Shadow" effect from other 2D image processing software, on an input black and white mask (for the grayscale version) or image with transparency (for the color version).

It differs from the [Shadows](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/effects/shadows-filter-node/shadows-filter-node.md) effect in that it returns images with full transparency applied, making for a more complete effect similar to what you'd expect in other software.

## Parameters

* **Angle**: *0.0 - 1.0*Incidence Angle of the (fake) light.
* **Distance**: *-0.5 - 0.5*Distance the shadow drop down to/moves away from the shape.
* **Size**: *0.0 - 1.0*Controls blurring/fuzzines of the shadow.
* **Spread**: *0.0 - 1.0*Cutoff/treshold for the blurring effect, makes the shadow spread away further.
* **Opacity**: *0.0 - 1.0*  
  Blending Opacity for the shadow effect.
* **(Shadow) Color**: *(Color value)*Color tint to be applied to the shadow.
* **Mask Color**: *(Color value) *(Grayscale Version Only)**Solid color to be used for the transparency mapped output.
* **Input Is Pre-Multiplied**: *False/True *(Color Version Only)**Whether the input should be assumed as pre-multiplied.
* **Pre-Multiply Output**: *False/True*Whether the output should be pre-multiplied.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="dropshadowex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
