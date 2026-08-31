---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/dirt.html"
breadcrumb-title: ""
description: Use the Dirt node to generate dirt accumulation masks based on mesh curvature, position, and occlusion.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Dirt
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Dirt
user-guide-description: ""
user-guide-title: ""
---

# Dirt

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](dirt.resources/dirt-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represent dirts in occluded and sunken edges and corners, based on baked AO and curvature.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. Required! |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. Required! |
| <b>Grunge input</b> <i>Grayscale Input</i> | Custom grunge map input, optional, enabled by parameter. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>World Space Normal</b> <i>Color Input</i> | Only used for Triplanar. |
| <b>Position</b> <i>Color Input</i> | Only used for Triplanar. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Dirt Level</b> <i>0.0 - 1.0</i> | Main control for amount of dirt. |
| <b>Dirt Contrast</b> <i>0.0 - 1.0</i> | Controls main contrast for the dirt in the mask. |
| <b>Grunge Amount</b> <i>0.0 - 1.0</i> | Sets how grungy the dirt is. Set to 0 for perfectly smooth dirt. |
| <b>Edges Masking</b> <i>0.0 - 1.0</i> | Amount of dirt to remove from raised edges (based on the curvature map). |
| <b>Use Custom Grunge</b> <i>False/True</i> | Enables use of custom grunge map input instead of built-in Grunge. |
| <b>Grunge Scale</b> <i>1 - 16</i> | Sets tiling scale of Grunge detail. |
| <b>Use Triplanar</b> <i>False/True</i> | Use [Triplanar projection](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/utilities-mesh-based-gen/tri-planar/tri-planar.md) for Grunge mapping, removes seams. |
| <b>Triplanar Blending Contrast</b> <i>0.001 - 1.0</i> | Sets contrast of the Triplanar projection. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="dirt.resources/dirt-02.gif" />
        </td>
    </tr>
</table>
