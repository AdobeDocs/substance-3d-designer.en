---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/cloth-wear.html"
breadcrumb-title: ""
description: Use the Cloth Wear node to generate wear masks on cloth surfaces based on mesh curvature and contact areas.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Cloth Wear
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Cloth Wear
user-guide-description: ""
user-guide-title: ""
---


# Cloth Wear

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](cloth-wear.png){width="128px"}

## Cloth Wear

**In:** *Mesh Based Generators**/Mask Generators*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

The mask represents frazzled edges on cloth materials. It uses a cloth detail Heightmap that determines most of the look; without an appropriate map, the effect looks very basic.

## Parameters

### Inputs

* **Cloth Height**: *Grayscale Input*   
  Height for the cloth pattern only. This is not the height of your (baked) object, but rather a tiling detail pattern.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **Curvature**: *Grayscale Input*   
  Baked/generated curvature to determine raised edges.

### Parameters

* **Hard Edges Amount**: *0.0 - 1.0*
* **Wear Softness**: *0.0 - 5.0*Determines how blurred out/soft the worn edges are.

## Example Images

![](cloth-wear-ex.gif)

</td>
</tr>
</table>
