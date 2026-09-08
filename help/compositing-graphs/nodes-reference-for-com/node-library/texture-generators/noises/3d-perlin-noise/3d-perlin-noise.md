---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/3d-perlin-noise.html"
breadcrumb-title: ""
description: Use the 3D Perlin Noise node to generate smooth Perlin noise patterns in 3D space for creating natural-looking volumetric textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Perlin Noise
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Perlin Noise
user-guide-description: ""
user-guide-title: ""
---

# 3D Perlin Noise

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](../../../../../../assets/3dperlinnoise.png){width="200px"}

**In:** *Texture Generators**/Noises*

**Intermediate**

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The **3D Perlin Noise** node generates a Perlin noise in 3D space based on the **Position Map** input.

This node can be tested with [Cube 3D GBuffers](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d-gbuffers/cube-3d-gbuffers.md) as input instead of an actual baked map (as seen in the Example Image below).

>[!WARNING]
>
> This noise is meant to be used with the *GPU engine only* (i.e., **Direct3D** or **OpenGL**). Go to **Tools &gt; Switch engine...** or press the **F9** key to select the desired engine.

</td>
</tr>
</table>

## Parameters

* **Invert** *Boolean*  
  Inverts the output image.
* **Scale** *Float*  
  Controls the scale of the 3D Perlin noise.
* **Size** *Float3*  
  Controls the size of the 3D Perlin noise in the **X**, **Y** and **Z** axes. Non-uniform values result in a *stretching or squashing* effect.
* **Offset** *Float3*  
  Applies an offset to the *position* of the 3D Perlin noise in the **X**, **Y** and **Z** axes.
* **Distortion Intensity** *Float*  
  Controls the intensity of a *warping effect* applied on the 3D Perlin noise.
* **Distortion Scale Multiplier** *Float*  
  Controls the scale of the *deforming pattern* used in the warping effect controlled by the **Distortion Intensity**.
* **Baseline** *Float*  
  Applies an *offset* to the baseline *luminance* value for the 3D Perlin noise value distribution.
* **Contrast** *Float*  
  Adjusts the contrast of the 3D Perlin noise.
* **Absolute** *Boolean*  
  Uses absolute values in the 3D Perlin noise. This effectively *inverts* the value distribution for values *below 0.5*.
* **Enable Tiling** *Boolean*  
  Adjusts the 3D Perlin noise so its resulting pattern *repeats* in the X, Y and Z axes.

## Example Images

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/3dperlin.gif){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](../../../../../../assets/3dperlinnoise-variant2.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](../../../../../../assets/3dperlinnoise-variant.jpg){width="256px"}

</td>
</tr>
</table>
