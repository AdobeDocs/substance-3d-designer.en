---
title: "Create Color Palette (16)"
description: "Use the Create Color Palette node to extract a 16-color palette from textures for stylized effects."
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Create Color Palette (16)"
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/create-color-palette-16.html"
---

# Create Color Palette (16)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Quantize Color icon](CreateColorPalette16.png "Quantize Color icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Creates an ordered list of colors and outputs it as a palette, with a maximum of 16 colors.

The node can append new colors to an existing palette, using the set of 'Palette' inputs.

This node may be used in combination with the following nodes: [Quantize Color](../quantize-color/quantize-color.md), [Apply Color Palette](../apply-color-palette/apply-color-palette.md), [Modify Color Palette](../modify-color-palette/modify-color-palette.md), [View Color Palette](../view-color-palette/view-color-palette.md).

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
</tr>
</table>

## Input connectors

|  |  |
| --- | --- |
| <b>Palette</b> *Color* PRIMARY | An ordered list of RGB colors encoded as a row of pixels. The palette can hold a maximum of 256 colors.   This input is optional. If used, colors set up by the node are appended to this palette.   The palette may be visualized with the [View Color Palette](../view-color-palette/view-color-palette.md) node. |
| <b>Palette Color Amount</b> *Integer* | The amount of colors stored in the palette.   If that number does not match the actual amount of colors in the 'Palette' image input, the visualization may be incomplete or have more blank slots than absolutely necessary. |

## Output connectors

|  |  |
| --- | --- |
| <b>Palette</b> *Color* | The updated palette with the specified colors appended to it. |
| <b>Palette Color Amount</b> *Integer* | The updated amount of colors stored in the palette, with the specified amount of colors added to it. |

## Parameters

|  |  |
| --- | --- |
| <b>Color amount</b> *Integer* | The amount of colors which should be added to the palette. |
| <b>Color &#35;</b> *Float3*   *As many parameters available as the 'Color amount' value* | A color which should be added to the palette.   Colors are appended to the palette in the same order as this numbered list. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Create color palette: Example 1](create_color_palette_example_1.png "Create color palette: Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Create color palette: Example 2](create_color_palette_example_2.png "Create color palette: Example 2"){zoomable="yes"}

</td>
</tr>
</table>

![Create color palette: Example 3](create_color_palette_example_3.png "Create color palette: Example 3"){zoomable="yes"}
