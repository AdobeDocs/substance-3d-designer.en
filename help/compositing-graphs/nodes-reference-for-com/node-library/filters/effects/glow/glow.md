---
title: "Glow"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Glow"
---

# Glow

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](glow-greyscale.png){width="128px"}

![](glow-3.png){width="128px"}

## Glow

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs an "Outer Glow"-type of effect, as seen in other popular image editing software. Essentially adds a fading gradient outline around the input.

Keep in mind that this is not intended to work for images with Alpha Channels, as you might expect. Even the color version only expects binary, black and white masks as input; it only allows for using a colored glow. If you're after a version that works on images with transparency, see [Shape Glow](../shape-glow/shape-glow.md).

Important: make sure to use the appropriate version for your input! Use "Glow" for Color inputs, or "Glow Grayscale" for Grayscale inputs.

## Parameters

* **Glow Amount**: *0.0 - 1.0*Global opacity for the glow effect.
* **Clear Amount**: *0.0 - 1.0*Treshold for when to cut off the glow effect. Useful for semi-transparent areas.
* **Glow Size**: *0.0 - 20.0*Controls how far the glow effect reaches.
* **Glow Color**: *(Color value) (Color Version Only)*Sets the color of the glow effect.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="glow-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
