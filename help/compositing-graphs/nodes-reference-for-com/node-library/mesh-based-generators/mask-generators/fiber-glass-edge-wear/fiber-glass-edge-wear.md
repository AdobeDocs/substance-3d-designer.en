---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/fiber-glass-edge-wear.html"
breadcrumb-title: ""
description: Use the Fiber Glass Edge Wear node to generate wear masks on fiberglass edges based on mesh curvature.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Fiber Glass Edge Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Fiber Glass Edge Wear
user-guide-description: ""
user-guide-title: ""
---


# Fiber Glass Edge Wear

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](fiber-glass-edge-wear.png){width="128px"}

## Fiber Glass Edge Wear

**In:** *Mesh Based Generators**/Mask Generators*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

Represents a mask specifically intended for a fibreglass-type of wear, could perhaps be used for cloth. Due to the very tiled, repetitive nature of the fibres, Triplanar blending can optionally be enabled.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for edge highlighting. Required!
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for masking occluded areas. Not required, but definitely recommended.
* **Grunge Input**: *Grayscale Input*   
  Optional custom slot to override fiber pattern.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **World Space Normal**: *Color Input*   
  Only used for Triplanar.
* **Position**: *Color Input*   
  Only used for Triplanar.

### Parameters

* **Wear Level**: *0.0 - 1.0*Like a [Histogram Scan](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-scan/histogram-scan.md), progressively reveals the wear.
* **Wear Contrast**: *0.0 - 1.0*Sets total effect contrast.
* **Edges Smoothness**: *0.0 - 16.0*Sets bleed out/blurring from highlighted edges.
* **Grunge Amount**: *0.0 - 1.0*Sets how much of the fibre effect to blend in between the edges. Tweak this together with Wear Level to get maximum control.
* **Ambient Occlusion Masking**: *0.0 - 1.0*Sets amount of influence the AO has on hiding the effect.
* **Curvature Weight**: *0.0 - 1.0*Sets amount of influence Convex edges from the Curvature have.
* **Use Custom Grunge**: *False/True*Overrides built-in fibres with custom map.
* **Use Triplanar**: *False/True*Enables [Tri Planar](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/utilities-mesh-based-gen/tri-planar/tri-planar.md) to hide seams.
* **Triplanar Blending Contrast**: *0.0 - 1.0*Controls contrast of the Triplanar effect.

## Example Images

![](fiber-glass-edge-wear-ex.gif)

</td>
</tr>
</table>
