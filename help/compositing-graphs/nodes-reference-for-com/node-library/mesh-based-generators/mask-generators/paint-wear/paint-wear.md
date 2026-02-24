---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/paint-wear.html"
breadcrumb-title: ""
description: Use the Paint Wear node to generate paint wear masks based on mesh geometry for creating realistic paint chipping effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Paint Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Paint Wear
user-guide-description: ""
user-guide-title: ""
---


# Paint Wear

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](paint-wear.png){width="128px"}

## Paint Wear

**In:** *Mesh Based Generators**/Mask Generators*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents paint chipping and wearing away at edges.

## Parameters

### Inputs

* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Curvature**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Variation Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Sets the total amount of paint wear, gradually revealing.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Occlusion**: *0.0 - 1.0*Sets amount of effect the baked AO has on preventing wear in darker areas.
* **Radius**: *0.0 - 2.0*Sets how far the chipping effect spreads from Convex edges.
* **Variation**: *0.0 - 1.0*Set amount of variation (grunge) to blend into the effect.
* **Override variation mask**: *False/True*Enables custom variation (grunge) map input slot.

## Example Images

![](paint-wear-ex.gif)

</td>
</tr>
</table>
