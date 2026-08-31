---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/gaussian-spots-2.html"
breadcrumb-title: ""
description: Use the Gaussian Spots 2 node to generate advanced Gaussian spot patterns for creating organic texture variations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Gaussian spots 2
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Gaussian spots 2
user-guide-description: ""
user-guide-title: ""
---

# Gaussian spots 2

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Gaussian spots 2 - Icon](gaussian-spots-2.resources/gaussian-spots-2-01.png "Gaussian spots 2 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A variation of the smooth <b>Gaussian spots</b> noises.  
Based on the [Gaussian noise](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/gaussian-noise/gaussian-noise.md) node, with narrower gradients and higher frequencies.

See also: [Gaussian spots 1](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/gaussian-spots-1/gaussian-spots-1.md)

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

![Gaussian spots 2 - Example 1](gaussian-spots-2.resources/gaussian-spots-2-02.png "Gaussian spots 2 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Gaussian spots 2 - Example 2](gaussian-spots-2.resources/gaussian-spots-2-03.gif "Gaussian spots 2 - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Gaussian spots 2 - Example 3](gaussian-spots-2.resources/gaussian-spots-2-04.gif "Gaussian spots 2 - Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Gaussian spots 2 - Example 4](gaussian-spots-2.resources/gaussian-spots-2-05.gif "Gaussian spots 2 - Example 4"){zoomable="yes"}

</td>
</tr>
</table>
