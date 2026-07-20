---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/leaks.html"
breadcrumb-title: ""
description: Use the Leaks node to generate leak patterns based on mesh geometry for creating water stains and fluid effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Leaks
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Leaks
user-guide-description: ""
user-guide-title: ""
---

# Leaks

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](leaks.resources/leaks.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This node represents leaking streaks of dirt and grime coming from sharp edges. As streaks are generated with baked Position, they always run downwards.

Make sure to try changing the variation mask: because it drives the placement of streaks, it can have a much larger influence than with other Mask Generators.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Position</b> <i>Grayscale Input</i> | Baked position map, used for streak directions. Required! |
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for streak placement. Required! |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. Recommended, but you could use flat white instead. |
| <b>Normal World Space</b> <i>Color Input</i> | Baked World Space Normalmap, used for streak direction. Required! |
| <b>Variation Mask</b> <i>Grayscale Input</i> | Optional variation mask, enable by setting the override to True. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Total level of the result. Progressively reveals the effect, affects length as well. Should be set fairly high to get long drips. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Variation</b> <i>0.0 - 1.0</i> | Sets the amount of large-scale variation used to mask the streaks. Setting this value to 0 leads to full uniform streaks, so avoid this. |
| <b>Lenght</b> <i>0.0 - 8.0</i> | Length of the streak drips. Setting this value too high at a small scale will lead to visible stepping. Play around with the Level too. |
| <b>Occlude</b> <i>X, Y, Z, None</i> | Sets what direction the AO should affect. |
| <b>Override variation mask</b> <i>False/True</i> | Enables overriding of the variation mask with a custom input slot. Using sparser or denser masks can be interesting and is a good way to control the drips. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="leaks.resources/leaks-ex.gif" />
        </td>
    </tr>
</table>
