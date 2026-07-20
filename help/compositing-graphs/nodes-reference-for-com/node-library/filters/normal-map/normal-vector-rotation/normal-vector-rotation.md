---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-vector-rotation.html"
breadcrumb-title: ""
description: Use the Normal Vector Rotation node to rotate normal map vectors for adjusting surface lighting and detail orientation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Vector Rotation
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Vector Rotation
user-guide-description: ""
user-guide-title: ""
---

# Normal Vector Rotation

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/normal-vector-rotation.png){width="128px"}

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Normal utility node that rotates all vectors of an input Normalmap in Tangent space. Doesn't actually transform pixels, instead it modifies the values they represent. It can make use of an optional map to add random rotations to grayscale facets.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Normal</b> <i>Color Input</i> | Base map to perform rotation on. Required. |
| <b>Rotation Map (optional)</b> <i>Grayscale Input</i> | Grayscale map that modulates Rotation strength. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Rotation Angle</b> <i>0.0 - 1.0</i> | Sets Angle by which to rotate the Normalmap |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switch between different Normal Map formats (inverts the green channel) |
