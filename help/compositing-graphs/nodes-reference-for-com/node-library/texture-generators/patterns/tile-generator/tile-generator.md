---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/tile-generator.html"
breadcrumb-title: ""
description: Use the Tile Generator node to create procedural tile patterns with customizable size, offset, and variation controls.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Tile Generator
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Tile Generator
user-guide-description: ""
user-guide-title: ""
---

# Tile Generator

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](tile-generator.resources/tile-generator.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Tile generator is one of the most advanced nodes in the library. If you learn to master it, you can create any kind of pattern (within some limitations). As of Version 2017 2.1 there have been some big updates, bringing this node more in line with what [Tile Sampler](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-sampler/tile-sampler.md) can do.

This node is highly useful for a variety of scenarios, but keep in mind that simply reading parameters will not fully teach you how to use them. We suggest you experiment too!

For 99% of all cases, the color version is NOT needed!

Some general usage tips:

* You can start with a basic shape, but if you have a custom input (Set **Pattern Type** to *Image Input*), create it first! It determines a lot of the look.
* Start by correctly setting your X and Y amounts.
* Find the right **Size** mode: Relative modes like **Interstice** behave quite different from **Absolute** modes.
* Adjust global **Scale** and non-uniform **Size** next.
* Finally, tweak any **"Variation"** parameter until it meets your needs. Subtlety is key with variation!

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Pattern Input 1-6</b> <i>Grayscale Input</i> | Custom pattern image, used when the "Pattern" parameter is set to "Image Input". |
| <b>Background</b> <i>Grayscale Input</i> | Background to use instead of solid color. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>X Amount</b> <i>1 - 64</i> | Amount of X-repetitions of the pattern. |
| <b>Y Amount</b> <i>1 - 64</i> | Amount of Y-repetitions of the pattern. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |
| <b>Pattern</b> |  |
| <b>Pattern</b> <i>Image Input, Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half Bell, Ridged Bell, Crescent, Capsule, Cone</i> | Selects which pattern shape to use. |
| <b>Pattern Input Number</b> <i>1 - 6</i> | Number of different Image inputs to use. Only available when <i>Image Input</i> is selected above. |
| <b>Pattern Input Distribution</b> <i>Random, By Pattern Number</i> | How to pick between the different Image Inputs, if more than 1 is selected. |
| <b>Pattern Specific</b> <i>0.0 - 1.0</i> | Lets you change the selected pattern's shape. Effect is dependent on selected pattern. |
| <b>Image Input Filtering (Engine &gt;v4 only)</b> <i>Bilinear + Mipmaps, Bilinear, Nearest</i> |  |
| <b>Rotation</b> <i>0, 90, 180, 270</i> | Rotates all tiles globally by a set angle in 90 degree steps. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Randomy rotates a tile by one of four 90 degree steps. |
| <b>Quincunx Flip</b> <i>False/True</i> | Rotates every other tile by 90 degrees. |
| <b>Symmetry Random</b> <i>0.0 - 1.0</i> | Randomly mirrors certain patterns by the selected Symmetry random Mode. The higher this value, the more patterns will be mirrored. |
| <b>Symmetry Random Mode</b> <i>Horizontal + Vertical, Horizontal, Vertical</i> | Determines mirroring behaviour when Symmetry random is higher than 0. |
| <b>Size</b> |  |
| <b>Size Mode</b> <i>Normal - Interstice, Normal - Size, Keep Ratio, Absolute, Pixel</i> | Sets general behavior of the pattern size.<br><br>Normal - Interstice lets you define the gap between the pattern elements. It is affected by the X and Y amount.<br><br>Normal - Size lets you define the size of the pattern elements, irrespective of the gap. It is affected by the X and Y amount.<br><br>Keep Ratio lets you set a size affected by X and Y amount, but the X and Y ratio between the two is left intact.<br><br>Absolute lets you set an absolute size that is not affected by X and Y amount.<br><br>Pixel lets you set an absolute size in pixels, unaffected by X and Y amount. Changing the resolution will affect the size of the elements. |
| <b>Middle Size</b> <i>0.0 - 1.0</i> | Changes size on an alternating column- and row-basis. |
| <b>Interstice X/Y</b> <i>0.0 - 1.0</i> | Only available in Normal - Interstice Size mode. Changes interstice gap. Affects the seam between shapes, allows for non-uniform control unlike <b>Scale</b>. |
| <b>Size (Absolute/Pixel)</b> <i>0.0 - 1.0</i> | Only available outside of Normal - Interstice size mode. Sets non-uniform size, unlike <b>Scale</b>. |
| <b>Scale</b> <i>0.0 - 2.0</i> | Sets global Scale. |
| <b>Scale Random</b> <i>0.0 - 1.0</i> | Sets global scale variation per-tile. |
| <b>Scale Random Seed</b> <i>0 - 1000</i> | Offsets scale variation seed. |
| <b>Position</b> |  |
| <b>Offset</b> <i>0.0 - 1.0</i> | Offsets the entire pattern incrementally over every consecutive row or column (behaviour depends on Vertical Offset parameter). |
| <b>Offset Random</b> <i>0.0 - 1.0</i> | Randomises line offsetting. |
| <b>Offset Random Seed</b> <i>0 - 1000</i> | Changes the relative seed for the random offsetting effect. |
| <b>Vertical Offset</b> <i>False/True</i> | Sets whether Offset effect happens over rows or lines; Horizontal or Vertical. |
| <b>Position Random</b> <i>0.0 - 1.0</i> | Randomises position in a non-uniform way, with separate control for X and Y. |
| <b>Global Offset</b> <i>0.0 - 1.0</i> | Shifts the entire result over both X- and Y-axes. |
| <b>Rotation</b> |  |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Does a uniform free Rotation of all pattern tiles. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Randomises free rotation of all tiles. The higher this value, the more tiles can be rotated. |
| <b>Color</b> |  |
| <b>Color</b> <i>(Grayscale value)</i> | Sets tile solid color. |
| <b>Luminance/Color Random</b> <i>0.0 - 1.0</i> | Introduces per-tile Color or Luminance variation. |
| <b>Luminance By Number</b> <i>False/True</i> | Fades Luminance over the entire pattern. |
| <b>Luminance By Scale</b> <i>False/True</i> | Makes Luminance variation dependent on tile scale. |
| <b>Checker Mask</b> <i>False/True</i> | Hides every other tile. |
| <b>Horizontal Mask</b> <i>False/True</i> | Hides every other column. |
| <b>Vertical Mask</b> <i>False/True</i> | Hides every other row. |
| <b>Random Mask</b> <i>0.0 - 1.0</i> | Randomly hides tiles. The higher this value, the more tiles will disappear. |
| <b>Invert Mask</b> <i>False/True</i> | Inverts the result of any masking effects from this section. |
| <b>Blending Mode</b> <i>Add, Max, Add Sub</i> | Sets what blending mode to use. |
| <b>Background Color</b> <i>(Grayscale value)</i> | Sets solid background color. |
| <b>Global Opacity</b> <i>0.0 - 1.0</i> | Sets global tiles opacity. |
| <b>Reverse Rendering Order</b> <i>False/True</i> | Renders tiles back to front or vice-versa. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="tile-generator.resources/tilesampler-ex.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-generator.resources/image2020-9-17-14-50-18.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-generator.resources/image2020-9-17-14-52-4.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-generator.resources/image2020-9-17-14-53-47.png" />
        </td>
    </tr>
</table>
