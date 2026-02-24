---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-to-height-hq.html"
breadcrumb-title: ""
description: Use the Normal To Height HQ node to convert normal maps to high-quality height maps for surface detail extraction.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal To Height HQ
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Normal To Height HQ
user-guide-description: ""
user-guide-title: ""
---


# Normal To Height HQ

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](normal-to-height-hq.png){width="128px"}

## Normal To Height HQ

**In:** *Filters/Normal Map*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

A reverse-conversion node that attempts to convert a tangent-space Normalmap back into a Heightmap. This is the more advanced node; [Normal to Height](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/normal-map/normal-to-height/normal-to-height.md) has less options and uses different calculations.

Useful for when you only have a Normalmap source, yet still want to perform operations combining it with a Heightmap. Keep in mind that this will never be able to provide a 100% correct result, as information is lost by nature of the process when Height is converted to Normal. It can never replace a properly generated Heightmap!

## Parameters

* **Normal Format**: *DirectX, OpenGL*  
  Switches between different Normalmap formats (inverts the green channel).
* **Relief Balance**: *0.0 - 1.0*Blends between low and high frequency bias.
* **Height Intensity**: *0.0 - 1.0*Intensity or multiplier for the Heightmap, works a bit like global opacity.
* **Height Normalize**: *False/True*Automatically scales the Heightmap range to use full contrast, like an [auto-levels](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/auto-levels/auto-levels.md).
* **Quality**: *Normal, High*Switches between speed or quality.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="normal2height-hq-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
