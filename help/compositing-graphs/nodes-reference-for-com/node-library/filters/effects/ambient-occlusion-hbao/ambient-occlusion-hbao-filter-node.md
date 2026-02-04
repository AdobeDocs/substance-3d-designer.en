---
title: "Ambient Occlusion (HBAO) (Filter Node) | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Ambient Occlusion (HBAO) (Filter Node)"
---

# Ambient Occlusion (HBAO) (Filter Node)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](hbao.png){width="128px"}

## Ambient Occlusion (HBAO)

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Takes a Heightmap as input and generates an Ambient Occlusion map from that. It uses Horizon-Based Ambient Occlusion, an algorithm originally intended for screen-space realtime AO-generation. Very useful for creating procedural AO maps from procedural Heightmaps.

For an alternative, more advanced but slower version of AO, see [Ambient Occlusion (RTAO)](../ambient-occlusion-rtao/ambient-occlusion-rtao.md)

## Parameters

* **Use World Units**: *False/True*Toggles use of world or sceen-space units. Enables extra parameters that allow for more precise control.
* **Height Depth**: *0.0 - 1.0*Only used when World Units is set to False. Controls global scaling.
* **Surface Size**: **0.0 - 1000.0**Only used when World Units is set to True. Controls global scaling.
* **Height Scale (cm)**: *0.0 - 1000.0*Only used when World Units is set to True. Controls global scaling.
* **Radius**: *0.0 - 1.0*Controls the spread of the AO.
* **Quality**: *4 samples, 8 samples, 16 samples*  
  Sets Quality level by determining amount of samples used for calculation.
* **GPU Optimization**: *False/True*Enables internal GPU optimisation, speeds up processing.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="image2021-6-18-11-11-11-1.png" width="300px"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c1_image" src="image2021-6-18-11-11-22.png" width="300px"/></div> |
| --- | --- |
|  |  |

</td>
</tr>
</table>

 