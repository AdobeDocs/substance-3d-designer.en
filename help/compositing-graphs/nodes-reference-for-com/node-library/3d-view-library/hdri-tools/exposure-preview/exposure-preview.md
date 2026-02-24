---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/exposure-preview.html"
breadcrumb-title: ""
description: Use the Exposure Preview node to preview exposure adjustments in HDRI environments before final rendering.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Exposure Preview
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Exposure Preview
user-guide-description: ""
user-guide-title: ""
---


# Exposure Preview

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](hdr-exposure-preview.png){width="200px"}

## Exposure Preview

**In:** *3D View/HDRI Tools*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Helper node to preview exposure steps. Users sets a min and max value, the node generates a much larger image with a number different exposed versions of the original input. The different versions are always stacked horizontally, the amount depends on the resolution of the node or graph.

## Parameters

* **Max Exposure (EV)**: *-8.0 - 8.0*  
  Maximum exposure of the top, brightest image.
* **Min Exposure (EV)**: *-8.0 - 8.0*Minimum exposure of the bottom, darkest image.

## Example Images

![](exp-preview-ex.png)

</td>
</tr>
</table>
