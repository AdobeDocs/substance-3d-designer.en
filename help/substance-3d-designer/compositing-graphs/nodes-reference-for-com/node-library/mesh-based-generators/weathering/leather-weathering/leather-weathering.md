---
title: "Leather Weathering | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Leather Weathering"
---

# Leather Weathering

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](leather-weathering.png){width="128px"}

## Leather Weathering

**In:** *Mesh Based Generators**/Weathering*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This is a full-material effect that works on multiple channels at once. It adds a random leather wear effect, with control for age and dirtiness. It is similar to [Fabric Weathering](../fabric-weathering/fabric-weathering.md), but tuned specifically for leather.  
This effect does not work very well unless you have proper baked AO and World Space Normalmaps plugged in, as it requires these to adequately calculate and generate everything.

Make sure to fully understand the [Link Creation Modes](https://support.allegorithmic.com/documentation/display/SD5/Link+Creation+Modes) when working with full materials.

## Parameters

### Inputs

* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Normal Wold Space**: *Color Input*
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
* **Effect**   
  * **Dust**: *0.0 - 1.0*Blends in a darker dust effect, based on areas facing up in the World Space Normalmap.
  * **Dirtiness**: *0.0 - 1.0*Blends in a global dirt/smudge effect, based mostly on areas occluded (dark) in the AO.
  * **Edges Wearing**: *0.0 - 1.0*Adds a sharpening/intensifying effect to edges, based on Material Normal.
  * **Used**: *0.0 - 1.0*Blends in a global worn leather look.
  * **Age**: *0.0 - 1.0*Blends in a worn leather look in creases based on AO. Placement is influenced a lot by Age Treshold.
  * **Age Threshlod**: *0.0 - 1.0*Sets the appearance treshold for the Age effect.
  * **Cracks Scale**: *1.0 - 16.0*Sets the depth of the worn leather from Used and Age effect.
  * **Cracks Warp Intensity**: *0.0 - 1.0*Sets the intensity of the worn leather from Used and Age effect.
  * **Sharp Edges Scratches Scale**: *1.0 - 32.0*
  * **Sharp Edges Scratches Warp Intensity**: *0.0 - 1.0*
  * **Used Leather Desaturation**: *0.0 - 1.0*Sets the saturation of the worn leather look from Age and Used effects.
  * **Used Leather Brightness**: *0.0 - 1.0*Sets the brightness of the worn leather look from Age and Used effects.
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

![](leather-ex.gif)

![](leather-ex2.png){width="233px"}

</td>
</tr>
</table>
