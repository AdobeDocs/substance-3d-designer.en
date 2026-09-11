---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/uv-mapper-grayscale.html"
breadcrumb-title: ""
description: Use the UV Mapper Grayscale node to map grayscale textures along splines for procedural texture generation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > UV Mapper Grayscale
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: UV Mapper Grayscale
user-guide-description: ""
user-guide-title: ""
---

# UV Mapper Grayscale

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](uv-mapper-grayscale.resources/uv-mapper-grayscale-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Maps the input grayscale image using the coordinates provided in the UV input.

</td>
</tr>
</table>

>[!NOTE]
>
> See also [UV Mapper Color](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/uv-mapper-color/uv-mapper-color.md).

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>UV</b> <i>Color</i> | Image coordinates encoded in the red (U) and green (V) channels of a color image. |
| <b>Input</b> <i>Color</i> | The grayscale image which should be mapped to the coordinates provided in the UV input. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Color</i> | The result of mapping the Input image using the input UV coordinates, as a grayscale image. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="uv-mapper-grayscale.resources/UVMapper-Variant1-Before.jpg" alt="UVMapper-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="uv-mapper-grayscale.resources/UVMapperGrayscale-Variant1-After.jpg" alt="UVMapperGrayscale-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="uv-mapper-grayscale.resources/UVMapper-Variant2-Before.jpg" alt="UVMapper-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="uv-mapper-grayscale.resources/UVMapper-Variant2-After.jpg" alt="UVMapper-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

![Node example 1](uv-mapper-grayscale.resources/UVMapper-Graph.jpg "Node example 1")
