---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/directional-noise-3.html"
breadcrumb-title: ""
description: Use the Directional Noise 3 node to generate directional noise patterns with three octaves for creating directional textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Directional noise 3
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Directional noise 3
user-guide-description: ""
user-guide-title: ""
---



# Directional noise 3

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Directional noise 3 - Icon](directional_noise_3.png "Directional noise 3 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the <b>Directional noise</b> noises.

See also: [Directional noise 1](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/directional-noise-1/directional-noise-1.md), [Directional noise 2](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/directional-noise-2/directional-noise-2.md), [Directional noise 4](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/directional-noise-4/directional-noise-4.md)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Outputs

</td>
<td style="border: 0;" valign="top">

### Parameters

</td>
<td style="border: 0;" valign="top">

### Examples

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
| <b>Scale</b>  Integer | The subdivision of the grid used to generate the noise tiles.    A higher value results in more tiles being drawn and a denser noise. |
| <b>Disorder</b>  Float | Displaces the ingredients of the noise.    This can be used to animate the noise. |
| <b>Disorder speed</b>  Float | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the noise. |
| <b>Disorder anisotropy</b>  Float | Controls the span of directions of the displacement applied by the <b>Disorder</b> parameter, where a higher value results in a narrower, more defined direction.    The direction is controlled by the <b>Disorder anisotropy angle</b> parameter. |
| <b>Disorder anisotropy angle</b>  Float | Controls the direction of the displacement applied by the <b>Disorder</b> parameter, when the 'Disorder anisotropy' parameter is not zero. |
| <b>Angle</b>  Float | The angle used to set the direction of the noise, in number of turns and starting from horizontal right. |
| <b>Angle random</b>  Float | The maximum amout of random variation applied to the <b>Angle</b> value, in number of turns. |
| <b>Tile offset</b>  Float2 | Controls the position of the portion of infinite plane used to render the noise. |
| <b>Non-square expansion</b>  Boolean | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Directional noise 3 - Example 1](directional_noise_3.png "Directional noise 3 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Directional noise 3 - Example 2](noise_directional_noise_3_v2_speed0.6_aniso0.gif "Directional noise 3 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Directional noise 3 - Example 3](noise_directional_noise_3_v2_speed0.6_aniso1.gif "Directional noise 3 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Directional noise 3 - Example 4](noise_directional_noise_3_v2_speed0.3_aniso0.6.gif "Directional noise 3 - Example 4"){zoomable="yes"}

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
