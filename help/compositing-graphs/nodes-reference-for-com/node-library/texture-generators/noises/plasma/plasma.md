---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/plasma.html"
breadcrumb-title: ""
description: Use the Plasma node to generate plasma-like noise patterns for creating organic and fluid texture effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Plasma
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Plasma
user-guide-description: ""
user-guide-title: ""
---

# Plasma

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](plasma.resources/plasma-01.png){width="128px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This generates a slightly different variant of [Gaussian Noise](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/gaussian-noise/gaussian-noise.md), with longer dark streaks as valleys. It has a similar Distance control for scale, which maintains tiling.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Scale</b> <i>1 - 128</i> | Sets the global scale for the effect. |
| <b>Disorder</b> <i>0.0 - 1.0</i> | Phase-shifts the noise to introduce small variation. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="plasma.resources/plasma-02.gif" />
        </td>
    </tr>
</table>
