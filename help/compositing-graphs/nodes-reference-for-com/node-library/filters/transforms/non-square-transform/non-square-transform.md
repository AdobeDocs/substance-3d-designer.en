---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/non-square-transform.html"
breadcrumb-title: ""
description: Use the Non-Square Transform node to apply transformations to non-square textures with independent X and Y scaling.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Non-Square Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Non-Square Transform
user-guide-description: ""
user-guide-title: ""
---



# Non-Square Transform

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](safe-transform.png)

![](safe-transform-grayscale.png)

## Non-Square Transform (Grayscale)

**In:** *Filters/Transforms*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Nonsquare-safe version of [Transform 2D](../../../../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/transformation-2d/transformation-2d.md). Automatically detects nonsquare ratios and can transform square input images onto a nonsquare canvas.

Make sure you fully understand the [Graph Parameters ](../../../../../../help/compositing-graphs/graph-parameters/graph-parameters.md)to make the best use of this node, as you will need to set a few settings correctly:

* Your **Graph** Size should be nonsquare, otherwise there is no need for this node.
* Set the Non Square Transform **node's** Output Size to "*Relative to Parent*".
* Set the **node's** tiling mode to "*No Tiling*" if you only want to transform your input to a single position.

## Parameters

* **Tile Mode**: *Automatic, Manual*Enable automatic non-square compensations or not.
* **Tile**: *1 - 16*Only accessible when Tile Mode is set to Manual. Allows you to change the scale in a tiling-safe way.
* **Offset**: *0.0 - 1.0*  
  Moves or translates the result. Double-click the slider to enter negative values.
* **Rotation**: *0.0 - 1.0*Rotates the input image.
* **Safe Rotation (Square Only)**: *False/True*Snaps to safe values to maintain sharpness of pixels.
* **Background Color**: *(Color value)*Background color to fill image with. Only visible when [Tiling Mode in Base Parameters is set to "*No Tiling*"](../../../../../../help/compositing-graphs/graph-parameters/graph-parameters.md).

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="nonsquare-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
