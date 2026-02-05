---
title: "Spline Sample Thickness"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Sample Thickness"
---

# Spline Sample Thickness

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-sample-thickness-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Modifies the thickness of the input splines by mapping an input Thickness Map onto them.

The effect of the mapped height map can be adjusted by changing its blending mode and the opacity of that effect.

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

<b>Thickness Map</b> *Grayscale*The input grayscale image used to change the input spline’s thickness.

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

<b>Sampling Mode</b> *Integer*The method of mapping the values in the Thickness Map to the splines:  
*- Texture space*: The values are applied to the splines where they would be if placed in a texture using the texture’s UV coordinates. This effectively applies the value to the splines ‘in place’;  
*- Horizontal along spline*: The values are applied to the encoded splines’ coordinates directly (see Spline Coords input), where each row is applied to a different spline from top to bottom;  
*- Hor. along spline (rand. offset X)*: The values are applied to the encoded splines’ coordinates directly (see Spline Coords input), with a random horizontal offset in the Scale map for each spline (I.e., each row in Spline Coords);  
*- Hor. along spline (rand. offset Y)*: The values are applied to the encoded splines’ coordinates directly (see Spline Coords input), with a random vertical offset in the Scale map for each spline (I.e., each row in Spline Coords).

<b>Opacity</b> *Float*A multiplier for the intensity of the Thickness Map input’s contribution to the spline’s thickness.<b></b>

<b>Blending Mode</b> *Integer*The method of blending the Thickness Map’s data with the input spline’s thickness:  
*- Copy*: Override the spline’s thickness with the Height Map values;  
*- Add*: Add the Thickness Map values to the spline’s thickness;  
*- Subtract*: Subtract the Thickness Map values to the spline’s thickness;  
*- Multiply*: Multiply the Thickness Map values against the spline’s thickness.

+++Preview
<b>Segments Amount</b> *Integer*Adjusts the number of segments used to draw the spline visualization in the Preview output.  
A higher value results in a smoother line.

<b>Show Direction Helper</b> *Boolean*Displays a dot at the start of the spline and an arrowhead at its end in the Preview output.

<b>Show Thickness Envelope</b> *Boolean*  
Displays additional lines at the edges of the spline’s thickness.

<b>Thickness (px)</b> *Float*Adjusts the thickness of the spline visualization in pixels in the Preview output.

+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineSampleThickness-Variant1-Before.jpg" alt="SplineSampleThickness-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineSampleThickness-Variant1-After.jpg" alt="SplineSampleThickness-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineSampleThickness-Variant2-Before.jpg" alt="SplineSampleThickness-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineSampleThickness-Variant2-After.jpg" alt="SplineSampleThickness-Variant2-After">
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

![Node example 1](SplineSampleThickness-Variant1-After1.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineSampleThickness-Demo.gif "Node example 2")

</td>
</tr>
</table>

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
