---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-quadratic.html"
breadcrumb-title: ""
description: Use the Spline Quadratic node to create smooth quadratic splines with three control points.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Quadratic)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline (Quadratic)
user-guide-description: ""
user-guide-title: ""
---

# Spline (Quadratic)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Spline (Quadratic): icon](../../../../../../assets/spline-quadratic-icon.png "Spline (Quadratic): icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline between two points <b>p1</b> and <b>p3</b> at arbitrary locations.

The trajectory of the spline is controlled by the ‘out’ tangent of <b>p1</b> and the ‘in’ tangent of <b>p3</b>, *both* controlled by a single point <b>p3</b>.

The span of the arc formed by the spline is *adjustable*, so that some of its trajectory from its extremities can remain straight.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the input splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image:<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Tangents Z<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the output splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the output splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the output splines encoded in the RGBA channels of a color image:<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Tangents Z<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of output splines. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Flip direction</b> <i>Boolean</i> | Inverts the direction of the spline. |
| <b>Uniform distribution</b> <i>Boolean</i> | When <i>True</i>, the points of the spline are evenly spaced from start to end.. |
| <b>Append input spline</b> <i>Boolean</i> | Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs.. |
| <b>Non-square correction</b> <i>Boolean</i> | Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions. This also impacts uniform distribution. |
| <b>Smoothness</b> <i>Float</i> | Adjusts the <i>span of the arc</i> formed by the spline, where 1 means the full length of the spline is arched and 0 means the spline is entirely straight. The arc progresses from point <b>p3</b> along the spline up to its extremities. |
| <b>Height</b> |  |
| <b>Start height</b> <i>Float</i> | Adjusts the height of the <b>p1</b> point where a lower value means a lower or deeper location.<br>This impacts the height of the spline at <b>p1</b>. |
| <b>End height</b> <i>Float</i> | Adjusts the height of the <b>p3</b> point where a lower value means a lower or deeper location.<br>This impacts the thickness of the spline at <b>p3</b>. |
| <b>Auto tangent height</b> <i>Boolean</i> | Adjusts the height of the <b>p3</b> point where a lower value means a lower or deeper location.<br>This impacts the thickness of the spline at <b>p3</b>. |
| <b>Tangent height</b> <i>Float</i> | Adjusts the height driven by the tangents controlled by the <b>p2</b> point.<br>This impacts the height along the spline as it draws away from <b>p1</b> and goes into <b>p3</b>.<br><i>Note:</i> This parameter is only available when <b>Auto tangent height</b> is set to 'False'. |
| <b>Thickness</b> |  |
| <b>Start thickness</b> <i>Float</i> | Adjusts the thickness of the <b>p1</b> point. This impacts the thickness of the spline at <b>p1</b>.<br><i>Note:</i> Thickness is used by specific Spline nodes. |
| <b>End thickness</b> <i>Float</i> | Adjusts the thickness of the <b>p3</b> point. This impacts the thickness of the spline at <b>p3</b>.<br><i>Note:</i> Thickness is used by specific Spline nodes. |
| <b>Auto tangent thickness</b> <i>Boolean</i> | Automatically sets the thickness of the spline tangents to interpolate linearly from the <b>Start Thickness</b> to the <b>End Thickness</b>.<br><i>Note:</i> Thickness is used by specific Spline nodes. |
| <b>Tangent thickness</b> <i>Float</i> | Adjusts the thickness driven by the tangents controlled by the <b>p2</b> point.<br>This impacts the thickness along the spline as it draws away from <b>p1</b> and goes into <b>p3</b>.<br><i>Note:</i> Thickness is used by specific Spline nodes.<br><i>Note 2:</i> This parameter is only available when <b>Auto tangent thickness</b> is set to 'False'. |
| <b>Points coordinates</b> |  |
| <b>p1</b> <i>Float2</i> | Sets the position of the <b>p1</b> point in texture space. |
| <b>p2</b> <i>Float2</i> | Sets the position of the <b>p2</b> point in texture space.<br>The <b>p2</b> point controls the <i>tangents</i> of both <b>p1</b> and <b>p3</b> points. |
| <b>p3</b> <i>Float2</i> | Sets the position of the <b>p3</b> point in texture space. |
| <b>Preview</b> |  |
| <b>Show tangents</b> <i>Boolean</i> | Displays the <b>p1</b> point ‘out’ tangent and <b>p3</b> point ‘in’ tangent in the <b>Preview</b> output. Inverts the direction of the spline. |
| <b>Show direction helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the <b>Preview</b> output. |
| <b>Show thickness envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline’s thickness. |
| <b>Segments amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the <b>Preview</b> output.<br>A higher value results in a smoother line. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness in pixels of the spline visualization in the <b>Preview</b> output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Spline (Quadratic): Example 1](../../../../../../assets/spline-quadratic-example-1.png "Spline (Quadratic): Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Spline (Quadratic): Example 2](../../../../../../assets/spline-quadratic-example-2.png "Spline (Quadratic): Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Spline (Quadratic): Demo](../../../../../../assets/spline-quadratic-demo.gif "Spline (Quadratic): Demo"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
