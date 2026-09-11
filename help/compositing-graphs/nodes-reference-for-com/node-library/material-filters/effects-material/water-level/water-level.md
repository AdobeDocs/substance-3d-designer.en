---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/effects-material/water-level.html"
breadcrumb-title: ""
description: Use the Water Level node to blend materials based on water level height for creating realistic water effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Effects (Material) > Water Level
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Water Level
user-guide-description: ""
user-guide-title: ""
---

# Water Level

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](water-level.resources/water-level.png){width="128px"}

<b>In:</b> Material Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

All-in-one effect that adds a water level to a full material input. Input material must have a good, high-quality Heightmap for the effect to work. The result is PBR-correct.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Water Level</b> <i>0.0 - 1.0</i> | Main control to raise or lower the water level. |
| <b>Water Darkness</b> <i>0.0 - 1.0</i> | Sets general "transparency" of the water. |
| <b>Edges Wetness</b> <i>0.0 - 1.0</i> | Determines how much of a wet look the water edges should have. |
| <b>Edges Wetness Distance</b> <i>0.0 - 1.0</i> | Sets how far the wet edges reach. |
| <b>Depth Blur Amount</b> <i>0.0 - 1.0</i> | Sets amount of blur based on depth below water. Modifies blur radius. |
| <b>Depth Blur Opacity</b> <i>0.0 - 1.0</i> | Determines how much depth blur is blended in, can be used to lower the effect of the blur. |
| <b>Sludge Color</b> <i>(Color value)</i> | Sets the color of the sludge effect. |
| <b>Sludge Depth</b> <i>0.0 - 1.0</i> | Sets the depth at which sludge starts appearing, relative to water level. |
| <b>Sludge Opacity</b> <i>0.0 - 1.0</i> | Sets global opacity of the sludge effect. |
| <b>Frost</b> <i>0.0 - 1.0</i> | Sets the amount of frost. Starts appearing from the outer edges and moves inwards. |
| <b>Frost Intensity</b> <i>0.0 - 1.0</i> | Sets the intensity of frost, controls the "opacity" of the effect. |
| <b>Frost Cracks</b> <i>0.0 - 1.0</i> | Sets the amount of cracks in the transitions from frozen to liquid. |
| <b>Frost Normal Format</b> <i>DirectX/OpenGL</i> | Switches Frost Normalmap effect green channel. |
