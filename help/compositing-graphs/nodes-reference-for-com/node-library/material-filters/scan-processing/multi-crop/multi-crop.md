---
title: "Multi Crop | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi Crop"
---

# Multi Crop

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](crop-multi.png){width="128px"}

![](crop-multi-grayscale.png){width="128px"}

## Multi Crop (Grayscale)

**In:** *Material Filters/Scan Processing*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

This is the multi-channel version of Crop. It crops out an area from an image and is mainly intended for use with multi-angle photos, which are then combined with [Multi-Angle to Albedo](../multi-angle-to-albedo/multi-angle-to-albedo.md) or [Multi-Angle to Normal](../multi-angle-to-normal/multi-angle-to-normal.md).

>[!NOTE]
>
> See the original [Crop](../crop/crop.md) for more info.

## Parameters

### Parameters

* **Input Count**: *1 - 8*Sets the number of inputs to process in parallel.
* **Input Size**: *0 - 8192*Input images' resolution and proportions. Very important for non-square images.
* **Background**: *(Color value) / (Grayscale value)*Background uniform value for areas not covered by Crop.
* **Transform**: *(Transformation Matrix)*  
  Rotates and scales the result. The result can be modified by directly interacting with the canvas.
* **Offset**: *0.0 - 1.0*  
  Moves or translates the result. The result can be modified by directly interacting with the canvas.
* **Is Normal (only for Color version)**: *False/True*Whether or not the input should be treated as a Normalmap.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>

 