---
title: "Material Blend"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Material Blend"
---

# Material Blend

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](material-blend.png){width="128px"}

## Material Blend

**In:** *Material Filters/Blending*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Material Blend is the Multi-Channel, Full Material Equivalent of [the atomic Blend Node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blend/blend.md). It blends between two full materials (all possibe channels) based on a grayscale mask, or optionally based on one single color from a Color ID mask.

This node is useful if you want to blend two materials and have a grayscale map but no full Color ID bake. If you do have a Color ID bake and want to blend more than two materials, we suggest you use [Multi-Material Blend](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/blending-material/multi-material-blend/multi-material-blend.md).

## Parameters

### Inputs

* **ColorID**: *Color Input*   
  Optional Baked color ID map.
* **Greyscale Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Channels**   
  * Toggle material channels on and off in this group, when using Specular/Glossiness maps instead of Metallic/Roughness for example.
* **Diffuse**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Base Color**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Normal**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
* **Specular**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Emissive**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Glossiness**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Roughness**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Metallic**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Specular Level**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Ambient Occlusion**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Height**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Opacity**   
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*
* **Color ID Mask**: *False/True*Use Color ID mask instead of grayscale mask. Keep in mind that this is only for one color!
* **Color**: *(Color value)*Which color to pick and convert to white.
* **Fuzziness**: *0.01 - 1.0*The extent to which the color you picked blends over into its neighbours.
* **Padding**: *0.0 - 1.0*Transition contrast of the color you picked.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
