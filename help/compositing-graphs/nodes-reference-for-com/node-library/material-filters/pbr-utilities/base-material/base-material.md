---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/pbr-utilities/base-material.html"
breadcrumb-title: ""
description: Use the Base Material node to create base material properties for building physically-based materials from scratch.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > Base Material
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Base Material
user-guide-description: ""
user-guide-title: ""
---

# Base Material

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](base-material.resources/base-material-01.png){width="128px"}

<b>In:</b> Material Filters &gt; PBR Utilities

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The quickest, easiest way to create a Multi-Channel material in [Adobe Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html). This node returns a bundled Full material based on simple, solid color settings and values. This can then be used as placeholder or to refine into a complex material.

The node is very useful when texturing full props and blending multiple materials. In fact, you could start every single material from this node, without ever needing a complex material base.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
|  | Optional inputs for every channel that can be toggled with the switches in "User Defined Inputs". |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>PBR Workflow</b> <i>Metal - Roughness, Specular - Glossiness</i> | Sets the PBR model used. |
| <b>Material Preset</b> <i>Custom, Dielectric, Gold, Silver, Aluminium, Iron, Copper, Titanium, Nickel, Cobalt, Platinum</i> | Quick shortcut to create certain metals. Disables irrelevant options. |
| <b>Base Color</b> <i>(Color value)</i> | Solid color used for Base Color. |
| <b>Metallic</b> <i>(Grayscale value)</i> | Solid value used for Metallic. |
| <b>Diffuse Color</b> <i>(Color value)</i> | Solid color used for Diffuse. |
| <b>Specular</b> <i>(Color value)</i> | Solid color used for Specular. |
| <b>Specular Presets</b> <i>Plastic, Wood, Stone, Brick, Sand, Concrete, Fabric, Rusted Metal, Water, Ice, Glass</i> | Optional quick presets to set PBR-correct Specular values. |
| <b>Specular Range</b> <i>0.0 - 1.0</i> | Adjusts Specular range. |
| <b>Roughness - Glossiness</b> |  |
| <b>Roughness Value</b> <i>(Grayscale value)</i> | Set the global, base roughness value, if channel is active. |
| <b>Glossiness Value</b> <i>(Grayscale value)</i> | Solid color used for Glossiness, if channel is active. |
| <b>Grunge Amount</b> <i>0.0 - 1.0</i> | Extent to which the optional Grunge map input is blended in to Gloss or Roughness. |
| <b>Grunge Tiling</b> <i>1 - 16</i> | Extent to tile the optional Grunge map by. |
| <b>Custom Grunge Input</b> <i>False/True</i> | Enables or disables the optional custom Grunge map . |
| <b>Normal</b> |  |
| <b>Normal from Height Intensity</b> <i>0.0 - 16.0</i> | Optionally converts custom Heightmap to normal and returns this as the material Normalmap. |
| <b>Height</b> |  |
| <b>Height Position</b> <i>0.0 - 1.0</i> | Solid value used for Height output. |
| <b>Height Range</b> <i>0.0 - 1.0</i> | Sets influence of User-Defined Heightmap, if enabled. |
| <b>User-Defined Maps</b> | Toggles on or off all user-defined maps, returning these instead of any solid values. |
