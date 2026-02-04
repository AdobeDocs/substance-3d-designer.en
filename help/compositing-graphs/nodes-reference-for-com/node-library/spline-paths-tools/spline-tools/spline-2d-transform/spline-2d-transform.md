---
title: "Spline 2D Transform | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline 2D Transform"
---

# Spline 2D Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-2d-transform-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Applies a global transformation to all input splines, including inverting their direction.

</td>
</tr>
</table>

## Input connectors

<b>Preview</b> *Grayscale*The preview of the input splines as a grayscale image.

<b>Spline Coords</b> *Color*The coordinates of the input splines’ points encoded in the RGBA channels of a color image:  
<b>    R</b> - X position  
<b>    G</b> - Y position  
<b>    B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*Additional data of the input splines encoded in the RGBA channels of a color image.  
<b>    R</b> - Tangents X  
<b>    G</b> - Tangents Y  
<b>    B</b> - Unused  
<b>    A</b> - Unused

<b>Spline Amount</b> *Integer*The number of input splines.

## Output connectors

<b>Preview</b> *Grayscale*The preview of the output splines as a grayscale image.

<b>Spline Coords</b> *Color*The coordinates of the output splines’ points encoded in the RGBA channels of a color image.  
    <b>R</b> - X position  
    <b>G</b> - Y position  
    <b>B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*Additional data of the output splines encoded in the RGBA channels of a color image.  
    <b>R</b> - Tangents X  
    <b>G</b> - Tangents Y  
    <b>B</b> - Unused  
    <b>A</b> - Unused

<b>Spline Amount</b> *Integer*The number of output splines.

## Parameters

<b>Flip Direction</b> *Boolean*Inverts the direction of the spline.

<b>Transform Matrix</b> *Float4*The transformation matrix applied to the splines.  
Three modes of editing the matrix parameters are available:  
*- Transformation gizmo*: tweak the handles of the gizmo displayed in the 2D View when the Spline 2D Transform node is selected;  
*- Rotation/Stretch*: Individually control the rotation and stretching of the splines. Note that values are always applied relatively to the current transformation. E.g., applying 50% width twice results in a 25% width;  
*- Matrix values*: Click the Edit Matrix Values button to input the raw numerical values of the matrix directly.

<b>Offset</b> *Float2*Applies a position offset to the splines in X (horizontal) and Y (vertical).

+++Preview


Show Direction HelperBooleanDisplays a dot at the start of the spline and an arrowhead at its end in the Preview output.





Show Thickness EnvelopeBooleanDisplays additional lines at the edges of the spline’s thickness.





Segments AmountIntegerAdjusts the number of segments used to draw the spline visualization in the Preview output.A higher value results in a smoother line.





Thickness (px)FloatAdjusts the thickness of the spline visualization in pixels in the Preview output.



+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="Spline2DTransform-Variant1-Before.jpg" alt="Spline2DTransform-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="Spline2DTransform-Variant2-After.jpg" alt="Spline2DTransform-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="Spline2DTransform-Variant1-Before.jpg" alt="Spline2DTransform-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="Spline2DTransform-Variant1-After.jpg" alt="Spline2DTransform-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](Spline2DTransform-Demo1.gif "Node example 1")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

 