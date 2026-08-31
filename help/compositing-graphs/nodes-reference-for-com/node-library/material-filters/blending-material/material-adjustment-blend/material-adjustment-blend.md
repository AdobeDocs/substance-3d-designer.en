---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/blending-material/material-adjustment-blend.html"
breadcrumb-title: ""
description: Use the Material Adjustment Blend node to blend material adjustments between materials for fine-tuning composite effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Material Adjustment Blend
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Adjustment Blend
user-guide-description: ""
user-guide-title: ""
---

# Material Adjustment Blend

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](material-adjustment-blend.resources/material-adjustment-blend-01.png){width="128px"}

<b>In:</b> Material Filters &gt; Blending

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node allows adjusting of any and all channels of a full material, based on a mask. It is intended for making a full material workflow easier and quicker.

It is useful for when you want to adjust a few channels of a material (such as making diffuse brighter and roughness darker) based on the same mask.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Color ID Mask</b> <i>Color Input</i> | Mask slot used for masking the node's effects. |
| <b>Greyscale Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggles material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.<br><br>This also enables and disables the appearance of the channel's relevant groups. |
| <b>Diffuse</b> | Performs adjustment operations on the Diffuse channel, in areas defined by the mask. |
| <b>Base Color</b> | Performs adjustment operations on the Base Color channel, in areas defined by the mask. |
| <b>Normal</b> |  |
| <b>Intensity</b> <i>0.0 - 1.0</i> | Tones down Normal Intensity |
| <b>Specular</b> | Performs adjustment operations on the Specular channel, in areas defined by the mask. |
| <b>Emissive</b> | Performs adjustment operations on theEmissive channel, in areas defined by the mask. |
| <b>Glossiness</b> | Performs adjustment operations on the Glossiness channel, in areas defined by the mask. |
| <b>Roughness</b> | Performs adjustment operations on the Roughness channel, in areas defined by the mask. |
| <b>Metallic</b> | Performs adjustment operations on the Metallic channel, in areas defined by the mask. |
| <b>Specular Level</b> | Performs adjustment operations on the Specular Level channel, in areas defined by the mask. |
| <b>Ambient Occlusion</b> | Performs adjustment operations on the Ambient Occlusion channel, in areas defined by the mask. |
| <b>Height</b> | Performs adjustment operations on the Height channel, in areas defined by the mask. |
| <b>Opacity</b> | Performs adjustment operations on the Opacity channel, in areas defined by the mask. |
| <b>Color ID Mask</b> <i>False/True</i> | Set to use Color ID Mask instead of grayscale mask. |
| <b>Fuzziness</b> <i>0.01 - 1.0</i> | If Color ID Mask is enabled, this determines the spread of the Color ID selection color. |
| <b>Color</b> <i>(Color value)</i> | Sets what color to pick from the Color ID map and mask with. |
| <b>Padding</b> <i>0.0 - 1.0</i> | Determines Blending contrast/transitions of the Color ID masking. |
