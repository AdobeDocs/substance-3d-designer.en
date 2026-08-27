---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/mosaic.html"
breadcrumb-title: ""
description: Use the Mosaic node to create mosaic tile effects by dividing textures into pixelated blocks and patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Mosaic
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mosaic
user-guide-description: ""
user-guide-title: ""
---

# Mosaic

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](mosaic.resources/mosaic-1.png){width="128px"}

![](mosaic.resources/mosaic-grayscale.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

"Facetises" an existing, smooth, sloping gradient map by performing a multi-pass [Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/warp/warp.md) effect. When the same map is used for both inputs, it essentially grows and accentuates the brightest areas.

This is useful for adding more definition to grayscale maps such as Heightmap, as it can introduce more definition to shapes.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Color</b> <i>Color/Grayscale Input</i> |  |
| <b>Mosaic Map</b> <i>Grayscale Input</i> | Warp driver map. Can be the same as First input. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Samples</b> <i>0 - 16</i> | Determines multi-sample quality. |
| <b>Intensity</b> <i>0.0 - 1.0</i> | Strength of the effect. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="mosaic.resources/mosaci-ex.png" />
        </td>
    </tr>
</table>
