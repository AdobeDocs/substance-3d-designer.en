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
<td style="border: 0;" valign="top">

![](../../../../../../assets/snow-cover.png){width="128px"}

## Snow Cover

**In:** *Material Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

All-in-one effect to add snow buildup on a full material. Strongly relies on a good, high-quality Heightmap, such as from a photoscan. The result is intended to be PBR-correct.

## Parameters

### Inputs

* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Channels**  
  Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.
* **Fresh Snow**: *0.0 - 1.0*Sets amount of snow in Raised areas. The result is tied to the Melted Snow parameter.
* **Melted Snow**: *0.0 - 1.0*Sets amount of melted snow in lowered corners.
* **Buildup**: *0.0 - 1.0*Mostly affects Height output, determines height pile-up effect.
* **Smoothness**: *0.0 - 1.0*Sets smoothing out of height details by snow buildup.
* **Flakes Intensity**: *0.0 - 1.0*Mainly affects Normalmap, intensity of flake details.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
