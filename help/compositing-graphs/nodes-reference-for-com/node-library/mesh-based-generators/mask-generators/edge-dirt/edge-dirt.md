---
title: "Edge Dirt | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Dirt"
---

# Edge Dirt

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-dirt.png){width="128px"}

## Edge Dirt

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents a dirt effect that accumulates around edges, based solely on a curvature map.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for effect placement. Required!
* **Variation Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects, only used when override parameter is enabled.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Sets the amount of dirt.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Variation**: *0.0 - 1.0*Blends in how much large-scale masking/breakup should happen.
* **Override variation mask**: *False/True*

## Example Images

![](edge-dirt-ex.gif)

</td>
</tr>
</table>

 