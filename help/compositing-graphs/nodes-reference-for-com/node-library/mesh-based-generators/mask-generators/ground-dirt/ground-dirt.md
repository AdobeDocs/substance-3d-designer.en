---
title: "Ground Dirt"
description: "Use the Ground Dirt node to generate dirt accumulation masks based on mesh position and orientation relative to ground."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Ground Dirt
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/ground-dirt.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - masking
  - reflections
  - add-objects-to-images
---




# Ground Dirt

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](ground-dirt.png){width="128px"}

## Ground Dirt

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents dirt that has accumulated from the ground up, the opposite of [Bottom To Top](../bottom-to-top/bottom-to-top.md) or [Dust](../dust/dust.md). It has no custom map override.

## Inputs

* **Position**: *Grayscale Input*   
  Baked position map to base effect on. Required!
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

## Parameters

* **Level**: *0.0 - 1.0*  
  Sets the total appearance level of the dirt.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Dirt Height**: *0.0 - 1.0*Sets up to what height (proportionally) the dirt should appear.

## Example Images

![](ground-dirt-ex.gif)

</td>
</tr>
</table>
