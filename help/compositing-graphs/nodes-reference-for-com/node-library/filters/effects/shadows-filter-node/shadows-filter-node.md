---
title: "Shadows (Filter Node)"
description: "Use the Shadows filter node to generate shadow effects from input textures for adding depth and realism to materials."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Shadows (Filter Node)
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/shadows-filter-node.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - shading
  - effects
  - gradients
---




# Shadows (Filter Node)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shadows-1.png){width="128px"}

## Shadows

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

A raw, grayscale-only version of the [Shape Drop Shadow](../shape-drop-shadow/shape-drop-shadow.md) node. It only takes a black and white, binary shapes as input and returns only the shadow.

Can be useful if you're just after the shadow and do not want to work with a more complete node, for example when building your own material or baked lighting.

## Parameters

* **Shadow Distance**: *0.0 - 1.0*Controls how far away the shadow should fall.
* **Light Angle**: *0.0 - 1.0*Controls the incidence angle of the light.
* **Edges Softness**: *0.0 - 1.0*Determines how hard or soft the shadows edges are.
* **Samples**: *1 - 16*Sets quality for the Edges Softness setting.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="shadow-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
