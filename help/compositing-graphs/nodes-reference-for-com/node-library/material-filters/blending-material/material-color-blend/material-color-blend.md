---
title: "Material Color Blend | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Material Color Blend"
---

# Material Color Blend

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](material-color-blend.png){width="128px"}

## Material Color Blend

**In:** *Material Filters/Blending*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

This node allows for adjustments to a Multi Channel, Full Material by blending solid colors on top. This is the main difference with [Material Adjustment Blend](../material-adjustment-blend/material-adjustment-blend.md), which only allows for [Levels](../../../../atomic-nodes/levels/levels.md)-type adjustments to channels, whereas this node uses [Blend](../../../../atomic-nodes/blend/blend.md)-type adjustments with a solid color.

This node is most useful when you want to either introduce a flat color hint into Diffuse or Base Color, or went you want to "flatten" out other channels by using a set, solid color value.

## Parameters

### Inputs

* **ColorID**: *Color Input*   
  Mask slot used for masking the node's effects.
* **Greyscale Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Channels**   
  * Toggle material channels on and off in this group, when using Specular/Glossiness maps instead of Metallic/Roughness for example.
* **Diffuse**   
  * **Color**: *(Color value)*Which color value to blend on top of the Diffuse Channel.
  * **Opacity**: *0.0 - 1.0*  
    Blending Opacity between Foreground and Background.
  * **Blending Mode**: *Normal, Add, Subtract, Multiply, Add/Sub, Max, Min, Switch*Blend mode to use in the operation.
* **Base Color**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Normal**   
  * **Source**: *Height, Mask*
  * **Blending Mode**: *Combine, Blend*
  * **Height Intensity**: *0.0 - 1.0*
  * **Height Opacity**: *0.0 - 1.0*
  * **Format**: *DirectX, OpenGL*
* **Specular**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Emissive**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Glossiness**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Roughness**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Metallic**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Specular Level**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Ambient Occlusion**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Height**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Opacity**   
  * Blends a solid color on top of this channel with options as in the Diffuse group.
* **Color ID Mask**: *False/True*Use Color ID mask instead of grayscale mask. Keep in mind that this is only for one color!  
  Enables all the below options.
* **Color**: *(Color value)*Which color to pick and convert to white.
* **Fuzziness**: *0.01 - 1.0*The extent to which the colour you picked blends over into its neighbours.
* **Padding**: *0.0 - 1.0*Transition contrast of the color you picked.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>

 