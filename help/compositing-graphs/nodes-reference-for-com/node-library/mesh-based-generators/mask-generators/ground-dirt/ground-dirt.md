---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/ground-dirt.html"
breadcrumb-title: ""
description: Use the Ground Dirt node to generate dirt accumulation masks based on mesh position and orientation relative to ground.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Ground Dirt
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Ground Dirt
user-guide-description: ""
user-guide-title: ""
---

# Ground Dirt

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](ground-dirt.resources/ground-dirt-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents dirt that has accumulated from the ground up, the opposite of [Bottom To Top](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/bottom-to-top/bottom-to-top.md) or [Dust](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/dust/dust.md). It has no custom map override.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Position</b> <i>Grayscale Input</i> | Baked position map to base effect on. Required! |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total appearance level of the dirt. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Dirt Height</b> <i>0.0 - 1.0</i> | Sets up to what height (proportionally) the dirt should appear. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="ground-dirt.resources/ground-dirt-02.gif" />
        </td>
    </tr>
</table>
