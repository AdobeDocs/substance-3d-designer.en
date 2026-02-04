---
title: "Spline Select"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Select"
---

# Spline Select

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-select-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Selects splines in the input list according to the specified criteria, and outputs a new list including the selected splines only.

Selected splines can also be trimmed.

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

<b>Selection Mode</b> *Integer*The method of selecting the splines in the input list:  
*- First*: Selects the first spline in the list;  
*- Last*: Selects the last spline in the list;  
*- Index*: Selects the spline with specified index;  
*- Range*: Selects the splines which indexes are included in the specified range.

<b>Spline Index</b> *Integer* (Available when ‘Selection Mode’ is set to ‘Index’)The index of the spline which should be selected.

<b>Range Start</b> *Integer* (Available when ‘Selection Mode’ is set to ‘Range’)The lowest index in the range of selected splines.

<b>Range End</b> *Integer* (Available when ‘Selection Mode’ is set to ‘Range’)The highest index in the range of selected splines.<b></b>

<b>Start</b> *Float*Offsets the start of the portion of the spline which should be selected. This effectively trims the spline.  
The value represents the normalized length of the spline.

<b>End</b> *Float*Offsets the end of the portion of the spline which should be selected. This effectively trims the spline.  
The value represents the normalized length of the spline.

+++Preview


Segments AmountIntegerAdjusts the number of segments used to draw the spline visualization in the Preview output.A higher value results in a smoother line.





Show Direction HelperBooleanDisplays a dot at the start of the spline and an arrowhead at its end in the Preview output.





Show Thickness EnvelopeBooleanDisplays additional lines at the edges of the spline’s thickness.





Thickness (px)FloatAdjusts the thickness of the spline visualization in pixels in the Preview output.



+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineSelect-Variant1-Before.jpg" alt="SplineSelect-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineSelect-Variant1-After2.jpg" alt="SplineSelect-Variant1-After2">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineSelect-Variant2-Before.jpg" alt="SplineSelect-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineSelect-Variant2-After.jpg" alt="SplineSelect-Variant2-After">
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

![Node example 1](SplineSelect-Demo.gif "Node example 1")

</td>
<td style="border: 0;" valign="top">



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
