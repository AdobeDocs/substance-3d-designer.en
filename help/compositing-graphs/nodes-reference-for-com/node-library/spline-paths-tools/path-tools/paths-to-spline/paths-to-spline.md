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

![Node icon](paths-to-splines-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Converts a paths into splines which can be visualized using a [Spline Render](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-render/spline-render.md) node and processed using [Spline nodes](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-tools.md).

</td>
</tr>
</table>

>[!NOTE]
>
> Splines are curves thus cannot retain the sharpness of paths. Expect some smoothing of shapes when converting paths into splines.

>[!TIP]
>
> This node can be used after the [Mask to Paths](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) node to form a chain that converts a mask into splines.

## Input connectors

<b>Paths</b> *Color*  
A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) or to another Path-processing node.

## Output connectors

<b>Spline Coords</b>*Color*The coordinates of the input splines’ points encoded in the RGBA channels of a color image:  
    <b>R</b> - X position  
    <b>G</b> - Y position  
    <b>B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*  
Additional data of the input splines encoded in the RGBA channels of a <b>color</b> image:  
<b>R</b> - Tangents X  
<b>G</b> - Tangents Y  
<b>B</b> - Unused  
<b>A</b> - Unused

<b>Spline Amount</b> *Integer*  
The number of input splines.

## Parameters

<b>Splines Precision</b> *Integer*  
The base-2 logarithm (log2) of the number of vertices sampled in each path of the Paths input to build the corresponding spline.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="PathsToSpline-Variant1-Before.jpg" alt="PathsToSpline-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PathsToSpline-Variant1-After.jpg" alt="PathsToSpline-Variant1-After">
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
      <img src="PathsToSpline-Variant2-After.jpg" alt="PathsToSpline-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>
