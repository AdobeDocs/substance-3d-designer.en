---
title: "PBR Render Mapping"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > PBR Render Mapping"
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

This is an extension node for the [PBR Render node](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md), that allows you to map a separate texture onto the shape from a previous [PBR Render](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md). Its main goal is to let you remap each separate channel from your [PBR Render](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md), back onto the shape, to create composite map-channel breakdowns, as in the examples below. You're free to create your own composite method and masks by using the PBR Render Mapping nodes as component.

Color and Grayscale version exist for the two types of data: use color for diffuse maps, use grayscale for roughness, metal and other grayscale maps.

### Inputs

* **Texture**: *Color/Grayscale Input*  
  Texture to map onto shape.
* **UVs**: *Color Input*Mandatory UV-data input from a [PBR Render node.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md)

## Parameters

* **Background Color**: *(Color value)*Set a solid color value to use in the background.

## Example Images

Example is a composite of four different PBR Render Mapping nodes, using a [Histogram Select](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-select/histogram-select.md) on a [Linear gradient](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/gradient-linear-1/gradient-linear-1.md) as masks.

![](pbr-render-mapping-ex.png){width="256px"}

![](pbr-render-mapping-ex-2.png){width="256px"}

</td>
</tr>
</table>
