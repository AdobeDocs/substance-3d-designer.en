---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/blending-material/multi-material-blend.html"
breadcrumb-title: ""
description: Use the Multi-Material Blend node to blend multiple materials together for creating complex material combinations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Multi-Material Blend
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi-Material Blend
user-guide-description: ""
user-guide-title: ""
---

# Multi-Material Blend

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/multi-material-blend.png){width="128px"}

<b>In:</b> Material Filters &gt; Blending

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node combines multiple materials based on a Material ID / Color ID map, one that can be baked from a mesh. It takes up to 16 different full materials, with whatever kind of channels you enable in the Channels group.

The node is very useful when texturing full props, as it allows full parametrisation of materials while still dynamically combining them all. Perfect for texturing simple to complex props that have proper ID bakes, or even for creating fully pipelined "Template" Substances that fully cohere to team standards.

Keep in mind that when using this, Material 1, Slot 1 is always the default material and will appear anywhere no other material appears. That is why you cannot set up a color for it. If you want to play this safe, you can for example plug in a [Base Material](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/base-material/base-material.md) that is set to rough black.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>1-16 Full material slots</b> | Amount of slots is determined by the <b>Materials</b> dropdown. |
| <b>Color ID</b> <i>Color Input</i> | Baked Color ID map. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Materials</b> <i>2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16</i> | Sets the maximum amount of different materials to blend. |
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Material 2-16</b> | One group appears for every material enabled. |
| <b>Color</b> <i>(Color value)</i> | Color to pick from the ID map that matches this material slot. |
| <b>Fuzziness</b> <i>0.01 - 1.0</i> | Bleed over into neighbouring colors. |
| <b>Padding</b> <i>0.0 - 1.0</i> | Hardness of transitions: mask contrast. |
