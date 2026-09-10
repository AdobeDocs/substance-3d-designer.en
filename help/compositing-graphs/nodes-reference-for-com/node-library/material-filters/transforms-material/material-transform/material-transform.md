---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/transforms-material/material-transform.html"
breadcrumb-title: ""
description: Use the Material Transform node to apply transformations to material outputs including rotation, scale, and offset.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Transforms (Material) > Material Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Transform
user-guide-description: ""
user-guide-title: ""
---

# Material Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](material-transform.resources/material-transforms.png){width="128px"}

<b>In:</b> Material Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Material Transform is simply the "Multi-Channel" Materials version of [the atomic Transformation 2D node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/transformation-2d/transformation-2d.md). It transforms all channels of an input material at the same time, with the same interface as Transform 2D.

Just make sure to set up the Channels properly! By default, both Metallic/Roughness and Specular/Glossiness are enabled, which could lead to some confusion.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Transformation</b> <i>(Transformation Matrix)</i> | Rotates and scales the result. Moving/panning is done via the Offset parameter |
| <b>Offset</b> <i>-0.5 - 0.5</i> | Moves or translates the result. When the Transformation control is present, the result can be modified by directly interacting with the canvas. |
| <b>Normal Format</b> | Choose between DirectX and OpenGL formats (flip green). |
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
