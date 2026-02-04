---
title: "Season Filter | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Effects (Material) > Season Filter"
---

# Season Filter

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](default-icon.png){width="128px"}

## Season Filter

**In:** *Material Filters/Effects*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This node adds effects such as an animated water level, snow, ice and/or moss.

Keep in mind that this is an older filter that is not intended to be fully PBR-correct. It is mostly kept for legacy/compatibility reasons, although it can still be useful in some cases. More recent PBR-correct versions can be found in [Snow Cover](../snow-cover/snow-cover.md) and [Water Level](../water-level/water-level.md).

The node requires a proper set of material inputs, mainly with a decently detailed Heightmap or Normalmap.

## Parameters

### Inputs

* **Mask** : *Grayscale Input*   
  Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter.

### Parameters

* **Channels**   
  * Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.
* **Advanced**   
  * **Normal Format**: *DirectX, OpenGL*  
    Switches between different Normalmap formats (inverts the green channel).
  * **Mask**: *False/True*  
    Toggles the use of the Mask map on or off.
  * **Light Intensity**: *0.0 - 1.0*  
    Intensity of the (faked) light.
  * **Light Angle**: *0.0 - 1.0*  
    Incidence angle of the (faked) light
* **Effect**   
  * **Effect From Height or Normal**: *Height, Normal*Chooses which input map drives the effects.
  * **Water Level**: *0.0 - 1.0*Raises or lowers the water level based on Height/Normal info.
  * **Water Details**: *0.0 - 1.0*Sets amount of details in the water.
  * **Refraction**: *0.0 - 1.0*Sets amount of fake refraction in the effect.
  * **Reflection**: *0.0 - 1.0*Sets amount of fake reflection in the effect.
  * **Reflection Distance**: *0.0 - 1.0*Controls reflection visuals.
  * **Reflection Angle**: *0.0 - 1.0*Controls reflection visuals.
  * **Flow Direction**: *0.0 - 1.0*Controls animation flow (use Substance Player to visualise).
  * **Ice**: *0.0 - 1.0*Sets how frozen the water is.
  * **Ice Details**: *0.0 - 1.0*Sets amount of details in the ice.
  * **Snow**: *0.0 - 1.0*Sets amount of snow coverage.
  * **Moss**: *0.0 - 1.0*Sets amount of moss coverage.
  * **Moss Scale**: *1 - 4*Sets scale of generated moss texture.
  * **Moss Color**: *(Color value)*Sets color of moss.
  * **Water Color**: *(Color value)*Sets color of water, including alpha/opacity.
* **Blending**   
  * **Diffuse Intensity**: *0.0 - 1.0*  
    Blending strength of the Diffuse.
  * **Base Color Intensity**: *0.0 - 1.0*  
    Blending strength of the Base Color.
  * **Normal Intensity**: *0.0 - 1.0*  
    Blending strength of the Normal.
  * **Specular Intensity**: *0.0 - 1.0*  
    Blending strength of the Specular.
  * **Glossiness Intensity**: *0.0 - 1.0*  
    Blending strength of the Glossiness.
  * **Roughness Intensity**: *0.0 - 1.0*  
    Blending strength of the Roughness.
  * **Ambient Occlusion Intensity**: *0.0 - 1.0*  
    Blending strength of the Ambient Occlusion.
  * **Height Intensity**: *0.0 - 1.0*  
    Blending strength of the Height.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>

 