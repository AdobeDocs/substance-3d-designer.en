---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/point-list.html"
breadcrumb-title: ""
description: Use the Point List node to create and manage lists of points for spline and path generation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Point List
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Point List
user-guide-description: ""
user-guide-title: ""
---

# Point List

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](../../../../../../assets/point-list-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a list of points to be traversed by a spline.

If an existing point list is supplied to the <b>Point</b> inputs, the generated list is appended to the input list.

</td>
</tr>
</table>

>[!TIP]
>
> This node can be used to supply points to the [Spline (Poly Quadratic)](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-poly-quadratic/spline-poly-quadratic.md) node in order to build splines.

>[!IMPORTANT]
>
> The <b>Point List</b> and <b>Point Number</b> connectors are *not compatible* with <b>Spline Coord</b>, <b>Spline Data</b> and <b>Spline Amount</b> connectors, for they rely on different data.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the points as a grayscale image. |
| <b>Point List Input</b> <i>Color</i> | A list of input points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;&nbsp;&nbsp;* Integer part: Smoothness;<br>&nbsp;&nbsp;&nbsp;&nbsp;* Fractional part: Thickness. |
| <b>Point Number Input</b> <i>Integer</i> | The number of input points. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Grayscale</i> | The preview of the points as a grayscale image. |
| <b>Point List</b> <i>Color</i> | The output list of points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;&nbsp;&nbsp;* Integer part: Smoothness;<br>&nbsp;&nbsp;&nbsp;&nbsp;* Fractional part: Thickness. |
| <b>Point Number</b> <i>Integer</i> | The output number of points. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Point Number</b> <i>Integer</i> | The number of generated points. |
| <b>Global Smoothness Adjustment</b> <i>Float</i> | Applies a uniform offset to the smoothness value of all points.<br>The resulting smoothness value is clamped to the &#91;0;1&#93; range. |
| <b>Points Properties</b> |  |
| <b>p&#35; Properties</b> <i>Float3</i> | Sets the properties of the p# point.<br>*- Height:* Adjusts the height of the point where a lower value means a lower or deeper location;<br>*- Smoothness:* Offsets the start of the smoothing of the spline at p#, where a value of 0 results in a hard trajectory and 1 in an entirely smooth one;<br>*- Thickness:* Adjusts the thickness of the spline at p#. Thickness is used by specific Spline nodes. |
| <b>Points Coordinates</b> |  |
| <b>p&#35;</b> <i>Float2</i> | Sets the position of the p# point in texture space. |
| <b>Preview</b> |  |
| <b>Show Labels</b> <i>Boolean</i> | For each point, displays the point's name next to it in the 'Preview' output. |
| <b>Label Size</b> <i>Float</i> (Available when 'Show Labels' is set to 'True') | The size of the label for each point in texture space, where 0.1 is a tenth of the texture's width. |
| <b>Show Points</b> <i>Boolean</i> | Displays the points in the 'Preview' output. |
| <b>Points Size</b> <i>Float</i> (Available when 'Show Points' is set to 'True') | The radius of the points in texture space, where 0.1 is a tenth of the texture's width. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 1](../../../../../../assets/PointList-Variant1.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](../../../../../../assets/PointList-Demo1.gif "Node example 2")

</td>
</tr>
</table>
