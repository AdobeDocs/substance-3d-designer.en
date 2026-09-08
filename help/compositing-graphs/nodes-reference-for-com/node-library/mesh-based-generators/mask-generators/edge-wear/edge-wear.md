---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/edge-wear.html"
breadcrumb-title: ""
description: Use the Edge Wear node to generate wear masks on mesh edges for creating realistic edge damage and weathering effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Edge Wear
user-guide-description: ""
user-guide-title: ""
---

# Edge Wear

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/edge-wear.png){width="128px"}

## Edge Wear

**In:** *Mesh Based Generators**/Mask Generators*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This node represents wear on object edges. It has quite a few parameters, but is not the easiest to use: we recommend that you play around and get a feel for things. The node is quite powerful, although no custom override mask can be done.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked map used for internal effects and masking
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Sets total spread of the effect.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Threshold**: *0.0 - 1.0*Similar to Level, sets total spread of the effect.
* **Edges Width**: *0.0 - 1.0*Sets the fullness of the highlighting effect. Reduce to make them sparser.
* **Disorder**: *0.0 - 1.0*  
  Sets the amount of noise to blend in to break up the smoothness.

## Example Images

![](../../../../../../assets/edge-wear-ex.gif)

</td>
</tr>
</table>
