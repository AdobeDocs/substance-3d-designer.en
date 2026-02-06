---
title: "Path 2D Transform"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Path 2D Transform"
---

# Path 2D Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](path-2d-transform-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Transforms Paths using a gizmo.

</td>
</tr>
</table>

## Input connectors

<b>Paths</b> *Color*  
A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../mask-to-paths/mask-to-paths.md) or to another Path-processing node.

## Output connectors

<b>Paths</b> *Color*  
The transformed Paths. You can either use [Preview Paths](../preview-paths/preview-paths.md) to get an idea of what the result represents, use another Paths-processing node, or input it to a [Paths to Spline](../paths-to-spline/paths-to-spline.md) to further process it as Splines.

## Parameters

<b>Transform matrix</b> *Float4*  
The transformation matrix applied to the splines. Three modes of editing the matrix parameters are available:  
*- Transformation gizmo:* tweak the handles of the gizmo displayed in the [2D View](../../../../../../interface/2d-view/2d-view.md) when the Spline 2D Transform node is selected;  
*- Rotation/Stretch:* Individually control the rotation and stretching of the splines. Note that values are always applied relatively to the current transformation. E.g., applying 50% width twice results in a 25% width;  
*- Matrix values:* Click the <b>Edit Matrix Values</b> button to input the raw numerical values of the matrix directly.

<b>Offset</b> *Float2*  
Applies a position offset to the splines in X (horizontal) and Y (vertical).

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsPolygon_Variant1.jpg" alt="PathsPolygon_Variant1">
      <br><i>Before</i>
    </td>
    <td>
      <img src="Paths2DTransform-Variant1.jpg" alt="Paths2DTransform-Variant1">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsPolygon_Variant1.jpg" alt="PathsPolygon_Variant1">
      <br><i>Before</i>
    </td>
    <td>
      <img src="Paths2DTransform-Variant2.jpg" alt="Paths2DTransform-Variant2">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>
