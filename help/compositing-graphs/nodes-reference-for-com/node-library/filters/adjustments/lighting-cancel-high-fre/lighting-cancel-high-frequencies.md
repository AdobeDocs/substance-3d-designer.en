---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/lighting-cancel-high-frequencies.html"
breadcrumb-title: ""
description: Use the Lighting Cancel High Frequencies node to remove high-frequency lighting details from textures for material analysis.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Lighting Cancel High Frequencies
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Lighting Cancel High Frequencies
user-guide-description: ""
user-guide-title: ""
---

# Lighting Cancel High Frequencies

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/lighting-cancel-high-frequencies.png){width="128px"}

## Lighting Cancel High Frequencies

**In:** *Filters/Adjustments*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Similar to [Highpass](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/highpass/highpass.md), but more suited for full color images (it doesn't desaturate the result as much), this node tries to cancel out high frequency, small lighting details.

Also see [Lighting Cancel Low Frequencies](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/lighting-cancel-low-fre/lighting-cancel-low-frequencies.md), and the more advanced, recommended [Luminance Highpass](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/luminance-highpass/luminance-highpass.md).

## Parameters

* **Intensity**: *0.0 -* 1.0  
  Strength of the lighting cancel effect.
* **Radius**: *0.0 - 10.0*Radius or size of the lighting details to cancel.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="../../../../../../assets/lighting-cancel-highfrequencies-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
