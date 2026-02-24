---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/sun-bleach.html"
breadcrumb-title: ""
description: Use the Sun Bleach node to generate masks based on sun exposure for creating realistic sun-bleached and faded effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Sun Bleach
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Sun Bleach
user-guide-description: ""
user-guide-title: ""
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

This mask is similar to [Light](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/light/light.md), but has support for AO too, leading to a mask that represents light bleaching and fading on top of an effect.

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
