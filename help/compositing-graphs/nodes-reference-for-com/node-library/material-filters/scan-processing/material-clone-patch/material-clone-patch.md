---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/material-clone-patch.html"
breadcrumb-title: ""
description: Use the Material Clone Patch node to clone and patch texture regions for repairing artifacts in scanned materials.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Material Clone Patch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Clone Patch
user-guide-description: ""
user-guide-title: ""
---

# Material Clone Patch

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](material-clone-patch.resources/clone-patch-material.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is the Multi-Channel, full material version of [Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md). It performs a Clone Patch on any and all channels of a material. [See the original version for more information!](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md)

This is very useful if you want to remove a detail from all channels of a material. Outputs debug images for multiple channels to see what the smart patch area looks like exactly.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Shape</b> <i>Square, Disc</i> | Sets Stamp shape. Used only as base. |
| <b>Edge</b> |  |
| <b>Threshold (for multiple channels)</b> <i>0.0 - 1.0</i> | Sets how far the blended area should reach. This grows in steps, along shapes in the target area, so it has very little effect with uniform backgrounds. Be careful with changing this too much between channels, as it could lead to visual discrepancies! |
| <b>Blur</b> <i>0.0 - 2.0</i> | Blurs the edges of the stamp area in case a softer transition is needed. |
| <b>Smoothness</b> <i>0.0 - 2.0</i> | Rounds off the edges of the stamp shape, making for smoother-flowing outlines. |
| <b>Grid Resolution</b> <i>1 - 11</i> | Sets the quality resolution of the blending analysis. A higher value means more accurate blending. |
| <b>Transformations</b> |  |
| <b>Source Matrix</b> <i>(Transformation Matrix)</i> | Transforms source (Scale &amp; Rotation). Cannot be done on canvas, change through these parameters only. |
| <b>Source Offset</b> <i>-0.5 - 0.5</i> | Translates source location. Cannot be done on canvas, change through these parameters only. *This parameter is probably the main one you want to change!* |
| <b>Target Matrix</b> <i>(Transformation Matrix)</i> | Transforms target location (Scale &amp; Rotation). Can also be done through gizmo on canvas. |
| <b>Target Offset</b> <i>-0.5 - 0.5</i> | Translates target location. Can also be done through gizmo on canvas. |
