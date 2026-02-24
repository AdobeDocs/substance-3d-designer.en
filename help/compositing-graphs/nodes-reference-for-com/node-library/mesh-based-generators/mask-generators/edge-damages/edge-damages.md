---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/edge-damages.html"
breadcrumb-title: ""
description: Use the Edge Damages node to generate damage masks on mesh edges for creating realistic edge wear and breakage effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Damages
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Edge Damages
user-guide-description: ""
user-guide-title: ""
---


# Edge Damages

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](edge-damages.png){width="128px"}

## Edge Damages

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents damage done to raised, convex edges based on curvature and baked AO.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for effect placement. Required!
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for effect placement. Required!
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Amount of edge damage to apply.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Damages Intensity**: *0.0 - 1.0*Shifts between a chipped, consistent look and a chaotic, scratched, heavily damaged look.

## Example Images

![](edge-damages-ex.gif)

</td>
</tr>
</table>
