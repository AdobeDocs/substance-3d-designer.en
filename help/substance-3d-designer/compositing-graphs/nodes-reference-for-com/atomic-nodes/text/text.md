---
title: "Text | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Text"
---

# Text

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Text](comp_text.png "Atomic node: Text"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

The Text node provides a way to place-user created text in your graphs. Users can also select settings like Font, Alignment and rotation to customize the text placement.

The Text node is very powerful and the only way to easily place text. It can be a bit tricky to use due to placement always happening on a limited, square canvas, and fonts being driven by a system-defined external list.

</td>
</tr>
</table>

Only Truetype (.ttf) and certain Opentype fonts are supported. If any fonts are missing from the list, this is probably the reason. <b>Fonts can not be exposed as a parameter.</b>

When a Graph using Text is published to sbsar, the font is embedded into the package, just like with bitmaps and other resources, to ensure it works across all systems and applications.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">

<!-- 
 >[!VIDEO](text-tooltip.mp4)
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
| <b>Color mode</b> *Boolean* | Toggles between a grayscale and a color output image. |
| <b>Text</b> *String* | Determines the text description. |
| <b>Font</b> *String* | The font resource used to render the text. |
| <b>Font size</b> *Float* | The font size for the text in points. |
| <b>Alignment</b> *Integer* | Sets the text alignment as left, center (default) or right. |
| <b>Transformation</b> *Float4* | The 2x2 transformation matrix applied to the rendered text. |
| <b>Position</b> *Float2* | The position of the text in the output image. |
| <b>Background</b> *Float/Float4* | The output image's background color. |
| <b>Font color</b> *Float/Float4* | The color of the text. |

## Input connectors

|  |  |
| --- | --- |
| <b>Background</b> *Grayscale/Color* PRIMARY | The output image's background color. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
