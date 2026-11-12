---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blending/luminosity-blend-node.html"
breadcrumb-title: ""
description: Use the Luminosity blend node to blend textures based on luminosity values for creating brightness-based composite effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Luminosity (Blend Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Luminosity (Blend Node)
user-guide-description: ""
user-guide-title: ""
---

# Luminosity (Blend Node)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

<b>In:</b> Filters &gt; Blending

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs a Luminosity blend mode, which preserves the hue and chrominance of the Background, while adopting the luminance of the Foreground.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Foreground</b> <i>Color Input</i> |  |
| <b>Background</b> <i>Color Input</i> |  |
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background. |
| <b>Alpha Blending</b> <i>False/True</i> | Toggles blending of the Foreground and Background alpha channels. If set to False, the alpha channel of the foreground is ignored. |
