---
title: "Lighting Cancel High Frequencies | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Lighting Cancel High Frequencies"
---

# Lighting Cancel High Frequencies

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](lighting-cancel-high-frequencies.png){width="128px"}

## Lighting Cancel High Frequencies

**In:** *Filters/Adjustments*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Similar to [Highpass](../highpass/highpass.md), but more suited for full color images (it doesn't desaturate the result as much), this node tries to cancel out high frequency, small lighting details.

Also see [Lighting Cancel Low Frequencies](../lighting-cancel-low-fre/lighting-cancel-low-frequencies.md), and the more advanced, recommended [Luminance Highpass](../luminance-highpass/luminance-highpass.md).

## Parameters

* **Intensity**: *0.0 -* 1.0  
  Strength of the lighting cancel effect.
* **Radius**: *0.0 - 10.0*Radius or size of the lighting details to cancel.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="lighting-cancel-highfrequencies-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
