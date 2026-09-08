---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/tile-random.html"
breadcrumb-title: ""
description: Use the Tile Random node to create randomized tile patterns with procedural variation for organic texture effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Tile Random
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Tile Random
user-guide-description: ""
user-guide-title: ""
---

# Tile Random

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](tile-random.resources/tile-random.png){width="128px"}

<b>In:</b> Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Tile Random generates a procedural tile pattern that has a little bit more chaos in the tile shapes than its counterpart, [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md). It does this by randomly splitting certain tiles into smaller tiles. We suggest you first find your way around Tile Generator before tackling Tile Random, as many concepts are similar.

Tile Random is used instead of [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md) when the goal is an older-looking, less organised pattern. It does have its limitations though, so consider [Tile Sampler](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-sampler/tile-sampler.md) for any other advanced needs.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Pattern Input</b> <i>Grayscale Input (Color Input)</i> | Custom pattern image, used when the "Pattern" parameter is set to "Image Input". |
| <b>Background Input</b> <i>Grayscale Input (Color input)</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>X Amount</b> <i>1 - 64</i> | Amount of X-repetitions of the pattern. |
| <b>Y Amount</b> <i>1 - 64</i> | Amount of Y-repetitions of the pattern. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |
| <b>Pattern</b> |  |
| <b>Pattern</b> <i>Pattern Input, Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half Bell, Ridged Bell, Crescent, Capsule, Cone</i> | Selects what pattern shape to use. |
| <b>Image Input Filtering (Engine &gt; v4)</b> <i>Bilinear + Mipmaps, Bilinear, Nearest</i> |  |
| <b>Pattern Specific</b> <i>0.0 - 1.0</i> | Lets you change the selected pattern's shape. The effect is dependent on the selected pattern. |
| <b>Pattern Specific Random</b> <i>0.0 - 1.0</i> | Randomisation effect is dependent on the selected pattern. |
| <b>Rotation</b> <i>0, 90, 180, 270, random horizontal, random vertical</i> | Sets rotation in 90 degree steps, with optional randomisation. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Adds random free rotation. |
| <b>Symmetry Random</b> <i>0.0 - 1.0</i> | Randomly mirrors certain patterns by the selected Symmetry random Mode. The higher this value, the more patterns will be mirrored. |
| <b>Symmetry Random Mode</b> <i>Horizontal + Vertical, Horizontal, Vertical</i> | Determines mirroring behaviour when Symmetry random is higher than 0. |
| <b>Split</b> |  |
| <b>Mode</b> <i>none, auto, auto horizontal, auto vertical, random h+v</i> | Sets the rule on how to split tiles. |
| <b>Threshold</b> <i>0.0 - 1.0</i> | Size treshold for when to split a tile. |
| <b>Multiplier</b> <i>0 - 10</i> | Splitting multiplier. The higher this value, the more splits. |
| <b>Size</b> |  |
| <b>Random X</b> <i>0.0 - 1.0</i> | Randomises non-uniform scaling over X-axis. |
| <b>Random Y</b> <i>0.0 - 1.0</i> | Randomises non-uniform scaling over Y-axis. |
| <b>Interstice</b> |  |
| <b>Mode</b> <i>Relative to smallest brick, Relative to largest brick</i> | Sets what brick size interstice is relative to. |
| <b>Amount</b> <i>0.0 - 1.0</i> | Sets gap size between bricks. |
| <b>Shape</b> |  |
| <b>Scale</b> <i>0.0 - 1.0</i> | Globally scales every tile. |
| <b>Scale Random</b> <i>0.0 - 1.0</i> | Random scaling on a per-tile basis. |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Global rotation for every tile. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Rotates randomly on a per-tile basis. |
| <b>Rotation Constraint</b> <i>False/True</i> | Constrains the scale so rotated tiles never overlap. |
| <b>Position</b> |  |
| <b>Offset</b> <i>0.0 - 1.0</i> | Moves or translates the tiles globally, slides over X-axis only |
| <b>Offset Random</b> <i>0.0 - 1.0</i> | Randomises offset per-tile, slides over X-axis only |
| <b>Random</b> <i>0.0 - 1.0</i> | Randomises position, tiles move on both X- and Y-axis. |
| <b>Random Constraints</b> <i>False/True</i> | Constrains scale so tiles touch, but don't overlap. Tones down the Random Position effect significantly. |
| <b>Color</b> |  |
| <b>Color</b> <i>(Grayscale value) / (Color value)</i> | Sets solid color for all tiles. |
| <b>Color Random</b> <i>0.0 - 1.0</i> | Randomises color on a per-tile basis. |
| <b>Color Parametrisation</b> <i>none, area, size x, size y</i> | Makes color variation dependent on one of these settings. |
| <b>Color Parametrisation Intensity</b> <i>0.0 - 1.0</i> | Multiplier for the above Parametrisation effect. |
| <b>Color Parametrisation Effect (for Color only)</b> <i>RGB+Alpha, RGB only, Alpha only</i> | Determines color-only parametrisation effect. |
| <b>Background Color</b> <i>(Grayscale value) / (Color value)</i> | Sets solid background color. |
| <b>Blending Mode</b> <i>Add/Sub, Max / Add/Sub, Alpha Blend (Color)</i> | Sets blending mode for tiles onto background. |
| <b>Mask</b> |  |
| <b>Random</b> <i>0.0 - 1.0</i> | Randomly begins masking out tiles. The higher the value, the more tiles dissappear. |
| <b>Invert</b> <i>False/True</i> | Inverts the mask result. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="tile-random.resources/tile-random-1.png" />
        </td>
    </tr>
</table>
