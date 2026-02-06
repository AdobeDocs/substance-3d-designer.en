---
title: "Flood Fill to BBox Size"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to BBox Size"
---

# Flood Fill to BBox Size

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](floodfill-to-bbox-size.png){width="128px"}

## Flood Fill to BBox Size

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a grayscale map from a [Flood Fill](../flood-fill/flood-fill.md) base, with values tied to each tile's individual size.

Values are relative to the total canvas size (a full white tile would mean it stretches the entire canvas), so contrast is often low.

## Parameters

* **Output**: *max(X, Y), X, Y*Sets what metric the value is based on: width, length or both.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="floodbbox-ex1.png" width="256px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
