---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/symmetry-slice.html"
breadcrumb-title: ""
description: Use the Symmetry Slice node to slice textures along symmetry axes for creating mirrored patterns and effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Symmetry Slice
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Symmetry Slice
user-guide-description: ""
user-guide-title: ""
---


# Symmetry Slice

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](mirror-2.png){width="128px"}

## Symmetry Slice

**In:** *Filters/Transforms*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Complex Symmetry/mirroring operation node. Allows for a large variety of geometric operations with full control, but requires some experimenting.

Compared to [Mirror](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/mirror-filter-node/mirror-filter-node.md) and [Symmetry](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/symmetry/symmetry.md), this node has many more options.

## Parameters

* **Symmetry Mode**: *0 - 6*Choose symmetry geometry/mirror line. Options are Horizontal, Vertical, Diagonal Left-Right, Diagonal Right-Left, Vertical Invert, Corner and Diagonal Corner.
* **Transfer Mode**: *0 - 6  
  Blend mode. Options are:*
* **Blend**: *0.0 - 1.0*Blends the original image back into the result.
* **Flip Side**: *False/True*Flips origin, meaning the origin side of the operation is reversed. Left to right symmetry for example becomes right to left.
* **Flip Side2**: *False/True*Only used when Symmetry Mode is 5 or 6. Flip corner origin.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="symslice.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
