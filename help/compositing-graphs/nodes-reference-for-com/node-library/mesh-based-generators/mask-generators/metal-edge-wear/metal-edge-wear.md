---
title: "Metal Edge Wear"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Metal Edge Wear"
---

# Metal Edge Wear

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](metal-edge-wear.png){width="128px"}

## Metal Edge Wear

**In:** *Mesh Based Generators**/Mask Generators*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents edge wear on a metal object, with scratches and chips appearing on Convex raised edges, potentially masked out by baked AO dark areas.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Grunge Input**: *Grayscale Input*
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **World Space Normal**: *Color Input*
* **Position**: *Color Input*

### Parameters

* **Wear Level**: *0.0 - 1.0*Sets the total amount of wear, gradually reveals.
* **Wear Contrast**: *0.0 - 1.0*Sets the contrast of the final result.
* **Edges Smoothness**: *0.0 - 16.0*Sets smoothness of the falloff from the edges from the Curvature.
* **Grunge Amount**: *0.0 - 1.0*Sets amount of grunge to blend in between edges.
* **Grunge Scale**: *1 - 16*Sets the scale of the Grunge.
* **Ambient Occlusion Masking**: *0.0 - 1.0*Sets amount of effect the AO has on the final effect, dark areas being masked out.
* **Curvature Weight**: *0.0 - 1.0*Sets amount of effect the Convex edges from the Curvature have on the final effect.
* **Use Custom Grunge**: *False/True*Enables a custom Grunge map input slot.
* **Use Triplanar**: *False/True*Enable [Tri Planar](../../utilities-mesh-based-gen/tri-planar/tri-planar.md) projection to hide seams.
* **Triplanar Blending Contrast**: *0.0 - 1.0*Sets blending contrast for the Triplanar Projection.

## Example Images

![](metal-edge-wear-ex.gif)

</td>
</tr>
</table>
