---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-poly-quadratic.html"
breadcrumb-title: ""
description: Use the Spline Poly Quadratic node to create complex quadratic splines with multiple control points.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Poly Quadratic)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline (Poly Quadratic)
user-guide-description: ""
user-guide-title: ""
---

# Spline (Poly Quadratic)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-poly-quadratic.resources/spline-poly-quadratic-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a spline along several points. The amount and locations of these points may be arbitrary or gathered from a [Point List](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/point-list/point-list.md) node.

</td>
</tr>
</table>

The trajectory of the spline can be smoothed away from its intermediary points, in that each intermediary point is the meeting point of the ‘out’ and ‘in’ tangents of its neighbours.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the input splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |
| <b>Points Preview</b> <i>Grayscale</i> | The preview of the points as a grayscale image. |
| <b>Input Point List</b> <i>Color</i> | (available when ‘Use Input Point List’ is True) A list of points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Integer part: Smoothness;<br>&nbsp;&nbsp;- Fractional part: Thickness. |
| <b>Point Number</b> <i>Integer</i> | (available when ‘Use Input Point List’ is True) The number of points. |

>[!IMPORTANT]
>
> The <b>Point List</b> and <b>Point Number</b> connectors are *not compatible* with <b>Spline Coord</b>, <b>Spline Data</b> and <b>Spline Amount</b> connectors, for they rely on different data.

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the output splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the output splines’ points encoded in the RGBA channels of a color image.<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the output splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of output splines. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Points Amount</b> <i>Integer</i> | The arbitrary number of points used to build the spline. |
| <b>Input Spline Connection Mode</b> <i>Integer</i> | The method used to connect the input Splines:<br>- <i>Auto:</i> The end of the last input spline is connected to the start of the generated spline, and the end to the generated spline is connected to the start of the first input spline;<br>- <i>Manual:</i> You can specify which of the input splines should be connected to the extremities of the generated spline, and where on the input splines these connections should land. |
| <b>Close Spline</b> <i>Boolean</i> | Controls whether the end point of the spline should be connected to its start point.<br>The smoothing applied to the spline at the start and end points is specified by the Smoothness values of those points. |
| <b>Flip Direction</b> <i>Boolean</i> | Inverts the direction of the spline. |
| <b>Use Input Point List</b> <i>Boolean</i> | Use the list of points supplied to the Input Point List and Point Number input connectors instead of an arbitrary list of points.<br>The list of points can be supplied by a [Point List](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/point-list/point-list.md) node. |
| <b>Connect Start to Input Spline</b> <i>Boolean</i> | When True, the start of the generated spline is connected to the last point of the last spline in the input splines. |
| <b>Start Connection Spline Index</b> <i>Integer</i> | (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect Start to Input Spline’ is set to ‘True’) The index of the input spline which should be connected to the start of the generated spline. |
| <b>Start Connection Position</b> <i>Float</i> | (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect Start to Input Spline’ is set to ‘True’) The position on the selected input spline where the connection to the start of the generated spline should land.<br>This value is the normalized length of the selected input spline. |
| <b>Connect End to Input Spline</b> <i>Boolean</i> | When True, the end of the generated spline is connected to the first point of the first spline in the input splines. |
| <b>End Connection Spline Index</b> <i>Integer</i> | (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect End to Input Spline’ is set to ‘True’) The index of the input spline which should be connected to the end of the generated spline. |
| <b>End Connection Position</b> <i>Float</i> | (Available when ‘Input Spline Connection Mode’ is set to ‘Manual’ and ‘Connect End to Input Spline’ is set to ‘True’) The position on the selected input spline where the connection to the end the generated spline should land.<br>This value is the normalized length of the selected input spline. |
| <b>Uniform Distribution</b> <i>Boolean</i> | When True, the points of the spline are evenly spaced from start to end. |
| <b>Append Input Spline</b> <i>Boolean</i> | Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.<br>This also impacts uniform distribution. |
| <b>Global Smoothness Adjustment</b> <i>Float</i> | Applies a uniform offset to the smoothness value of all points.<br>The resulting smoothness value is clamped to the &#91;0;1&#93; range. |
| <b>Points Properties</b> |  |
| <b>p&#35; Properties</b> <i>Float3</i> | Sets the properties of the p# point.<br>- <i>Height:</i> Adjusts the height of the point where a lower value means a lower or deeper location;<br>- <i>Smoothness:</i> Offsets the start of the smoothing of the spline at p#, where a value of 0 results in a hard trajectory and 1 in an entirely smooth one;<br>- <i>Thickness:</i> Adjusts the thickness of the spline at p#. Thickness is used by specific Spline nodes. |
| <b>Points Coordinates</b> |  |
| <b>p&#35;</b> <i>Float2</i> | Sets the position of the p# point in texture space. |
| <b>Preview</b> |  |
| <b>Show Tangents</b> <i>Boolean</i> | Displays the tangents of the p1 and p3 points to p2 in the Preview output. |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Show Thickness Envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline’s thickness. |
| <b>Show Points Label</b> <i>Boolean</i> | For each point, displays the point's name next to it in the 'Preview' output. |
| <b>Points Label Size</b> <i>Float</i> | (Available when 'Show Points Label' is set to 'True') The size of the label for each point in texture space, where 0.1 is a tenth of the texture's width. |
| <b>Show Points</b> <i>Boolean</i> | Displays the control points for the spline. |
| <b>Points Size</b> <i>Float</i> | (Available when 'Show Points' is set to 'True') The radius of the points in texture space, where 0.1 is a tenth of the texture's width. |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output.<br>A higher value results in a smoother line. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness of the spline visualization in pixels in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-poly-quadratic.resources/SplinePolyQuadratic-Variant1-Before.jpg" alt="SplinePolyQuadratic-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-poly-quadratic.resources/SplinePolyQuadratic-Variant1-After.jpg" alt="SplinePolyQuadratic-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-poly-quadratic.resources/SplinePolyQuadratic-Demo.gif "Node example 2")

</td>
</tr>
</table>
