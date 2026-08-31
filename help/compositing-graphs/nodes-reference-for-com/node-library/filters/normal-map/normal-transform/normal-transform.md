---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-transform.html"
breadcrumb-title: ""
description: Use the Normal Transform node to apply transformations to normal maps while preserving vector directions correctly.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Transform
user-guide-description: ""
user-guide-title: ""
---

# Normal Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](normal-transform.resources/normal-transform-01.png){width="128px"}

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Similar to the atomic Transform 2D node, this allows for transformation of Normalmaps without breaking Tangent-space, instead it is recalculated on the fly, resulting in always correct Normalmaps.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Matrix2x2</b> <i>(Transformation Matrix):</i> | Rotate or Scale the input. |
| <b>Offset</b> <i>-0.5 - 0.5</i> | Moves or translates the result. When the Transformation control is present, result can be modified by directly interacting with the canvas. |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switch between different Normal Map formats (inverts the green channel) |
