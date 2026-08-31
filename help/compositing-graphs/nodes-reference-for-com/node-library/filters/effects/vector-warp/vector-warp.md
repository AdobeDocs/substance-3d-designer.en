---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/vector-warp.html"
breadcrumb-title: ""
description: Use the Vector Warp node to warp textures using vector fields for creating fluid and organic distortion effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Vector Warp
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Vector Warp
user-guide-description: ""
user-guide-title: ""
---

# Vector Warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](vector-warp.resources/vector-warp-01.png){width="128px"}

![](vector-warp.resources/vector-warp-02.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Vector warp is an advanced distortion effect, similar to [Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/warp/warp.md) and [Directional Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/directional-warp/directional-warp.md), with the main difference being that it is driven by a (color) vector bitmap rather than a grayscale map. This means it is more powerful and versatile than its atomic node cousins.

The Vector Map is similar to a Normalmap, but it does not need to be normalised and only the R and Green (X and Y) channel are used. Blue and Alpha channels can be left black if you want. Constructing a good Vector Map can be the biggest challenge in using this node; you can either [convert grayscale maps to Normal](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md), or construct the map by combining channels with[ RGBA Merge.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/channels/rgba-merge/rgba-merge.md) Alternatively, something like a ["Flow Map"](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/painting/advanced-channel-painting/flow-map-painting) is also useable.

This node can be useful when you want to do very specific distortions with varying directions, where standard Warp nodes don't cut it.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Color Input</i> | Map to distort. |
| <b>Vector Map</b> <i>Color Input</i> | Distortion driver map. Color channels Red and Blue are used. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 1.0</i> | Intensity multiplier for the Vector Map. |
| <b>Vector Format</b> <i>DirectX, OpenGL</i> | Swaps the Green channel between Up and Down interpretation. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="vector-warp.resources/vector-warp-03.png" />
        </td>
    </tr>
</table>
