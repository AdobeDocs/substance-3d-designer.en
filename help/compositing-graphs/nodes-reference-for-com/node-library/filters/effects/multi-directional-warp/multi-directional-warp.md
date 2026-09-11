---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/multi-directional-warp.html"
breadcrumb-title: ""
description: Use the Multi Directional Warp node to apply warping effects in multiple directions for creating complex distortion patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Multi Directional Warp
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi Directional Warp
user-guide-description: ""
user-guide-title: ""
---

# Multi Directional Warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](multi-directional-warp.resources/multi-directional-warp-color.png)![](multi-directional-warp.resources/multi-directional-warp-grayscalepng.png)

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Multi-Directional Warp applies [Directional Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/directional-warp/directional-warp.md) multiple times in opposite directions while the displaced texture stays in place. It differs from the standard Directional Warp in that it can push in multiple directions, whereas the atomic version only allows for one. In this way it solves the classic problem where Directional Warp always seems to push your image away too much in a single direction, instead it works along multiple directions or axes instead of a single direction.

It differs mainly from [Non Uniform Directional Warp](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/non-uniform-directional/non-uniform-directional-warp.md) in that it is slightly more limited: the direction for the warp is only controlled through parameters, and can not be set through an input map. The advantage is it is slightly easier to use and can be more precise depending on your usecase.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Grayscale/Color Input</i> | Base map to which the warping will be applied. Can be color or grayscale. |
| <b>Intensity Input</b> <i>Grayscale Input</i> | Mandatory mask map that drives the intensity of the warping effect, must be grayscale. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 20.0</i> | Sets the intensity of the warp effect, how far to push pixels out. |
| <b>Warp Angle</b> <i>0.0 - 1.0</i> | Sets the Angle or direction in which to apply the Warp effect. |
| <b>Mode</b> <i>Average, Max, Min, Chain</i> | Sets the Blend mode for consecutive passes. Only has effect if Direcions is 2 or 4! |
| <b>Directions</b> <i>1, 2, 4</i> | Sets in how many Axes the warp works. 1 means it moves in the direction of the Angle, and the opposite of that direction, 2 means the axis of the angle, plus the perpendicular axis, 4 means the previous axes, plus 45 degree inclements. |
