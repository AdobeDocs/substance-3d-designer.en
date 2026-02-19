---
title: "PBR Render Mapping"
description: "Use the PBR Render Mapping node to convert material outputs to different PBR render mapping formats."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > PBR Render Mapping
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/pbr-utilities/pbr-render-mapping.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - pbr
  - creative-effects
  - texture
---




# PBR Render Mapping

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](pbr-render-mapping-color.png)![](pbr-render-mapping-grayscale.png)

## PBR Render Mapping (Color/Grayscale)

**In:** *Material Filters/PBR Utilities*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

This is an extension node for the [PBR Render node](../pbr-render/pbr-render.md), that allows you to map a separate texture onto the shape from a previous [PBR Render](../pbr-render/pbr-render.md). Its main goal is to let you remap each separate channel from your [PBR Render](../pbr-render/pbr-render.md), back onto the shape, to create composite map-channel breakdowns, as in the examples below. You're free to create your own composite method and masks by using the PBR Render Mapping nodes as component.

Color and Grayscale version exist for the two types of data: use color for diffuse maps, use grayscale for roughness, metal and other grayscale maps.

### Inputs

* **Texture**: *Color/Grayscale Input*  
  Texture to map onto shape.
* **UVs**: *Color Input*Mandatory UV-data input from a [PBR Render node.](../pbr-render/pbr-render.md)

## Parameters

* **Background Color**: *(Color value)*Set a solid color value to use in the background.

## Example Images

Example is a composite of four different PBR Render Mapping nodes, using a [Histogram Select](../../../filters/adjustments/histogram-select/histogram-select.md) on a [Linear gradient](../../../texture-generators/patterns/gradient-linear-1/gradient-linear-1.md) as masks.

![](pbr-render-mapping-ex.png){width="256px"}

![](pbr-render-mapping-ex-2.png){width="256px"}

</td>
</tr>
</table>
