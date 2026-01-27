---
title: "Blend | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Blend"
---

# Blend

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Blend](comp_blend.png "Atomic node: Blend"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Combines two images using a specified blending mode and an optional mask.

It is the most useful node of all Atomic nodes, almost any Graph you build in [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) will make use of this node.

</td>
</tr>
</table>

Its functionality is similar to having two layers above one another in [Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html) or [Photoshop](https://www.adobe.com/ch_fr/products/photoshop/landpa.html), that blend together by the blending mode you set on the top layer.

>[!TIP]
>
> Learn about the blending modes available in the Blend node in [this dedicated page](blending-modes-des/blending-modes-description.md).

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">

<!-- 
 >[!VIDEO](blend-tooltip.mp4)
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
| <b>Opacity</b> *Float* | Opacity of the Foreground layer blending into the Background. It works independent to the Opacity input and acts as an additional multiplier to it. |
| <b>Blending mode</b> *Integer* [Static](../../../../glossary/glossary.md) | Sets the blending operation to be used.   See the [dedicated page about blending modes](blending-modes-des/blending-modes-description.md). |
| <b>Alpha blending</b> *Integer* [Static](../../../../glossary/glossary.md) | Determines blending behavior when color inputs have Alpha channels:<ul data-preserve-html="true"> <li data-preserve-html="true">Use source alpha</li> <li data-preserve-html="true">Ignore alpha</li> <li data-preserve-html="true">Straight alpha blending</li> <li data-preserve-html="true">Premultiplied alpha blending</li> </ul> |
| <b>Cropping area</b> *Float4* [Static](../../../../glossary/glossary.md) | Allow for setting a custom cropping region that behaves like an additional Opacity mask. Any area cropped shows only the background. |

## Input connectors

|  |  |
| --- | --- |
| <b>Foreground</b> *Grayscale/Color* | Top or foreground layer of the Blend operation. |
| <b>Background</b> *Grayscale/Color* PRIMARY | Bottom or background layer of the blend operation. |
| <b>Opacity</b> *Grayscale* | Optional Alpha mask input. |

>[!IMPORTANT]
>
> Blend nodes have dynamic inputs that switch between Grayscale and Color depending on your connections.<b> A Blend Node can only blend two inputs of the same type</b>.
> 
> Connecting a Color and Grayscale input to the Foreground and Background will result in a dashed red connection line, signifying a calculation error.
> 
> This is the number one reason new users run into problems with Color vs Grayscale connections: make sure both connections are of the same type!

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
