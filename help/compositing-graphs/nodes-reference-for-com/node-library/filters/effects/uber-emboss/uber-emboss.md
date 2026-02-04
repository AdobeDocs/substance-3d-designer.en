---
title: "Uber Emboss | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Uber Emboss"
---

# Uber Emboss

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](uber-emboss.png){width="128px"}

## Uber Emboss

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Advanced, feature-rich version of [Emboss](../../../../atomic-nodes/emboss/emboss.md). Performs an elaborate 2D, fake lighting effect based on a Heightmap.

Useful when creating baked-in lighting for certain texturing styles when a lot of control is needed.

## Parameters

### Inputs

* **Color**: *Color Input*   
  Base image to modify.
* **Height**: *Grayscale Input*   
  Heightmap used as driver for the effect.

### Parameters

* **Ambient Color**: *(Color value)*Color used in shadowed areas.
* **Diffuse Color**: *(Color value)*Color used in lit areas.
* **Specular Color**: *(Color value)*Color used for specular reflections
* **Light Intensity**: *0.0 - 1.0*  
  Intensity of the (faked) light.
* **Light Angle**: *0.0 - 1.0*  
  Incidence angle of the (faked) light
* **Specular Intensity**: *0.0 - 1.0*Intensity of the specular reflections.
* **Specular Glossiness**: *0.0 - 1.0*Size of the specular highlight.
* **Diffuse Roughness**: *0.0 - 1.0*Roughness used in calculating the diffuse lighting.
* **Shadows Opacity**: *0.0 - 1.0*Blending opacity of the shadowed areas.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="uberemboss-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>

 