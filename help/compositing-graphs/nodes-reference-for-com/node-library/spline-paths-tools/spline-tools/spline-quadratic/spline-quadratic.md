---
title: "Spline (Quadratic)"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Quadratic)"
---

# Spline (Quadratic)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Spline (Quadratic): icon](spline-quadratic-icon.png "Spline (Quadratic): icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline between two points <b>p1</b> and <b>p3</b> at arbitrary locations.

The trajectory of the spline is controlled by the ‘out’ tangent of <b>p1</b> and the ‘in’ tangent of <b>p3</b>, *both* controlled by a single point <b>p3</b>.

The span of the arc formed by the spline is *adjustable*, so that some of its trajectory from its extremities can remain straight.

</td>
</tr>
</table>

## Input connectors

|  |  |
| --- | --- |
| <b>Preview</b> *Grayscale* | The preview of the input splines as a grayscale image. |
| <b>Spline Coords</b> *Color* | The coordinates of the input splines’ points encoded in the RGBA channels of a color image: <b>R</b> - X position <b>G</b> - Y position <b>B</b> - Height <b>A</b> - Packed data:          - Sign: Spline is closed (negative) or open (positive);          - Absolute value: Thickness + 1. |
| <b>Spline Data</b> *Color* | Additional data of the input splines encoded in the RGBA channels of a color image:  <b>R</b> - Tangents X  <b>G</b> - Tangents Y  <b>B</b> - Tangents Z  <b>A</b> - Unused |
| <b>Spline Amount</b> *Integer* | The number of input splines. |

## Output connectors

|  |  |
| --- | --- |
| <b>Preview</b> *Grayscale* | The preview of the output splines as a grayscale image. |
| <b>Spline Coords</b> *Color* | The coordinates of the output splines’ points encoded in the RGBA channels of a color image:  <b>R</b> - X position  <b>G</b> - Y position  <b>B</b> - Height  <b>A</b> - Packed data:          - Sign: Spline is closed (negative) or open (positive);          - Absolute value: Thickness + 1. |
| <b>Spline Data</b> *Color* | Additional data of the output splines encoded in the RGBA channels of a color image:  <b>R</b> - Tangents X  <b>G</b> - Tangents Y <b>B</b> - Tangents Z  <b>A</b> - Unused |
| <b>Spline Amount</b> *Integer* | The number of output splines. |

## Parameters

|  |  |
| --- | --- |
| <b>Flip direction</b> *Boolean* | Inverts the direction of the spline. |
| <b>Uniform distribution</b> *Boolean* | When *True*, the points of the spline are evenly spaced from start to end.. |
| <b>Append input spline</b> *Boolean* | Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs.. |
| <b>Non-square correction</b> *Boolean* | Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions. This also impacts uniform distribution. |
| <b>Smoothness</b> *Float* | Adjusts the *span of the arc* formed by the spline, where 1 means the full length of the spline is arched and 0 means the spline is entirely straight. The arc progresses from point <b>p3</b> along the spline up to its extremities. |

+++Height


+++

+++Thickness


+++

+++Points coordinates


+++

+++Preview


+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Spline (Quadratic): Example 1](spline-quadratic-example-1.png "Spline (Quadratic): Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Spline (Quadratic): Example 2](spline-quadratic-example-2.png "Spline (Quadratic): Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Spline (Quadratic): Demo](spline-quadratic-demo.gif "Spline (Quadratic): Demo"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
