---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/multi-clone-patch.html"
breadcrumb-title: ""
description: Use the Multi Clone Patch node to clone and patch multiple texture channels for repairing scanned material artifacts.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi Clone Patch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi Clone Patch
user-guide-description: ""
user-guide-title: ""
---

# Multi Clone Patch

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](multi-clone-patch.resources/multi-clone-patch-01.png){width="128px"}

![](multi-clone-patch.resources/multi-clone-patch-02.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node is the Multi-input version of [Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md). It links together up to eight inputs and performs the exact same Clone Patch operation on all of them. It is mainly intended for use with multi-angle photos, which are then combined with [Multi-Angle to Albedo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-albedo/multi-angle-to-albedo.md) or [Multi-Angle to Normal](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-normal/multi-angle-to-normal.md).

>[!NOTE]
>
> See [Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md) for more info, see [Material Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/material-clone-patch/material-clone-patch.md) for the material version.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Input Count</b> <i>1 - 8</i> | Sets amount of inputs that will receive the same Patch operation. |
| <b>Is Normal (only for Color)</b> <i>False/True</i> | Sets whether the input is a Normalmap, and whether blending should be treated as such. |
| <b>Shape</b> <i>Square, Disc</i> | Sets Stamp shape. Used only as base. |
| <b>Edge</b> |  |
| <b>Threshold</b> <i>0.0 - 1.0</i> | Sets how far the blended area should reach. This grows in steps along shapes in the target area; it has very little effect with uniform backgrounds. |
| <b>Blur</b> <i>0.0 - 2.0</i> | Blurs the edges of the stamp area, in case a softer transition is needed. |
| <b>Smoothness</b> <i>0.0 - 2.0</i> | Rounds off the edges of the stamp shape, making for smoother-flowing outlines. |
| <b>Grid Resolution</b> <i>1 - 11</i> | Sets quality resolution of the blending analysis. A higher value means more accurate blending. |
| <b>Transformations</b> |  |
| <b>Source Matrix</b> <i>(Transformation Matrix)</i> | Transforms source (Scale &amp; Rotation). Cannot be done on canvas, change through these parameters only. |
| <b>Source Offset</b> <i>-0.5 - 0.5</i> | Translates source location. Cannot be done on canvas, change through these parameters only. *This parameter is probably the main one you want to change!* |
| <b>Target Matrix</b> <i>(Transformation Matrix)</i> | Transforms target location (Scale &amp; Rotation). Can also be done through gizmo on canvas. |
| <b>Target Offset</b> <i>-0.5 - 0.5</i> | Translates target location. Can also be done through gizmo on canvas. |
