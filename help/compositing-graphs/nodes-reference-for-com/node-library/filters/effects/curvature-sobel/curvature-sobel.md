---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/curvature-sobel.html"
breadcrumb-title: ""
description: Use the Curvature Sobel node to detect curvature edges using Sobel operators for creating edge-based masks.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Curvature Sobel
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Curvature Sobel
user-guide-description: ""
user-guide-title: ""
---


# Curvature Sobel

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](curvature-sobel.png){width="128px"}

## Curvature Sobel

**In:** *Filters/Effects*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a simple, harsh single-pass curvature conversion to input [Normalmap](../../../../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md). The resulting map has white tints for convex areas and black tints for concave. Curvature will always produce thicker lines and sharp transitions.

This node is useful for quick highlighting or darkening of certain edges. It is slightly different from [Curvature](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/effects/curvature-filter-node/curvature-filter-node.md), as it produces better quality results but is still sharp and harsh.

## Parameters

* **Intensity**: *0.0 - 1.0*Intensity of the effect, adjusts contrast.
* **Normal type**: *DirectX, OpenGL*

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="curv-sobel-ex.png" width="300px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
