---
title: "Dirt"
description: "Use the Dirt node to generate dirt accumulation masks based on mesh curvature, position, and occlusion."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Dirt
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/dirt.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - intermediate
helpx_learn_topic:
  - masking
  - reflections
  - creative-effects
---




# Dirt

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](dirt.png){width="128px"}

## Dirt

**In:** *Mesh Based Generators**/Mask Generators*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represent dirts in occluded and sunken edges and corners, based on baked AO and curvature.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for internal effects and masking. Required!
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking. Required!
* **Grunge input**: *Grayscale Input*   
  Custom grunge map input, optional, enabled by parameter.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **World Space Normal**: *Color Input*   
  Only used for Triplanar.
* **Position**: *Color Input*   
  Only used for Triplanar.

### Parameters

* **Dirt Level**: *0.0 - 1.0*Main control for amount of dirt.
* **Dirt Contrast**: *0.0 - 1.0*Controls main contrast for the dirt in the mask.
* **Grunge Amount**: *0.0 - 1.0*Sets how grungy the dirt is. Set to 0 for perfectly smooth dirt.
* **Edges Masking**: *0.0 - 1.0*Amount of dirt to remove from raised edges (based on the curvature map).
* **Use Custom Grunge**: *False/True*Enables use of custom grunge map input instead of built-in Grunge.
* **Grunge Scale**: *1 - 16*Sets tiling scale of Grunge detail.
* **Use Triplanar**: *False/True*Use [Triplanar projection](../../utilities-mesh-based-gen/tri-planar/tri-planar.md) for Grunge mapping, removes seams.
* **Triplanar Blending Contrast**: *0.001 - 1.0*Sets contrast of the Triplanar projection.

## Example Images

![](dirt-ex.gif)

</td>
</tr>
</table>
