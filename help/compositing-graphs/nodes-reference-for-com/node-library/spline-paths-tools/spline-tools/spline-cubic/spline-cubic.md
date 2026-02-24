---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-cubic.html"
breadcrumb-title: ""
description: Use the Spline Cubic node to create smooth cubic splines with four control points for curved paths.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Cubic)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline (Cubic)
user-guide-description: ""
user-guide-title: ""
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
<b>Start Height</b> *Float*Adjusts the height of the p1 point where a lower value means a lower or deeper location.  
This impacts the height of the spline at p1.

<b>End Height</b> *Float*Adjusts the height of the p2 point where a lower value means a lower or deeper location.  
This impacts the thickness of the spline at p2.

<b>Auto Tangent Height</b> *Boolean*Automatically sets the height of the spline tangents to interpolate linearly from the Start Height to the End Height.

<b>p1 Tangent Height</b> *Float* (available when ‘Auto Tangent Height’ is True)  
Adjusts the height of the p1 point ‘out’ tangent where a lower value means a lower or deeper location.  
This impacts the height along the spline as it draws away from p1.

<b>p2 Tangent Height</b> *Float* (available when ‘Auto Tangent Height’ is True)  
Adjusts the height of the p2 point ‘in’ tangent where a lower value means a lower or deeper location.  
This impacts the height along the spline as it draws away from p2.

+++

+++Thickness
<b>Start Thickness</b> *Float*Adjusts the thickness of the p1 point.  
This impacts the thickness of the spline at p1.  
Note: Thickness is used by specific Spline nodes.

<b>End Thickness</b> *Float*Adjusts the thickness of the p2 point.  
This impacts the thickness of the spline at p2.  
Note: Thickness is used by specific Spline nodes.

<b>Auto Tangent Thickness</b> *Boolean*Automatically sets the thickness of the spline tangents to interpolate linearly from the Start Thickness to the End Thickness.  
Note: Thickness is used by specific Spline nodes.

<b>p1 Tangent Thickness</b> *Float* (available when ‘Auto Tangent Thickness’ is True)  
Adjusts the thickness of the p1 point ‘out’ tangent.  
This impacts the thickness along the spline as it draws away from p1.  
Note: Thickness is used by specific Spline nodes.

<b>p2 Tangent Thickness</b> *Float* (available when ‘Auto Tangent Thickness’ is True)  
Adjusts the thickness of the p2 point ‘in’ tangent.  
This impacts the thickness along the spline as it draws away from p2.  
Note: Thickness is used by specific Spline nodes.

+++

+++Points Coordinates
<b>p1</b> *Float2*Sets the position of the p1 point in texture space.

<b>p1 Tangent</b> *Float2*Sets the position of the p1 point ‘out’ tangent handle in texture space.

<b>p2</b> *Float2*Sets the position of the p2 point in texture space.

<b>p2 Tangent</b> *Float2*Sets the position of the p2 point ‘in’ tangent handle in texture space.

+++

+++Preview
<b>Show Tangents</b> *Boolean*Displays the p1 point ‘out’ tangent and p2 point ‘in’ tangent in the Preview output.

<b>Show Direction Helper</b> *Boolean*Displays a dot at the start of the spline and an arrowhead at its end in the Preview output.

<b>Segments Amount</b> *Integer*Adjusts the number of segments used to draw the spline visualization in the Preview output.  
A higher value results in a smoother line.

<b>Thickness (px)</b> *Float*Adjusts the thickness in pixels of the spline visualization in the Preview output.

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
