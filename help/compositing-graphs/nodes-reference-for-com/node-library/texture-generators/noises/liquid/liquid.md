---
title: "Liquid"
description: "Use the Liquid node to generate liquid and fluid patterns for creating water, oil, and other fluid surface effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Liquid
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/liquid.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - blending
  - pbr
  - effects
---




# Liquid

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](liquid.png){width="128px"}

## Liquid

**In:** *Texture Generators**/Noises*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

This is a simple variant of [Gaussian Noise](../gaussian-noise/gaussian-noise.md), which [warps](../../../../atomic-nodes/warp/warp.md) with itself to create a liquid-like effect.

## Parameters

* **Scale**: *1 - 128*  
  Sets the global scale for the effect.
* **Disorder**: *0.0 - 1.0*  
  Phase-shifts the noise to introduce small variation
* **Warp Intensity**: *0.0 - 1.0*  
  Sets the intensity of the warp effect.
* **Non Square Expansion**: *False/True*  
  Enables compensation of squash and stretch with non-square ratios.

## Example Images

![](liquid-ex.gif)

</td>
</tr>
</table>
