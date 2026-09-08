---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/utilities-mesh-based-generators/3d-planar-projection.html"
breadcrumb-title: ""
description: Use the 3D Planar Projection node to project textures onto mesh surfaces using planar projection for texture mapping.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Utilities (Mesh Based Generators) > 3D Planar Projection
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Planar Projection
user-guide-description: ""
user-guide-title: ""
---

# 3D Planar Projection

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/3d-planar-gray.png)![](../../../../../../assets/3d-planar.png)

## 3D Planar Projection (Color)

**In:** *Mesh Based Generators**/Utilities*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a planar projection based on baked mesh data (Position and World Normal Maps). Allows you to project and place decals across seams, independent of original UV-mapping.

## Parameters

### Inputs

* **Position Map**: *Color Input*Baked Position Map
* **World Space Normal**: *Color Input*Baked World Space Normal Map
* **Projected Texture**: *Color Input*Input texture to project onto target.

### Parameters

* **Positioning**   
  * **Project Input**: *UV Position, World Space Position*Choose whether the projection position is set in 2D/UV or in 3D/World space.
  * **Target UV Position**:  
    Only with UV Position Input, best used to pick a point in the 2D view on the Position map.
  * **Target Position**: *(Color value)*Only with World Space Position Input, lets you define an exact 3D coordinate.
  * **Target Normal**: *(Color value)*
  * **Rotation**: *0.0 - 1.0  
    Rotates the projected texture along it' normal axis.*
  * **Scale**: *0.0 - 1.0*  
    Set the global scale for the projected texture.
  * **Size**: *0.0 - 2.0*Perform non-uniform scaling on the projected texture.
* **Masking**   
  * **Maximum Depth**: *0.0 - 1.0*Controls how deep the projected texture will appear, when it will cut-off.
  * **Depth Fade**: *0.0 - 1.0*Set the transition for the cut-off depth to be sudden or faded.
  * **Normal Threshold**: *-1.0 - 1.0*Set the treshold for surfaces not exactly aligned with the projection normal.
  * **Normal Fade**: *0.0 - 1.0*Set the transition for surfaces not aligned to sudden or fade.

## Example Images

![](../../../../../../assets/3d-planar-projection-ex.gif)

</td>
</tr>
</table>
