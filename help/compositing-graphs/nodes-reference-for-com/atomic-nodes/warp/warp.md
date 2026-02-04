---
title: "Warp | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Warp"
---

# Warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Warp](comp_warp.png "Atomic node: Warp"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Displaces the pixel values in the input image according to the slopes computed from a separate gradient input, resulting in deformation.

Unlike the Directional Warp this node pushes away uniformly from white areas, in a direction defined by the slope or gradient of the Gradient Input.

</td>
</tr>
</table>

The node can be a little tricky to work with, as the result of the effect is very heavily dependent on the Gradient Input: small tweaks to the Gradient can make a huge visual difference with the same Intensity values. Make sure to play around with Contrast, Luminance and scale of the Gradient Input, as well as the Intensity slider on this node.

If you are familiar with Normal maps, you can imagine the workings of this node to be similar to converting the Gradient Input to a [Normal map](../normal/normal.md), and then distorting the Base Input in the direction defined by the Normal map vectors. In fact, this same thing can be achieved with the [Vector Warp](../../node-library/filters/effects/vector-warp/vector-warp.md). Similar effects can also be found in [Slope Blur](../../node-library/filters/blurs/slope-blur/slope-blur.md).

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">



</td>
<td width="100.00%" style="border: 0;" valign="top">



</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Intensity</b> *Float* | Sets the intensity of the warp. |
| <b>Input filtering mode</b> *Boolean* | Controls whether nearest or bilinear filtering is used to sample the Input. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale/Color* PRIMARY | The color or grayscale image. |
| <b>Gradient input</b> *Grayscale* | The slope of the gradient of the grayscale input image determines the warp effect in the output image. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*

 