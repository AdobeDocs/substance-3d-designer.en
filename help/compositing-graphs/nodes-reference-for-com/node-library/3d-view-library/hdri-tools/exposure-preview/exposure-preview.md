---
title: "Exposure Preview | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Exposure Preview"
---

# Exposure Preview

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](hdr-exposure-preview.png){width="200px"}

## Exposure Preview

**In:** *3D View/HDRI Tools*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Helper node to preview exposure steps. Users sets a min and max value, the node generates a much larger image with a number different exposed versions of the original input. The different versions are always stacked horizontally, the amount depends on the resolution of the node or graph.

## Parameters

* **Max Exposure (EV)**: *-8.0 - 8.0*  
  Maximum exposure of the top, brightest image.
* **Min Exposure (EV)**: *-8.0 - 8.0*Minimum exposure of the bottom, darkest image.

## Example Images

![](exp-preview-ex.png)

</td>
</tr>
</table>

 