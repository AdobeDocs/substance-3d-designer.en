---
title: "Spline Fill"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Fill"
---

# Spline Fill

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-fill-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Fills the interior of input Splines with solid white. The exterior is filled with solid black.

Open splines are closed with a straight line from start to end. Intersections where the spline crosses itself are resolved by inverting the interior and exterior sides of the lines at those junctions.

</td>
</tr>
</table>

>[!IMPORTANT]
>
> It is not recommended to use this node on splines that are out of the &#91;0 ,1&#93; tile. The filling process is unreliable in that case.

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

<b>Output</b> *Grayscale*  
The result image of filling the input Splines with flat white against a flat black background.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineFill-Variant1-Before.jpg" alt="SplineFill-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineFill-Variant1-After.jpg" alt="SplineFill-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineFill-Demo.gif "Node example 2")

</td>
</tr>
</table>
