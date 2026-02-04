---
title: "Directional blur"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Directional blur"
---

# Directional blur

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Directional blur](comp_dirmotionblur.png "Atomic node: Directional blur"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Applies blurring in a specified direction according to an intensity map.

This node performs an operation similar to a motion blur on an input. Unlike the regular '[Blur](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blur/blur.md)' node, which blurs equally in all directions, 'Directional blur' works along a user-defined angle.

</td>
</tr>
</table>

Similarly to 'Blur', it is also a faster and low-quality operation. An extended, higher-quality alternative is provided in [Anisotropic Blur](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blurs/anisotropic-blur/anisotropic-blur.md), with a performande trade-off

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

+++Directional blur and Anisotropic blur


This images below show the Directional blur and theAnisotropic blurin effect on the same input shape, with similar parameters. Anisotropic Blur has been set to full anisotropy and high quality.



[Anisotropic blur](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blurs/anisotropic-blur/anisotropic-blur.md)



Directional blur







Anisotropic blur





+++

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
| <b>Intensity</b> *Float* | Sets the blurring radius in pixels. |
| <b>Angle</b> *Float* | The direction of the blur effect in number of turns clockwise, starting from horizontal – I.e., direction vector (1, 0). |

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale/Color* [PRIMARY](../../../../glossary/glossary.md) | The image to be processed. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
