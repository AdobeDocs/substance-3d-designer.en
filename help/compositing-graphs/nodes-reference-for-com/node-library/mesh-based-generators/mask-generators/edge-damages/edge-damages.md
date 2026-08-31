---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/edge-damages.html"
breadcrumb-title: ""
description: Use the Edge Damages node to generate damage masks on mesh edges for creating realistic edge wear and breakage effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Damages
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Edge Damages
user-guide-description: ""
user-guide-title: ""
---

# Edge Damages

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](edge-damages.resources/edge-damages-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents damage done to raised, convex edges based on curvature and baked AO.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for effect placement. Required! |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for effect placement. Required! |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Amount of edge damage to apply. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Damages Intensity</b> <i>0.0 - 1.0</i> | Shifts between a chipped, consistent look and a chaotic, scratched, heavily damaged look. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="edge-damages.resources/edge-damages-02.gif" />
        </td>
    </tr>
</table>
