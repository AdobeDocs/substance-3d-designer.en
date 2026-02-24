---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/height-normal-blender.html"
breadcrumb-title: ""
description: Use the Height Normal Blender node to blend height and normal maps for combining surface detail information.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Height Normal Blender
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Height Normal Blender
user-guide-description: ""
user-guide-title: ""
---


# Height Normal Blender

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](height-normal-blender.png){width="128px"}

## Height Normal Blender

**In:** *Filters/Normal Map*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

A shortcut node that blends a grayscale Heightmap onto a Normalmap. The Height input is converted to a Normalmap internally and then blended correctly with the Normal input.

This is a quicker way to blend details than manually doing this with separate nodes, but you might find it lacks some control and refinement for certain needs.

## Parameters

### Inputs

* **Height**: *Grayscale Input*   
  Grayscale Heightmap to blend with.
* **Normal**: *Color Input*   
  Base Normalmap to blend onto.

### Parameters

* **Normal Intensity**: *0.0 - 16.0*Intensity of the Height input's normal conversion.
* **Normal Format**: *DirectX, OpenGL*  
  Switches between different Normalmap formats (inverts the green channel).

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
