---
title: "Dirt gradient | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Dirt gradient"
---

# Dirt gradient

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Dirt gradient - Icon](dirt_gradient.png "Dirt gradient - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the grainy <b>Dirt</b> noises, featuring a directional falloff gradient.

See also: [Dirt 1](../dirt-1/dirt-1.md), [Dirt 2](../dirt-2/dirt-2.md), [Dirt 3](../dirt-3/dirt-3.md), [Dirt 4](../dirt-4/dirt-4.md), [Dirt 5](../dirt-5/dirt-5.md)

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
| <b>Disorder</b>  Float | Displaces the ingredients of the noise.    This can be used to animate the noise. |
| <b>Disorder speed</b>  Float | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the noise. |
| <b>Disorder anisotropy</b>  Float | Controls the span of directions of the displacement applied by the <b>Disorder</b> parameter, where a higher value results in a narrower, more defined direction.    The direction is controlled by the <b>Disorder anisotropy angle</b> parameter. |
| <b>Disorder anisotropy angle</b>  Float | Controls the direction of the displacement applied by the <b>Disorder</b> parameter, when the <b>Disorder anisotropy</b> parameter is not zero. |
| <b>Non-square expansion</b>  Boolean | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Dirt gradient - Example 1](dirt_gradient.png "Dirt gradient - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Dirt gradient - Example 2](noise_dirt_gradient_v2_speed0.6_aniso0.gif "Dirt gradient - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Dirt gradient - Example 3](noise_dirt_gradient_v2_speed0.6_aniso1.gif "Dirt gradient - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Dirt gradient - Example 4](noise_dirt_gradient_v2_speed0.3_aniso0.6.gif "Dirt gradient - Example 4"){zoomable="yes"}

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
