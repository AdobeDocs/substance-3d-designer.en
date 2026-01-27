---
title: "Grease | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Grease"
---

# Grease

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](grease.png){width="128px"}

## Grease

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask is specifically intended for character faces and other specific areas. Generates a skin-grease type of mask on areas of low thickness.

## Parameters

### Inputs

* **Thickness**: *Grayscale Input*   
  Baked Thickness map on which the entire effect is based. Required!
* **Noise**: *Grayscale Input*   
  Optional Noise map to override Grease grunge with.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Sets the total amount of effect to appear.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Thickness Threshold**: *0.0 - 1.0*Sets a minimum thickness at which the effect should appear. Equally important as Level; tweak this to fit your Thickness map.
* **Override Noise**: *False/True*Set to override internal grease grunge map with custom input slot.

## Example Images

![](grease-ex.gif)

</td>
</tr>
</table>
