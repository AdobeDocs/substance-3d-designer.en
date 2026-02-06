---
title: "Spline Circle"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Circle"
---

# Spline Circle

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-circle-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline in the shape of a circle.

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

<b>Circle Radius</b> *Float*  
Adjusts the radius of the circle in texture space.

<b>Circle Pre-Rotation</b> *Float*  
Applies a rotation to the base circle before Size is applied.

<b>Circle Size</b> *Float2*  
Adjusts the horizontal size (X) and vertical size (Y) of the circle.

<b>Circle Post-Rotation</b> *Float*  
Applies a rotation to the base circle after Size is applied.

<b>Circle Position</b> *Float2*  
Sets the position of the centre of the circle in texture space.

<b>Start Thickness</b> *Float*Adjusts the thickness of the circle’s start point.  
This thickness is interpolated along the spline to the End Thickness.  
Note: Thickness is used by specific Spline nodes.

<b>End Thickness</b> *Float*Adjusts the thickness of the circle’s end point.  
This thickness is interpolated along the spline to the Start Thickness.  
Note: Thickness is used by specific Spline nodes.

<b>Start Height</b> *Float*Adjusts the height of the circle’s start point where a lower value means a lower or deeper location.  
This height is interpolated along the spline to the End Height.

<b>End Height</b> *Float*Adjusts the height of the circle’s end point where a lower value means a lower or deeper location.  
This height is interpolated along the spline from the Start Height.

<b>Trim</b> *Float2*Offsets the start and end points of the spline along the circle.  
These values are normalised.

<b>Spiral</b> *Float*Displaces the start point of the circle from its radius to its centre.  
The distance from the centre is then interpolated along the spline to the end of the spline.  
This value is normalised.

<b>Spiral Turns</b> *Float*Defines the number of turns made by the spiral around its centre.

<b>Spiral Power</b> *Float*Applies a power curve to the distance from the centre used to draw the spiral.  
A value higher than one means a greater portion of the spiral remains close to the centre.

<b>Flip Direction</b> *Boolean*  
Inverts the direction of the spline.

<b>Uniform Distribution</b> *Boolean*  
When True, the points of the spline are evenly spaced from start to end.

<b>Append Input Spline</b> *Boolean*  
Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs.

<b>Non-Square Correction</b>*Boolean*Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.  
This also impacts uniform distribution.

+++Preview
<b>Show Direction Helper</b> *Boolean*Displays a dot at the start of the spline and an arrowhead at its end in the Preview output.

<b>Show Thickness Envelope</b> *Boolean*  
Displays additional lines at the edges of the spline’s thickness.

<b>Segments Amount</b> *Integer*Adjusts the number of segments used to draw the spline visualization in the Preview output.  
A higher value results in a smoother line.

<b>Thickness (px)</b> *Float*Adjusts the thickness in pixels of the spline visualization in the Preview output.

+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](SplineCircle-Variant1.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineCircle-Demo.gif "Node example 2")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Example 3](SplineCircle-Variant2.jpg "Example 3")

</td>
<td style="border: 0;" valign="top">

![Example 4](SplineCircle-Variant3.jpg "Example 4")

</td>
</tr>
</table>
