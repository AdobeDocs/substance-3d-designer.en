---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/weathering/metal-weathering.html"
breadcrumb-title: ""
description: Use the Metal Weathering node to add realistic rust and corrosion effects to metal materials based on mesh geometry.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Metal Weathering
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Metal Weathering
user-guide-description: ""
user-guide-title: ""
---

# Metal Weathering

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](metal-weathering.resources/metal-weathering.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Weathering

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Normal WS</b> <i>Color Input</i> | Baked World Space Normalmap used for internal effects and masking. |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Advanced</b> |  |
| <b>Normal Format</b> <i>Direct X, Open GL</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Mask</b> <i>False/True</i> | Toggles the use of the Mask map on or off. |
| <b>Effect</b> |  |
| <b>Dust</b> <i>0.0 - 1.0</i> |  |
| <b>Dirtiness</b> <i>0.0 - 1.0</i> |  |
| <b>Edges Wearing</b> <i>0.0 - 1.0</i> |  |
| <b>Paint Peeling</b> <i>0.0 - 1.0</i> |  |
| <b>Rust</b> <i>0.0 - 1.0</i> |  |
| <b>Rust Peeling</b> <i>0.0 - 1.0</i> |  |
| <b>Rust Verdigris</b> <i>Rust, Verdigris</i> |  |
| <b>Paint Cracks Scale</b> <i>1.0 - 16.0</i> |  |
| <b>Paint Cracks Warp Intensity</b> <i>0.0 - 1.0</i> |  |
| <b>Sharp Edges Scratches Scale</b> <i>1.0 - 32.0</i> |  |
| <b>Sharp Edges Scratches Warp Intensity</b> <i>0.0 - 1.0</i> |  |
| <b>Raw Metal Color</b> <i>(Color value)</i> |  |
| <b>Raw Metal Specular Color</b> <i>(Color value)</i> |  |
| <b>Raw Metal Glossiness Value</b> <i>(Grayscale value)</i> |  |
| <b>Raw Metal Roughness Value</b> <i>(Grayscale value)</i> |  |
| <b>Blending</b> |  |
| <b>Diffuse Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Diffuse. |
| <b>Base Color Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Base Color. |
| <b>Normal Intensity</b> <i>0.0 - 64.0</i> | Blending strength of the Normal. |
| <b>Specular Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Specular. |
| <b>Glossiness Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Glossiness. |
| <b>Roughness Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Roughness. |
| <b>Metallic Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Metallic. |
| <b>Ambient Occlusion Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Ambient Occlusion. |
| <b>Height Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Height. |
