---
title: "Uniform color | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Uniform color"
---

# Uniform color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Uniform color](comp_uniform.png "Atomic node: Uniform color"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Generates a flat grayscale or color value.

It is a simple node that is used very often as a starting point for adding colors or creating specific values.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">

<!-- 
 >[!VIDEO](uniform-color-tooltip.mp4)
 -->

</td>
<td width="100.00%" style="border: 0;" valign="top">



</td>
</tr>
</table>

>[!TIP]
>
> Performance optimization
> 
> Both of these adjustments lowers the node's computation time and memory footprint:
> 
> * If a grayscale value is needed, make sure to switch the node's to 'Grayscale'.
> * Since the node's output is a flat color, you may use the lowest resolution possible. Set the node's '[Output size](../../../output-size/output-size.md)' parameter to use the 'Absolute' [inheritance method](../../../inheritance-compositing/inheritance-in-substance-compositing-graphs.md) and a resolution of 16x16 pixels.

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
| <b>Color mode</b> *Boolean* | Toggles between a grayscale and a color output image. |
| <b>Output color</b> *Float/Float4* | Selects the flat color to use in the output image.   When using the 'Color' color mode, the Alpha channel is used for opacity where 0 is fully transparent and 1 is fully opaque.. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Color/Grayscale* |  |

## Examples

*Coming soon.*
