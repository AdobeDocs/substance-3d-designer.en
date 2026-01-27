---
title: "Directional warp | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Directional warp"
---

# Directional warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Directional warp](comp_directionalwarp.png "Atomic node: Directional warp"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Displaces pixels in a specified direction according to an intensity map, which can result in deformation.

Warps an input in a user-set direction, multiplied by a user-set Intensity map. It works similar to Warp, but then only in a specific direction.

</td>
</tr>
</table>

The Warp node is a fairly simple but useful node that serves as a good basis for other more advanced effects. There are more advanced alternatives such as other related nodes of interest are [Slope Blur](../../node-library/filters/blurs/slope-blur/slope-blur.md) and [Vector Warp](../../node-library/filters/effects/vector-warp/vector-warp.md).

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">

<!-- 
 >[!VIDEO](directional-warp-tooltip.mp4)
 -->

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
| <b>Warp angle</b> *Float* | Sets the angle of the warp effect, in number of turns.. |
| <b>Input filtering mode</b> *Boolean* | Controls whether nearest or bilinear filtering is used to sample the <b>Input</b>. |
| <b>Intensity map offset</b> *Float* | This value is subtracted from the the <b>Intensity input</b> image values. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale/Color* PRIMARY | The grayscale or color input image on which the warping effect should be applied. |
| <b>Intensity input</b> *Grayscale* | The grayscale image defining the amount of warping that should be applied to the <b>Input</b> image. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Directional Warp - Example 1](dir-warp.gif "Directional Warp - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Directional Warp - Example 2](dir-warp02.gif "Directional Warp - Example 2"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Directional Warp - Example 3](dir-warp03.gif "Directional Warp - Example 3"){zoomable="yes"}

</td>
</tr>
</table>
