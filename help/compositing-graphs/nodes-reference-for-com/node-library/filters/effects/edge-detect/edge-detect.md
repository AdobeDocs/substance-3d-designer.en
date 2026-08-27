---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/edge-detect.html"
breadcrumb-title: ""
description: Use the Edge Detect node to detect edges in textures for creating outlines and edge-based mask effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Edge Detect
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Edge Detect
user-guide-description: ""
user-guide-title: ""
---

# Edge Detect

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](edge-detect.resources/edge-detect.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Detects contrast in a black and white images, then creates a black and white mask highlighting the contrast.

Useful in many cases where some sort of mask for edges is needed. Keep in mind that it works best with high-contrast input; if needed, adjust the contrast before passing something into this node.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Edge Width</b> <i>1.0 - 16.0</i> | Width of the detected areas around the edges. |
| <b>Edge Roundness</b> <i>0.0 - 16.0</i> | Rounds, blurs and smooths together the generated mask. |
| <b>Invert</b> <i>False/True</i> | Inverts the result. |
| <b>Tolerance</b> <i>0.0 - 1.0</i> | Tolerance treshold factor for where edges should appear. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="edge-detect.resources/edge-detect-ex.png" />
        </td>
    </tr>
</table>
