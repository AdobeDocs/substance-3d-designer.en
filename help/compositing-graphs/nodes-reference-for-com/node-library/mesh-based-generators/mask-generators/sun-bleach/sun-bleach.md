---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/sun-bleach.html"
breadcrumb-title: ""
description: Use the Sun Bleach node to generate masks based on sun exposure for creating realistic sun-bleached and faded effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Sun Bleach
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Sun Bleach
user-guide-description: ""
user-guide-title: ""
---

# Sun Bleach

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](sun-bleach.resources/sun-bleach-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask is similar to [Light](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/light/light.md), but has support for AO too, leading to a mask that represents light bleaching and fading on top of an effect.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Normal World Space</b> <i>Color Input</i> |  |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total amount of bleaching, moves the effect further down. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Occlusion</b> <i>0.0 - 1.0</i> | Sets the influence of the AO on the final result. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="sun-bleach.resources/sun-bleach-02.gif" />
        </td>
    </tr>
</table>
