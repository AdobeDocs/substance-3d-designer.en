---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/edge-notch.html"
breadcrumb-title: ""
description: Use the Edge Notch node to generate notch patterns on mesh edges for creating realistic edge damage and indentation effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Notch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Edge Notch
user-guide-description: ""
user-guide-title: ""
---


# Edge Notch

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-notch.png){width="128px"}

## Edge Notch

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents a simple mask for raised edges, broken up by a high-frequency noise. See [Edge Dirt](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/edge-dirt/edge-dirt.md) or [Edge Damages](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/mask-generators/edge-damages/edge-damages.md) for more options.

## Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for highlighting edges. Required!
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

## Parameters

* **Level**: *0.0 - 1.0*  
  Sets the level of the Edge Notch effect.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.

## Example Images

![](edge-notch-ex.gif)

</td>
</tr>
</table>
