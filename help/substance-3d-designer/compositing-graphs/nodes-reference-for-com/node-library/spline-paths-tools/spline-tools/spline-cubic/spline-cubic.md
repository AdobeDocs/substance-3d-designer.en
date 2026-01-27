---
title: "Spline (Cubic) | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Cubic)"
---

# Spline (Cubic)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-cubic-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline between two points <b>p1 </b>and <b>p2</b> at arbitrary locations.

The trajectory of the spline is controlled by the ‘out’ tangent of <b>p1</b> and the ‘in’ tangent of <b>p2</b>.

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

<b>Flip Direction</b> *Boolean*  
Inverts the direction of the spline.

<b>Append Input Spline</b> *Boolean*  
Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs.

<b>Non-Square Correction</b>*Boolean*Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.  
This also impacts uniform distribution.

+++Height


Start HeightFloatAdjusts the height of the p1 point where a lower value means a lower or deeper location.This impacts the height of the spline at p1.





End HeightFloatAdjusts the height of the p2 point where a lower value means a lower or deeper location.This impacts the thickness of the spline at p2.





Auto Tangent HeightBooleanAutomatically sets the height of the spline tangents to interpolate linearly from the Start Height to the End Height.





p1 Tangent HeightFloat(available when ‘Auto Tangent Height’ is True)Adjusts the height of the p1 point ‘out’ tangent where a lower value means a lower or deeper location.This impacts the height along the spline as it draws away from p1.





p2 Tangent HeightFloat(available when ‘Auto Tangent Height’ is True)Adjusts the height of the p2 point ‘in’ tangent where a lower value means a lower or deeper location.This impacts the height along the spline as it draws away from p2.



+++

+++Thickness


Start ThicknessFloatAdjusts the thickness of the p1 point.This impacts the thickness of the spline at p1.Note: Thickness is used by specific Spline nodes.





End ThicknessFloatAdjusts the thickness of the p2 point.This impacts the thickness of the spline at p2.Note: Thickness is used by specific Spline nodes.





Auto Tangent ThicknessBooleanAutomatically sets the thickness of the spline tangents to interpolate linearly from the Start Thickness to the End Thickness.Note: Thickness is used by specific Spline nodes.





p1 Tangent ThicknessFloat(available when ‘Auto Tangent Thickness’ is True)Adjusts the thickness of the p1 point ‘out’ tangent.This impacts the thickness along the spline as it draws away from p1.Note: Thickness is used by specific Spline nodes.





p2 Tangent ThicknessFloat(available when ‘Auto Tangent Thickness’ is True)Adjusts the thickness of the p2 point ‘in’ tangent.This impacts the thickness along the spline as it draws away from p2.Note: Thickness is used by specific Spline nodes.



+++

+++Points Coordinates


p1Float2Sets the position of the p1 point in texture space.





p1 TangentFloat2Sets the position of the p1 point ‘out’ tangent handle in texture space.





p2Float2Sets the position of the p2 point in texture space.





p2 TangentFloat2Sets the position of the p2 point ‘in’ tangent handle in texture space.



+++

+++Preview


Show TangentsBooleanDisplays the p1 point ‘out’ tangent and p2 point ‘in’ tangent in the Preview output.





Show Direction HelperBooleanDisplays a dot at the start of the spline and an arrowhead at its end in the Preview output.





Segments AmountIntegerAdjusts the number of segments used to draw the spline visualization in the Preview output.A higher value results in a smoother line.





Thickness (px)FloatAdjusts the thickness in pixels of the spline visualization in the Preview output.



+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](SplineCubic-Variant1.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineCubic-Variant2.jpg "Node example 2")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 3](SplineCubic-Demo.gif "Node example 3")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
