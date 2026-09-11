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
<td width="33.33%" style="border: 0;" valign="top">

![](bitmap-to-material-light.resources/b2m-light.png)

<b>In:</b> Material Filters &gt; 1-Click

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node converts a single Diffuse/Basecolor input into a full material. As the simple, "light" version of [Allegorithmic's fully fledged Bitmap2Material, which can be purchased separately](https://www.allegorithmic.com/products/bitmap2material), it gives you a bit of a taste of the full version. It can work well for simpler cases.

While not guaranteed to result in perfect, PBR-correct materials, it is a good and quick way to get started if you only have a single image and want a full material.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggles material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Global</b> |  |
| <b>Depth Balance</b> <i>-1.0 - 1.0</i> | Sets a bias/shift for the Heightmap. |
| <b>Diffuse</b> |  |
| <b>Sharpen</b> <i>0.0 - 1.0</i> | Adds sharpening to the diffuse result. |
| <b>Hue</b> <i>0.0 - 1.0</i> | Tints diffuse with a user-selected Hue shift. |
| <b>Saturation</b> <i>0.0 - 1.0</i> | Modifies saturation of Diffuse result. |
| <b>Brightness</b> <i>0.0 - 1.0</i> | Adjusts Diffuse result brightness. |
| <b>Contrast</b> <i>-1.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Relief</b> | The Relief group controls both Normal and Height outputs. |
| <b>Output Normal Format</b> <i>DirectX, OpenGL</i> | Switches between Normal formats (flips green). |
| <b>Invert Generated Relief</b> <i>False/True</i> | Inverts interpretation of height. |
| <b>Normal Strength</b> <i>0.0 - 20.0</i> | Sets strength of generated Normalmap. |
| <b>Relief Equalizer</b> <i>0.0 - 1.0</i> | Sets conversion balances for different detail scales. |
| <b>Pinch Intensity</b> <i>0.0 - 1.0</i> | Makes Normal transitions sharper. Effectively adds a sharpening filter before converting to normal, making the edges more pronounced. |
| <b>Normal Sharpen</b> <i>0.0 - 1.0</i> | Sharpens Normalmap after conversion, brings out the details. |
| <b>Normal Soften</b> <i>0.0 - 1.0</i> | Softens Normalmap after conversion, hides details. |
| <b>Specular</b> |  |
| <b>Specular Diffuse Influence</b> <i>0.0 - 1.0</i> | Sets influence of diffuse on Specular. Affects Glossiness and Roughness outputs as well. |
| <b>Specular Saturation</b> <i>0.0 - 1.0</i> | Changes saturation for Specular output. |
| <b>Specular Sharpen</b> <i>0.0 - 1.0</i> | Sharpens Specular output. |
| <b>Specular Levels In</b> <i>0.0 - 1.0</i> | Sets input levels for Specular interpretation. |
| <b>Specular Levels Out</b> <i>0.0 - 1.0</i> | Modifies output levels of Specular. |
| <b>Metallic Specular Influence</b> <i>0.0 - 1.0</i> | Determines influence of the optional Metallic input on Specular map. |
| <b>Glossiness</b> |  |
| <b>Glossiness Levels In</b> <i>0.0 - 1.0</i> | Sets input levels for Glossiness interpretation. |
| <b>Glossiness Levels Out</b> <i>0.0 - 1.0</i> | Modifies Glossiness output levels. |
| <b>Metallic Glossiness Influence</b> <i>0.0 - 1.0</i> | Determines influence of the optional Metallic input on Glossiness map. |
| <b>Roughness</b> |  |
| <b>Roughness Levels In</b> <i>0.0 - 1.0</i> | Sets input levels for Roughness interpretation. |
| <b>Roughness Levels Out</b> <i>0.0 - 1.0</i> | Modifies Roughness output levels. |
| <b>Metallic Roughness Influence</b> <i>0.0 - 1.0</i> | Determines influence of the optional Metallic input on Glossiness map. |
| <b>Ambient Occlusion</b> |  |
| <b>Ambient Occlusion In Diffuse</b> <i>0.0 - 1.0</i> | Blends in generated AO into Diffuse output. |
| <b>Ambient Occlusion Spread</b> <i>0.0 - 1.0</i> | Sets how far generated AO spreads. |
| <b>Ambient Occlusion Light Distance</b> <i>0.0 - 1.0</i> | Sets AO "depth" interpretation. Has less influence when there is a large Spread. |
| <b>Ambient Occlusion Light Angle</b> <i>0.0 - 1.0</i> | Sets fake lighting AO cast angle. Can be used to compensate for any directional AO already in the Diffuse, if set to an opposite angle. |
| <b>Ambient Occlusion Levels</b> <i>0.0 - 1.0</i> | Modifies AO output levels. |
