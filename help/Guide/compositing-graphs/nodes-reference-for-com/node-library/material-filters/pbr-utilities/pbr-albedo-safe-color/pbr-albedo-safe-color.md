---
title: "PBR Albedo Safe Color | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > PBR Albedo Safe Color"
---

# PBR Albedo Safe Color

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](pbr-albedo-safe-color.png){width="128px"}

## PBR Albedo Safe Color

**In:** *Material Filters/PBR Utilities*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

This is a utility node that makes corrections if Basecolor or Diffuse values are outside an acceptable, PBR-correct range. When set to Metallic, the node also attempts to correct Basecolor values based on Metallic intensity.

Also see [PBR BaseColor / Metallic Validate](../pbr-basecolor-metallic/pbr-basecolor-metallic-validate.md) for visual feedback on which areas might be wrong.

This is useful as a quick correction tool, especially when one is still learning PBR, but not intended as an absolute measure that is always supposed to be correct.

## Parameters

* **PBR Workflow**: *Base Color - Metallic, Diffuse - Specular*Switches between two different PBR workflows.
* **Tolerance**: *0.0 - 1.0*Amount of tolerance for values that are out-of-range.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
