---
title: "Spline Bridge (List)"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Bridge (List)"
---

# Spline Bridge (List)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-bridge-list-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates splines traversing all splines in the input list, along these splines.

The generated splines can be Linear (straight) or Quadratic Bezier (curved).

</td>
</tr>
</table>

>[!TIP]
>
> The generated splines go from the first spline in the list to the last and traverse the intermediary splines by strictly following the order of these splines in the list.
> 
> Therefore, you should be mindful about the order in which you append splines together beforehand.

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

<b>Bridge Spline Amount</b> *Integer*The number of splines generated across the input splines.

<b>Bridge Splines Type</b> *Integer*The type of spline that is generated:  
* Linear: a sharp spline connecting intermediary splines with straight trajectories from Start to End;  
* Quadratic Bezier: a curved spline connecting intermediary splines with smooth trajectories from Start to End.  
Note: At least 3 input splines are requires to compute a Quadratic Bezier spline.

<b>Input Splines are Closed</b> *Boolean*Controls whether the first and last points of input splines should be processed as a single point. This prevent duplicating the first and last traversing splines.

<b>Flip Direction</b> *Boolean*Inverts the direction of the spline.

<b>Close Bridge Spline</b> *Boolean*Extends the traversing splines to connect back to the first spline in the input list.

<b>First Bridge Spline Offset</b>*Float2*Applies an offset to the start of all traversed splines. The value is the normalized length of the input splines.  
Generated splines that meet the start or end of the traversed splines are left there.

<b>Last Bridge Spline Offset</b>*Float2*  
Applies an offset to the end of all traversed splines. The value is the normalized length of the input splines.  
Generated splines that meet the start or end of the traversed splines are left there.

<b>Random Offset Range</b> *Integer*The maximum distance used for the random offset applied on splines.  
*- Parent spline:* The full length of the parent splines is used. May cause overlaps.  
*- Interval:* The interval between bridge splines is used. This mitigates overlaps. This distance decreases as the amount of bridge splines increases.

<b>Start Random Offset</b> *Float*A multiplier for the random offset applied on the start position of bridge splines, where the maximum distance is specified by the <b>Random offset range</b> parameter.

<b>End Random Offset</b> *Float*A multiplier for the random offset applied on the end position of bridge splines, where the maximum distance is specified by the <b>Random offset range</b> parameter.

<b>Global Random Offset</b> *Float*A multiplier for the *equal amount* of random offset applied on the *both* the start and end position of bridge splines, where the maximum distance is specified by the <b>Random offset range</b> parameter.

<b>Uniform Distribution</b> *Boolean*When True, the points of the generated splines are evenly spaced from start to end.

+++Thickness
<b>Thickness Mode</b> *Integer*The method of acquiring the thickness value for the bridge splines.  
*- Inherit from parent splines:* The thickness of the parent splines at the start and end positions of the bridge splines is used  
*- Override:* The arbitrary value you specify in the <b>Thickness</b> parameter is used

<b>Thickness</b> *Float*The absolute thickness value applied to the bridge splines.

<b>Thickness Random</b> *Float*A random multiplier for the thickness of the bridge splines, where the initial thickness that this multiplier is applied to is specified by the <b>Thickness mode</b> parameter.

+++

+++Height
<b>Height Mode</b> *Integer*The method of acquiring the height value for the bridge splines.  
*- Inherit from parent splines:* The height of the parent splines at the start and end positions of the bridge splines is used  
*- Override:* The arbitrary value you specify in the <b>Height</b> parameter is used

<b>Height Offset</b> *Float*The amount of offset applied to the height inherited from the parent splines, before that height is applied to the bridge splines.

<b>Height</b> *Float*The absolute height value applied to the bridge splines.

<b>Height Random</b> *Float*A random amount of adjustment to the height of the bridge splines, where that adjustment depends on the selected <b>Height mode</b> parameter:  
*- Inherit from parent splines:* The value is a multiplier for the inherited height.  
*- Override:* The value is an offset added to the height.

+++

<b>Non-Square Correction</b>*Boolean*

Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.  
This also impacts uniform distribution.

+++Preview
<b>Show Direction Helper</b> *Boolean*Displays a dot at the start of the spline and an arrowhead at its end in the Preview output.

<b>Show Thickness Envelope</b> *Boolean*  
Displays additional lines at the edges of the spline’s thickness.

<b>Segments Amount</b> *Integer*Adjusts the number of segments used to draw the spline visualization in the Preview output.  
A higher value results in a smoother line.

<b>Thickness (px)</b> *Float*Adjusts the thickness of the spline visualization in pixels in the Preview output.

<b>Background Preview Intensity</b> *Float*The intensity of the Preview visualization.

+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineBridge-List_Variant1_Before.jpg" alt="SplineBridge-List_Variant1_Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineBridge-List_Variant1_After.jpg" alt="SplineBridge-List_Variant1_After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineBridge-List_Demo.gif "Node example 2")

</td>
</tr>
</table>

![Node in graph](SplineBridge-List_Graph.jpg "Node in graph")
