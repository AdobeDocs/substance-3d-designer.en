---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/3d-texture-sdf.html"
breadcrumb-title: ""
description: Use the 3D Texture SDF node to generate signed distance field textures from 3D data for creating smooth shapes and effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > 3D Texture SDF
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: 3D Texture SDF
user-guide-description: ""
user-guide-title: ""
---


# 3D Texture SDF

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](3dtexturesdf.png){width="200px"}

**In:** *Filter/Effect*

**Simple**

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The **3D Texture SDF** node generates the *signed distance field* of a shape from the **Input**'s *3D texture* mask representing the slices of the shape's *volume*.

</td>
</tr>
</table>

## Parameters

### Inputs

* **Mask Input** *Grayscale*  
  The *3D texture* mask representing the slices of a shape's *volume*.

### Parameters

* **Threshold** *Float*  
  When the shape volume is described by a *fading gradient*, sets the gradient value at which the *surface* of the shape is *detected*.
* **Output** *Integer*  
  The type of distance field which should be output:  
  * *Distance Field*: outputs a distance field describing the distances *outside* the shape.  
  * *Signed Distance Field*: outputs a distance field describing the distances *outside* (positive) and *inside* (negative) the shape.

## Example Images

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3dtexturesdf-variant.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](3dtexturesdf-variant2.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](3dtexturesdf-node.png){width="256px"}

</td>
</tr>
</table>
