---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-bridge-2-splines.html"
breadcrumb-title: ""
description: Use the Spline Bridge node to bridge textures between two splines for creating seamless connections.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Bridge (2 Splines)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Bridge (2 Splines)
user-guide-description: ""
user-guide-title: ""
---

# Spline Bridge (2 Splines)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-bridge-2-splines.resources/spline-bridge-2-splines-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates splines from <b>Spline &#35;1</b> to <b>Spline &#35;2</b> along these splines. The generated splines can be Linear (straight) or Cubic Bezier (curved).

</td>
</tr>
</table>

>[!IMPORTANT]
>
> If the data supplied to the <b>Spline &#35;1</b> and <b>Spline &#35;2</b> inputs contain more than one spline, only the last spline in each list is used.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview &#35;1</b> <i>Grayscale</i> | The preview of the input splines #1 as a grayscale image. |
| <b>Spline Coords &#35;1</b> <i>Color</i> | The coordinates of the input splines' points #1 encoded in the RGBA channels of a color image.<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data &#35;1</b> <i>Color</i> | Additional data of the input splines #1 encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount &#35;1</b> <i>Integer</i> | The number of input splines #1. |
| <b>Preview &#35;2</b> <i>Grayscale</i> | The preview of the input splines #2 as a grayscale image. |
| <b>Spline Coords &#35;2</b> <i>Color</i> | The coordinates of the input splines' #2 points encoded in the RGBA channels of a color image.<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data &#35;2</b> <i>Color</i> | Additional data of the input splines #2 encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount &#35;2</b> <i>Integer</i> | The number of input splines #2. |
| <b>Start Tangent Length Curve</b> <i>Grayscale</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The image describing a curve using the values of its first row of pixels.<br>This input is used to control the length of the 'out' tangents for the start point of each generated spline along Spline #1.<br>You may use a Curve node to author the curve. |
| <b>Start Tangent Rotation Curve</b> <i>Grayscale</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The image describing a curve using the values of its first row of pixels.<br>This input is used to control the rotation of the 'out' tangents for the start point of each generated spline along Spline #1.<br>The grayscale value of the image represents a number of turns.<br>You may use a Curve node to author the curve. |
| <b>End Tangent Length Curve</b> <i>Grayscale</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The image describing a curve using the values of its first row of pixels.<br>This input is used to control the length of the 'in' tangents for the end point of each generated spline along Spline #2.<br>You may use a Curve node to author the curve. |
| <b>End Tangent Rotation Curve</b> <i>Grayscale</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The image describing a curve using the values of its first row of pixels.<br>This input is used to control the rotation of the 'in' tangents for the end point of each generated spline along Spline #2.<br>The grayscale value of the image represents a number of turns.<br>You may use a Curve node to author the curve. |

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
| <b>Bridge Splines Amount</b> <i>Integer</i> | The number of splines generated along Spline #1 to Spline #2. |
| <b>Bridge Splines Type</b> <i>Integer</i> | The type of spline that is generated:<br><br>- Linear: a straight spline from Start to End;<br>- Cubic Bezier: a curved spline from Start to End, the curve being controlled by the length and angle of the Start and End points. |
| <b>Start Spline &#35;1</b> <i>Float</i> | Offsets the location along Spline #1 from where splines are generated. The value is the normalized length of Spline #1.<br>A higher value results in the same number of splines being packed more tightly together. |
| <b>Start Spline &#35;2</b> <i>Float</i> | Offsets the location along Spline #2 from where splines are generated. The value is the normalized length of Spline #2.<br>A higher value results in the same number of splines being packed more tightly together. |
| <b>End Spline &#35;1</b> <i>Float</i> | Offsets the location along Spline #1 up to where splines are generated. The value is the normalized length of Spline #1.<br>A lower value results in the same number of splines being packed more tightly together. |
| <b>End Spline &#35;1</b> <i>Float</i> | Offsets the location along Spline #2 up to where splines are generated. The value is the normalized length of Spline #2.<br>A lower value results in the same number of splines being packed more tightly together. |
| <b>Offset Spline &#35;1</b> <i>Float</i> | Applies an offset to the starting point of all splines along Spline #1. The value is the normalized length of Spline #1.<br>Splines that meet the start or end of the spline are left there. |
| <b>Offset Spline &#35;2</b> <i>Float</i> | Applies an offset to the starting point of all splines along Spline #2. The value is the normalized length of Spline #2.<br>Splines that meet the start or end of the spline are left there. |
| <b>Offset Random Start</b> <i>Float</i> | Applies a random offset to the starting point of each spline along Spline #1. The value is the normalized distance between splines on Spline #1.<br>When left at 0, the splines are evenly spaced between the Start Spline #1 and End Spline #1 points. |
| <b>Offset Random End</b> <i>Float</i> | Applies a random offset to the ending point of each spline along Spline #2. The value is the normalized distance between splines on Spline #2.<br>When left at 0, the splines are evenly spaced between the Start Spline #2 and End Spline #2 points. |
| <b>Tangent Length Start</b> <i>Float</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The length of the 'out' tangent for the start point on Spline #1 of all generated splines. |
| <b>Tangent Length End</b> <i>Float</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The length of the 'in' tangent for the end point on Spline #2 of all generated splines. |
| <b>Tangent Rotation Start</b> <i>Float</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The rotation of the 'out' tangent for the start point on Spline #1 of all generated splines.<br>The value is a number of turns. |
| <b>Tangent Rotation End</b> <i>Float</i> (Available when 'Bridge Splines Type' is set to 'Cubic Bezier') | The rotation of the 'in' tangent for the end point on Spline #2 of all generated splines.<br>The value is a number of turns. |
| <b>Preview</b> |  |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output. A higher value results in a smoother line. |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Show Thickness Envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline's thickness. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness of the spline visualization in pixels in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-bridge-2-splines.resources/spline-bridge-2-splines-02.jpg" alt="SplineBridge-2Splines_Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-bridge-2-splines.resources/spline-bridge-2-splines-03.jpg" alt="SplineBridge-2Splines_Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-bridge-2-splines.resources/spline-bridge-2-splines-04.gif "Node example 2")

</td>
</tr>
</table>
