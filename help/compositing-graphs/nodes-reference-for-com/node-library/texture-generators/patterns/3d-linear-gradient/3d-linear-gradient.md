---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/3d-linear-gradient.html"
breadcrumb-title: ""
description: Use the 3D Linear Gradient node to create linear gradients based on 3D world position for spatial effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > 3D Linear Gradient
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Linear Gradient
user-guide-description: ""
user-guide-title: ""
---

# 3D Linear Gradient

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](3d-linear-gradient.resources/3d-linear-gradient-01.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Creates a volumetric gradient based on input Position map. Effectively generates a transition from black to white between 2 points in 3D Space. Intened for use with the GPU engine only.

Also see [3D Volume Mask](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/3d-volume-mask/3d-volume-mask.md) for a similar effect.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Points Position Mode</b> <i>UV Positions, World Space Positions</i> | Choose if the Gradient Points work in UV Space (works best when setting them in 2D view) or in in 3D coordinates, if you want to manually enter an exact position. |
| <b>Point 1</b> | Start Point of the gradient. Can be 2D or 3D Coordinates based on Position Mode. |
| <b>Point 2</b> | End Point of the gradient. Can be 2D or 3D Coordinates based on Position Mode. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="3d-linear-gradient.resources/3d-linear-gradient-02.gif" />
        </td>
    </tr>
</table>
