---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-circle.html"
breadcrumb-title: ""
description: Use the Spline Circle node to create circular splines for generating round patterns and shapes.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Circle
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Circle
user-guide-description: ""
user-guide-title: ""
---

# Spline Circle

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-circle.resources/spline-circle-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline in the shape of a circle.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the input splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines' points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the output splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the output splines' points encoded in the RGBA channels of a color image.<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the output splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of output splines. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Circle Radius</b> <i>Float</i> | Adjusts the radius of the circle in texture space. |
| <b>Circle Pre-Rotation</b> <i>Float</i> | Applies a rotation to the base circle before Size is applied. |
| <b>Circle Size</b> <i>Float2</i> | Adjusts the horizontal size (X) and vertical size (Y) of the circle. |
| <b>Circle Post-Rotation</b> <i>Float</i> | Applies a rotation to the base circle after Size is applied. |
| <b>Circle Position</b> <i>Float2</i> | Sets the position of the centre of the circle in texture space. |
| <b>Start Thickness</b> <i>Float</i> | Adjusts the thickness of the circle's start point. This thickness is interpolated along the spline to the End Thickness.<br>Note: Thickness is used by specific Spline nodes. |
| <b>End Thickness</b> <i>Float</i> | Adjusts the thickness of the circle's end point. This thickness is interpolated along the spline to the Start Thickness.<br>Note: Thickness is used by specific Spline nodes. |
| <b>Start Height</b> <i>Float</i> | Adjusts the height of the circle's start point where a lower value means a lower or deeper location. This height is interpolated along the spline to the End Height. |
| <b>End Height</b> <i>Float</i> | Adjusts the height of the circle's end point where a lower value means a lower or deeper location. This height is interpolated along the spline from the Start Height. |
| <b>Trim</b> <i>Float2</i> | Offsets the start and end points of the spline along the circle. These values are normalised. |
| <b>Spiral</b> <i>Float</i> | Displaces the start point of the circle from its radius to its centre. The distance from the centre is then interpolated along the spline to the end of the spline. This value is normalised. |
| <b>Spiral Turns</b> <i>Float</i> | Defines the number of turns made by the spiral around its centre. |
| <b>Spiral Power</b> <i>Float</i> | Applies a power curve to the distance from the centre used to draw the spiral. A value higher than one means a greater portion of the spiral remains close to the centre. |
| <b>Flip Direction</b> <i>Boolean</i> | Inverts the direction of the spline. |
| <b>Uniform Distribution</b> <i>Boolean</i> | When True, the points of the spline are evenly spaced from start to end. |
| <b>Append Input Spline</b> <i>Boolean</i> | Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points' positions and thickness to retain the spline shape in non-square resolutions. This also impacts uniform distribution. |
| <b>Preview</b> |  |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Show Thickness Envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline's thickness. |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output. A higher value results in a smoother line. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness in pixels of the spline visualization in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](spline-circle.resources/spline-circle-02.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-circle.resources/spline-circle-03.gif "Node example 2")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Example 3](spline-circle.resources/spline-circle-04.jpg "Example 3")

</td>
<td style="border: 0;" valign="top">

![Example 4](spline-circle.resources/spline-circle-05.jpg "Example 4")

</td>
</tr>
</table>
