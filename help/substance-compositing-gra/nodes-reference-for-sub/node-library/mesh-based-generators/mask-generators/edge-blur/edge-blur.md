---
title: "Edge Blur"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Blur"
---

# Edge Blur

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-blur.png){width="128px"}

## Edge Blur

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask highlights edges based on a baked curvature map. It is one of the more simple Mask Generators.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used to base the effect on.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Sets the amount of edge highlighting.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Blur Radius**: *0.0 - 8.0*Sets the amount of blurring on the highlighted edges.

## Example Images

![](edge-blur-ex.gif)

</td>
</tr>
</table>
