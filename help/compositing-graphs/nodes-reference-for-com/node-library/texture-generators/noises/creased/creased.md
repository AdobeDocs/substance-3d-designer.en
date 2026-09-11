---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/creased.html"
breadcrumb-title: ""
description: Use the Creased node to generate crease patterns for creating folded fabric and wrinkled surface texture effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Creased
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Creased
user-guide-description: ""
user-guide-title: ""
---

# Creased

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](creased.resources/creased.png){width="128px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node generates a cloth-like noise. It can be interpreted as Heightmap

Creased is useful for when you need a semi-directional-noise with large scale variation.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Scale</b> <i>1 - 8</i> | Sets the global scale for the effect. |
| <b>Warp Intensity</b> <i>0.0 - 128.0</i> | Sets the strengt of the bend/warp effect. |
| <b>Disorder</b> <i>0.0 - 100.0</i> | Slightly offsets the layers used to generate the noise, to introduce variation. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="creased.resources/creased-ex.gif" />
        </td>
    </tr>
</table>
