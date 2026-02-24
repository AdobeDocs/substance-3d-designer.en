---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/3d-texture-offset.html"
breadcrumb-title: ""
description: Use the 3D Texture Offset node to offset textures in 3D space for creating parallax effects and surface variations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > 3D Texture Offset
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: 3D Texture Offset
user-guide-description: ""
user-guide-title: ""
---


# 3D Texture Offset

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3dtextureoffsetgrayscale.png){width="200px"}

</td>
<td style="border: 0;" valign="top">

![](3dtextureoffsetcolor.png){width="200px"}

</td>
</tr>
</table>

**In:** *Filter/Transformation*

**Simple**

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The **3D Texture Offset** node applies an *offset transformation* in the **X**, **Y** and **Z** axes on an object described by the *3D texture* connected to the **Input**.

</td>
</tr>
</table>

## Parameters

### Inputs

* **Input** *Grayscale/Color*  
  The *3D texture* describing a 3D object.  
  The object is commonly described in a *unit cube*.

### Parameters

* **Offset** *Float3*  
  The amount of offset in *world space* applied on the object described by the *3D texture* connected to the **Input**.

## Example Images

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3dtextureoffset-variant.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](3dtextureoffset-node.png){width="256px"}

</td>
</tr>
</table>
