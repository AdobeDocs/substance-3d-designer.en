---
title: "3D Simplex Noise"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Simplex Noise"
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
Similar to [3D Perlin Noise](../3d-perlin-noise/3d-perlin-noise.md), but faster and simpler, for cases when performance and speed matter.

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
