---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-to-height-hq.html"
breadcrumb-title: ""
description: Use the Normal To Height HQ node to convert normal maps to high-quality height maps for surface detail extraction.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal To Height HQ
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal To Height HQ
user-guide-description: ""
user-guide-title: ""
---

# Normal To Height HQ

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](normal-to-height-hq.resources/normal-to-height-hq.png){width="128px"}

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A reverse-conversion node that attempts to convert a tangent-space Normalmap back into a Heightmap. This is the more advanced node; [Normal to Height](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/normal-map/normal-to-height/normal-to-height.md) has less options and uses different calculations.

Useful for when you only have a Normalmap source, yet still want to perform operations combining it with a Heightmap. Keep in mind that this will never be able to provide a 100% correct result, as information is lost by nature of the process when Height is converted to Normal. It can never replace a properly generated Heightmap!

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Relief Balance</b> <i>0.0 - 1.0</i> | Blends between low and high frequency bias. |
| <b>Height Intensity</b> <i>0.0 - 1.0</i> | Intensity or multiplier for the Heightmap, works a bit like global opacity. |
| <b>Height Normalize</b> <i>False/True</i> | Automatically scales the Heightmap range to use full contrast, like an [auto-levels](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/auto-levels/auto-levels.md). |
| <b>Quality</b> <i>Normal, High</i> | Switches between speed or quality. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="normal-to-height-hq.resources/normal2height-hq-ex.png" />
        </td>
    </tr>
</table>
