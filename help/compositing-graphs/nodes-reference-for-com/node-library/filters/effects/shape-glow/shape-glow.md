---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/shape-glow.html"
breadcrumb-title: ""
description: Use the Shape Glow node to add glow effects to shapes and textures for creating luminous and atmospheric visual effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Shape Glow
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape Glow
user-guide-description: ""
user-guide-title: ""
---


# Shape Glow

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shape-glow-grayscale.png){width="128px"}

![](shape-glow.png){width="128px"}

## Shape Glow (Grayscale)

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Creates a soft glow around an input mask (for the grayscale version) or a shape with an alpha channel (for the color version). Compared to [Glow](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/glow/glow.md), this works in ways more similar to other 2D image editing software, as it is a more complete effect with more controls.

## Parameters

* **Mode**: *Soft, Precise*Switches between two accuracy modes.
* **Width**: *-1.0 - 1.0*Controls how far the glow reaches.
* **Spread**: *0.0 - 1.0*Cut-off / treshold for the blurring effect, makes the glow appear solid close to the shape.
* **Opacity**: *0.0 - 1.0*  
  Blending Opacity for the glow effect.
* **(Shadow) Color**: *(Color value)*Color tint to be applied to the glow.
* **Mask Color**: *(Color value) *(Grayscale Version Only)**Solid color to be used for the transparency mapped output.
* **Input Is Pre-Multiplied**: *False/True *(Color Version Only)**Whether the input should be assumed as pre-multiplied.
* **Pre-Multiply Output**: *False/True*Whether the output should be pre-multiplied.

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="shapeglow-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
