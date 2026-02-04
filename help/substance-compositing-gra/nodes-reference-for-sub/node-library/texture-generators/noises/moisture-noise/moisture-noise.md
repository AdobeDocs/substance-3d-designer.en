---
title: "Moisture noise 1"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Moisture noise 1"
---

# Moisture noise 1

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Moisture noise 1 - Icon](moisture_noise_1.png "Moisture noise 1 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the rich and spongy <b>Moisture</b> noises.  
  
Discs of varying hardness and size and scattered and add or subtract from the color below, starting from a base gray.

See also: [Moisture noise 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/moisture-noise-2/moisture-noise-2.md)

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
| <b>Scale</b>  Integer | The subdivision of the grid used to generate the noise tiles.    A higher value results in more tiles being drawn and a denser noise. |
| <b>Disorder</b>  Float | Displaces the ingredients of the noise.    This can be used to animate the noise. |
| <b>Disorder speed</b>  Float | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the noise. |
| <b>Disorder anisotropy</b>  Float | Controls the span of directions of the displacement applied by the <b>Disorder</b> parameter, where a higher value results in a narrower, more defined direction.    The direction is controlled by the <b>Disorder anisotropy angle</b> parameter. |
| <b>Disorder anisotropy angle</b>  Float | Controls the direction of the displacement applied by the <b>Disorder</b> parameter, when the <b>Disorder anisotropy</b> parameter is not zero. |
| <b>Pattern size</b>  Float2 | A multiplier for the size of a scattered pattern., where 1.0 is its original scaterring size. |
| <b>Pattern angle</b>  Float | The angle used to set the direction of the scattered pattern, in number of turns and starting from horizontal right. |
| <b>Pattern angle random</b>  Float | The maximum amout of random variation applied to the <b>Pattern angle</b> value, in number of turns. |
| <b>Global opacity</b>  Float | The opacity of all ingredients of the noise, where 0.0 results in a base flat gray and 1.0 is the result of the full addition or subtraction applied by the ingredients. |
| <b>Tile offset</b>  Float2 | Controls the position of the portion of infinite plane used to render the noise. |
| <b>Non-square expansion</b>  Boolean | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Moisture noise 1 - Example 1](moisture_noise_1.png "Moisture noise 1 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Moisture noise 1 - Example 2](noise_moisture_noise_1_v2_speed0.6_aniso0.gif "Moisture noise 1 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Moisture noise 1 - Example 3](noise_moisture_noise_1_v2_speed0.6_aniso1.gif "Moisture noise 1 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Moisture noise 1 - Example 4](noise_moisture_noise_1_v2_speed0.3_aniso0.6.gif "Moisture noise 1 - Example 4"){zoomable="yes"}

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
