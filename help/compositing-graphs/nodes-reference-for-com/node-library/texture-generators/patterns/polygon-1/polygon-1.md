---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/polygon-1.html"
breadcrumb-title: ""
description: Use the Polygon 1 node to generate basic polygonal patterns with customizable sides and properties for geometric textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Polygon 1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Polygon 1
user-guide-description: ""
user-guide-title: ""
---

# Polygon 1

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/polygon-1-1.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a polygon shape, with many options for adjustment. See [Polygon 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/polygon-2/polygon-2.md) for a simpler version.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Sides</b> <i>3 - 32</i> | Sets the amount of sides the polygon should have. |
| <b>Explode</b> <i>0.0 - 1.0</i> | Moves polygon "slices" apart. |
| <b>Triangle Size</b> <i>0.0 - 1.0</i> | Adjusts size of slices/triangles. Any adjustment could break the shape apart, only 1,1. is perfectly connected! |
| <b>Scale</b> <i>0.0 - 1.0</i> | Scales the whole shape as one. |
| <b>Auto Scale</b> <i>False/True</i> | Adjusts scales so the whole polygon fits into view, with default parameters. |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Rotates the entire shape. |
| <b>Gradient</b> <i>False/True</i> | Generates gradient slices/triangles instead of solid ones. Note: becomes similar to Polygon 2 with this setting enabled. |
| <b>Gradient Invert</b> <i>False/True</i> | Flips the gradient direction if "Gradient" is enabled. |
| <b>Tiling</b> <i>1 - 16</i> | Sets the amount of times the result should tile. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |
| <b>Non Square Tiling</b> <i>False/True</i> | When Non Square Expansion is enabled, this will tile the shape without squashing. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/polygon-1-ex.gif" />
        </td>
    </tr>
</table>
