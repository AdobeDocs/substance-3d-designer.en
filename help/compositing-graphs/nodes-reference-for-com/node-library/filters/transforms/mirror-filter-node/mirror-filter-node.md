---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/mirror-filter-node.html"
breadcrumb-title: ""
description: Use the Mirror filter node to mirror textures horizontally or vertically for creating symmetrical patterns and effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Mirror (Filter Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mirror (Filter Node)
user-guide-description: ""
user-guide-title: ""
---

# Mirror (Filter Node)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](mirror-filter-node.resources/mirror-2.png){width="128px"}

![](mirror-filter-node.resources/mirror-grayscale.png){width="128px"}

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Mirrors the input image over a chosen axis, from a chosen side. Very useful, quick way to get symmetrical effects.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Mode</b> <i>Mirror Axis X, Mirror Axis Y, Mirror Corner</i> | Choose to mirror left-right, top-bottom, or both. |
| <b>Axis X Offset</b> <i>0.0 - 1.0</i> | Only used when Axis X is chosen, define an offset. |
| <b>Axis Y Offset</b> <i>0.0 - 1.0</i> | Only used when Axis Y is chosen, define an offset. |
| <b>Invert Axis X</b> <i>False/True</i> | Only used when Axis X is chosen, Flip direction. |
| <b>Invert Axis Y</b> <i>False/True</i> | Only used when Axis Y is chosen, Flip direction. |
| <b>Corner Type</b> <i>Top Left, Top Right, Bottom Left, Bottom Right</i> | Only used when Corner type is chosen, define what corner to mirror from. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="mirror-filter-node.resources/mirror-example.png" />
        </td>
    </tr>
</table>
