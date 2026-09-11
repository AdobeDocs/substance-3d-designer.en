---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/splatter-circular.html"
breadcrumb-title: ""
description: Use the Splatter Circular node to scatter circular shapes across textures for creating organic and random patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Splatter Circular
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Splatter Circular
user-guide-description: ""
user-guide-title: ""
---

# Splatter Circular

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](splatter-circular.resources/splatter-circular.png){width="128px"}

![](splatter-circular.resources/splatter-circular-color.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Splatter Circular generates a ring-based pattern with various controls. It can use pre-defined shapes or custom inputs. It's similar to[ Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md), but with a circular placement instead of a grid.

This is useful for when you want to place shapes in a circular way with various randomisation options.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

Both inputs are optional.

|  |  |
|:---|:---|
| <b>Pattern Image Input 1-6</b> <i>Grayscale Input (Color input)</i> | Splatter Circular only: Custom pattern image, used when the "Pattern" parameter is set to "Image Input". |
| <b>Background</b> <i>Grayscale Input (Color input)</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Pattern Amount</b> <i>1 - 64</i> | Amount of pattern tiles to place on a ring. |
| <b>Pattern Amount Random</b> <i>0.0 - 1.0</i> | Randomisation of the amount of patterns to be placed. Best used with a Ring Amount higher than 1. |
| <b>Pattern Amount Random Min</b> <i>1 - 10</i> | Sets the minimal amount of patterns for randomisation. |
| <b>Ring Amount</b> <i>1 - 10</i> | Sets the number of rings to fill. The rings are always placed inside the outer one, and space evenly. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |
| <b>Pattern</b> |  |
| <b>Pattern</b> <i>Image Input, Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half Bell, Ridged Bell, Crescent, Capsule, Cone</i> | Selects what pattern shape to use. |
| <b>Pattern Input Number</b> <i>1 - 6</i> | Sets number of different Image inputs to use. Only available when <i>Image Input</i> is selected above. |
| <b>Pattern Input Distribution</b> <i>Random, By Pattern Number, By Ring Number</i> | Sets how multiple Pattern Inputs are chosen. Random means a random one is chosen, Pattern Number means they are just placed in a looping sequence, By ring numbers means every ring has a different one in sequence. |
| <b>Image Input Filtering</b> <i>Bilinear + Mipmaps, Bilinear, Nearest</i> |  |
| <b>Pattern Specific</b> <i>0.0 - 1.0</i> | Lets you change the selected pattern's shape. The effect is dependent on the selected pattern. |
| <b>Symmetry Random</b> <i>0.0 - 1.0</i> | Sets the number of tiles that should be randomly flipped/mirrored according to the below behaviour. |
| <b>Symmetry Random Mode</b> <i>Horizontal + Vertical, Horizontal, Vertical</i> | Determines symmetry mirroring behaviour. |
| <b>Position</b> |  |
| <b>Radius</b> <i>0.0 - 1.0</i> | Sets the radius from the center at which the patterns are placed. |
| <b>Radius Random</b> <i>0.0 - 1.0</i> | Randomises the radius for every pattern tile. |
| <b>Ring Radius Multiplier</b> <i>0.0 - 1.0</i> | Affects spacing of multiple rings. |
| <b>Angle Random</b> <i>0.0 - 1.0</i> | Randomises the angle of each pattern. A higher amounts means more rotation. |
| <b>Spiral Factor</b> <i>0.0 - 1.0</i> | Turns the rings into Spirals, where every tile is placed at a slightly increasing radius. |
| <b>Spread</b> <i>0.0 - 2.0</i> | Sets the amount of turns a ring does. This can be increased beyond its limits. |
| <b>Offset along Direction</b> <i>0.0 - 1.0</i> | Moves every pattern out from the center along its angle. The effect greatly depends on Angle Random, or it looks just like a multiplier for the Radius. |
| <b>Global Offset</b> <i>0.0 - 1.0</i> | Translates the entire shape. |
| <b>Size</b> |  |
| <b>Connect Patterns</b> <i>False/True</i> | Makes the length of pattern tiles dependent on the radius, meaning each shape should touch the previous and next one. |
| <b>Size (Connected)</b> <i>0.0 - 1.0</i> | Changes the size of each pattern globally. When connected, it's relative to the total radius. |
| <b>Size Random</b> <i>0.0 - 1.0</i> | Randomises the size of each pattern individually. |
| <b>Scale</b> <i>0.0 - 2.0</i> | Uniformly scales each pattern. |
| <b>Scale Random</b> <i>0.0 - 1.0</i> | Randomises uniform scaling. |
| <b>Scale by Pattern Number</b> <i>0.0 - 1.0</i> | Makes the pattern scale dependent on the position along the ring. |
| <b>Invert Pattern Number</b> <i>False/True</i> | Used with the previous option, this can invert scaling from small to large and vice-versa. |
| <b>Scale by Ring Number</b> <i>0.0 - 1.0</i> | Makes scale dependent on ring number. |
| <b>Invert Ring Number</b> <i>False/True</i> | Used with the previous option, it can invert scaling from small to large and vice-versa. |
| <b>Rotation</b> |  |
| <b>Pattern Rotation</b> <i>0.0 - 1.0</i> | Rotates every pattern uniformly. |
| <b>Pattern Rotation Random</b> <i>0.0 - 1.0</i> | Randomises pattern rotation. |
| <b>Pattern Rotation Pivot</b> <i>Center, Min X, Max X, Min Y, Max Y</i> | Sets the pivot point position around which to rotate every pattern individually. |
| <b>Center Orientation</b> <i>False/True</i> | Rotates every pattern so it faces towards the center of the ring. Turning it of gives them all the same orientation - this can produce unwanted effects with Offset along direction. |
| <b>Ring Rotation</b> <i>0.0 - 1.0</i> | Rotates entire ring around center. |
| <b>Ring Rotation Random</b> <i>0.0 - 1.0</i> | Randomises rotation per ring. |
| <b>Ring Rotation Offset</b> <i>0.0 - 1.0</i> | Offsets rotation per ring. |
| <b>Color</b> |  |
| <b>Color</b> <i>(Grayscale value)</i> | Color to multiply with selected pattern. |
| <b>Luminance Random</b> <i>0.0 - 1.0</i> | Randomizss color or Luminance for every pattern tile. |
| <b>Luminance By Scale</b> <i>0.0 - 1.0</i> | Makes Luminance dependent on the individual pattern scale. |
| <b>Luminance by Pattern Number</b> <i>0.0 - 1.0</i> | Makes Luminance dependent on the pattern sequence. Can for example be used with spirals. |
| <b>Invert Pattern Number</b> <i>False/True</i> | Inverts the previous option. |
| <b>Luminance by Ring Number</b> <i>0.0 - 1.0</i> | Makes Luminance dependent on the ring sequence. |
| <b>Invert Ring Number</b> <i>False/True</i> | Inverts the previous option. |
| <b>Random Mask</b> <i>0.0 - 1.0</i> | Randomly hides patterns. |
| <b>Background Color</b> <i>(Grayscale value)</i> | Changes solid background color. |
| <b>Blending Mode</b> <i>Add, Max, Add Sub</i> | Sets how to blend overlapping patterns. |
| <b>Global Opacity</b> <i>0.0 - 1.0</i> | Sets the global opacity of the entire result. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="splatter-circular.resources/circularsplatter-ex.png" />
        </td>
    </tr>
</table>
