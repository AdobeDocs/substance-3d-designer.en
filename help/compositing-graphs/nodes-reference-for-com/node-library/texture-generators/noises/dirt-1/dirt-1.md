---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/dirt-1.html"
breadcrumb-title: ""
description: Use the Dirt 1 node to generate basic dirt patterns for creating weathered surface details and accumulation effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Dirt 1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Dirt 1
user-guide-description: ""
user-guide-title: ""
---

# Dirt 1

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Dirt 1 - Icon](dirt-1.resources/dirt-1-01.png "Dirt 1 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the grainy <b>Dirt</b> noises.

See also: [Dirt 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/dirt-2/dirt-2.md), [Dirt 3](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/dirt-3/dirt-3.md), [Dirt 4](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/dirt-4/dirt-4.md), [Dirt 5](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/dirt-5/dirt-5.md), [Dirt gradient](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/dirt-gradient/dirt-gradient.md)

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
| <b>Disorder anisotropy angle</b> <i>Float</i> | Controls the direction of the displacement applied by the <b>Disorder</b> parameter, when the <b>Disorder anisotropy</b> parameter is not zero. |
| <b>Tile offset</b> <i>Float2</i> | Controls the position of the portion of infinite plane used to render the noise. |
| <b>Non-square expansion</b> <i>Boolean</i> | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Dirt 1 - Example 1](dirt-1.resources/dirt-1-02.png "Dirt 1 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Dirt 1 - Example 2](dirt-1.resources/dirt-1-03.gif "Dirt 1 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Dirt 1 - Example 3](dirt-1.resources/dirt-1-04.gif "Dirt 1 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Dirt 1 - Example 4](dirt-1.resources/dirt-1-05.gif "Dirt 1 - Example 4"){zoomable="yes"}

</td>
</tr>
</table>
