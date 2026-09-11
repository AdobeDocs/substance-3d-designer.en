---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/shape-mapper.html"
breadcrumb-title: ""
description: Use the Shape Mapper node to map shapes onto textures with customizable transformations and positioning.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape mapper
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape mapper
user-guide-description: ""
user-guide-title: ""
---

# Shape mapper

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Shape mapper - Icon](shape-mapper.resources/shape_mapper.png "Shape mapper - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Projects an input image along a circle or polygon.

The projection deforms the image to follow the shape's outline, and make it fit exactly a specified amount of times without gaps.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Grayscale</i> | The pattern which should be placed along the shape. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The result of the projection of the pattern along the shape, as a grayscale bitmap. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Shape</b> <i>Integer</i> | Sets the type of shape along which patterns should be placed:<ul data-preserve-html="true"> <li data-preserve-html="true">Circle</li> <li data-preserve-html="true">Polygon</li> </ul> |
| <b>Pattern amount</b> <i>Integer</i> | The amount of patterns placed along the selected shape. |
| <b>Link segments with pattern amount</b> <i>Boolean</i>   *Available when 'Shape' is set to 'Polygon'* | Use the <b>Pattern amount</b> as the number of <b>Segments</b>.   This prevents patterns from wrapping around corners, ensuring a straight and consistent aspect. |
| <b>Segments</b> <i>Integer</i>   *Available when 'Shape' is set to 'Polygon' and 'Link segements with pattern amount' is set to 'False'* | The amount of segments for the polygon along which patterns are placed.   Segments are *evenly sized*, and all vertices are *equidistant from the center*, such that increasing the amount of segments makes the polygon converge towards a circle. |
| <b>Radius</b> <i>Float</i> | A multiplier for the radius of the shape, where 1.0 is half the length of the image's shortest side. |
| <b>Width</b> <i>Float</i> | A multiplier for the width of the patterns along the shape, where 1.0 is half the length of the image's shortest side. |
| <b>Rotation</b> <i>Float</i> | The amount of rotation applied to the shape, in number of turns clockwise from the horizontal right. |
| <b>Flip one on two</b> <i>Boolean</i> | Flip one every other shape vertically. |
| <b>Filtering mode</b> <i>Integer</i> | The method of filtering applied to the patterns placed along the shape:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Nearest:</i> Applies the value from the closest projected pixel as-is, resulting in a crisper yet aliased look.</li> <li data-preserve-html="true"><i>Bilinear:</i> Applies a bilinear filter to interpolate the projected pixel with its neighbors, for a smoother yet blurrier look.</li> </ul> |
| <b>Non-square expansion</b> <i>Boolean</i> | In non-square images, keeps the generated shape square and expands the image generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
