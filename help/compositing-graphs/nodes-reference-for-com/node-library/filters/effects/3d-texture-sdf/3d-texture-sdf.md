---
title: "3D Texture SDF | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > 3D Texture SDF"
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

 