---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/arc-pavement.html"
breadcrumb-title: ""
description: Use the Arc Pavement node to generate arc-shaped pavement patterns for creating curved road and path textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Arc Pavement
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Arc Pavement
user-guide-description: ""
user-guide-title: ""
---

# Arc Pavement

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](arc-pavement.resources/arcpavement-ex.png)

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a Parisian arc pavement pattern. This effect cannot be achieved with standard [Tile Generator ](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md)or [Tile Sampler](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-sampler/tile-sampler.md), hence this dedicated node.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Scale</b> <i>1 - 8</i> | Sets global scale/tiling. |
| <b>Pattern Amount</b> <i>1 - 32</i> | Sets amount of bricks used in every arc. |
| <b>Pattern Amount Random</b> <i>0.0 - 1.0</i> | Randomises the amount of bricks in every arc. Has the added effect of giving bricks different scales. |
| <b>Pattern Minimum Amount</b> <i>1 - 10</i> | Controls the minimum amount of bricks when randomising arcs. |
| <b>Arcs Amount</b> <i>0 - 20</i> | Sets the amount of arcs stacked vertically. Changes brick height. |
| <b>Pattern</b> <i>Input Image, Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradations, Waves, Half Bell, Ridged Bell, Crescent, Capsule, Cone</i> | Selects what pattern shape to use. |
| <b>Input Image Filtering</b> <i>Bilinear + Mipmaps, Bilinear, Nearest</i> |  |
| <b>Pattern Scale</b> <i>0.0 - 1.0</i> | Sets scale for each tile. |
| <b>Pattern Width</b> <i>0.0 - 1.0</i> | Sets width for each tile. |
| <b>Pattern Height</b> <i>0.0 - 1.0</i> | Sets height for each tile. |
| <b>Pattern Width Random</b> <i>0.0 - 1.0</i> | Randomises tile width. |
| <b>Pattern Height Random</b> <i>0.0 - 1.0</i> | Randomises tile height. |
| <b>Global Pattern Width Random</b> <i>0.0 - 1.0</i> | Randomises tile width, without creating bigger gaps between them. |
| <b>Pattern Height Decrease</b> <i>0.0 - 1.0</i> | Controls squashing of tile height at the ends of every arc. |
| <b>Color Random</b> <i>0.0 - 1.0</i> | Randomises tile colors. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="arc-pavement.resources/arcpavement-ex.png" />
        </td>
    </tr>
</table>
