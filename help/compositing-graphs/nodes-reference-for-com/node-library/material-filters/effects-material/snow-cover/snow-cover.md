---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/effects-material/snow-cover.html"
breadcrumb-title: ""
description: Use the Snow Cover node to add snow accumulation effects to materials based on surface angle and position.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Effects (Material) > Snow Cover
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Snow Cover
user-guide-description: ""
user-guide-title: ""
---

# Snow Cover

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](snow-cover.resources/snow-cover.png){width="128px"}

<b>In:</b> Material Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

All-in-one effect to add snow buildup on a full material. Strongly relies on a good, high-quality Heightmap, such as from a photoscan. The result is intended to be PBR-correct.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Fresh Snow</b> <i>0.0 - 1.0</i> | Sets amount of snow in Raised areas. The result is tied to the Melted Snow parameter. |
| <b>Melted Snow</b> <i>0.0 - 1.0</i> | Sets amount of melted snow in lowered corners. |
| <b>Buildup</b> <i>0.0 - 1.0</i> | Mostly affects Height output, determines height pile-up effect. |
| <b>Smoothness</b> <i>0.0 - 1.0</i> | Sets smoothing out of height details by snow buildup. |
| <b>Flakes Intensity</b> <i>0.0 - 1.0</i> | Mainly affects Normalmap, intensity of flake details. |
