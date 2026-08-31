---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-sample-thickness.html"
breadcrumb-title: ""
description: Use the Spline Sample Thickness node to sample thickness values along splines for procedural effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Sample Thickness
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Sample Thickness
user-guide-description: ""
user-guide-title: ""
---

# Spline Sample Thickness

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-sample-thickness.resources/spline-sample-thickness-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Modifies the thickness of the input splines by mapping an input Thickness Map onto them.

The effect of the mapped height map can be adjusted by changing its blending mode and the opacity of that effect.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the input splines as a grayscale image. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |
| <b>Thickness Map</b> <i>Grayscale</i> | The input grayscale image used to change the input spline’s thickness. |

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
| <b>Sampling Mode</b> <i>Integer</i> | The method of mapping the values in the Thickness Map to the splines:<br>- <i>Texture space</i>: The values are applied to the splines where they would be if placed in a texture using the texture’s UV coordinates. This effectively applies the value to the splines ‘in place’;<br>- <i>Horizontal along spline</i>: The values are applied to the encoded splines’ coordinates directly (see Spline Coords input), where each row is applied to a different spline from top to bottom;<br>- <i>Hor. along spline (rand. offset X)</i>: The values are applied to the encoded splines’ coordinates directly (see Spline Coords input), with a random horizontal offset in the Scale map for each spline (I.e., each row in Spline Coords);<br>- <i>Hor. along spline (rand. offset Y)</i>: The values are applied to the encoded splines’ coordinates directly (see Spline Coords input), with a random vertical offset in the Scale map for each spline (I.e., each row in Spline Coords). |
| <b>Opacity</b> <i>Float</i> | A multiplier for the intensity of the Thickness Map input’s contribution to the spline’s thickness. |
| <b>Blending Mode</b> <i>Integer</i> | The method of blending the Thickness Map’s data with the input spline’s <span id="_Hlk135820484"></span>thickness:<br>- <i>Copy</i>: Override the spline’s thickness with the Height Map values;<br>- <i>Add</i>: Add the Thickness Map values to the spline’s thickness;<br>- <i>Subtract</i>: Subtract the Thickness Map values to the spline’s thickness;<br>- <i>Multiply</i>: Multiply the Thickness Map values against the spline’s thickness. |
| <b>Preview</b> |  |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output.<br>A higher value results in a smoother line. |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Show Thickness Envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline’s thickness. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness of the spline visualization in pixels in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-sample-thickness.resources/spline-sample-thickness-02.jpg" alt="SplineSampleThickness-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-sample-thickness.resources/spline-sample-thickness-03.jpg" alt="SplineSampleThickness-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-sample-thickness.resources/spline-sample-thickness-04.jpg" alt="SplineSampleThickness-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-sample-thickness.resources/spline-sample-thickness-05.jpg" alt="SplineSampleThickness-Variant2-After">
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

![Node example 1](spline-sample-thickness.resources/spline-sample-thickness-06.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-sample-thickness.resources/spline-sample-thickness-07.gif "Node example 2")

</td>
</tr>
</table>
