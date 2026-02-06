---
title: "Spline Flow Mapper"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Flow Mapper"
---

# Spline Flow Mapper

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-flow-mapper-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Draws a flow map where flow vector data is drawn along the input splines.

This lets you use splines to control the direction, trajectory, intensity and thickness of flow, as well as the gradient ramp used to fade the drawn data into the neutral background.

</td>
</tr>
</table>

>[!IMPORTANT]
>
> The result may include undesired artifacts outside of the spline's envelope when using very low thickness values. This is a known issue.

## Input connectors

<b>Spline Coords</b> *Color*The coordinates of the input splines’ points encoded in the RGBA channels of a color image:  
<b>    R</b> - X position  
<b>    G</b> - Y position  
<b>    B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*Additional data of the input splines encoded in the RGBA channels of a color image.  
<b>    R</b> - Tangents X  
<b>    G</b> - Tangents Y  
<b>    B</b> - Unused  
<b>    A</b> - Unused

<b>Spline Amount</b> *Integer*The number of input splines.

<b>Attenuation Profile Curve</b> *Grayscale*The image describing a curve using the values of its first row of pixels.  
When the Attenuation Profile parameter is set to Input Profile Curve, this input is used to control the gradient ramp for the attenuation of the flow vector data drawn along the spline.  
You may use a [Curve](../../../../atomic-nodes/curve/curve.md) node to author the curve.

## Output connectors

<b>Output</b> *Color*The output flow map encoded in a color image.

## Parameters

<b>Segments Amount</b> *Integer*Splines are simplified into segments before vector flow data traverses them.  
A higher amount of segments results in a smoother flow mapping along curves.

<b>Mode</b> *Integer*The method of selecting the splines along which vector flow data should be drawn:  
*- Draw Spline List*: All the splines in the input list are used;  
*- Draw Single Spline*: Only the spline with the specified index is used;  
*- Draw Spline Range*: Only the splines which index is included in the specified range are used.

<b>Draw Spline Index</b> *Integer* (Available when ‘Mode’ is set to ‘Draw Single Spline’)The index of the spline along which vector flow data should be drawn.

<b>Draw Spline Range</b> *Integer2* (Available when ‘Mode’ is set to ‘Draw Spline Range’)The range of indexes for the splines along which vector flow data should be drawn.

<b>Thickness Mode</b> *Integer*The method of setting the thickness of the drawn vector flow data  
*- Manual*: Set the thickness explicitly with an arbitrary value;  
*- From Spline*: Use the thickness of the spline.

<b>Thickness</b> *Float* (Available when ‘Thickness Mode’ is set to ‘Manual’)The arbitrary value for the thickness of the vector flow data drawn along the splines.<b></b>

<b>Thickness Multiplier</b> *Float* (Available when ‘Thickness Mode’ is set to ‘From Spline’)A global multiplier for the thickness of the vector flow data drawn along the splines, when that thickness it driven by that of the splines.

<b>Direction</b> *Integer*The direction of the vector flow in relation to the spline.  
*- Tangent*: Use the spline’s tangent vector;  
*- Normal*: Use the spline’s normal vector;  
*- Normal Mirrored*: Use the mirrored version of the spline’s normal vector.

<b>Flip Direction</b> *Boolean*Inverts the direction of the splines, which also impacts the direction of the flow vector.

<b>Attenuation Profile</b> *Integer*The gradient ramp used to draw the attenuation of the flow vector data drawn along the spline:  
*- Linear*: Use a linear gradient ramp;  
*- Gaussian*: Use a gaussian gradient ramp  
*- Input Profile Curve*: Use the curve provided to the Attenuation Profile Curve input as a gradient ramp.

<b>Start Attenuation</b> *Boolean*Adds a half-circle at the start of the spline. The half-circle uses the same attenuation as the spline.

<b>End Attenuation</b> *Boolean*Adds a half-circle at the end of the spline. The half-circle uses the same attenuation as the spline.

<b>Spline Height Attenuation</b> *Float*The intensity of the flow vector data drawn along the spline is multiplied against the spline’s height, where the drawn data fades to the background’s neutral (0.5, 0.5, 0) color as the height gets closer to 0.

<b>Non-Square Correction</b>*Boolean*Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.  
This also impacts uniform distribution.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineFlowMapper-Variant1-Before.jpg" alt="SplineFlowMapper-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineFlowMapper-Variant1-After.jpg" alt="SplineFlowMapper-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineFlowMapper-Demo.gif "Node example 2")

</td>
</tr>
</table>
