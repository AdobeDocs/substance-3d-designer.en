---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/effects-material/season-filter.html"
breadcrumb-title: ""
description: Use the Season Filter node to apply seasonal effects to materials for creating spring, summer, fall, and winter variations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Effects (Material) > Season Filter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Season Filter
user-guide-description: ""
user-guide-title: ""
---

# Season Filter

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](season-filter.resources/default-icon.png){width="128px"}

<b>In:</b> Material Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node adds effects such as an animated water level, snow, ice and/or moss.

Keep in mind that this is an older filter that is not intended to be fully PBR-correct. It is mostly kept for legacy/compatibility reasons, although it can still be useful in some cases. More recent PBR-correct versions can be found in [Snow Cover](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/effects-material/snow-cover/snow-cover.md) and [Water Level](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/effects-material/water-level/water-level.md).

The node requires a proper set of material inputs, mainly with a decently detailed Heightmap or Normalmap.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Advanced</b> |  |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Mask</b> <i>False/True</i> | Toggles the use of the Mask map on or off. |
| <b>Light Intensity</b> <i>0.0 - 1.0</i> | Intensity of the (faked) light. |
| <b>Light Angle</b> <i>0.0 - 1.0</i> | Incidence angle of the (faked) light |
| <b>Effect</b> |  |
| <b>Effect From Height or Normal</b> <i>Height, Normal</i> | Chooses which input map drives the effects. |
| <b>Water Level</b> <i>0.0 - 1.0</i> | Raises or lowers the water level based on Height/Normal info. |
| <b>Water Details</b> <i>0.0 - 1.0</i> | Sets amount of details in the water. |
| <b>Refraction</b> <i>0.0 - 1.0</i> | Sets amount of fake refraction in the effect. |
| <b>Reflection</b> <i>0.0 - 1.0</i> | Sets amount of fake reflection in the effect. |
| <b>Reflection Distance</b> <i>0.0 - 1.0</i> | Controls reflection visuals. |
| <b>Reflection Angle</b> <i>0.0 - 1.0</i> | Controls reflection visuals. |
| <b>Flow Direction</b> <i>0.0 - 1.0</i> | Controls animation flow (use Substance Player to visualise). |
| <b>Ice</b> <i>0.0 - 1.0</i> | Sets how frozen the water is. |
| <b>Ice Details</b> <i>0.0 - 1.0</i> | Sets amount of details in the ice. |
| <b>Snow</b> <i>0.0 - 1.0</i> | Sets amount of snow coverage. |
| <b>Moss</b> <i>0.0 - 1.0</i> | Sets amount of moss coverage. |
| <b>Moss Scale</b> <i>1 - 4</i> | Sets scale of generated moss texture. |
| <b>Moss Color</b> <i>(Color value)</i> | Sets color of moss. |
| <b>Water Color</b> <i>(Color value)</i> | Sets color of water, including alpha/opacity. |
| <b>Blending</b> |  |
| <b>Diffuse Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Diffuse. |
| <b>Base Color Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Base Color. |
| <b>Normal Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Normal. |
| <b>Specular Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Specular. |
| <b>Glossiness Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Glossiness. |
| <b>Roughness Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Roughness. |
| <b>Ambient Occlusion Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Ambient Occlusion. |
| <b>Height Intensity</b> <i>0.0 - 1.0</i> | Blending strength of the Height. |
