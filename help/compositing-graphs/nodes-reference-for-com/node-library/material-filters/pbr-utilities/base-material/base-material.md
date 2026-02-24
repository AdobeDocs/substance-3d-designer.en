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
<td style="border: 0;" valign="top">

![](pbr-base-material.png){width="128px"}

## Base Material

**In:** *Material Filters/PBR Utilities*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

The quickest, easiest way to create a Multi-Channel material in [Adobe Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html). This node returns a bundled Full material based on simple, solid color settings and values. This can then be used as placeholder or to refine into a complex material.

The node is very useful when texturing full props and blending multiple materials. In fact, you could start every single material from this node, without ever needing a complex material base.

## Parameters

### Inputs

* Optional inputs for every channel that can be toggled with the switches in "User Defined Inputs".

### Parameters

* **PBR Workflow**: *Metal - Roughness, Specular - Glossiness*Sets the PBR model used.
* **Material Preset**: *Custom, Dielectric, Gold, Silver, Aluminium, Iron, Copper, Titanium, Nickel, Cobalt, Platinum*Quick shortcut to create certain metals. Disables irrelevant options.
* **Base Color**: *(Color value)*Solid color used for Base Color.
* **Metallic**: *(Grayscale value)*Solid value used for Metallic.
* **Diffuse Color**: *(Color value)*Solid color used for Diffuse.
* **Specular**: *(Color value)*Solid color used for Specular.
* **Specular Presets**: *Plastic, Wood, Stone, Brick, Sand, Concrete, Fabric, Rusted Metal, Water, Ice, Glass*Optional quick presets to set PBR-correct Specular values.
* **Specular Range**: *0.0 - 1.0*Adjusts Specular range.
* **Roughness - Glossiness**   
  * **Roughness Value**: *(Grayscale value)*Set the global, base roughness value, if channel is active.
  * **Glossiness Value**: *(Grayscale value)*Solid color used for Glossiness, if channel is active.
  * **Grunge Amount**: *0.0 - 1.0*Extent to which the optional Grunge map input is blended in to Gloss or Roughness.
  * **Grunge Tiling**: *1 - 16*Extent to tile the optional Grunge map by.
  * **Custom Grunge Input**: *False/True*Enables or disables the optional custom Grunge map .
* **Normal**   
  * **Normal from Height Intensity**: *0.0 - 16.0*Optionally converts custom Heightmap to normal and returns this as the material Normalmap.
* **Height**   
  * **Height Position**: *0.0 - 1.0*Solid value used for Height output.
  * **Height Range**: *0.0 - 1.0*Sets influence of User-Defined Heightmap, if enabled.
* **User-Defined Maps**   
  * Toggles on or off all user-defined maps, returning these instead of any solid values.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
