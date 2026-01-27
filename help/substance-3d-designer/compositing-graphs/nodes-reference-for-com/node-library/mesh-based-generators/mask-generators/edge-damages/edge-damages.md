---
title: "Edge Damages | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Damages"
---

# Edge Damages

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-damages.png){width="128px"}

## Edge Damages

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents damage done to raised, convex edges based on curvature and baked AO.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for effect placement. Required!
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for effect placement. Required!
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Amount of edge damage to apply.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Damages Intensity**: *0.0 - 1.0*Shifts between a chipped, consistent look and a chaotic, scratched, heavily damaged look.

## Example Images

![](edge-damages-ex.gif)

</td>
</tr>
</table>
