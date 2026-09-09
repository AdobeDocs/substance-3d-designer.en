---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/quad-transform.html"
breadcrumb-title: ""
description: Use the Quad Transform node to apply quadrilateral transformations to textures for perspective correction and warping.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Quad Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Quad Transform
user-guide-description: ""
user-guide-title: ""
---

# Quad Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](quad-transform.resources/quad-transform-grayscale.png){width="128px"}

![](quad-transform.resources/quad-transform.png){width="128px"}

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Special transform node that allows transformation of a quad shape through interaction with its corner points. Allows very specific transforms in a hands-on way.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>p00</b> | Top Left Point. |
| <b>p01</b> | Bottom Left Point |
| <b>p10</b> | Top Right Point. |
| <b>p11</b> | Bottom Right Point. |
| <b>Culling</b> <i>Front only, Back only, Front over Back, Back over Front</i> | Set culling/hiding of shape when points cross over each other. |
| <b>Enable Tiling</b> <i>False/True</i> |  |
| <b>Background Color</b> <i>(Grayscale value)</i> | Solid background color if tiling is off. |
| <b>Sampling</b> <i>Bilinear, Nearest</i> | Set sampling quality. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="quad-transform.resources/quad-example.gif" />
        </td>
    </tr>
</table>
