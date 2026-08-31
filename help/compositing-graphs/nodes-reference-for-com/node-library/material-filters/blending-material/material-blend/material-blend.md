---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/blending-material/material-blend.html"
breadcrumb-title: ""
description: Use the Material Blend node to blend entire materials together using masks for creating composite material effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Material Blend
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Blend
user-guide-description: ""
user-guide-title: ""
---

# Material Blend

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](material-blend.resources/material-blend-01.png){width="128px"}

<b>In:</b> Material Filters &gt; Blending

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Material Blend is the Multi-Channel, Full Material Equivalent of [the atomic Blend Node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blend/blend.md). It blends between two full materials (all possibe channels) based on a grayscale mask, or optionally based on one single color from a Color ID mask.

This node is useful if you want to blend two materials and have a grayscale map but no full Color ID bake. If you do have a Color ID bake and want to blend more than two materials, we suggest you use [Multi-Material Blend](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/blending-material/multi-material-blend/multi-material-blend.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>ColorID</b> <i>Color Input</i> | Optional Baked color ID map. |
| <b>Greyscale Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, when using Specular/Glossiness maps instead of Metallic/Roughness for example. |
| <b>Diffuse</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Base Color</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Normal</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Specular</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Emissive</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Glossiness</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Roughness</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Metallic</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Specular Level</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Ambient Occlusion</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Height</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Opacity</b> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity between Foreground and Background |
| <b>Blending Mode</b> <i>Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch</i> |  |
| <b>Color ID Mask</b> <i>False/True</i> | Use Color ID mask instead of grayscale mask. Keep in mind that this is only for one color! |
| <b>Color</b> <i>(Color value)</i> | Which color to pick and convert to white. |
| <b>Fuzziness</b> <i>0.01 - 1.0</i> | The extent to which the color you picked blends over into its neighbours. |
| <b>Padding</b> <i>0.0 - 1.0</i> | Transition contrast of the color you picked. |
