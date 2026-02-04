---
title: "3D Texture Offset"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > 3D Texture Offset"
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
