---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/dust.html"
breadcrumb-title: ""
description: Use the Dust node to generate dust accumulation masks based on mesh geometry for creating realistic dust and grime effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Dust
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Dust
user-guide-description: ""
user-guide-title: ""
---

# Dust

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](dust.resources/dust-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents dust accumulated in occluded, lowered areas, as well as only in areas that face upwards. Requires proper baked AO and World Space Normals to work.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for dust placement. Required! |
| <b>World Space Normal</b> <i>Color Input</i> | Baked map used for dust placement. Required! |
| <b>Noise</b> <i>Grayscale Input</i> | Custom dust map (optional), only appears when Override Noise is set to True. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets total amount of dust. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts contrast of the dust. |
| <b>Occlusion Amount</b> <i>0.0 - 1.0</i> | Sets influence of AO; more dust will appear in occluded areas. |
| <b>Noise Opacity</b> <i>0.0 - 1.0</i> | Sets amount of noise that is visible in the dusty areas. |
| <b>Override Noise</b> <i>False/True</i> | Set to use custom dust map input. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="dust.resources/dust-02.gif" />
        </td>
    </tr>
</table>
