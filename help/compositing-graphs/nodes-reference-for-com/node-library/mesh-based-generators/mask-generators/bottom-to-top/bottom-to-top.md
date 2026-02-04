---
title: "Bottom To Top"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Bottom To Top"
---

# Bottom To Top

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](bottom-to-top.png){width="128px"}

## Bottom To Top

**In:** *Mesh Based Generators/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://helpx.adobe.com/substance-3d-painter/features/smart-materials-and-masks.html) in [Painter](https://helpx.adobe.com/substance-3d-painter/home.html).

This generates a white to black transition from the bottom to the top of a model, useful for making geometry-based falloffs and selections.

## Parameters

### Inputs

* **Position**: *Color Input*   
  Baked Position map. Required!
* **Roughness:** *Grayscale Input*   
  This has nothing to do with PBR roughness, but is an (optional) variation map to break up the transition. Only appears when Roughness is set higher than 0.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Shifts the average level of the result between black or white, like a brightness adjustment.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the transition.
* **Roughness\_Variation**: *0.0 - 1.0*Determines amount of the Roughness map to blend in for variation. Increasing this over 0 reveals the map slot.

## Example Images

![](bottom-to-top-ex.gif)

</td>
</tr>
</table>
