---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-sobel.html"
breadcrumb-title: ""
description: Use the Normal Sobel node to generate normal maps from height maps using Sobel edge detection for surface detail.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Sobel
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Sobel
user-guide-description: ""
user-guide-title: ""
---

# Normal Sobel

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/normal-hq.png){width="128px"}

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Converts a Heightmap input to a Normalmap output. A slightly more advanced version of the [Normal Atomic Node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md), this node uses Sobel sampling rather than the standard sampling method.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 3.0</i> | Strength of the converted normals. |
| <b>Normal Format</b> <i>OpenGL, DirectX</i> | Switches between different Normalmap formats (inverts the green channel). |
