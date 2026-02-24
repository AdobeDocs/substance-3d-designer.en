---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/vector-morph.html"
breadcrumb-title: ""
description: Use the Vector Morph node to morph textures between two inputs using vector fields for smooth transitions.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Vector Morph
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Vector Morph
user-guide-description: ""
user-guide-title: ""
---



# Vector Morph

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](vector-morph-grayscale.png)![](vector-morph.png)

## Vector Morph (Grayscale)

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Distorts an input image by a Vector Map. The effect is similar to UV distortion with a Normalmap, or using a "flow map" in videogame shaders. Input pixels are moved by the vectors defined in the Red and Green values of the vector map.

This node itself is not the most difficult to use, but creating a proper Vector Map takes care. We recommend that you work with the highest bit-depths to ensure precision when morphing.

Vector Morph is very similar to [Vector Warp](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/effects/vector-warp/vector-warp.md): the main difference is that this Morph node does not "loop" or "tile" the result when it gets pushed outside of the canvas bounds. Instead, it clamps and repeats the edges.

## Parameters

### Inputs

* **Input**: *Color/Grayscale Input*The source input that should be the target for the warping.
* **Vector Field**: *Color Input*The Vector Map used to drive the warping.

### Parameters

* **Amount**: *0.0 - 1.0*Sets the intensity of the warping effect, works as a multiplier for the Vector Map.

## Example Images

</td>
</tr>
</table>
