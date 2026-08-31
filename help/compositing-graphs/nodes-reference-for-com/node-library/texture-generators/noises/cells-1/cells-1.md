---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/cells-1.html"
breadcrumb-title: ""
description: Use the Cells 1 node to generate basic cellular patterns for creating organic and biological texture effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Cells 1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Cells 1
user-guide-description: ""
user-guide-title: ""
---

# Cells 1

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Cells 1 - Icon](cells-1.resources/cells-1-01.png "Cells 1 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the <b>Cells</b> walled noises.  
  
User-selected patterns are scattered and overlaid using a Max blending mode.

See also: [Cells 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/cells-2/cells-2.md), [Cells 3](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/cells-3/cells-3.md), [Cells 4](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/cells-4/cells-4.md)

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
| <b>Pattern</b> <i>Integer</i> | The base shape scattered in the generated image. |
| <b>Pattern size</b> <i>Float2</i> | A multiplier for the size of a scattered pattern in its cell., where 1.0 is the full span of the cell. |
| <b>Pattern scale</b> <i>Float</i> | A multiplier for the <b>Pattern size</b>, where 1.0 is the full size. |
| <b>Luminance random</b> <i>Float</i> | The range of luminance randomly subtracted from the cells, where 1 is the full range. |
| <b>Angle</b> <i>Float</i> | The angle used to set the direction of the cells, in number of turns and starting from horizontal right. |
| <b>Angle random</b> <i>Float</i> | The maximum amout of random variation applied to the <b>Angle</b> value, in number of turns. |
| <b>Tile offset</b> <i>Float2</i> | Controls the position of the portion of infinite plane used to render the noise. |
| <b>Non-square expansion</b> <i>Boolean</i> | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Cells 1 - Example 1](cells-1.resources/cells-1-02.png "Cells 1 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Cells 1 - Example 2](cells-1.resources/cells-1-03.gif "Cells 1 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Cells 1 - Example 3](cells-1.resources/cells-1-04.gif "Cells 1 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Cells 1 - Example 4](cells-1.resources/cells-1-05.gif "Cells 1 - Example 4"){zoomable="yes"}

</td>
</tr>
</table>
