---
title: "BaseColor  Metallic  Roughness converter"
description: "Use the BaseColor Metallic Roughness Converter node to convert between different PBR material formats and workflows."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > BaseColor  Metallic  Roughness converter
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/pbr-utilities/basecolor-metallic-roughness-converter.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - materials
  - reflections
  - pbr
---




# BaseColor / Metallic / Roughness converter

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](pbr-convert.png){width="128px"}

## BaseColor / Metallic / Roughness converter

**In:** *Material Filters/PBR Utilities*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

This node converts Basecolor, Metallic and Roughness maps to different PBR model outputs, such as Specular/Glossiness model. Some of the included output targets are well-known render engines such as Vray, Corona, Redshift, Renderman and Arnold.

This is useful if you have graphs or materials that are made with one model of PBR, while your target requires a different model.

## Parameters

* **Use SpecularLevel input**: *False/True*Exposes an extra input slot to SpecularLevel input. This is also taken into account during conversion.
* ***Target**: *PBR Diffuse/Specular/Gloss, Vray (GGX), Corona, Corona 1.6+, Redshift 1.x, Arnold 4 (AiStandard), Arnold 4 (AlSurface), RenderMan (PxrSurface)**Sets the conversion target model.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
