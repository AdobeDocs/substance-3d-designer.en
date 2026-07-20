---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/clone-filter-node.html"
breadcrumb-title: ""
description: Use the Clone filter node to duplicate and offset texture regions for creating seamless patterns and tiling effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Clone (Filter Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Clone (Filter Node)
user-guide-description: ""
user-guide-title: ""
---

# Clone (Filter Node)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](clone-filter-node.resources/clone-4.png)

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Clones input image once to a specified location. Can function as a crude "clone stamp" tool.

Requires some care to get the intended results:

* Ideally, the input image will have an alpha channel (like a decal), since blending is just a straight copy.
* Mask defaults to black, so to see any results a uniform white grayscale value needs to be plugged in at least.
* Offset will clip outside of the image easily, so use small values.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Source</b> <i>Color Input</i> | Image to clone. Important: ideally, the image will have an alpha channel! |
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Defaults to black! |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Offset</b> <i>-</i> | Moves or translates the result. Positive is Left and Up, Negative is Right and Down. Use small values, 1.0 and above moves it outside of the image! |
| <b>Blur Mask</b> <i>0.0 - 10.0</i> | Apply a blur filter to mask, to soften edges. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="clone-filter-node.resources/clone-example.png" />
        </td>
    </tr>
</table>
