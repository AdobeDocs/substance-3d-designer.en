---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/weathering/leather-weathering.html"
breadcrumb-title: ""
description: Use the Leather Weathering node to add wear patterns and aging effects to leather materials based on mesh curvature.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Leather Weathering
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Leather Weathering
user-guide-description: ""
user-guide-title: ""
---

# Leather Weathering

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](leather-weathering.resources/leather-weathering.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Weathering

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is a full-material effect that works on multiple channels at once. It adds a random leather wear effect, with control for age and dirtiness. It is similar to [Fabric Weathering](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/weathering/fabric-weathering/fabric-weathering.md), but tuned specifically for leather.<br>This effect does not work very well unless you have proper baked AO and World Space Normalmaps plugged in, as it requires these to adequately calculate and generate everything.

Make sure to fully understand the [Link Creation Modes](https://support.allegorithmic.com/documentation/display/SD5/Link+Creation+Modes) when working with full materials.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Normal Wold Space</b> <i>Color Input</i> |  |
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
| <b>Dust</b> <i>0.0 - 1.0</i> | Blends in a darker dust effect, based on areas facing up in the World Space Normalmap. |
| <b>Dirtiness</b> <i>0.0 - 1.0</i> | Blends in a global dirt/smudge effect, based mostly on areas occluded (dark) in the AO. |
| <b>Edges Wearing</b> <i>0.0 - 1.0</i> | Adds a sharpening/intensifying effect to edges, based on Material Normal. |
| <b>Used</b> <i>0.0 - 1.0</i> | Blends in a global worn leather look. |
| <b>Age</b> <i>0.0 - 1.0</i> | Blends in a worn leather look in creases based on AO. Placement is influenced a lot by Age Treshold. |
| <b>Age Threshlod</b> <i>0.0 - 1.0</i> | Sets the appearance treshold for the Age effect. |
| <b>Cracks Scale</b> <i>1.0 - 16.0</i> | Sets the depth of the worn leather from Used and Age effect. |
| <b>Cracks Warp Intensity</b> <i>0.0 - 1.0</i> | Sets the intensity of the worn leather from Used and Age effect. |
| <b>Sharp Edges Scratches Scale</b> <i>1.0 - 32.0</i> |  |
| <b>Sharp Edges Scratches Warp Intensity</b> <i>0.0 - 1.0</i> |  |
| <b>Used Leather Desaturation</b> <i>0.0 - 1.0</i> | Sets the saturation of the worn leather look from Age and Used effects. |
| <b>Used Leather Brightness</b> <i>0.0 - 1.0</i> | Sets the brightness of the worn leather look from Age and Used effects. |
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
            <img src="leather-weathering.resources/leather-ex.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="leather-weathering.resources/leather-ex2.png" />
        </td>
    </tr>
</table>
