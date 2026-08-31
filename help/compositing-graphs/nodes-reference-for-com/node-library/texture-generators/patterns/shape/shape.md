---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/shape.html"
breadcrumb-title: ""
description: Use the Shape node to generate basic geometric shapes for creating patterns and textures in Substance 3D Designer.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape
user-guide-description: ""
user-guide-title: ""
---

# Shape

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](shape.resources/shape-01.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a variety of procedural shapes, with options to modify base shapes. The shapes are always perfectly interpolated and high-precision.

Despite its simplicity, this is a very useful node: it is the building block of most procedural Heightmap generation! By combining basic shapes with transform nodes, you can create a fully-procedural Heightmap shape that is much more precise than any bitmap.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Tiling</b> <i>1 - 16</i> | Sets the amount of times the result should tile. |
| <b>Pattern</b> <i>Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half Bell, Ridged Bell, Crescant, Capsule, Cone, Hemisphere</i> | Selects what pattern shape to use. |
| <b>Pattern Specific</b> <i>0.0 - 1.0</i> | Lets you change the selected pattern's shape. The effect is dependent on the selected pattern. |
| <b>Scale</b> <i>0.0 - 1.0</i> | Scales the entire shape. |
| <b>Size</b> <i>0.0 - 1.0</i> | Allows for non-uniform scaling over either X- or Y-axis. |
| <b>Angle</b> <i>0.0 - 1.0</i> | Rotates the entire shape. |
| <b>Rotation 45°</b> <i>False/True</i> | Rotates at pre-set 45 degrees. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |
| <b>Non Square Tiling</b> <i>False/True</i> | When Non Square Expansion is enabled, this will tile the shape without squashing. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="shape.resources/shape-02.gif" />
        </td>
    </tr>
</table>
