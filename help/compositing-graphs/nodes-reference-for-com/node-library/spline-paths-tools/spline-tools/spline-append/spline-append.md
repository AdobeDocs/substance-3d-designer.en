---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-append.html"
breadcrumb-title: ""
description: Use the Spline Append node to append multiple splines together to create longer continuous paths.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Append
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Append
user-guide-description: ""
user-guide-title: ""
---

# Spline Append

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-append.resources/spline-append-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

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
> Be mindful of the order in which you append splines, as this order is taken into account in other nodes, such as [Scatter on Splines](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/scatter-on-spline-color/scatter-on-spline-color.md), the [Spline Bridge](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-bridge-list/spline-bridge-list.md) nodes, etc.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview &#35;1</b> <i>Grayscale</i> | The preview of the first set of input splines as a grayscale image. |
| <b>Spline &#35;1 Coords</b> <i>Color</i> | The coordinates of the first set of input splines' points encoded in the RGBA channels of a color image.<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline &#35;1 Data</b> <i>Color</i> | Additional data of the first set of input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline &#35;1 Amount</b> <i>Integer</i> | The number of input splines in the first set. |
| <b>Preview &#35;2</b> <i>Grayscale</i> | The preview of the second set of input splines as a grayscale image. |
| <b>Spline &#35;2 Coords</b> <i>Color</i> | The coordinates of the second set of input splines' points encoded in the RGBA channels of a color image.<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline &#35;2 Data</b> <i>Color</i> | Additional data of the second set of input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline &#35;2 Amount</b> <i>Integer</i> | The number of input splines in the second set. |

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
| <b>Flip Spline &#35;1 Direction</b> <i>Boolean</i> | Inverts the direction of the splines in the first set. |
| <b>Flip Spline &#35;2 Direction</b> <i>Boolean</i> | Inverts the direction of the splines in the second set. |
| <b>Preview</b> |  |
| <b>Segments Amount</b> <i>Integer</i> | Adjusts the number of segments used to draw the spline visualization in the Preview output. A higher value results in a smoother line. |
| <b>Show Direction Helper</b> <i>Boolean</i> | Displays a dot at the start of the spline and an arrowhead at its end in the Preview output. |
| <b>Show Thickness Envelope</b> <i>Boolean</i> | Displays additional lines at the edges of the spline's thickness. |
| <b>Thickness (px)</b> <i>Float</i> | Adjusts the thickness of the spline visualization in pixels in the Preview output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](spline-append.resources/spline-append-02.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-append.resources/spline-append-03.jpg "Node example 2")

</td>
</tr>
</table>

![Node demo](spline-append.resources/spline-append-04.gif "Node demo")
