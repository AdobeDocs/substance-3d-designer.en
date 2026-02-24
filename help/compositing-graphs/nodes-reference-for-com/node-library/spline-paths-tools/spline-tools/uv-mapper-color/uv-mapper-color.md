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
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](uv-mapper-color-icon.png "Node icon")

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

## Input connectors

<b>UV</b> *Color*Image coordinates encoded in the red (U) and green (V) channels of a color image.

<b>Input</b> *Color*The color image which should be mapped to the coordinates provided in the UV input.

## Output connectors

<b>Output</b> *Color*The result of mapping the Input image using the input UV coordinates, as a color image.

## Parameters

<b>Background Color</b> *Float4*The background color of the output image.  
The background is visible in the areas of the image where UVs are not defined (I.e., the value is (0, 0, 0, 0)).

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="UVMapper-Variant1-Before.jpg" alt="UVMapper-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="UVMapper-Variant1-After.jpg" alt="UVMapper-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="UVMapper-Variant2-Before.jpg" alt="UVMapper-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="UVMapperColor-Variant2-After.jpg" alt="UVMapperColor-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

![Node in graph](UVMapperColor-Graph.jpg "Node in graph")

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
