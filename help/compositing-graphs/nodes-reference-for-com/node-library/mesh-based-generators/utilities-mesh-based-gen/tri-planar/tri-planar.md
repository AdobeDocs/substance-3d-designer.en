---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/utilities-mesh-based-generators/tri-planar.html"
breadcrumb-title: ""
description: Use the Tri Planar node to project textures from three orthogonal planes for seamless texture mapping on complex geometry.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Utilities (Mesh Based Generators) > Tri Planar
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Tri Planar
user-guide-description: ""
user-guide-title: ""
---

# Tri Planar

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/triplanar-1.png){width="128px"}

![](../../../../../../assets/triplanar-grayscale.png){width="128px"}

## Tri Planar (Grayscale)

**In:** *Mesh Based Generators**/Utilities*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This advanced node performs Triplanar projection mapping in 2D, based on baked Position an World Space Normal data. This means it essentially completely converts UV-coordinates into a (mostly) seam-free mapping based on the mesh itself.

This is a good way to avoid seams without having to rebake every time (it is possible to achieve something similar with the baker). The downside is that this node is quite heavy and thus not fast.

Do keep in mind that your bakes should be high-precision: 8-bit bakes will not lead to very nice results.

## Parameters

### Inputs

* **Position**: *Color Input*   
  Baked Position map. Ideally 16-bit or higher precision.
* **World Space Normal**: *Color Input*   
  Baked World Space Normal map, Ideally 16-bit or higher precision.
* **Input X**: *Color Input (Grayscale Input)*Input map to remap from UV to World Space via Triplanar projection. Used for all Axes when Image Inputs is set to 1, for X axis if set to 3.
* **Input Y**: *Color Input (Grayscale Input)*Only if Image Inputs is set to 3. Input map to remap from UV to World Space on the Y Axis.
* **Input Z**: *Color Input (Grayscale Input)*Only if Image Inputs is set to 3. Input map to remap from UV to World Space on the Z Axis.

### Parameters

* **Projection**: *All axis, X only, Y only, Z only*Sets which Axes to blend with.
* **Image Inputs**: *1 input, 3 inputs*  
  Set whether to use one Map for all Axes, or a specific map per Axis.
* **Blending Mode**: *linear, advanced*Increases accuracy and precision.
* **Blending Contrast**: *0.001 - 1.0*Transition contrast, blend between smooth or harsh transitions.
* **Normalization Factor**: *0.0 - 1.0*  
  Improves the projection blending by restoring the loss of contrast in the blending area.
* **Texture Tiling**: *0.0 - 10.0*Number of times to tile the input textures.
* **Global Rotation**: *0.0 - 1.0*  
  Global Rotation for all Axes.
* **Fix Mirrored Projection**: *False/True*Set how to handle Mirrored Projections.
* **Rotation X**: *0.0 - 1.0*Individual rotation over projection X-axis.
* **Rotation Y**: *0.0 - 1.0*Individual rotation over projection Y-axis.
* **Rotation Z**: *0.0 - 1.0*Individual rotation over projection Z-axis.
* **Offset X**: *0.0 - 1.0*Offset over projection X-axis.
* **Random Offset X**: *0.0 - 1.0*  
  Allow for randomisation of X-axis offset.
* **Offset Y**: *0.0 - 1.0*Offset over projection Y-axis.
* **Random Offset Y**: *0.0 - 1.0*  
  Allow for randomisation of Y-axis offset.
* **Offset Z**: *0.0 - 1.0*Offset over projection Z-axis.
* **Random Offset Z**: *0.0 - 1.0*  
  Allow for randomisation of Z-axis offset.

## Example Images

</td>
</tr>
</table>
