---
title: "Mosaic"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Mosaic"
---

# Mosaic

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](mosaic-1.png){width="128px"}

![](mosaic-grayscale.png){width="128px"}

## Mosaic (Grayscale)

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

"Facetises" an existing, smooth, sloping gradient map by performing a multi-pass [Warp](../../../../atomic-nodes/warp/warp.md) effect. When the same map is used for both inputs, it essentially grows and accentuates the brightest areas.

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

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="mosaci-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
