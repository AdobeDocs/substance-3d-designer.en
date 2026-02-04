---
title: "Leather Wear | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Leather Wear"
---

# Leather Wear

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](leather-wear.png){width="128px"}

## Leather Wear

**In:** *Mesh Based Generators**/Mask Generators*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents wear with a leather pattern, with more wear on edges based on Curvature. It is similar to [Fiber Glass Edge Wear](../fiber-glass-edge-wear/fiber-glass-edge-wear.md) in functionality and has mostly the same parameters.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for edge placement. Required!
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used occluding certain areas. Recommended, but not required.
* **Grunge Input**: *Grayscale Input*   
  Optional Grunge map input slot that can be toggled through the "Use Custom Grunge" parameter.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Wear Level**: *0.0 - 1.0*Sets global wear level, gradually revealing.
* **Wear Contrast**: *0.0 - 1.0*Sets contrast of the effect.
* **Grunge Amount**: *0.0 - 1.0*Sets the amount of grunge (default leather pattern) to blend in between edges.
* **Ambient Occlusion Masking**: *0.0 - 1.0*Sets extent to which the AO masks out the wear effects.
* **Curvature Weight**: *0.0 - 1.0*Sets extent to which the curvature's edges affect the final result. Even if set to 0, you still need a curvature map.
* **Use Custom Grunge**: *False/True*Enables overriding of the built-in default leather pattern. Use a custom input slot instead.

## Example Images

![](leather-wear-ex.gif)

</td>
</tr>
</table>

 