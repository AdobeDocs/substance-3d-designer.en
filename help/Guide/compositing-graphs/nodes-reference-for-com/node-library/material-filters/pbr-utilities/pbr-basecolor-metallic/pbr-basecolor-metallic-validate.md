---
title: "PBR BaseColor  Metallic Validate | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > PBR BaseColor  Metallic Validate"
---

# PBR BaseColor / Metallic Validate

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](pbr-basecolor-metallic-validate.png){width="128px"}

## PBR BaseColor / Metallic Validate

**In:** *Material Filters/PBR Utilities*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

A utility node that generates a Good-to-Bad "Heatmap" on which values are correct or incorrect according to PBR standards.

It is very useful as a learning tool for PBR, since it provides very clear visual feedback of what the mistakes are and where they can be found.

Don't use this as the end-all-tool, but still make sure you always have a clear understanding of why you're breaking any rules this tool might highlight.

## Parameters

* **Validation Mode**: *Albedo , Metal, Combined*Sets wether to check only Albedo, Metal, or both combined as an overview mode.
* **Albedo Dark Range Threshold**: *50 sRGB, 30 sRGB*Sets the lower Albedo limit to either 50 or 30 sRGB. Can decrease or increase tolerance for red areas.
* **Metal Reflectance Range**: *70-100% Reflective, 60-100% Reflective*Changes Metallic range to be deemed correct. Can decrease or increase tolerance for red areas.
* **Overlay Map**: *False/True*Quick debug mode to overlay input maps, allows for quicker tracking down of problem areas.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
