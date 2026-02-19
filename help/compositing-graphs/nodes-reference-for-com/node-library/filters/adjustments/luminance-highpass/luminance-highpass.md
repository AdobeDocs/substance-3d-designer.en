---
title: "Luminance Highpass"
description: "Use the Luminance Highpass node to extract high-frequency luminance details from textures for enhancing surface details."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Luminance Highpass
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/luminance-highpass.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - hdri
  - brightness
  - lighting
---




# Luminance Highpass

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](luminance-highpass.png){width="128px"}

## Luminance Highpass

**In:** *Filters/Adjustments*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Cancels out lighting information by performing a [highpass ](../highpass/highpass.md)on the input's Luminance value. Useful for fixing photographed textures with lighting information. Can be combined in  [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) with multiple passes to remove different frequencies of lighting details.

Does a slightly better job at preserving colors than [Lighting Cancel Low Frequencies.](../lighting-cancel-low-fre/lighting-cancel-low-frequencies.md)

## Parameters

* **Radius**: *0.0 - 64.0*Radius of the highpass effect. A smaller radius cancels smaller lighting, adjust to match the input images.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="luminance-highpass-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
