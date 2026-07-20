---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/multi-angle-to-normal.html"
breadcrumb-title: ""
description: Use the Multi-Angle to Normal node to generate normal maps from multi-angle scanned images for accurate surface detail.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi-Angle to Normal
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi-Angle to Normal
user-guide-description: ""
user-guide-title: ""
---

# Multi-Angle to Normal

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/multi-angle-to-normal.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node constructs a Normalmap out of a set of photographs/scans made under different lighting conditions. It allows for a much more accurate Normalmap conversion than when trying to extract Normals from one single albedo image.

It is more complicated than [Multi-Angle to Albedo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-albedo/multi-angle-to-albedo.md), as it requires you to use set, precise lighting angles for your inputs. Every sample's lighting angle should be spaced evenly and samples need to be input in sequence. So for three samples, lighting angles should be taken at: 0, 120, 240 - or any uniform offset of that (such as 90, 210, 330).

>[!NOTE]
>
> See [Multi-Angle to Albedo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-albedo/multi-angle-to-albedo.md) for the albedo version of this node. If you want to pre-process your inputs, [Multi Color Equalizer](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-color-equalizer/multi-color-equalizer.md), [Multi Crop](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-crop/multi-crop.md) and [Multi Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-clone-patch/multi-clone-patch.md) can be of use, since they are intended to be combined with these nodes.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input 1-8</b> <i>Color Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Samples Amount</b> <i>2 - 8</i> | Sets amount of samples (inputs) to process. |
| <b>Intensity</b> <i>0.0 - 1.0</i> | Sets Normalmap intensity. |
| <b>First Sample Light Angle</b> <i>0.0 - 360.0</i> | Sets the lighting angle direction of the first input. |
| <b>Next Sample Light Angle</b> <i>Counterclockwise, Clockwise</i> | Sets towards which direction the lighting in the next sample moves. |
