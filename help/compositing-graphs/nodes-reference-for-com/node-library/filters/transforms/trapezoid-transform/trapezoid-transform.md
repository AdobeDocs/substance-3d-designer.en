---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/trapezoid-transform.html"
breadcrumb-title: ""
description: Use the Trapezoid Transform node to apply trapezoidal distortion to textures for creating perspective correction effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Trapezoid Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Trapezoid Transform
user-guide-description: ""
user-guide-title: ""
---

# Trapezoid Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](trapezoid-transform.resources/trapeze-transform.png){width="128px"}

![](trapezoid-transform.resources/trapeze-transform-grayscale.png){width="128px"}

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Special transform node that modifies the input in a perspective/trapezoid warp manner. Has control for Top and Bottom stretch. Values can be pushed beyond limits for stronger effects.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Top Stretch</b> <i>0.0 - 1.0</i> | Set the amount of stretch or squash at the top. |
| <b>Bottom Stretch</b> <i>0.0 - 1.0</i> | Set the amount of stretch or squash at the botton. |
| <b>Background Color</b> <i>(Grayscale/Color value)</i> | Set solid background color in case tiling is turned off. |
| <b>Sampling</b> <i>Bilinear, Nearest</i> | Set sampling quality. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="trapezoid-transform.resources/trapeze-example.gif" />
        </td>
    </tr>
</table>
