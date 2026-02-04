---
title: "Edge Notch | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Notch"
---

# Edge Notch

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-notch.png){width="128px"}

## Edge Notch

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents a simple mask for raised edges, broken up by a high-frequency noise. See [Edge Dirt](../edge-dirt/edge-dirt.md) or [Edge Damages](../edge-damages/edge-damages.md) for more options.

## Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for highlighting edges. Required!
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

## Parameters

* **Level**: *0.0 - 1.0*  
  Sets the level of the Edge Notch effect.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.

## Example Images

![](edge-notch-ex.gif)

</td>
</tr>
</table>

 