---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/fiber-glass-edge-wear.html"
breadcrumb-title: ""
description: Use the Fiber Glass Edge Wear node to generate wear masks on fiberglass edges based on mesh curvature.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Fiber Glass Edge Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Fiber Glass Edge Wear
user-guide-description: ""
user-guide-title: ""
---

# Fiber Glass Edge Wear

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](fiber-glass-edge-wear.resources/fiber-glass-edge-wear-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

Represents a mask specifically intended for a fibreglass-type of wear, could perhaps be used for cloth. Due to the very tiled, repetitive nature of the fibres, Triplanar blending can optionally be enabled.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for edge highlighting. Required! |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for masking occluded areas. Not required, but definitely recommended. |
| <b>Grunge Input</b> <i>Grayscale Input</i> | Optional custom slot to override fiber pattern. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>World Space Normal</b> <i>Color Input</i> | Only used for Triplanar. |
| <b>Position</b> <i>Color Input</i> | Only used for Triplanar. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Wear Level</b> <i>0.0 - 1.0</i> | Like a [Histogram Scan](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-scan/histogram-scan.md), progressively reveals the wear. |
| <b>Wear Contrast</b> <i>0.0 - 1.0</i> | Sets total effect contrast. |
| <b>Edges Smoothness</b> <i>0.0 - 16.0</i> | Sets bleed out/blurring from highlighted edges. |
| <b>Grunge Amount</b> <i>0.0 - 1.0</i> | Sets how much of the fibre effect to blend in between the edges. Tweak this together with Wear Level to get maximum control. |
| <b>Ambient Occlusion Masking</b> <i>0.0 - 1.0</i> | Sets amount of influence the AO has on hiding the effect. |
| <b>Curvature Weight</b> <i>0.0 - 1.0</i> | Sets amount of influence Convex edges from the Curvature have. |
| <b>Use Custom Grunge</b> <i>False/True</i> | Overrides built-in fibres with custom map. |
| <b>Use Triplanar</b> <i>False/True</i> | Enables [Tri Planar](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/utilities-mesh-based-gen/tri-planar/tri-planar.md) to hide seams. |
| <b>Triplanar Blending Contrast</b> <i>0.0 - 1.0</i> | Controls contrast of the Triplanar effect. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="fiber-glass-edge-wear.resources/fiber-glass-edge-wear-02.gif" />
        </td>
    </tr>
</table>
