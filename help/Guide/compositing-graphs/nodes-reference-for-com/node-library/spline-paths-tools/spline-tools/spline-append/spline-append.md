---
title: "Spline Append | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Append"
---

# Spline Append

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-append-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Splines are packaged as a list. This node appends a list of input splines (set #2) onto an existing list (set #1).

The order of the lists is preserved, meaning appending a list D-E-F onto a list A-B-C results in a list A-B-C-D-E-F.

</td>
</tr>
</table>

>[!TIP]
>
> Be mindful of the order in which you append splines, as this order is taken into account in other nodes, such as [Scatter on Splines](../scatter-on-spline-color/scatter-on-spline-color.md), the [Spline Bridge](../spline-bridge-list/spline-bridge-list.md) nodes, etc.

## Input connectors

<b>Preview &#35;1</b> *Grayscale*The preview of the first set of input splines as a grayscale image.

<b>Spline &#35;1 Coords</b> *Color*The coordinates of the first set of input splines’ points encoded in the RGBA channels of a color image.  
    <b>R</b> - X position  
    <b>G</b> - Y position  
    <b>B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline &#35;1 Data</b> *Color*Additional data of the first set of input splines encoded in the RGBA channels of a color image.  
    <b>R</b> - Tangents X  
    <b>G</b> - Tangents Y  
    <b>B</b> - Unused  
    <b>A</b> - Unused

<b>Spline &#35;1 Amount</b> *Integer*The number of input splines in the first set.

<b>Preview &#35;2</b> *Grayscale*The preview of the second set of input splines as a grayscale image.

<b>Spline &#35;2 Coords</b> *Color*The coordinates of the second set of input splines’ points encoded in the RGBA channels of a color image.  
    <b>R</b> - X position  
    <b>G</b> - Y position  
    <b>B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline &#35;2 Data</b> *Color*Additional data of the second set of input splines encoded in the RGBA channels of a color image.  
    <b>R</b> - Tangents X  
    <b>G</b> - Tangents Y  
    <b>B</b> - Unused  
    <b>A</b> - Unused

<b>Spline &#35;2 Amount</b> *Integer*The number of input splines in the second set.

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

<b>Flip Spline &#35;1 Direction </b>*Boolean*Inverts the direction of the splines in the first set.

<b>Flip Spline &#35;2 Direction </b>*Boolean*Inverts the direction of the splines in the second set.

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

![Node example 1](SplineAppend-Demo.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineAppend-Graph.jpg "Node example 2")

</td>
</tr>
</table>

![Node demo](SplineAppend-Demo2.gif "Node demo")
