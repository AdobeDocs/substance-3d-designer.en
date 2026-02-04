---
title: "Rock Weathering | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Rock Weathering"
---

# Rock Weathering

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](rock-weathering.png){width="128px"}

## Rock Weathering

**In:** *Mesh Based Generators**/Weathering*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

## Parameters

### Inputs

* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Curvature**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Normal WS**: *Color Input*   
  Baked World Space Normalmap used for internal effects and masking.
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
  * **Dust**: *0.0 - 1.0*
  * **Dirtiness**: *0.0 - 1.0*
  * **Edges Wearing**: *0.0 - 1.0*
  * **Used Rock**: *0.0 - 1.0*
  * **Cracks Scale**: *1.0 - 60.0*
  * **Cracks Intensity**: *0.0 - 1.0*
  * **Age**: *0.0 - 1.0*
  * **Age Threshlod**: *0.0 - 1.0*
  * **Sharp Edges Scratches Scale**: *1.0 - 32.0*
  * **Sharp Edges Scratches Warp Intensity**: *0.0 - 1.0*
  * **Used Rock Desaturation**: *0.0 - 1.0*
  * **Used Rock Brightness**: *0.0 - 1.0*
* **Blending**   
  * **Diffuse Intensity**: *0.0 - 1.0*  
    Blending strength of the Diffuse.
  * **Base Color Intensity**: *0.0 - 1.0*  
    Blending strength of the Base Color.
  * **Normal Intensity**: *0.0 - 64.0*  
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

![](rock-ex.gif)

</td>
</tr>
</table>
