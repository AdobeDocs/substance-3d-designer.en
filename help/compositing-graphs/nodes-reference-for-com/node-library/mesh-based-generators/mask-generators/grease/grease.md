---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/grease.html"
breadcrumb-title: ""
description: Use the Grease node to generate grease accumulation masks based on mesh geometry and contact areas.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Grease
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Grease
user-guide-description: ""
user-guide-title: ""
---

# Grease

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/grease.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask is specifically intended for character faces and other specific areas. Generates a skin-grease type of mask on areas of low thickness.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Thickness</b> <i>Grayscale Input</i> | Baked Thickness map on which the entire effect is based. Required! |
| <b>Noise</b> <i>Grayscale Input</i> | Optional Noise map to override Grease grunge with. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total amount of effect to appear. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Thickness Threshold</b> <i>0.0 - 1.0</i> | Sets a minimum thickness at which the effect should appear. Equally important as Level; tweak this to fit your Thickness map. |
| <b>Override Noise</b> <i>False/True</i> | Set to override internal grease grunge map with custom input slot. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/grease-ex.gif" />
        </td>
    </tr>
</table>
