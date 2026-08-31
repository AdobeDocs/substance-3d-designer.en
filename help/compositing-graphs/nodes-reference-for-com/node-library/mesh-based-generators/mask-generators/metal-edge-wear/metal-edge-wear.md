---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/metal-edge-wear.html"
breadcrumb-title: ""
description: Use the Metal Edge Wear node to generate wear masks on metal edges based on mesh curvature and position.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Metal Edge Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Metal Edge Wear
user-guide-description: ""
user-guide-title: ""
---

# Metal Edge Wear

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](metal-edge-wear.resources/metal-edge-wear-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents edge wear on a metal object, with scratches and chips appearing on Convex raised edges, potentially masked out by baked AO dark areas.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Grunge Input</b> <i>Grayscale Input</i> |  |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>World Space Normal</b> <i>Color Input</i> |  |
| <b>Position</b> <i>Color Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Wear Level</b> <i>0.0 - 1.0</i> | Sets the total amount of wear, gradually reveals. |
| <b>Wear Contrast</b> <i>0.0 - 1.0</i> | Sets the contrast of the final result. |
| <b>Edges Smoothness</b> <i>0.0 - 16.0</i> | Sets smoothness of the falloff from the edges from the Curvature. |
| <b>Grunge Amount</b> <i>0.0 - 1.0</i> | Sets amount of grunge to blend in between edges. |
| <b>Grunge Scale</b> <i>1 - 16</i> | Sets the scale of the Grunge. |
| <b>Ambient Occlusion Masking</b> <i>0.0 - 1.0</i> | Sets amount of effect the AO has on the final effect, dark areas being masked out. |
| <b>Curvature Weight</b> <i>0.0 - 1.0</i> | Sets amount of effect the Convex edges from the Curvature have on the final effect. |
| <b>Use Custom Grunge</b> <i>False/True</i> | Enables a custom Grunge map input slot. |
| <b>Use Triplanar</b> <i>False/True</i> | Enable [Tri Planar](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/utilities-mesh-based-gen/tri-planar/tri-planar.md) projection to hide seams. |
| <b>Triplanar Blending Contrast</b> <i>0.0 - 1.0</i> | Sets blending contrast for the Triplanar Projection. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="metal-edge-wear.resources/metal-edge-wear-02.gif" />
        </td>
    </tr>
</table>
