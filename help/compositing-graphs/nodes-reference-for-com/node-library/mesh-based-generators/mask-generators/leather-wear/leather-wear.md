---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/leather-wear.html"
breadcrumb-title: ""
description: Use the Leather Wear node to generate wear masks on leather surfaces based on mesh curvature and contact points.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Leather Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Leather Wear
user-guide-description: ""
user-guide-title: ""
---

# Leather Wear

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](leather-wear.resources/leather-wear-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents wear with a leather pattern, with more wear on edges based on Curvature. It is similar to [Fiber Glass Edge Wear](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/fiber-glass-edge-wear/fiber-glass-edge-wear.md) in functionality and has mostly the same parameters.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for edge placement. Required! |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used occluding certain areas. Recommended, but not required. |
| <b>Grunge Input</b> <i>Grayscale Input</i> | Optional Grunge map input slot that can be toggled through the "Use Custom Grunge" parameter. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Wear Level</b> <i>0.0 - 1.0</i> | Sets global wear level, gradually revealing. |
| <b>Wear Contrast</b> <i>0.0 - 1.0</i> | Sets contrast of the effect. |
| <b>Grunge Amount</b> <i>0.0 - 1.0</i> | Sets the amount of grunge (default leather pattern) to blend in between edges. |
| <b>Ambient Occlusion Masking</b> <i>0.0 - 1.0</i> | Sets extent to which the AO masks out the wear effects. |
| <b>Curvature Weight</b> <i>0.0 - 1.0</i> | Sets extent to which the curvature's edges affect the final result. Even if set to 0, you still need a curvature map. |
| <b>Use Custom Grunge</b> <i>False/True</i> | Enables overriding of the built-in default leather pattern. Use a custom input slot instead. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="leather-wear.resources/leather-wear-02.gif" />
        </td>
    </tr>
</table>
