---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blurs/blur-hq.html"
breadcrumb-title: ""
description: Use the Blur HQ node to apply high-quality blur effects to textures for creating smooth, professional-looking blur results.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blurs > Blur HQ
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Blur HQ
user-guide-description: ""
user-guide-title: ""
---

# Blur HQ

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](blur-hq.resources/blur-hq-1.png){width="128px"}

![](blur-hq.resources/blur-hq-grayscale.png){width="128px"}

<b>In:</b> Filters &gt; Blurs

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs a High-Quality gaussian blur on the result. Much better quality than [the standard atomic box blur](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blur/blur.md)[.](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blur/blur.md)

Important: make sure to use the appropriate version for your input! Use "Blur HQ" for Color inputs, or "Blur HQ Grayscale" for Grayscale inputs.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 16.0</i> | Strength (Radius) of the blur. The higher this value, the further the blur will reach. |
| <b>Quality</b> <i>0 - 1</i> | Increases internal sampling amount for even higher quality, at reduced computation speed. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="blur-hq.resources/hqblur-example.gif" />
        </td>
    </tr>
</table>
