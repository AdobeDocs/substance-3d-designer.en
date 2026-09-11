---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/glow.html"
breadcrumb-title: ""
description: Use the Glow node to add glow effects to textures for creating luminous and emissive material appearances.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Glow
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Glow
user-guide-description: ""
user-guide-title: ""
---

# Glow

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](glow.resources/glow-greyscale.png){width="128px"}

![](glow.resources/glow-3.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs an "Outer Glow"-type of effect, as seen in other popular image editing software. Essentially adds a fading gradient outline around the input.

Keep in mind that this is not intended to work for images with Alpha Channels, as you might expect. Even the color version only expects binary, black and white masks as input; it only allows for using a colored glow. If you're after a version that works on images with transparency, see [Shape Glow](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/shape-glow/shape-glow.md).

Important: make sure to use the appropriate version for your input! Use "Glow" for Color inputs, or "Glow Grayscale" for Grayscale inputs.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Glow Amount</b> <i>0.0 - 1.0</i> | Global opacity for the glow effect. |
| <b>Clear Amount</b> <i>0.0 - 1.0</i> | Treshold for when to cut off the glow effect. Useful for semi-transparent areas. |
| <b>Glow Size</b> <i>0.0 - 20.0</i> | Controls how far the glow effect reaches. |
| <b>Glow Color</b> <i>(Color value) (Color Version Only)</i> | Sets the color of the glow effect. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="glow.resources/glow-ex.png" />
        </td>
    </tr>
</table>
