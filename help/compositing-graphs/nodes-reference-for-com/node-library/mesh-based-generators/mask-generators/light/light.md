---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/light.html"
breadcrumb-title: ""
description: Use the Light node to generate masks based on mesh lighting conditions for creating realistic material variations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Light
user-guide-description: ""
user-guide-title: ""
---

# Light

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/light-2.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask is a bit different from other Generators: it purely does fake lighting, based on the World Space Normalmap, returning a black and white "lightmap" mask.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Horizontal Angle</b> <i>0.0 - 1.0</i> | Sets the horizontal angle of the fake light. |
| <b>Vertical Angle</b> <i>0.0 - 1.0</i> | Sets the vertical angle of the fake light. |
| <b>Highlight Glossiness</b> <i>0.0 - 0.999</i> | Sets the falloff spread of the highlighted area. |
| <b>Highlight Level</b> <i>0.0 - 1.0</i> | Sets the brightness level of the highlighted area. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/light-ex.gif" />
        </td>
    </tr>
</table>
