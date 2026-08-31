---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/noise-upscale-1.html"
breadcrumb-title: ""
description: Use the Noise Upscale 1 node to upscale textures using noise-based algorithms for preserving detail when increasing texture resolution.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Noise Upscale 1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Noise Upscale 1
user-guide-description: ""
user-guide-title: ""
---

# Noise Upscale 1

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](noise-upscale-1.resources/noise-upscale-1-01.png){width="128px"}

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Takes an input noise procedural and scales it up to double resolution, keeping detail but without introducing too much tiling. Uses an "X" type of mask and blends with contrast similar to the original input (internal blend mode is Copy).

This node is mostly intended for optimising slow graphs that use heavy, big noises. It allows you to use higher resolutions without introducing too much extra compute time.

See also [Noise Upscale 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/noise-upscale-2/noise-upscale-2.md) and [Noise Upscale 3](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/noise-upscale-3/noise-upscale-3.md) for different variations of this process.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Offset1X</b> <i>0.0 - 1.0</i> | Slides top and bottom parts over X axis. |
| <b>Offset1Y</b> <i>0.0 - 1.0</i> | Slides top and bottom parts over Y axis. |
| <b>Offset2X</b> <i>0.0 - 1.0</i> | Slides left and right parts over X axis. |
| <b>Offset2Y</b> <i>0.0 - 1.0</i> | Slides left and right parts over Y axis. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="noise-upscale-1.resources/noise-upscale-1-02.png" />
        </td>
    </tr>
</table>
