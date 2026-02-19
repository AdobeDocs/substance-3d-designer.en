---
title: "Replace Color Range"
description: "Use the Replace Color Range node to replace colors within a specified range with new colors for color correction."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Replace Color Range
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/replace-color-range.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - color
  - creating-color-palettes
  - color-grading
---




# Replace Color Range

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](replace-color-range.png){width="128px"}

## Replace Color Range

**In:** *Filters/Adjustments*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Replaces Source Color by Target Color, with additional controls. Can for example be used to re-color parts of a Material ID map (bake).

For a more advanced version, see [Color Match.](../color-match/color-match.md)

## Parameters

* **Source Color**: *(Color value)*Color to replace.
* **Target Color**: *(Color value)*Color to replace with.
* **Source Range**: *0.0 -* 1.0  
  Range or tolerance of the picked Source. Can be increased so further neighbouring colours are also hue-shifted.
* **Threshold**: *0.0 - 1.0*Falloff/contrast for range. Set low to replace only Source color, set higher to replace colors blending into Source as well.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="replace-color-range-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
