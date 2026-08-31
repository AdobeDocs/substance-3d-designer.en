---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/messy-fibers-2.html"
breadcrumb-title: ""
description: Use the Messy Fibers 2 node to generate intermediate fiber patterns for creating woven and textile textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Messy fibers 2
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Messy fibers 2
user-guide-description: ""
user-guide-title: ""
---

# Messy fibers 2

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Messy fibers 2 - Icon](messy-fibers-2.resources/messy-fibers-2-01.png "Messy fibers 2 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the <b>Messy fibers</b> structured noises.

See also: [Messy fibers 1](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/messy-fibers-1/messy-fibers-1.md), [Messy fibers 3](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/messy-fibers-3/messy-fibers-3.md)

</td>
</tr>
</table>

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The generated noise as a grayscale bitmap. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Scale</b> <i>Integer</i> | The subdivision of the grid used to generate the noise tiles.    A higher value results in more tiles being drawn and a denser noise. |
| <b>Disorder</b> <i>Float</i> | Displaces the ingredients of the noise.    This can be used to animate the noise. |
| <b>Disorder speed</b> <i>Float</i> | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the noise. |
| <b>Disorder anisotropy</b> <i>Float</i> | Controls the span of directions of the displacement applied by the <b>Disorder</b> parameter, where a higher value results in a narrower, more defined direction.    The direction is controlled by the <b>Disorder anisotropy angle</b> parameter. |
| <b>Disorder anisotropy angle</b> <i>Float</i> | Controls the direction of the displacement applied by the <b>Disorder</b> parameter, when the 'Disorder anisotropy' parameter is not zero. |
| <b>Angle</b> <i>Float</i> | The angle used to set the direction of the threads, in number of turns and starting from horizontal right. |
| <b>Angle random</b> <i>Float</i> | The maximum amout of random variation applied to the <b>Angle</b> value, in number of turns. |
| <b>Lines number</b> <i>Float</i> | The amount of tiling applied to the base threads, where a higher value results in denser, thinner threads. |
| <b>Tile offset</b> <i>Float2</i> | Controls the position of the portion of infinite plane used to render the noise. |
| <b>Non-square expansion</b> <i>Boolean</i> | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Messy fibers 2 - Example 1](messy-fibers-2.resources/messy-fibers-2-02.png "Messy fibers 2 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Messy fibers 2 - Example 2](messy-fibers-2.resources/messy-fibers-2-03.gif "Messy fibers 2 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Messy fibers 2 - Example 3](messy-fibers-2.resources/messy-fibers-2-04.gif "Messy fibers 2 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Messy fibers 2 - Example 4](messy-fibers-2.resources/messy-fibers-2-05.gif "Messy fibers 2 - Example 4"){zoomable="yes"}

</td>
</tr>
</table>
