---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-render.html"
breadcrumb-title: ""
description: Use the Spline Render node to render splines as textures with customizable width, color, and blending modes.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Render
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Render
user-guide-description: ""
user-guide-title: ""
---

# Spline Render

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](../../../../../../assets/spline-render-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Draws strings of segments along the input <b>Splines</b> over the input <b>Background</b>.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Background</b> <i>Grayscale</i> | The grayscale image over which splines should be drawn. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The result image of drawing the input Splines on top of the Background. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Mode</b> <i>Integer</i> | The method of selecting which splines should be drawn:<br>- <i>Draw Spline List</i>: Draw all splines in the input list;<br>- <i>Draw Single Spline</i>: Draw only the specified spline from the input list;<br>- <i>Draw Spline Range</i>: Draw only the splines in the specified range from the input list. |
| <b>Draw Spline Index</b> <i>Integer</i> | (Available when ‘Mode’ is set to ‘Draw Single Spline’) The index of the spline that should be drawn. |
| <b>Draw Spline Range</b> <i>Integer2</i> | (Available when ‘Mode’ is set to ‘Draw Spline Range’) The range of indexes for the splines that should be drawn. |
| <b>Show Direction Helper</b> <i>Boolean</i> | For each spline, draws a dot at the start of the spline and an arrowhead at its end. |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments drawn along the splines.<br>A higher value results in smoother lines. |
| <b>Envelope Spline Amount</b> <i>Integer</i> | The number of duplicate segments that should be drawn along each spline’s thickness. |
| <b>Start</b> <i>Float</i> | Offsets the start of the portion of the spline which should be drawn.<br>The value represents the normalized length of the spline. |
| <b>End</b> <i>Float</i> | Offsets the end of the portion of the spline which should be drawn.<br>The value represents the normalized length of the spline. |
| <b>Thickness Size Mode</b> <i>Integer</i> | The method of computing the thickness of the drawn segments:<br>- <i>Image</i>: the value is normalized in texture space, where 1 is the full width of the image. Thickness is relative to the texture resolution;<br>- <i>Pixel</i>: the value is an absolute number of pixels in the texture, where 1 is a full pixel. Thickness is separate from the texture resolution. |
| <b>Thickness (image)</b> <i>Float</i> | (available when ‘Thickness Size Mode’ is set to Image) The thickness of the drawn segments normalized in texture space, where 1 is the full width of the image. |
| <b>Thickness (px)</b> <i>Float</i> | (available when ‘Thickness Size Mode’ is set to Pixel) The thickness of the drawn segments as an absolute number of pixels in the texture, where 1 is a full pixel. |
| <b>Enable Joints</b> <i>Boolean</i> | Fills the gaps between the individual segments drawn along the splines, using discs. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.<br>This also impacts uniform distribution. |
| <b>Color</b> |  |
| <b>Background Intensity</b> <i>Float</i> | The value multiplied against the Background input image. |
| <b>Spline Style</b> <i>Integer</i> | The method used to color the splines:<br>- <i>Solid</i>: The segments are drawn using a uniform grayscale value;<br>- <i>Gradient</i>: A gradient from black to white is applied along each string of segments from start to end;<br>- <i>Height</i>: The height of the splines is used as the grayscale value for drawing the segments. |
| <b>Spline Color</b> <i>Float</i> | The uniform grayscale value used to draw the segments.<br>When a Spline Style other than ‘Solid’ is selected, this color is multiplied against the styled color. |
| <b>Random Luminance</b> <i>Float</i> | For each string of uncut segments in a spline, applies a random offset in the specified range to the grayscale value used to draw that string. |
| <b>Blend Mode</b> <i>Integer</i> | The method of blending the colors of the background and overlapping segments drawn along the splines:<br>- <i>Max</i>: The brightest value is used;<br>- <i>Add</i>: The values are added together. |
| <b>Random Segments</b> |  |
| <b>Random Segments Start</b> <i>Float</i> | Adjusts the probability that the string of segments closer to the start of the spline is cut. |
| <b>Random Segments End</b> <i>Float</i> | Adjusts the probability that the string of segments closer to the end of the spline is cut. |
| <b>Random Offset</b> <i>Float</i> | Sets the maximum amount of displacement applied to each cut segment along its normal.<br>This parameter has no effect when Start and End are both set to 0. |
| <b>Random Offset Center</b> <i>Float</i> | Offsets the center of the random displacement applied to each cut segment along its normal. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="../../../../../../assets/SplineRender-Variant2-Before.jpg" alt="SplineRender-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="../../../../../../assets/SplineRender-Variant2-After.jpg" alt="SplineRender-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="../../../../../../assets/SplineRender-Variant1-Before.jpg" alt="SplineRender-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="../../../../../../assets/SplineRender-Variant1-After.jpg" alt="SplineRender-Variant1-After">
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

<table>
  <tr>
    <td>
      <img src="../../../../../../assets/SplineRender-Variant1-Before.jpg" alt="SplineRender-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="../../../../../../assets/SplineRender-Variant3.jpg" alt="SplineRender-Variant3">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 1](../../../../../../assets/SplineRender-Demo.gif "Node example 1")

</td>
</tr>
</table>
