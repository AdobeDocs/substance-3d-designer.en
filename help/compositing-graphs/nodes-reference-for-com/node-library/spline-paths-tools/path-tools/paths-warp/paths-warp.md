---
title: "Paths Warp"
description: "Use the Paths Warp node to warp textures along path curves for creating curved and organic patterns."
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Paths Warp"
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/path-tools/paths-warp.html"
---

# Paths Warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](paths-warp-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Deform the input Paths according to the <b>Gradient Input</b>. (Same effect as the [Warp](../../../../atomic-nodes/warp/warp.md) node.)

</td>
</tr>
</table>

## Input connectors

<b>Paths</b> *Color*  
A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../mask-to-paths/mask-to-paths.md) or to another Path-processing node.

<b>Gradient Input</b> *Grayscale*  
The height-like input controlling both the amount and the direction of warping. (Same effect as the [Warp](../../../../atomic-nodes/warp/warp.md) node.)

## Output connectors

<b>Paths</b> *Color*  
The tranformed Paths. You can either use [Preview Paths](../preview-paths/preview-paths.md) to get an idea of what the result represents, use another Paths-processing node, or input it to a [Paths to Spline](../paths-to-spline/paths-to-spline.md) to further process it as Splines.

## Parameters

<b>Intensity</b> *Float*  
The <b>Intensity</b> parameter sets the intensity of the warp.

<b>Number of steps</b> *Integer*  
Use a higher value to warp the input paths by multiple small increments.  
This can prevent the path to cross itself, especially when using high <b>Intensity</b> values.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsToSpline-Variant2-Before.jpg" alt="PathsToSpline-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PathsWarp-Variant1-After.jpg" alt="PathsWarp-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsToSpline-Variant2-Before.jpg" alt="PathsToSpline-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PathsWarp-Variant2-After.jpg" alt="PathsWarp-Variant2-After">
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

![Node example 1](PathsWarp-Demo1.gif "Node example 1")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
