---
title: "Metal Weathering | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Metal Weathering"
---

# Metal Weathering

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](metal-weathering.png){width="128px"}

## Metal Weathering

**In:** *Mesh Based Generators**/Weathering*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

## Parameters

### Inputs

* **Normal WS**: *Color Input*   
  Baked World Space Normalmap used for internal effects and masking.
* **Ambient Occlusion**: *Grayscale Input*   
  Baked map used for internal effects and masking.
* **Mask** : *Grayscale Input*   
  Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter.

### Parameters

* **Channels**   
  * Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.
* **Advanced**   
  * **Normal Format**: *Direct X, Open GL*  
    Switches between different Normalmap formats (inverts the green channel).
  * **Mask**: *False/True*  
    Toggles the use of the Mask map on or off.
* **Effect**   
  * **Dust**: *0.0 - 1.0*
  * **Dirtiness**: *0.0 - 1.0*
  * **Edges Wearing**: *0.0 - 1.0*
  * **Paint Peeling**: *0.0 - 1.0*
  * **Rust**: *0.0 - 1.0*
  * **Rust Peeling**: *0.0 - 1.0*
  * **Rust Verdigris**: *Rust, Verdigris*
  * **Paint Cracks Scale**: *1.0 - 16.0*
  * **Paint Cracks Warp Intensity**: *0.0 - 1.0*
  * **Sharp Edges Scratches Scale**: *1.0 - 32.0*
  * **Sharp Edges Scratches Warp Intensity**: *0.0 - 1.0*
  * **Raw Metal Color**: *(Color value)*
  * **Raw Metal Specular Color**: *(Color value)*
  * **Raw Metal Glossiness Value**: *(Grayscale value)*
  * **Raw Metal Roughness Value**: *(Grayscale value)*
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
  * **Metallic Intensity**: *0.0 - 1.0*  
    Blending strength of the Metallic.
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
