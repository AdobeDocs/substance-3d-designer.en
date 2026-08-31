---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/utilities-mesh-based-generators/material-mesh-data-blender.html"
breadcrumb-title: ""
description: Use the Material Mesh Data Blender node to blend material mesh data for creating smooth transitions between different material zones.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Utilities (Mesh Based Generators) > Material Mesh Data Blender
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Mesh Data Blender
user-guide-description: ""
user-guide-title: ""
---

# Material Mesh Data Blender

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](material-mesh-data-blender.resources/material-mesh-data-blender-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Utilities

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node is intended to make it a lot easier to add detail based on baked data. It comes with a lot of sliders to modify an input full material, based on any and all baked maps as input. Do experiment with it, as there are a lot of options.

It is useful for doing things like adding edge highlighting based on curvature or other maps, blending in some AO with the Diffuse/Basecolor, adding Specular Occlusion based on Curvature and/or AO, etc.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Full Material Input (Group "Material")</b> | Full set of material maps.<br><br>These are modified by this node and then returned again as output. |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Height</b> <i>Grayscale Input</i> |  |
| <b>Normal</b> <i>Color Input</i> |  |
| <b>Vertex Color</b> <i>Color Input</i> |  |
| <b>World Space Normal</b> <i>Color Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. Affects the availability of the below parameters. |
| <b>Baked Maps</b> | Whether or not to use the listed baked maps for calculations. Affects the availability of the below parameters. |
| <b>Diffuse AO</b> <i>0.0 - 1.0</i> | Amount of Ambient Occlusion to blend into the Diffuse. |
| <b>Diffuse Sharp Edges</b> <i>0.0 - 1.0</i> | Amount of the curvature map to blend into the Diffuse. |
| <b>Diffuse Color From Vertex Color</b> <i>0.0 - 1.0</i> | Amount of the Vertex Color bake to blend into the Diffuse. |
| <b>Diffuse Pre Lighting</b> <i>0.0 - 1.0</i> | Amount of (fake) pre-lighting, based on the World Space Normals. |
| <b>Diffuse Cartoon Lighting Balance</b> <i>0.0 - 1.0</i> | Shifts between realistic and cartoonish lighting for the Diffuse. |
| <b>Diffuse Cartoon Pre Lighting Layers</b> <i>0 - 10</i> | Controls the look of the cartoonish lighting calculations. |
| <b>Diffuse Cartoon Outlines</b> <i>0.0 - 1.0</i> | Controls the look of the cartoonish lighting calculations. |
| <b>Base Color AO</b> <i>0.0 - 1.0</i> | Amount of Ambient Occlusion to blend into the Basecolor. |
| <b>Base Color Sharp edges</b> <i>0.0 - 1.0</i> | Amount of the curvature map to blend into the Basecolor. |
| <b>Base Color From Vertex Color</b> <i>0.0 - 1.0</i> | Amount of the Vertex Color bake to blend into the Basecolor. |
| <b>Normal Material Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the baked (tangent) Normalmap. |
| <b>SpecularAO</b> <i>0.0 - 1.0</i> | Blending strength of the AO in the Specular. |
| <b>Specular Bright Sharp Edges</b> <i>0.0 - 1.0</i> | Blending strength of the Curvature in the Specular. |
| <b>Specular Cartoon Outlines</b> <i>0.0 - 1.0</i> | Blending strength of a cartoon Specular edge-outline effect, based on the Curvature. |
| <b>Glossiness Dark Sharp Edges</b> <i>0.0 - 1.0</i> | Blending strength of the Curvature in the Glossiness. |
| <b>Roughness Bright Sharp Edges</b> <i>0.0 - 1.0</i> | Blending strength of the Curvature in the Roughness. |
| <b>Roughness Cartoon Outlines</b> <i>0.0 - 1.0</i> | Blending strength of a cartoon Roughness edge-outline effect, based on the Curvature. |
| <b>Metallic Bright Sharp Edges</b> <i>0.0 - 1.0</i> | Blending strength of the Curvature in the Metallic. |
| <b>Metallic Cartoon Outlines</b> <i>0.0 - 1.0</i> | Blending strength of a cartoon Metallic edge-outline effect, based on the Curvature. |
| <b>AO Materiel Intensity</b> <i>0.0 - 1.0</i> | Blend strength of baked map AO with Material-generated AO, what degree to combine both AO maps at. |
| <b>Height Material Intensity</b> <i>0.0 - 1.0</i> | Blend strength of baked map Height with Material-generated Height, what degree to combine both Heightmaps at. |
| <b>Height Material Blending Type</b> <i>Reinforce, Interpolation</i> | Blend mode for combining both Heightmaps. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="material-mesh-data-blender.resources/material-mesh-data-blender-02.gif" />
        </td>
    </tr>
</table>
