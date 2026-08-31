---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/paint-wear.html"
breadcrumb-title: ""
description: Use the Paint Wear node to generate paint wear masks based on mesh geometry for creating realistic paint chipping effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Paint Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Paint Wear
user-guide-description: ""
user-guide-title: ""
---

# Paint Wear

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](paint-wear.resources/paint-wear-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents paint chipping and wearing away at edges.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Variation Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total amount of paint wear, gradually revealing. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Occlusion</b> <i>0.0 - 1.0</i> | Sets amount of effect the baked AO has on preventing wear in darker areas. |
| <b>Radius</b> <i>0.0 - 2.0</i> | Sets how far the chipping effect spreads from Convex edges. |
| <b>Variation</b> <i>0.0 - 1.0</i> | Set amount of variation (grunge) to blend into the effect. |
| <b>Override variation mask</b> <i>False/True</i> | Enables custom variation (grunge) map input slot. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="paint-wear.resources/paint-wear-02.gif" />
        </td>
    </tr>
</table>
