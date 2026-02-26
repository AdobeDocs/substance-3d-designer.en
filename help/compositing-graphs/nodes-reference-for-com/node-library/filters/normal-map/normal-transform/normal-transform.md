---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-transform.html"
breadcrumb-title: ""
description: Use the Normal Transform node to apply transformations to normal maps while preserving vector directions correctly.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Transform
user-guide-description: ""
user-guide-title: ""
---

# Normal Transform

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/normal-transform.png){width="128px"}

## Normal Transform

**In:** *Filters/Normal Map*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Similar to the atomic Transform 2D node, this allows for transformation of Normalmaps without breaking Tangent-space, instead it is recalculated on the fly, resulting in always correct Normalmaps.

## Parameters

* **Matrix2x2**: *(Transformation Matrix):*  
  Rotate or Scale the input.
* **Offset**: *-0.5 - 0.5*  
   Moves or translates the result. When the Transformation control is present, result can be modified by directly interacting with the canvas.
* **Normal Format**: *DirectX, OpenGL*  
   Switch between different Normal Map formats (inverts the green channel)

</td>
</tr>
</table>
