---
title: "UV Mapper Grayscale"
description: "Use the UV Mapper Grayscale node to map grayscale textures along splines for procedural texture generation."
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > UV Mapper Grayscale"
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/uv-mapper-grayscale.html"
---

# UV Mapper Grayscale

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](uv-mapper-grayscale-icon.png "Node icon")

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
> See also [UV Mapper Color](../uv-mapper-color/uv-mapper-color.md).

## Input connectors

<b>UV</b> *Color*Image coordinates encoded in the red (U) and green (V) channels of a color image.

<b>Input</b> *Color*The grayscale image which should be mapped to the coordinates provided in the UV input.

## Output connectors

<b>Output</b> *Color*The result of mapping the Input image using the input UV coordinates, as a grayscale image.

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
      <img src="UVMapperGrayscale-Variant1-After.jpg" alt="UVMapperGrayscale-Variant1-After">
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
      <img src="UVMapper-Variant2-After.jpg" alt="UVMapper-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

![Node example 1](UVMapper-Graph.jpg "Node example 1")

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
