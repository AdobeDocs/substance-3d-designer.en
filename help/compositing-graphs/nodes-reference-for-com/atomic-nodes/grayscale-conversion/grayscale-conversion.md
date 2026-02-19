---
title: "Grayscale conversion"
description: "Use the Grayscale Conversion node to convert color textures to grayscale using various conversion methods."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Grayscale conversion
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/grayscale-conversion.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - gradients
  - color
  - colorize
---




# Grayscale conversion

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Grayscale conversion](comp_grayscaleconversion.png "Atomic node: Grayscale conversion"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Converts a color image to grayscale by weighing the luminance of each color channel.

This node may be used as an optimised method to extract a grayscale channel out of a color image, by setting all 'Channel weights' values to 0 except the desired channel, which should be set to 1.

</td>
</tr>
</table>

Most nodes can be set to output in either grayscale or color, where the former is preferred for simplicity and performance reasons.

Indeed, it is recommended to work in grayscale from the outset and colorize images later in your workflow, using for instance a [Gradient map](../gradient-map/gradient-map.md) node.

This means that a grayscale conversion node is generally only reserved for cases where you specifically want to convert a color image to grayscale. In those cases also take a look at [Grayscale conversion advanced](../../node-library/filters/adjustments/grayscale-conversion-adv/grayscale-conversion-advanced.md) and [Color to mask](../../node-library/filters/adjustments/color-to-mask/color-to-mask.md).

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
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Channel weights</b> *Float4* | Sets the weight of each of the RGBA channels in the grayscale conversion.   By default, an even split is done across the RGB channels. |
| <b>Flatten alpha</b> *Boolean* | Sets the behaviour of the Alpha on the final grayscale result, as grayscale values cannot contain Alpha information.   When *True*, the grayscale conversion is multiplied against the input image's Alpha channel |
| <b>Background value</b> *Float* | Sets the base background value when the input has an alpha mask. I.e., determines which pixels are to be treated as transparent.   *Available when 'Flatten alpha' is set to 'True'.* |

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Color* PRIMARY | The color image to be processed. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* |  |

## Examples

*Coming soon.*
