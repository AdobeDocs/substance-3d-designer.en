---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-merge-list.html"
breadcrumb-title: ""
description: Use the Spline Merge List node to merge multiple splines into a single spline list for combined operations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Merge List
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Spline Merge List
user-guide-description: ""
user-guide-title: ""
---


# Spline Merge List

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-merge-list-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Merges all splines in the input list into a single spline.

</td>
</tr>
</table>

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

## Output connectors

<b>Preview</b> *Grayscale*The preview of the merged splines as a grayscale image.

<b>Spline Coords</b> *Color*The coordinates of the merged splines’ points encoded in the RGBA channels of a color image.  
    <b>R</b> - X position  
    <b>G</b> - Y position  
    <b>B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*Additional data of the merged splines encoded in the RGBA channels of a color image.  
    <b>R</b> - Tangents X  
    <b>G</b> - Tangents Y  
    <b>B</b> - Unused  
    <b>A</b> - Unused

<b>Spline Amount</b> *Integer*The number of merged splines.

## Parameters

<b>Closed Spline Distance Threshold</b> *Float*The distance in texture space below which two extremities of a same spline are processed as a single point closing that spline.  
This prevents overlaps when scattering shapes or mapping images along the splines.

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
      <img src="SplineMergeList-Variant2-Before.jpg" alt="SplineMergeList-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineMergeList-Variant2-After.jpg" alt="SplineMergeList-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineMergeList-Variant1-Before.jpg" alt="SplineMergeList-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineMergeList-Variant1-After.jpg" alt="SplineMergeList-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

![Node demo](SplineMergeList-Demo.gif "Node demo")

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
