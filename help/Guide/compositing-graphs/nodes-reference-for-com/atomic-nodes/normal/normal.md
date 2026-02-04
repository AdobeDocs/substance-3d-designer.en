---
title: "Normal | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Normal"
---

# Normal

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Normal](comp_normal.png "Atomic node: Normal"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Computes a normal map from a grayscale image interpreted as a height map.

The node converts an input grayscale map to a tangent-space Normal map output. It has a few user options to set intensity and encoding.

</td>
</tr>
</table>

It is a very useful node that is used often to convert height map inputs to normal maps for realtime-ready materials. There are alternatives to be found in [Normal Sobel](../../node-library/filters/normal-map/normal-sobel/normal-sobel.md) and Height To Normal World Units.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">

<!-- 
 >[!VIDEO](normal-tooltip.mp4)
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
| <b>Intensity</b> *Float* | Modifies the intensity of height map.   Sets how intense the input height map is interpreted for converting to normals. Depending on input maps, values above 100 have little more effect. |
| <b>Normal format</b> *Boolean* | Inverts the Y coordinates of the height map (OpenGL).   Sets how the Green (Y) channel is encoded. Basically a "Flip Green/Y" switch. |
| <b>Alpha channel content</b> *Boolean* | Fill the normal map's alpha channel with the input texture.   Fill Alpha With Input/Force Alpha To 1:  This allows for the Alpha channel to be set to solid, instead of using the Input as an additional Alpha. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale* PRIMARY | Input image interpreted as a height map. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Color* |  |

## Examples

*Coming soon.*
