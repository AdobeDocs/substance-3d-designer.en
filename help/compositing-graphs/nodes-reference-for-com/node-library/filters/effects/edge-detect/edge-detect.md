---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/edge-detect.html"
breadcrumb-title: ""
description: Use the Edge Detect node to detect edges in textures for creating outlines and edge-based mask effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Edge Detect
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Edge Detect
user-guide-description: ""
user-guide-title: ""
---


# Edge Detect

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-detect.png){width="128px"}

## Edge Detect

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Detects contrast in a black and white images, then creates a black and white mask highlighting the contrast.

Useful in many cases where some sort of mask for edges is needed. Keep in mind that it works best with high-contrast input; if needed, adjust the contrast before passing something into this node.

## Parameters

* **Edge Width**: *1.0 - 16.0*Width of the detected areas around the edges.
* **Edge Roundness**: *0.0 - 16.0*Rounds, blurs and smooths together the generated mask.
* **Invert**: *False/True*  
  Inverts the result.
* **Tolerance**: *0.0 - 1.0*Tolerance treshold factor for where edges should appear.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="edge-detect-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
