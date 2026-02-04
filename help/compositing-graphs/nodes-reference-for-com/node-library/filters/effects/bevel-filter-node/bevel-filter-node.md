---
title: "Bevel (Filter Node) | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Bevel (Filter Node)"
---

# Bevel (Filter Node)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](bevel.png){width="128px"}

## Bevel

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Peforms an edge-beveling effect on an input grayscale Heightmap. Returns both beveled Heightmap and Normalmap based on that Heightmap.

This is a useful node for applying exact curve profiles on an ideally binary (high contract black/white), basic Heightmap.

## Parameters

### Inputs

* **input**: *Grayscale Input*   
  Heightmap to convert.
* **Custom Curve**: *Grayscale Input*   
  Gradient that determines the exact curve/slope. Ideally a Gradient Linear node, on which you can perform any kind of adjustment such as [Levels](../../../../atomic-nodes/levels/levels.md) or [Curves](../../../../atomic-nodes/curve/curve.md). Only active when "Use Custom Curve" is True.

### Parameters

* **Distance**: *-1.0 - 1.0*How far the bevel effect should reach.
* **Corner Type**: *Round, Angular*Whether the beveling profile should be rounded or straight.
* **Smoothing**: *0.0 - 5.0*How much additional smoothing (blurring) to perform after the bevel.
* **Use Non-Uniform Blur**: *False/True*Whether smoothing should be done non-uniformly.
* **Use Custom Curve**: *False/True*Toggles use of your own custom height curve. See above for more info.
* **Normal Intensity**: *0.0 - 50.0*Intensity of the generated Normalmap.
* **Normal Format**: *DirectX, OpenGL*  
  Switch between different Normalmap formats (inverts the Green channel).

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="bevel-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>

 