---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-poly-quadratic.html"
breadcrumb-title: ""
description: Use the Spline Poly Quadratic node to create complex quadratic splines with multiple control points.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Poly Quadratic)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Spline (Poly Quadratic)
user-guide-description: ""
user-guide-title: ""
---


# Spline (Poly Quadratic)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-poly-quadratic-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a spline along several points. The amount and locations of these points may be arbitrary or gathered from a [Point List](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/point-list/point-list.md) node.

</td>
</tr>
</table>

The trajectory of the spline can be smoothed away from its intermediary points, in that each intermediary point is the meeting point of the ‘out’ and ‘in’ tangents of its neighbours.

## Input connectors

<b>Preview</b> *Grayscale*The preview of the input splines as a grayscale image.

<b>Spline Coords</b> *Color*The coordinates of the input splines’ points encoded in the RGBA channels of a color image:  
<b>    R</b> - X position  
<b>    G</b> - Y position  
<b>    B</b> - Height  
<b>    A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*Additional data of the input splines encoded in the RGBA channels of a color image.  
<b>    R</b> - Tangents X  
<b>    G</b> - Tangents Y  
<b>    B</b> - Unused  
<b>    A</b> - Unused

<b>Spline Amount</b> *Integer*The number of input splines.

<b>Points Preview</b>*Grayscale*The preview of the points as a grayscale image.

<b>Input Point List</b> *Color* (available when ‘Use Input Point List’ is True)  
A list of points encoded in the RGBA channels of a color image:  
    <b>R</b> - X position  
    <b>G</b> - Y position  
    <b>B</b> - Height  
    <b>A</b> - Packed data:  
        * Integer part: Smoothness;  
        * Fractional part: Thickness.

<b>Point Number</b> *Integer* (available when ‘Use Input Point List’ is True)  
The number of points.

>[!IMPORTANT]
>
> The <b>Point List</b> and <b>Point Number</b> connectors are *not compatible* with <b>Spline Coord</b>, <b>Spline Data</b> and <b>Spline Amount</b> connectors, for they rely on different data.

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

<b>Points Amount</b> *Integer*The arbitrary number of points used to build the spline.

<b>Input Spline Connection Mode</b> *Integer*The method used to connect the input Splines:  
*- Auto:* The end of the last input spline is connected to the start of the generated spline, and the end to the generated spline is connected to the start of the first input spline;  
*- Manual:* You can specify which of the input splines should be connected to the extremities of the generated spline, and where on the input splines these connections should land.

<b>Close Spline</b> *Boolean*Controls whether the end point of the spline should be connected to its start point.  
The smoothing applied to the spline at the start and end points is specified by the Smoothness values of those points.

<b>Flip Direction</b> *Boolean*  
Inverts the direction of the spline.

<b>Use Input Point List</b> *Boolean*Use the list of points supplied to the Input Point List and Point Number input connectors instead of an arbitrary list of points.  
The list of points can be supplied by a [Point List](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/point-list/point-list.md) node.

<b>Connect Start to Input Spline</b> *Boolean*When True, the start of the generated spline is connected to the last point of the last spline in the input splines.

<b>Start Connection Spline Index</b> *Integer* (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect Start to Input Spline’ is set to ‘True’)The index of the input spline which should be connected to the start of the generated spline.

<b>Start Connection Position</b> *Float* (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect Start to Input Spline’ is set to ‘True’)The position on the selected input spline where the connection to the start of the generated spline should land.  
This value is the normalized length of the selected input spline.

<b>Connect End to Input Spline</b> *Boolean*When True, the end of the generated spline is connected to the first point of the first spline in the input splines.

<b>End Connection Spline Index</b> *Integer* (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect End to Input Spline’ is set to ‘True’)The index of the input spline which should be connected to the end of the generated spline.

<b>End Connection Position</b> *Float* (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect End to Input Spline’ is set to ‘True’)The position on the selected input spline where the connection to the end the generated spline should land.  
This value is the normalized length of the selected input spline.

<b>Uniform Distribution</b> *Boolean*  
When True, the points of the spline are evenly spaced from start to end.

<b>Append Input Spline</b> *Boolean*  
Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs.

<b>Non-Square Correction</b>*Boolean*Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.  
This also impacts uniform distribution.

<b>Global Smoothness Adjustment</b> *Float*Applies a uniform offset to the smoothness value of all points.  
The resulting smoothness value is clamped to the &#91;0;1&#93; range.

+++Points Properties
<b>p&#35; Properties</b> *Float3*Sets the properties of the p# point.  
*- Height:* Adjusts the height of the point where a lower value means a lower or deeper location;  
*- Smoothness:* Offsets the start of the smoothing of the spline at p#, where a value of 0 results in a hard trajectory and 1 in an entirely smooth one;  
*- Thickness:* Adjusts the thickness of the spline at p#. Thickness is used by specific Spline nodes.

+++

+++Points Coordinates
<b>p&#35;</b> *Float2*Sets the position of the p# point in texture space.

+++

+++Preview
<b>Show Tangents</b> *Boolean*Displays the tangents of the p1 and p3 points to p2 in the Preview output.

<b>Show Direction Helper</b> *Boolean*Displays a dot at the start of the spline and an arrowhead at its end in the Preview output.

<b>Show Thickness Envelope</b> *Boolean*  
Displays additional lines at the edges of the spline’s thickness.

<b>Show Points Label</b> *Boolean*  
For each point, displays the point's name next to it in the 'Preview' output.

<b>Points Label Size</b> *Float* (Available when 'Show Points Label' is set to 'True')  
The size of the label for each point in texture space, where 0.1 is a tenth of the texture's width.

<b>Show Points</b> *Boolean*  
Displays the control points for the spline.

<b>Points Size</b> *Float* (Available when 'Show Points' is set to 'True')  
The radius of the points in texture space, where 0.1 is a tenth of the texture's width.

<b>Segments Amount</b> *Integer*Adjusts the number of segments used to draw the spline visualization in the Preview output.  
A higher value results in a smoother line.

<b>Thickness (px)</b> *Float*Adjusts the thickness of the spline visualization in pixels in the Preview output.

+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplinePolyQuadratic-Variant1-Before.jpg" alt="SplinePolyQuadratic-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplinePolyQuadratic-Variant1-After.jpg" alt="SplinePolyQuadratic-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplinePolyQuadratic-Demo.gif "Node example 2")

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
