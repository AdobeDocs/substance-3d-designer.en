---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/caustics.html"
breadcrumb-title: ""
description: Use the Caustics node to generate caustic light patterns for creating underwater and refractive lighting effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Caustics
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Caustics
user-guide-description: ""
user-guide-title: ""
---

# Caustics

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](caustics.resources/rt-caustics-grayscale.png){width="128px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates projected caustics based on a height map and a light direction.Comes in both Grayscale and color versions, differences are subtle but the color version adds color dispersioneffects. Light is cast from a single point, no Environment map is used.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Output Color Space</b> <i>Raw, sRGB</i> | Set output color space. |
| <b>Photon Grid Size</b> <i>Auto, 512, 1024, 2048, 4096</i> | Sets quality by adjusting grid size, but defaults to matching input. Can be used to speed up calculation. |
| <b>Surface Height Scale</b> <i>0.0 - 1.0</i> | Multiplier to determine how the height is interpreted. |
| <b>Surface Height Position</b> <i>0.0 - 1.0</i> | Set distance of refracting surface to projection. |
| <b>Surface IOR</b> <i>1.0 - 2.0</i> | Set refraction index, in the color version this adds more color dispersion. |
| <b>Photon Size</b> <i>1.0 - 50.0</i> | Photon size affects crispness of the effect. |
| <b>Dispersion</b> <i>0.0 - 0.01 (Color version only)</i> | Affect just the color dispersion. Not visible when IOR is low. |
| <b>Jittering</b> <i>0.0 - 1.0</i> | Add irregular jittering to the cast photon particles. |
| <b>Light Position</b> | Moves the light position. Also done through a gizmo in the 2D view. |
| <b>Background Color</b> <i>(Color value) (Color version only)</i> | Change the background color. Limited to black in the grayscale version. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enable compensation of squash and stretch with non-square ratios. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="caustics.resources/rt-caustics-grayscale-1.png" />
        </td>
    </tr>
</table>
