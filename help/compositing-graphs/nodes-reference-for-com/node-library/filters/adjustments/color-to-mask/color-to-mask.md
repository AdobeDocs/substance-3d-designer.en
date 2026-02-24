---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/color-to-mask.html"
breadcrumb-title: ""
description: Use the Color to Mask node to convert specific colors to masks for creating selective processing and masking effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Color to mask
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Color to mask
user-guide-description: ""
user-guide-title: ""
---


# Color to mask

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Color to mask - Icon](color_to_mask.png "Color to mask - Icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Extracts a greyscale mask from selected colors in a color image.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Inputs

</td>
<td style="border: 0;" valign="top">

### Outputs

</td>
<td style="border: 0;" valign="top">

### Parameters

</td>
<td style="border: 0;" valign="top">

### Examples

</td>
</tr>
</table>

## Inputs

|  |  |
| --- | --- |
| <b>Input</b>  Color | The input color image that a mask should be extracted from based on its colors. |
| <b>Color Input</b>  Color   *Available when 'Use color input' is set to 'True'* | The input color image used to define the reference color per pixel. |

## Outputs

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* | The generated mask as a grayscale bitmap. |

## Parameters

|  |  |
| --- | --- |
| <b>Use color input</b>  Boolean | Use an input image instead of a uniform color, in order to define a reference color per pixel.    The input image is provided by the <b>Color input</b> input. |
| <b>Color</b>  Float3   *Available when 'Use color input' is set to 'False'* | The reference uniform color around which the color selection should be performed. |
| <b>Threshold</b>  Float | The distance to the reference color below which colors are selected. |
| <b>Selection fade</b>  Float | Fade the color selection based on the distance to the reference color. |
| <b>Distance color space</b>  Integer | The Equalize process involves comparing colors to determine the distance between them. Certain color spaces and distance algorithms are better suited for specific use cases.   This drop-down list lets you select the color space used to compare the colors:<ul data-preserve-html="true"> <li data-preserve-html="true"><b><i>RGB (Data):</i></b> Color is split into Red, Green, Blue channels and distributed straight along those axis, disregarding human perception. This is appropriate for images holding raw data.</li> <li data-preserve-html="true"><i>Linear sRGB (Color):</i> Color is split into Red, Green, Blue channels and distributed in a linear relationship to the pixel light intensity. This is appropriate for image which may be visualised on displays.</li> <li data-preserve-html="true"><b><i>Luminance (Color):</i></b> Color is split into Hue, Chroma, Luminance values where only the Luminance value is used in the comparaison. This is appropriate for image which may be visualised on displays.</li> <li data-preserve-html="true"><i>Lab (Color):</i> A standardized perceptual color space, which distributes colors in such a way that colors that 'feel' close are actually close in the cube. This is appropriate for image which may be visualised on displays.</li> <li data-preserve-html="true"><i>Angle (Normal):</i> Color is split into the X, Y, Z axes of a vector and compared through a dot product. This is appropriate for images holding Tangent Space Normals.</li> </ul> |
| <b>Distance weights</b>  Float3 | The Lab color distance algorithm (DeltaE2000) introduces certain weight factors for each lightness, chroma, and hue value.   Lower values will decrease the influence of the factors in the color difference algorithm.   Since the eye will generally accept larger differences in lightness (L) than in chroma (C) or hue (H), a default ratio for (L:C:H) is (0.5:1:1). A 0.5:1:1 ratio will allow twice as much difference in lightness as in chroma or hue. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
