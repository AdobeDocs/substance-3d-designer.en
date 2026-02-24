---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/messy-fibers-3.html"
breadcrumb-title: ""
description: Use the Messy Fibers 3 node to generate complex fiber patterns for creating fabric and textile texture effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Messy fibers 3
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Messy fibers 3
user-guide-description: ""
user-guide-title: ""
---


# Messy fibers 3

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Messy fibers 3 - Icon](messy_fibers_3.png "Messy fibers 3 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the <b>Messy fibers</b> structured noises.

See also: [Messy fibers 1](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/messy-fibers-1/messy-fibers-1.md), [Messy fibers 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/messy-fibers-2/messy-fibers-2.md)

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
| <b>Angle</b>  Float | The angle used to set the direction of the threads, in number of turns and starting from horizontal right. |
| <b>Angle random</b>  Float | The maximum amout of random variation applied to the <b>Angle</b> value, in number of turns. |
| <b>Luminance random</b>  Float | The range of luminance randomly subtracted from the threads, where 1 is the full range. |
| <b>Tile offset</b>  Float2 | Controls the position of the portion of infinite plane used to render the noise. |
| <b>Non-square expansion</b>  Boolean | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Messy fibers 3 - Example 1](messy_fibers_3.png "Messy fibers 3 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Messy fibers 3 - Example 2](noise_messy_fibers_3_v2_speed0.1_aniso0.gif "Messy fibers 3 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Messy fibers 3 - Example 3](noise_messy_fibers_3_v2_speed0.1_aniso1.gif "Messy fibers 3 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Messy fibers 3 - Example 4](noise_messy_fibers_3_v2_speed0.1_aniso0.6.gif "Messy fibers 3 - Example 4"){zoomable="yes"}

</td>
</tr>
</table>
