---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-blend.html"
breadcrumb-title: ""
description: Use the Normal Blend node to blend normal maps together for creating smooth transitions between surface details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Blend
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Blend
user-guide-description: ""
user-guide-title: ""
---

# Normal Blend

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](normal-blend.resources/normal-blend.png){width="128px"}

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Normal Blend allows you to blend two Normalmaps together with an optional mask, while making sure all values stay normalised. It doesn't differ much from an [atomic Blend Node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blend/blend.md), but has added internal calculations for Normalmaps.

Normal Blend is not intended for combining (overlaying) Normalmaps, where the top map adds detail to the bottom map. For that, use [Normal Combine](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/normal-map/normal-combine/normal-combine.md) instead.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>NormalFG</b> <i>Color Input</i> | Foreground/Top Normalmap. |
| <b>NormalBG</b> <i>Color Input</i> | Background/Bottom Normalmap. |
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Can be toggled with the "Use Mask" parameter. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Use Mask</b> <i>False/True</i> | Toggles the use of the Mask map on or off. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="normal-blend.resources/normalblend-ex.gif" /><br><i>(.gif format introduces dithering in example, in-application results are smooth)</i>
        </td>
    </tr>
</table>
