---
title: "3D Linear Gradient"
description: "Use the 3D Linear Gradient node to create linear gradients based on 3D world position for spatial effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > 3D Linear Gradient
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/3d-linear-gradient.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - intermediate
helpx_learn_topic:
  - gradients
  - effects
  - 3d
---




# 3D Linear Gradient

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3d-linear-gradient.png){width="128px"}

## 3D Linear Gradient

**In:** *Texture Generators**/Patterns*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Creates a volumetric gradient based on input Position map. Effectively generates a transition from black to white between 2 points in 3D Space. Intened for use with the GPU engine only.

Also see [3D Volume Mask](../3d-volume-mask/3d-volume-mask.md) for a similar effect.

## Parameters

* **Points Position Mode**: *UV Positions, World Space Positions*Choose if the Gradient Points work in UV Space (works best when setting them in 2D view) or in in 3D coordinates, if you want to manually enter an exact position.
* **Point 1**:   
  Start Point of the gradient. Can be 2D or 3D Coordinates based on Position Mode.
* **Point 2**:   
  End Point of the gradient. Can be 2D or 3D Coordinates based on Position Mode.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.

## Example Images

![](3d-gradient.gif)

</td>
</tr>
</table>
