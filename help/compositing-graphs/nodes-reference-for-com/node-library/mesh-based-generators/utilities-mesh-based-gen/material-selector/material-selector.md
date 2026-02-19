---
title: "Material Selector"
description: "Use the Material Selector node to select materials based on mesh data for creating multi-material texture effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Utilities (Mesh Based Generators) > Material Selector
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/utilities-mesh-based-generators/material-selector.html"
helpx_creative_field:
  - painting-illustration
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - intermediate
helpx_learn_topic:
  - masking
  - add-objects-to-images
  - replacing-backgrounds
---




# Material Selector

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](material-selector.png){width="128px"}

## Material Selector

**In:** *Mesh Based Generators**/Utilities*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Converts a full-color ID map to a binary, black and white mask. Allows blending and combining of different colors into one mask.

This is handy if you don't want to use [Multi-Material Blend](../../../material-filters/blending-material/multi-material-blend/multi-material-blend.md) and prefer to use the mask manually, or alternatively if you want to manually use those same masks in other locations.

## Parameters

* **Materials**: 1 - 16  
  Sets number of materials that combining is enabled for.
* **Enable Material #1-16**: False/True  
  Toggles blending and combining of colors into the final output mask. Can be enabled for as many colors as you want to combine.
* **Material #1-16**: (Color value)  
  Colorpicker for the materials color that will be converted to black and white.
* **Color Picker Parameters**   
  Modifies blending and conversion of the color to black and white.  
  * **Fuzziness**: 0.01 - 1.0  
    How much to blend in with neighbouring colors.
  * **Padding**: 0.0 - 1.0  
    Sharpness of the transition, like Contrast.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="matselector-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
