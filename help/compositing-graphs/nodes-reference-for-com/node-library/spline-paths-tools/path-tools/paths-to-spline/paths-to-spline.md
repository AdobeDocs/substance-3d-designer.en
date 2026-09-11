---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/path-tools/paths-to-spline.html"
breadcrumb-title: ""
description: Use the Paths to Spline node to convert path data into splines for use with spline-based nodes.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Paths to Spline
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Paths to Spline
user-guide-description: ""
user-guide-title: ""
---

# Paths to Spline

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](paths-to-spline.resources/paths-to-splines-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Converts a paths into splines which can be visualized using a [Spline Render](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-render/spline-render.md) node and processed using [Spline nodes](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-tools.md).

</td>
</tr>
</table>

>[!NOTE]
>
> Splines are curves thus cannot retain the sharpness of paths. Expect some smoothing of shapes when converting paths into splines.

>[!TIP]
>
> This node can be used after the [Mask to Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) node to form a chain that converts a mask into splines.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Paths</b> <i>Color</i> | A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) or to another Path-processing node. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;&nbsp;&nbsp;* Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;&nbsp;&nbsp;* Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a <b>color</b> image:<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Splines Precision</b> <i>Integer</i> | The base-2 logarithm (log2) of the number of vertices sampled in each path of the Paths input to build the corresponding spline. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="paths-to-spline.resources/PathsToSpline-Variant1-Before.jpg" alt="PathsToSpline-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="paths-to-spline.resources/PathsToSpline-Variant1-After.jpg" alt="PathsToSpline-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="paths-to-spline.resources/PathsToSpline-Variant2-Before.jpg" alt="PathsToSpline-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="paths-to-spline.resources/PathsToSpline-Variant2-After.jpg" alt="PathsToSpline-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>
