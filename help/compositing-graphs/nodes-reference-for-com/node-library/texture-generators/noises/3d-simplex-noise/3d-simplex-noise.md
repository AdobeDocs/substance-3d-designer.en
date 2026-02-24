---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/3d-simplex-noise.html"
breadcrumb-title: ""
description: Use the 3D Simplex Noise node to generate 3D simplex noise patterns for creating smooth, natural-looking volumetric textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Simplex Noise
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: 3D Simplex Noise
user-guide-description: ""
user-guide-title: ""
---


# 3D Simplex Noise

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3d-simplex-noise.png){width="128px"}

## 3D Simplex Noise

**In:** *Texture Generators**/Noises*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a procedural noise when a baked Position Map is plugged into the input slot. It is meant for use with the GPU engine only.  
Similar to [3D Perlin Noise](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/3d-perlin-noise/3d-perlin-noise.md), but faster and simpler, for cases when performance and speed matter.

This noise can be tested with [Cube 3D GBuffers](https://support.allegorithmic.com/documentation/display/SDDOC/Cube+3D+GBuffers) as input instead of an actual baked map (as seen in the Example Image below).

## Parameters

* **Scale**: *0.0 - 64.0*  
  Set the global scale for the effect.
* **Size**: *0.0 - 2.0*Perform non-uniform scaling on X, Y and Z axes separately.

## Example Images

![](3d-simplex.gif)

</td>
</tr>
</table>
