---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/luminance-highpass.html"
breadcrumb-title: ""
description: Use the Luminance Highpass node to extract high-frequency luminance details from textures for enhancing surface details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Luminance Highpass
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Luminance Highpass
user-guide-description: ""
user-guide-title: ""
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

Cancels out lighting information by performing a [highpass ](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/highpass/highpass.md)on the input's Luminance value. Useful for fixing photographed textures with lighting information. Can be combined in  [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) with multiple passes to remove different frequencies of lighting details.

Does a slightly better job at preserving colors than [Lighting Cancel Low Frequencies.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/lighting-cancel-low-fre/lighting-cancel-low-frequencies.md)

## Parameters

* **Radius**: *0.0 - 64.0*Radius of the highpass effect. A smaller radius cancels smaller lighting, adjust to match the input images.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="luminance-highpass-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
