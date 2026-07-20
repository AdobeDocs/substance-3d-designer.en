---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/shape-glow.html"
breadcrumb-title: ""
description: Use the Shape Glow node to add glow effects to shapes and textures for creating luminous and atmospheric visual effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Shape Glow
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape Glow
user-guide-description: ""
user-guide-title: ""
---

# Shape Glow

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/shape-glow-grayscale.png){width="128px"}

![](../../../../../../assets/shape-glow.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Creates a soft glow around an input mask (for the grayscale version) or a shape with an alpha channel (for the color version). Compared to [Glow](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/glow/glow.md), this works in ways more similar to other 2D image editing software, as it is a more complete effect with more controls.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Mode</b> <i>Soft, Precise</i> | Switches between two accuracy modes. |
| <b>Width</b> <i>-1.0 - 1.0</i> | Controls how far the glow reaches. |
| <b>Spread</b> <i>0.0 - 1.0</i> | Cut-off / treshold for the blurring effect, makes the glow appear solid close to the shape. |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity for the glow effect. |
| <b>(Shadow) Color</b> <i>(Color value)</i> | Color tint to be applied to the glow. |
| <b>Mask Color</b> <i>(Color value) (Grayscale Version Only)</i> | Solid color to be used for the transparency mapped output. |
| <b>Input Is Pre-Multiplied</b> <i>False/True (Color Version Only)</i> | Whether the input should be assumed as pre-multiplied. |
| <b>Pre-Multiply Output</b> <i>False/True</i> | Whether the output should be pre-multiplied. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/shapeglow-ex.png" />
        </td>
    </tr>
</table>
