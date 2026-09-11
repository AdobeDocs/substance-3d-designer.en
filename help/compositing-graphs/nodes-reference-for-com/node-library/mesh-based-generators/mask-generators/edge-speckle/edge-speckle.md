---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/edge-speckle.html"
breadcrumb-title: ""
description: Use the Edge Speckle node to generate speckled wear patterns on mesh edges for creating realistic edge damage effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Speckle
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Edge Speckle
user-guide-description: ""
user-guide-title: ""
---

# Edge Speckle

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](edge-speckle.resources/edge-speckle.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents edges with a slight speckle added to break them up. Also see [Edge Dirt](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/edge-dirt/edge-dirt.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for Edge highlighting. Required! |
| <b>Variation Mask</b> <i>Grayscale Input</i> | Optional mask slot used for masking the node's effects. Enable with "override variation mask". |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total amount of edge highlighting. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Edge selection</b> <i>0.0 - 1.0</i> | Sets the influence of convex edges. |
| <b>Variation</b> <i>0.0 - 1.0</i> | Sets extent to which the variation mask breaks up the effect. |
| <b>Override variation mask</b> <i>False/True</i> | Overrides built-in mask with custom input slot. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="edge-speckle.resources/edge-speckle-ex.gif" />
        </td>
    </tr>
</table>
