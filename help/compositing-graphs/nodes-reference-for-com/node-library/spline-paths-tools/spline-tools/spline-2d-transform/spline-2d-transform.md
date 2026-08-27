---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-2d-transform.html"
breadcrumb-title: ""
description: Use the Spline 2D Transform node to transform splines with translation, rotation, and scaling operations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline 2D Transform
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline 2D Transform
user-guide-description: ""
user-guide-title: ""
---

# Spline 2D Transform

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-2d-transform.resources/spline-2d-transform-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Applies a global transformation to all input splines, including inverting their direction.

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
| <b>Transform Matrix</b> <i>Float4</i> | The transformation matrix applied to the splines.<br>Three modes of editing the matrix parameters are available:<br><br>- <i>Transformation gizmo</i>: tweak the handles of the gizmo displayed in the 2D View when the Spline 2D Transform node is selected;<br>- <i>Rotation/Stretch</i>: Individually control the rotation and stretching of the splines. Note that values are always applied relatively to the current transformation. E.g., applying 50% width twice results in a 25% width;<br>- <i>Matrix values</i>: Click the Edit Matrix Values button to input the raw numerical values of the matrix directly. |
| <b>Offset</b> <i>Float2</i> | Applies a position offset to the splines in X (horizontal) and Y (vertical). |
| <b>Preview</b> |  |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Show Thickness Envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline's thickness. |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output. A higher value results in a smoother line. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness of the spline visualization in pixels in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-2d-transform.resources/Spline2DTransform-Variant1-Before.jpg" alt="Spline2DTransform-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-2d-transform.resources/Spline2DTransform-Variant2-After.jpg" alt="Spline2DTransform-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-2d-transform.resources/Spline2DTransform-Variant1-Before.jpg" alt="Spline2DTransform-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-2d-transform.resources/Spline2DTransform-Variant1-After.jpg" alt="Spline2DTransform-Variant1-After">
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

![Node example 1](spline-2d-transform.resources/Spline2DTransform-Demo1.gif "Node example 1")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
