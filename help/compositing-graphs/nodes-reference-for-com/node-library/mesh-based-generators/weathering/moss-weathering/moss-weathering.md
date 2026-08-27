---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/weathering/moss-weathering.html"
breadcrumb-title: ""
description: Use the Moss Weathering node to add moss growth patterns to materials based on mesh curvature and position.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Moss Weathering
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Moss Weathering
user-guide-description: ""
user-guide-title: ""
---

# Moss Weathering

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](moss-weathering.resources/moss-weathering.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Weathering

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is a full-material effect that works on multiple channels at once. It generates an overgrown moss effect, with a single control for Propagation.

This effect works best with a baked World Space Position map and an additional Heightmap. While this is not an exact requirement, it lends the effect more credible placement.

Make sure to properly understand the [Link Creation Modes](https://support.allegorithmic.com/documentation/display/SD5/Link+Creation+Modes) when working with full materials.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Position</b> <i>Color Input</i> | Baked World Space Position. |
| <b>Height</b> <i>Grayscale Input</i> | Additional Heightmap input. |
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
| <b>Moss Propagation</b> <i>0.0 - 1.0</i> | Sets the spread of the moss. Grows in steps from slight coverage to heavy, thick, dark moss. |
| <b>Blending</b> |  |
| <b>Diffuse Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Diffuse. |
| <b>Base Color Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Base Color. |
| <b>Normal Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Normal. |
| <b>Specular Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Specular. |
| <b>Glossiness Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Glossiness. |
| <b>Roughness Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Roughness. |
| <b>Ambient Occlusion Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Ambient Occlusion. |
| <b>Height Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Height. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="moss-weathering.resources/moss-ex.gif" />
        </td>
    </tr>
</table>
