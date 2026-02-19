---
title: "Anisotropic noise"
description: "Use the Anisotropic Noise node to generate directional noise patterns for creating anisotropic texture effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Anisotropic noise
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/anisotropic-noise.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - photography
helpx_experience_level:
  - intermediate
helpx_learn_topic:
  - asset-warp
  - normal-maps
  - effects
---




# Anisotropic noise

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Anisotropic noise - Icon](anisotropic_noise_v2.png "Anisotropic noise - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A horizontal or vertical stack of randomly colored strips fading into one another.  
  
The amount of strips is adjustable, as is the smoothness of their transitions.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Outputs

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* | The generated noise as a grayscale bitmap. |

## Parameters

|  |  |
| --- | --- |
| <b>X amount</b>  Integer | The amount of strips on the X axis. |
| <b>Y amount</b>  Integer | The amount of strips on the Y axis. |
| <b>Y amount by resolution</b>  Boolean | If True, the number of strips on the Y axis will be equal to the image size on that axis. |
| <b>Rotate</b>  Boolean | Rotates the noise 90 degrees. |
| <b>Smoothness</b>  Float | The amount of fading between the strips, where 0 is no fading and 1 is fading over their entire length. |
| <b>Smoothness interpolation</b>  Float | The weighting of the two methods of interpolation applied to fade the strips, where 0 is linear and 1 is Gaussian. |
| <b>Disorder</b>  Float | Displaces the ingredients of the noise.   This can be used to animate the noise. |
| <b>Disorder speed</b>  Float | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.   This can be used to control the speed of displacement when animating the noise. |
| <b>Non-square expansion</b>  Boolean | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Anisotropic noise - Example 1](anisotropic_noise_v2.png "Anisotropic noise - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Anisotropic noise - Example 2](noise_anisotropic_noise_v2_speed0.3_aniso0.6.gif "Anisotropic noise - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
