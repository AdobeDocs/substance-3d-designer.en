---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/1-click/bitmap-to-material-light.html"
breadcrumb-title: ""
description: Use the Bitmap to Material Light node to quickly convert bitmap images into materials with optimized lighting for fast workflows.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > 1-Click > Bitmap to Material Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Bitmap to Material Light
user-guide-description: ""
user-guide-title: ""
---

# Bitmap to Material Light

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/b2m-light.png)

## Bitmap to Material Light

**In:** *Material Filters/1-Click*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

This node converts a single Diffuse/Basecolor input into a full material. As the simple, "light" version of [Allegorithmic's fully fledged Bitmap2Material, which can be purchased separately](https://www.allegorithmic.com/products/bitmap2material), it gives you a bit of a taste of the full version. It can work well for simpler cases.

While not guaranteed to result in perfect, PBR-correct materials, it is a good and quick way to get started if you only have a single image and want a full material.

## Parameters

* **Channels**   
  * Toggles material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.
* **Global**   
  * **Depth Balance**: *-1.0 - 1.0*Sets a bias/shift for the Heightmap.
* **Diffuse**   
  * **Sharpen**: *0.0 - 1.0*Adds sharpening to the diffuse result.
  * **Hue**: *0.0 - 1.0*Tints diffuse with a user-selected Hue shift.
  * **Saturation**: *0.0 - 1.0*Modifies saturation of Diffuse result.
  * **Brightness**: *0.0 - 1.0*Adjusts Diffuse result brightness.
  * **Contrast**: *-1.0 - 1.0*  
    Adjusts the contrast of the result.
* **Relief**   
  The Relief group controls both Normal and Height outputs.  
  * **Output Normal Format**: *DirectX, OpenGL*Switches between Normal formats (flips green).
  * **Invert Generated Relief**: *False/True*Inverts interpretation of height.
  * **Normal Strength**: *0.0 - 20.0*Sets strength of generated Normalmap.
  * **Relief Equalizer**: *0.0 - 1.0*Sets conversion balances for different detail scales.
  * **Pinch Intensity**: *0.0 - 1.0*Makes Normal transitions sharper. Effectively adds a sharpening filter before converting to normal, making the edges more pronounced.
  * **Normal Sharpen**: *0.0 - 1.0*Sharpens Normalmap after conversion, brings out the details.
  * **Normal Soften**: *0.0 - 1.0*Softens Normalmap after conversion, hides details.
* **Specular**   
  * **Specular Diffuse Influence**: *0.0 - 1.0*Sets influence of diffuse on Specular. Affects Glossiness and Roughness outputs as well.
  * **Specular Saturation**: *0.0 - 1.0*Changes saturation for Specular output.
  * **Specular Sharpen**: *0.0 - 1.0*Sharpens Specular output.
  * **Specular Levels In**: *0.0 - 1.0*Sets input levels for Specular interpretation.
  * **Specular Levels Out**: *0.0 - 1.0*Modifies output levels of Specular.
  * **Metallic Specular Influence**: *0.0 - 1.0*Determines influence of the optional Metallic input on Specular map.
* **Glossiness**   
  * **Glossiness Levels In**: *0.0 - 1.0*Sets input levels for Glossiness interpretation.
  * **Glossiness Levels Out**: *0.0 - 1.0*Modifies Glossiness output levels.
  * **Metallic Glossiness Influence**: *0.0 - 1.0*Determines influence of the optional Metallic input on Glossiness map.
* **Roughness**   
  * **Roughness Levels In**: *0.0 - 1.0*Sets input levels for Roughness interpretation.
  * **Roughness Levels Out**: *0.0 - 1.0*Modifies Roughness output levels.
  * **Metallic Roughness Influence**: *0.0 - 1.0*Determines influence of the optional Metallic input on Glossiness map.
* **Ambient Occlusion**   
  * **Ambient Occlusion In Diffuse**: *0.0 - 1.0*Blends in generated AO into Diffuse output.
  * **Ambient Occlusion Spread**: *0.0 - 1.0*Sets how far generated AO spreads.
  * **Ambient Occlusion Light Distance**: *0.0 - 1.0*Sets AO "depth" interpretation. Has less influence when there is a large Spread.
  * **Ambient Occlusion Light Angle**: *0.0 - 1.0*Sets fake lighting AO cast angle. Can be used to compensate for any directional AO already in the Diffuse, if set to an opposite angle.
  * **Ambient Occlusion Levels**: *0.0 - 1.0*Modifies AO output levels.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
