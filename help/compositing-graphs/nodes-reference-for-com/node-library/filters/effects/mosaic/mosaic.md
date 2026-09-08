---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/mosaic.html"
breadcrumb-title: ""
description: Use the Mosaic node to create mosaic tile effects by dividing textures into pixelated blocks and patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Mosaic
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mosaic
user-guide-description: ""
user-guide-title: ""
---

# Mosaic

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/mosaic-1.png){width="128px"}

![](../../../../../../assets/mosaic-grayscale.png){width="128px"}

## Mosaic (Grayscale)

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

"Facetises" an existing, smooth, sloping gradient map by performing a multi-pass [Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/warp/warp.md) effect. When the same map is used for both inputs, it essentially grows and accentuates the brightest areas.

This is useful for adding more definition to grayscale maps such as Heightmap, as it can introduce more definition to shapes.

## Parameters

### Inputs

* **Color**: *Color/Grayscale Input*
* **Mosaic Map**: *Grayscale Input*   
  Warp driver map. Can be the same as First input.

### Parameters

* **Samples**: *0 - 16*Determines multi-sample quality.
* **Intensity**: *0.0 - 1.0*Strength of the effect.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="../../../../../../assets/mosaci-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
