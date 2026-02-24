---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/clone-filter-node.html"
breadcrumb-title: ""
description: Use the Clone filter node to duplicate and offset texture regions for creating seamless patterns and tiling effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Clone (Filter Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Clone (Filter Node)
user-guide-description: ""
user-guide-title: ""
---


# Clone (Filter Node)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](clone-4.png)

## Clone

**In:** *Filters/Transforms*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Clones input image once to a specified location. Can function as a crude "clone stamp" tool.

Requires some care to get the intended results:

* Ideally, the input image will have an alpha channel (like a decal), since blending is just a straight copy.
* Mask defaults to black, so to see any results a uniform white grayscale value needs to be plugged in at least.
* Offset will clip outside of the image easily, so use small values.

## Parameters

### Inputs

* **Source**: *Color Input*   
  Image to clone. Important: ideally, the image will have an alpha channel!
* **Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects. Defaults to black!

### Parameters

* **Offset**: *-*   
  Moves or translates the result. Positive is Left and Up, Negative is Right and Down. Use small values, 1.0 and above moves it outside of the image!
* **Blur Mask**: *0.0 - 10.0  
  Apply a blur filter to mask, to soften edges.*

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="clone-example.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
