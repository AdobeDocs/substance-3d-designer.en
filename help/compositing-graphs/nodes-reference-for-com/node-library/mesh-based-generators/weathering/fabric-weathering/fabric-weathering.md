---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/weathering/fabric-weathering.html"
breadcrumb-title: ""
description: Use the Fabric Weathering node to add wear and aging effects to fabric materials based on mesh geometry and curvature.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Fabric Weathering
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Fabric Weathering
user-guide-description: ""
user-guide-title: ""
---

# Fabric Weathering

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](fabric-weathering.resources/fabric-weathering-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Weathering

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is a full-material effect that works on multiple channels at once. It adds a random fabric wear effect, with control for age and dirtiness.<br>This effect does not work very well unless you have proper baked AO and World Space Normalmaps plugged in, since it requires these to adequately calculate and generate everything.

Make sure to fully understand the [Link Creation Modes](../../../../../../interface/the-graph-view/link-creation-modes/link-creation-modes.md) when working with full materials.

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
| <b>Used</b> <i>0.0 - 1.0</i> | Blends in very dark accumulated dirt in creases, based on AO. Maximum and Minimum values tend to be very extreme, use these with care. |
| <b>Age</b> <i>0.0 - 1.0</i> | Blends over a global tiling wear pattern. Treshold control below controls AO influence. Maximum and Minimum values tend to be very extreme. |
| <b>Age Threshlod</b> <i>0.0 - 1.0</i> | Sets the extent to which the AO affects the Age parameter. |
| <b>Age Creases</b> <i>0.0 - 1.0</i> | Controls the blending of subtle additional creases in the Age effect. |
| <b>Sharp Edges Scratches Scale</b> <i>1.0 - 32.0</i> | Sets the scale of small scratches, which mainly scrape away Used and Age effect. |
| <b>Sharp Edges Scratches Warp Intensity</b> <i>0.0 - 1.0</i> | Sets the intensity of the warp for the above small scratches. |
| <b>Old Fabric Desaturation</b> <i>0.0 - 1.0</i> | Controls the desaturation of the Age effect. |
| <b>Old Fabric Brightness</b> <i>0.0 - 1.0</i> | Controls the brightness of the Age effect. *This is a very important parameter to change to get the look you like, but results can be extreme: use with subte changes.* |
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
            <img src="fabric-weathering.resources/fabric-weathering-02.gif" />
        </td>
    </tr>
</table>
