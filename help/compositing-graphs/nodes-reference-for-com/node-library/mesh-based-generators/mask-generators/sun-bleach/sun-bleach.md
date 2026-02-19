---
title: "Sun Bleach"
description: "Use the Sun Bleach node to generate masks based on sun exposure for creating realistic sun-bleached and faded effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Sun Bleach
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/sun-bleach.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - masking
  - creative-effects
  - effects
---




# Sun Bleach

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](sun-bleach.png){width="128px"}

## Sun Bleach

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask is similar to [Light](../light/light.md), but has support for AO too, leading to a mask that represents light bleaching and fading on top of an effect.

## Inputs

* **Normal World Space**: *Color Input*
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

## Parameters

* **Level**: *0.0 - 1.0*  
  Sets the total amount of bleaching, moves the effect further down.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Occlusion**: *0.0 - 1.0*Sets the influence of the AO on the final result.

## Example Images

![](sun-bleach-ex.gif)

</td>
</tr>
</table>
