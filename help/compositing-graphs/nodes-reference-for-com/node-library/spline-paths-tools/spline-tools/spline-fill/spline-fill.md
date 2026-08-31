---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-fill.html"
breadcrumb-title: ""
description: Use the Spline Fill node to fill areas defined by closed splines with textures or colors.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Fill
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Fill
user-guide-description: ""
user-guide-title: ""
---

# Spline Fill

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](spline-fill.resources/spline-fill-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Fills the interior of input Splines with solid white. The exterior is filled with solid black.

Open splines are closed with a straight line from start to end. Intersections where the spline crosses itself are resolved by inverting the interior and exterior sides of the lines at those junctions.

</td>
</tr>
</table>

>[!IMPORTANT]
>
> It is not recommended to use this node on splines that are out of the &#91;0 ,1&#93; tile. The filling process is unreliable in that case.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines' points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The result image of filling the input Splines with flat white against a flat black background. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="spline-fill.resources/spline-fill-02.jpg" alt="SplineFill-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="spline-fill.resources/spline-fill-03.jpg" alt="SplineFill-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](spline-fill.resources/spline-fill-04.gif "Node example 2")

</td>
</tr>
</table>
