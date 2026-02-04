---
title: "Crop | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Crop"
---

# Crop

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](crop-10.png){width="128px"}

![](crop-grayscale.png){width="128px"}

## Crop (Grayscale)

**In:** *Material Filters/Scan Processing*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Crop is a parametric, non-destructive version of the familiar crop tool. You select an area of an image and the result is returned with the unselected areas discarded.

It can be useful in many ways, as performing a Crop operation with atomic nodes is not so straightforward. Especially for converting non-square images, this node comes in handy. Make sure to set the input resolution correctly in that case.

Very important to understand is that to use this node with ease, you must make good use of the ability to preview a different node than the one whose parameters you're editing!  
In short: **Double-click** the node you are using as input for this one (the original, uncropped image), then **single-click** the crop node that follows right after it. You can then modify the crop gizmo to fit the area you want to crop to.

## Parameters

* **Input Size**: *0 - 8192*Input image's resolution and proportions. Very important for non-square images.
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

 