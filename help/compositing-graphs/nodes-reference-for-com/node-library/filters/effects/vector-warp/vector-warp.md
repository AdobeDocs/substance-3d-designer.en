---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/vector-warp.html"
breadcrumb-title: ""
description: Use the Vector Warp node to warp textures using vector fields for creating fluid and organic distortion effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Vector Warp
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Vector Warp
user-guide-description: ""
user-guide-title: ""
---


# Vector Warp

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](vector-warp.png){width="128px"}

![](vector-warp-grayscale.png){width="128px"}

## Vector Warp (Grayscale)

**In:** *Filters/Effects*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Vector warp is an advanced distortion effect, similar to [Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/warp/warp.md) and [Directional Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/directional-warp/directional-warp.md), with the main difference being that it is driven by a (color) vector bitmap rather than a grayscale map. This means it is more powerful and versatile than its atomic node cousins.

The Vector Map is similar to a Normalmap, but it does not need to be normalised and only the R and Green (X and Y) channel are used. Blue and Alpha channels can be left black if you want. Constructing a good Vector Map can be the biggest challenge in using this node; you can either [convert grayscale maps to Normal](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md), or construct the map by combining channels with[ RGBA Merge.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/channels/rgba-merge/rgba-merge.md) Alternatively, something like a ["Flow Map"](https://helpx.adobe.com/substance-3d-painter/painting/advanced-channel-painting/flow-map-painting.html) is also useable.

This node can be useful when you want to do very specific distortions with varying directions, where standard Warp nodes don't cut it.

## Parameters

### Inputs

* **Input**: *Color Input*   
  Map to distort.
* **Vector Map**: *Color Input*   
  Distortion driver map. Color channels Red and Blue are used.

### Parameters

* **Intensity**: *0.0 - 1.0*Intensity multiplier for the Vector Map.
* **Vector Format**: *DirectX, OpenGL*Swaps the Green channel between Up and Down interpretation.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="vector-warp-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
