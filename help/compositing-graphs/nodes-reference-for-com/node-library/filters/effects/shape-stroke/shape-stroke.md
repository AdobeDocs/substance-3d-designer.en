---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/shape-stroke.html"
breadcrumb-title: ""
description: Use the Shape Stroke node to add stroke outlines to shapes for creating borders and edge effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Shape Stroke
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape Stroke
user-guide-description: ""
user-guide-title: ""
---

# Shape Stroke

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](shape-stroke.resources/shape-stroke.png){width="128px"}

![](shape-stroke.resources/shape-stroke-grayscale.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Adds a stroke or outline around a black and white mask (for the grayscale version) or a shape with an alpha channel (for the color version), as you might be familiar with from other 2D Image editing applications. Can be seen as a more complete version of [Edge Detect](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/edge-detect/edge-detect.md).

Very useful for a variety of image editing effects.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Width</b> <i>-1.0 - 1.0</i> | Width of the stroke effect. |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Global Opacity of the effect. |
| <b>(Outline) Color</b> <i>(Color value)</i> | Color used for the outline effect. |
| <b>Mask Color</b> <i>(Color value) (Grayscale Version Only)</i> | Solid color to be used for the transparency mapped output. |
| <b>Input Is Pre-Multiplied</b> <i>False/True (Color Version Only)</i> | Whether the input should be assumed as pre-multiplied. |
| <b>Pre-Multiply Output</b> <i>False/True</i> | Whether the output should be pre-multiplied. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="shape-stroke.resources/shapestroke-ex.png" />
        </td>
    </tr>
</table>
