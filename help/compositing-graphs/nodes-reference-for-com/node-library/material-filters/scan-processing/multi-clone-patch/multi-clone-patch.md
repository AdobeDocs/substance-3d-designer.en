---
title: "Multi Clone Patch | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi Clone Patch"
---

# Multi Clone Patch

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](clone-patch-multi.png){width="128px"}

![](clone-patch-multi-grayscale.png){width="128px"}

## Multi Clone Patch (Grayscale)

**In:** *Material Filters/Scan Processing*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This node is the Multi-input version of [Clone Patch](../clone-patch/clone-patch.md). It links together up to eight inputs and performs the exact same Clone Patch operation on all of them. It is mainly intended for use with multi-angle photos, which are then combined with [Multi-Angle to Albedo](../multi-angle-to-albedo/multi-angle-to-albedo.md) or [Multi-Angle to Normal](../multi-angle-to-normal/multi-angle-to-normal.md).

>[!NOTE]
>
> See [Clone Patch](../clone-patch/clone-patch.md) for more info, see [Material Clone Patch](../material-clone-patch/material-clone-patch.md) for the material version.

## Parameters

### Parameters

* **Input Count**: *1 - 8*Sets amount of inputs that will receive the same Patch operation.
* **Is Normal (only for Color)**: **False/True**Sets whether the input is a Normalmap, and whether blending should be treated as such.
* **Shape**: **Square, Disc**Sets Stamp shape. Used only as base.
* **Edge**  
  * **Threshold**: *0.0 - 1.0*Sets how far the blended area should reach. This grows in steps along shapes in the target area; it has very little effect with uniform backgrounds*.*
  * **Blur**: *0.0 - 2.0*Blurs the edges of the stamp area, in case a softer transition is needed.
  * **Smoothness**: *0.0 - 2.0*Rounds off the edges of the stamp shape, making for smoother-flowing outlines.
  * **Grid Resolution**: *1 - 11*Sets quality resolution of the blending analysis. A higher value means more accurate blending.
* **Transformations**  
  * **Source Matrix**: *(Transformation Matrix)*Transforms source (Scale &amp; Rotation). Cannot be done on canvas, change through these parameters only.
  * **Source Offset**: *-0.5 - 0.5*Translates source location. Cannot be done on canvas, change through these parameters only. *This parameter is probably the main one you want to change!*
  * **Target Matrix**: *(Transformation Matrix)*Transforms target location (Scale &amp; Rotation). Can also be done through gizmo on canvas.
  * **Target Offset**: *-0.5 - 0.5*Translates target location. Can also be done through gizmo on canvas.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>

 