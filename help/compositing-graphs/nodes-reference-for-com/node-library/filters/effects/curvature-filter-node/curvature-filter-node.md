---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/curvature-filter-node.html"
breadcrumb-title: ""
description: Use the Curvature filter node to generate curvature maps from height maps for detecting convex and concave surfaces.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Curvature (Filter Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Curvature (Filter Node)
user-guide-description: ""
user-guide-title: ""
---

# Curvature (Filter Node)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](curvature-filter-node.resources/curvature-filter-node-01.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs a simple, harsh single-pass curvature conversion to input [Normalmap](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md). The resulting map has white tints for convex areas and black tints for concave. Curvature will always produce pixel-thin lines and sharp transitions.

This node is useful for some quick highlighting or darkening of certain edges. It is limited in comparison to [Curvature Smooth](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/curvature-smooth/curvature-smooth.md) (which produces higher quality results) and [Curvature Sobel](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/curvature-sobel/curvature-sobel.md) (which has more options).

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 10.0</i> | Intensity of the effect. Increases contrast of the result. |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switches between different Normalmap formats (inverts the Green channel). |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="curvature-filter-node.resources/curvature-filter-node-02.png" />
        </td>
    </tr>
</table>
