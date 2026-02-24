---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/flood-fill-to-gradient.html"
breadcrumb-title: ""
description: Use the Flood Fill to Gradient node to fill regions with gradient values for creating smooth color transitions.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to Gradient
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Flood Fill to Gradient
user-guide-description: ""
user-guide-title: ""
---


# Flood Fill to Gradient

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](floodfill-to-gradient.png){width="128px"}

## Flood Fill to Gradient

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Transforms a [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md) base into (randomly oriented) gradients. Very useful for creating a Heightmap where tiles are randomly tilted and sloped.

## Parameters

### Inputs

* **Flood Fill**: *Color Input*Base Flood fill data.
* **Angle Input**: *Grayscale Input*  
  Opttional map to determine per-cell angle with an external map.
* **Slope Input**: *Grayscale Input*Optional map to determine per-cell gradient slope-strength.

### *Parameters*

* **Angle**: *0.0 - 1.0*Sets uniform, global angle/direction for all tiles.
* **Angle Variation**: *0.0 - 1.0*Randomises the angle for each tile individually. This is the most useful and powerful parameter!
* **Multiply by Bounding Box Size**: *0.0 - 1.0*Scales the entire linear effect by the tile's individual bounding box size. This means smaller tiles will end up being darker than larger ones.
* **Angle Image Input Multiplier**: *0.0 - 1.0*Set influence of optional Angle Input map on generated gradient directions
* **Slope Image Input Multiplier**: *0.0 - 1.0*  
  Set influence of optional Slope Input map on generated gradient slope strength.
* **Multiply by Slope Intensity**: *0.0 - 1.0*
* **Flat Slope Color**: *(Grayscale value)*Allows setting of solid value for flat slopes.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="floodgradient-ex2.png" width="256px"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c1_image" src="floodgradient-ex1.png" width="256px"/></div> |
| --- | --- |
|  |  |

</td>
</tr>
</table>
