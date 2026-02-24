---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/path-tools/quad-transform-on-path.html"
breadcrumb-title: ""
description: Use the Quad Transform on Path node to apply quadratic transformations to elements along path curves.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Quad Transform on Path
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Quad Transform on Path
user-guide-description: ""
user-guide-title: ""
---


# Quad Transform on Path

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](quad-transform-on-paths-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Deform a Paths using 4 handles.

</td>
</tr>
</table>

## Input connectors

<b>Paths</b> *Color*  
A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) or to another *Path*-processing node.

## Output connectors

<b>Paths</b> *Color*  
The transformed Paths. You can either use [Preview Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/preview-paths/preview-paths.md) to get an idea of what the result represents, use another Paths-processing node, or input it to a [Paths to Spline](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) to further process it as Splines.

## Parameters

<b>p00</b> *Float2*  
The position of the top-left handle.

<b>p01</b> *Float2*  
The position of the top-right handle.

<b>p02</b> *Float2*  
The position of the bottom-left handle.

<b>p03</b> *Float2*  
The position of the bottom-right handle.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsPolygon_Variant1.jpg" alt="PathsPolygon_Variant1">
      <br><i>Before</i>
    </td>
    <td>
      <img src="QuadTransformOnPaths-Variant1-After.jpg" alt="QuadTransformOnPaths-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsPolygon_Variant1.jpg" alt="PathsPolygon_Variant1">
      <br><i>Before</i>
    </td>
    <td>
      <img src="QuadTransformOnPaths-Variant2-After.jpg" alt="QuadTransformOnPaths-Variant2-After">
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

![Node example 1](QuadTransformOnPaths-Demo2.gif "Node example 1")

</td>
<td style="border: 0;" valign="top">

![Node example 2](QuadTransformOnPaths-Demo1.gif "Node example 2")

</td>
</tr>
</table>
