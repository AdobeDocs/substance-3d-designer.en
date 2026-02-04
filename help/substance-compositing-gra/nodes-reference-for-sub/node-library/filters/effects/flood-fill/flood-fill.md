---
title: "Flood Fill"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill"
---

# Flood Fill

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](floodfill.png){width="128px"}

## Flood Fill

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Flood Fill is part of an advanced set of effects that allow you to add much more variation to a basic, binary tiles texture. It is not meant to be used by itself: instead, it is more of a starting point for Other Flood Fill effects. This split, separate data allows for a more dynamic, more optimized and less destructive workflow.

The other Flood Fill effects are [Flood Fill to Gradient](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-to-gradient/flood-fill-to-gradient.md), [Flood Fill to Color/Grayscale](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-grayscale-col/flood-fill-to-grayscale-color.md), [Flood Fill to Random Grayscale](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-random-gra/flood-fill-to-random-grayscale.md), [Flood Fill to Random Color](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-random-color/flood-fill-to-random-color.md), [Flood Fill to BBox Size](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-to-bbox-size/flood-fill-to-bbox-size.md), [Flood Fill to Position](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-to-position/flood-fill-to-position.md), [Flood Fill Mapper](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-mapper/flood-fill-mapper.md) and [Flood Fill to Index](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-to-index/flood-fill-to-index.md)

>[!WARNING]
>
> The input map needs to be suited to Flood Fill to work. Ideally it is a binary map (black/white only, no grayscale) where every tile is separated from the other lines by a border that is full black (0,0,0) for every pixel. An example of a perfect candidate for this is the [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md).
> 
> Problems arise if tiles are not separated by full black pixels, usually when grayscale, sloping values are used. You can identify this by an overall lack of red values in the result, and possibly strange artifacting lines. In such cases, adjust the contrast on the input map or switch the input map out. Make sure to change the Safety/Speed trade-off setting to see if anything improves.

## Parameters

* **Safety/Speed trade-off**: *Simple or small shapes, Complex or big shapes, No failure mode.*Set the calculation mode to best suit input shapes. Allows for much more accurate results if the correct mode is chosen.
* **Avanced options**: *Display advanced Parameters and Output/Hide advanced Parameters and Output*
* **Override Safety/Speed trade-off**: *-1 - 100*Only visible with Advanced Options on. Allows for overriding internal features. Very advanced, serves for creating own effects or debugging.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="flood-ex2.png" width="256px"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c1_image" src="flood-ex1.png" width="256px"/></div> |
| --- | --- |
|  |  |

Good and bad examples of results from Flood Fill.

</td>
</tr>
</table>
