---
title: "Paths Select | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Paths Select"
---

# Paths Select

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](paths-select-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Isolate one path among multiples contained in Paths.

</td>
</tr>
</table>

## Input connectors

<b>Label</b> *Type*  
A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../mask-to-paths/mask-to-paths.md) or to another Path-processing node.

## Output connectors

<b>Paths</b> *Color*  
The Paths input with only one path. You can either use [Preview Paths](../preview-paths/preview-paths.md) to get an idea of what the result represents, use another Paths-processing node, or input it to a [Paths to Spline](../paths-to-spline/paths-to-spline.md) to further process it as Splines.

## Parameters

<b>Selection Mode</b> *Integer*The method used to select the Paths:  
*- By ID:* Selects the path from the list whose index matches the one specified in <b>Path ID</b>;  
*- By Length:* Selects the paths whose length is above or below the threshold specified in <b>Target Length</b>.

<b>Path ID</b> *Integer* (Available when <b>Selection Mode</b> is set to *By ID*)  
The index of the selected path.  
A value greater than the number of paths in <b>Paths *results in*</b> a blank output.

<b>Length Greater or Lower?</b> *Boolean* (Available when <b>Selection Mode</b> is set to *By Length*)  
Controls whether the selection should include or greater or lower length than the <b>Target Length</b>.

<b>Target Length</b> *Float*(Available when <b>Selection Mode</b> is set to *By Length*)  
The length threshold used to select splines.

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
      <img src="PathsSelect-Variant1.jpg" alt="PathsSelect-Variant1">
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
      <img src="PathsSelect-Variant2.jpg" alt="PathsSelect-Variant2">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>
