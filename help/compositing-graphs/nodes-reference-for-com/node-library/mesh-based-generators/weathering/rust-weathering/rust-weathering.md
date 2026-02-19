---
title: "Rust Weathering"
description: "Use the Rust Weathering node to generate rust patterns based on mesh geometry for creating realistic metal corrosion effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Rust Weathering
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/weathering/rust-weathering.html"
helpx_creative_field:
  - painting-illustration
  - video
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - materials
  - reflections
  - metal
---




# Rust Weathering

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](rust-weathering.png){width="128px"}

## Rust Weathering

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
* **Position**: *Color Input*
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
  * **Rust Spreading**: *0.0 - 1.0*
  * **Spreading Smoothness**: *0.0 - 1.0*
  * **Vernish Damage Scale**: *0.0 - 1.0*
  * **Drips Intensity**: *0.0 - 1.0*
  * **Drips Samples Amount**: *0 - 32*
  * **Drips Smoothness**: *0.0 - 1.0*
* **Blending**   
  * **Diffuse Intensity**: *0.0 - 1.0*  
    Blending strength of the Diffuse.
  * **Base Color Intensity**: *0.0 - 1.0*  
    Blending strength of the Base Color.
  * **Normal Intensity**: *0.0 - 32.0*  
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

![](rust-ex.gif)

</td>
</tr>
</table>
