---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/cloth-wear.html"
breadcrumb-title: ""
description: Use the Cloth Wear node to generate wear masks on cloth surfaces based on mesh curvature and contact areas.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Cloth Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Cloth Wear
user-guide-description: ""
user-guide-title: ""
---

# Cloth Wear

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](cloth-wear.resources/cloth-wear-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

The mask represents frazzled edges on cloth materials. It uses a cloth detail Heightmap that determines most of the look; without an appropriate map, the effect looks very basic.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Cloth Height</b> <i>Grayscale Input</i> | Height for the cloth pattern only. This is not the height of your (baked) object, but rather a tiling detail pattern. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>Curvature</b> <i>Grayscale Input</i> | Baked/generated curvature to determine raised edges. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Hard Edges Amount</b> <i>0.0 - 1.0</i> |  |
| <b>Wear Softness</b> <i>0.0 - 5.0</i> | Determines how blurred out/soft the worn edges are. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="cloth-wear.resources/cloth-wear-02.gif" />
        </td>
    </tr>
</table>
