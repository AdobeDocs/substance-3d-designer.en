---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/uv-mapper-color.html"
breadcrumb-title: ""
description: Use the UV Mapper Color node to map color textures along splines for procedural texture generation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > UV Mapper Color
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: UV Mapper Color
user-guide-description: ""
user-guide-title: ""
---

# UV Mapper Color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](uv-mapper-color.resources/uv-mapper-color-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Maps the input color image using the coordinates provided in the UV input.

</td>
</tr>
</table>

>[!NOTE]
>
> See also [UV Mapper Grayscale](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/uv-mapper-grayscale/uv-mapper-grayscale.md).

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>UV</b> <i>Color</i> | Image coordinates encoded in the red (U) and green (V) channels of a color image. |
| <b>Input</b> <i>Color</i> | The color image which should be mapped to the coordinates provided in the UV input. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Color</i> | The result of mapping the Input image using the input UV coordinates, as a color image. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Background Color</b> <i>Float4</i> | The background color of the output image.<br>The background is visible in the areas of the image where UVs are not defined (I.e., the value is (0, 0, 0, 0)). |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="uv-mapper-color.resources/UVMapper-Variant1-Before.jpg" alt="UVMapper-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="uv-mapper-color.resources/UVMapper-Variant1-After.jpg" alt="UVMapper-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="uv-mapper-color.resources/UVMapper-Variant2-Before.jpg" alt="UVMapper-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="uv-mapper-color.resources/UVMapperColor-Variant2-After.jpg" alt="UVMapperColor-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

![Node in graph](uv-mapper-color.resources/UVMapperColor-Graph.jpg "Node in graph")
