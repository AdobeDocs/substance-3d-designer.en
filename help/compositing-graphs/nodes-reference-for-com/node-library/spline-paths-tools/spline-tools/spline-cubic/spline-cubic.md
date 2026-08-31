---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-cubic.html"
breadcrumb-title: ""
description: Use the Spline Cubic node to create smooth cubic splines with four control points for curved paths.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline (Cubic)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline (Cubic)
user-guide-description: ""
user-guide-title: ""
---

# Spline (Cubic)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-cubic.resources/spline-cubic-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline between two points <b>p1 </b>and <b>p2</b> at arbitrary locations.

The trajectory of the spline is controlled by the ‘out’ tangent of <b>p1</b> and the ‘in’ tangent of <b>p2</b>.

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
| <b>Flip Direction</b> <i>Boolean</i> | Inverts the direction of the spline. |
| <b>Append Input Spline</b> <i>Boolean</i> | Adds the generated spline to the end of the list of splines connected to the <b>Spline</b> inputs. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points' positions and thickness to retain the spline shape in non-square resolutions. This also impacts uniform distribution. |
| <b>Height</b> |  |
| <b>Start Height</b> <i>Float</i> | Adjusts the height of the p1 point where a lower value means a lower or deeper location. This impacts the height of the spline at p1. |
| <b>End Height</b> <i>Float</i> | Adjusts the height of the p2 point where a lower value means a lower or deeper location. This impacts the thickness of the spline at p2. |
| <b>Auto Tangent Height</b> <i>Boolean</i> | Automatically sets the height of the spline tangents to interpolate linearly from the Start Height to the End Height. |
| <b>p1 Tangent Height</b> <i>Float</i> (available when 'Auto Tangent Height' is True) | Adjusts the height of the p1 point 'out' tangent where a lower value means a lower or deeper location. This impacts the height along the spline as it draws away from p1. |
| <b>p2 Tangent Height</b> <i>Float</i> (available when 'Auto Tangent Height' is True) | Adjusts the height of the p2 point 'in' tangent where a lower value means a lower or deeper location. This impacts the height along the spline as it draws away from p2. |
| <b>Thickness</b> |  |
| <b>Start Thickness</b> <i>Float</i> | Adjusts the thickness of the p1 point. This impacts the thickness of the spline at p1.<br>Note: Thickness is used by specific Spline nodes. |
| <b>End Thickness</b> <i>Float</i> | Adjusts the thickness of the p2 point. This impacts the thickness of the spline at p2.<br>Note: Thickness is used by specific Spline nodes. |
| <b>Auto Tangent Thickness</b> <i>Boolean</i> | Automatically sets the thickness of the spline tangents to interpolate linearly from the Start Thickness to the End Thickness.<br>Note: Thickness is used by specific Spline nodes. |
| <b>p1 Tangent Thickness</b> <i>Float</i> (available when 'Auto Tangent Thickness' is True) | Adjusts the thickness of the p1 point 'out' tangent. This impacts the thickness along the spline as it draws away from p1.<br>Note: Thickness is used by specific Spline nodes. |
| <b>p2 Tangent Thickness</b> <i>Float</i> (available when 'Auto Tangent Thickness' is True) | Adjusts the thickness of the p2 point 'in' tangent. This impacts the thickness along the spline as it draws away from p2.<br>Note: Thickness is used by specific Spline nodes. |
| <b>Points Coordinates</b> |  |
| <b>p1</b> <i>Float2</i> | Sets the position of the p1 point in texture space. |
| <b>p1 Tangent</b> <i>Float2</i> | Sets the position of the p1 point 'out' tangent handle in texture space. |
| <b>p2</b> <i>Float2</i> | Sets the position of the p2 point in texture space. |
| <b>p2 Tangent</b> <i>Float2</i> | Sets the position of the p2 point 'in' tangent handle in texture space. |
| <b>Preview</b> |  |
| <b>Show Tangents</b> <i>Boolean</i> | Displays the p1 point 'out' tangent and p2 point 'in' tangent in the Preview output. |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output. A higher value results in a smoother line. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness in pixels of the spline visualization in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](spline-cubic.resources/spline-cubic-02.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-cubic.resources/spline-cubic-03.jpg "Node example 2")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 3](spline-cubic.resources/spline-cubic-04.gif "Node example 3")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
