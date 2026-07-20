---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/weathering/cracks-weathering.html"
breadcrumb-title: ""
description: Use the Cracks Weathering node to add crack patterns to materials based on mesh curvature and stress points.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Cracks Weathering
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Cracks Weathering
user-guide-description: ""
user-guide-title: ""
---

# Cracks Weathering

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](cracks-weathering.resources/cracks-weathering.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Weathering

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is a full-material effect that works on multiple channels at once. It adds a random crack pattern, with control over spread and depth.

Make sure to properly understand the [Link Creation Modes](../../../../../../interface/the-graph-view/link-creation-modes/link-creation-modes.md) when working with full materials.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked or generated map used for internal effects and masking. |
| <b>Height</b> <i>Grayscale Input</i> | Baked or generated map used for internal effects and masking. |
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Advanced</b> |  |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Mask</b> <i>False/True</i> | Toggles the use of the Mask map on or off. |
| <b>Effect</b> |  |
| <b>Cracks Propagation</b> <i>0.0 - 1.0</i> | How far the cracks should spread. This is the main control for this effect. |
| <b>Cracks Depth</b> <i>0.0 - 1.0</i> | Depth of the crack effect. This mostly affects height and slightly affects visula thickness. |
| <b>Blending</b> | Controls how strongly the effect blends into each resulting channel. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="cracks-weathering.resources/cracks-ex.gif" />
        </td>
    </tr>
</table>
