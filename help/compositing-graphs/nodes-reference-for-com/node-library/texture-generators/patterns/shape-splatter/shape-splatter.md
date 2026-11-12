---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/shape-splatter.html"
breadcrumb-title: ""
description: Use the Shape Splatter node to scatter shapes across textures for creating procedural patterns and details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape Splatter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape Splatter
user-guide-description: ""
user-guide-title: ""
---

# Shape Splatter

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](shape-splatter.resources/shape-splatter.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A very complex node, designed to be used in conjunction with accompanying nodes [Shape Splatter Blend](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter-blend/shape-splatter-blend.md), [Shape Splatter to Mask](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter-to-mask/shape-splatter-to-mask.md) and [Shape Splatter Data Extract](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter-data-ext/shape-splatter-data-extract.md). Used to splatter shapes in a similar way to[ Tile Sampler](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-sampler/tile-sampler.md) or [Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md), but with a dynamic, non-destructive process that allows control over every step, through a multi-level system similar to [Flood Fill.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md) Whereas Flood Fill takes a base input map from an external source, Shape Splatter generates the map and ensuing data in a single step, as a sort of more advanced version of [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md)..

It's main purpose is to allow placement of shapes onto and driven by a height map and to then generate various maps from the Splatter Data. For example placing rocks, twigs and leaves on a landscape, oriented and driven by various maps. Different maps can then be used for height, normal, basecolor, roughness and any other channel, while all are still based on the same shared Splatter Data.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Background Height</b> <i>Grayscale Input</i> | Background height to place tiles onto and drive various effects. |
| <b>Pattern 1-8</b> <i>Grayscale Input</i> | Optional Pattern |
| <b>Pattern Distribution</b> <i>Grayscale Input</i> | Grayscale map to |
| <b>Shape Scale</b> <i>Grayscale Input</i> | Grayscale map to drive tile scaling. |
| <b>Shape Rotation</b> <i>Grayscale Input</i> | Grayscale map to drive tile rotation. |
| <b>Height Offset</b> <i>Grayscale Input</i> | Grayscale map to use as an offset for Tile height. |
| <b>Height Scale</b> <i>Grayscale Input</i> | Grayscale map to use as an offset for Tile height. |
| <b>Mask Random</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>Vector Map</b> <i>Color Input</i> | Color vector map to drive Tile positioning and rotation. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>X Amount</b> <i>1 - 64</i> | Amount of X repetitions of the pattern. |
| <b>Y Amount</b> <i>1 - 64</i> | Amount of Y repetitions of the pattern. |
| <b>Pattern</b> |  |
| <b>Pattern Input Number</b> <i>1 - 8</i> | Set amount of different patterns to use. Unlocks new Pattern Input slots. |
| <b>Pattern Distribution Mode</b> <i>Random, Pattern Index, Line Index, Column Index</i> | Set how to determine what pattern to use. Randomly or by pattern, line or column. |
| <b>Pattern Distribution Map Multiplier</b> <i>0.0 - 1.0</i> | Set the influence of the optional Distribution map for the placement of patterns. |
| <b>Pattern Rotation</b> <i>0, 90, 180, 270</i> | Set preset, 90 degree rotation of patterns. |
| <b>Pattern Rotation Random</b> <i>0.0 - 1.0</i> | Set the amount of random 90-degree step rotation for patterns. |
| <b>Size</b> |  |
| <b>Scale</b> <i>0.0 - 5.0</i> | Set the uniform scale for every tile. |
| <b>Scale Random</b> <i>0.0 - 1.0</i> | Randomize uniform scale for every tile. |
| <b>Scale No Overlap</b> <i>0.0 - 1.0</i> | Scale random uniformly, but only down, to avoid overlapping tiles. Should not be used in conjunction with previous two parameters. |
| <b>Scale Map Multiplier</b> <i>0.0 - 1.0</i> | Set influence of scale map. |
| <b>Size</b> <i>0.0 - 1.0</i> | Allows for non-uniform scaling of tiles. |
| <b>Size Ratio from Bg Slope</b> <i>0.0 - 1.0</i> | Uses Background map slope (calculated Normal) to non-uniformly scale tiles. Simulates perspective warping. |
| <b>Size by X/Y Amount Ratio</b> <i>0.0 - 1.0</i> | Non-uniform scaling to compensate for a different ratio in X and Y Amounts. |
| <b>Position</b> |  |
| <b>Position Random</b> <i>0.0 - 2.0</i> | Randomly offset opsition for every tile. |
| <b>Random Distribution</b> <i>Gaussian, Uniform</i> | Sets calculation to use for previous parameter. Does not make a huge difference, more noticeable with high numbers. Gaussian tends to give a more even spread. |
| <b>Vector Map Multiplier</b> <i>0.0 - 1.0</i> | Influence of the vector input map on offsets. |
| <b>Offset Horizontal</b> <i>-2.0 - 2.0</i> | Global Horizontal offset. |
| <b>Offset Vertical</b> <i>-2.0 - 2.0</i> | Global Vertical offset. |
| <b>Out of Bounds Option</b> <i>Scale Shape, Constrain Position</i> | Action to perform when a tile would appear Out-of-Bounds. |
| <b>Rotation</b> |  |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Globally rotates all tiles. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Rotates randomly per-tile. |
| <b>Rotation from Bg Slope</b> <i>0.0 - 1.0</i> | Uses Background map slope (calculated Normal) to rotate tiles. Can be used to have shapes point up or down on slopes. |
| <b>Rotation Map Multiplier</b> <i>0.0 - 1.0</i> | Blends in the effect of Rotation map on per-Tile rotation. |
| <b>Vector Map Multiplier</b> <i>0.0 - 1.0</i> | Blends in the effect of Rotation map on per-Tile rotation. |
| <b>Height</b> |  |
| <b>Height Scale Auto Adjust</b> <i>False/True</i> | Automatically adjust the height range relative to background, instead of defining an absolute range. Allows less or more control. |
| <b>Height Offset</b> <i>-1.0 - 1.0</i> | Modifier to offset/move all tiles uniformly through the range of height. |
| <b>Height Offset Random</b> <i>0.0 - 1.0</i> | Randomly changes height offset on a per-tile basis. |
| <b>Height Offset Map Mulitplier</b> <i>0.0 - 1.0</i> | Modifier to set influence of Offset Map. |
| <b>Height Scale</b> <i>0.0 - 1.0</i> | Modifier to scale/expand all tiles uniformly over the range of height. Opposed to offset this pushes values further apart, like contrast. |
| <b>Height Scale Random</b> <i>0.0 - 1.0</i> | Randomly changes height scale on a per-tile basis. |
| <b>Height Scale Map Multiplier</b> <i>0.0 - 1.0</i> | Modifier to set influence of Scale Map. |
| <b>Conform to Background</b> <i>0.0 - 1.0</i> | Affects blending of tiles with background. No conforming means heightmaps stay rigid, conforming measn the follow background shape. Good for leaves vs sticks for example. |
| <b>Smooth Conformed Background</b> <i>0.0 - 2.0</i> | Smoothing value for previous effect, to avoid incorrect or extreme variations. |
| <b>Skew from Bg Slope</b> <i>0.0 - 1.0</i> | Adjust/ slope tile height driven by Background slope (calculated normal). |
| <b>Background Slope Smoothness</b> <i>0.0 - 2.0</i> | Smoothing value for previous effect, to avoid incorrect or extreme variations. |
| <b>Cutout Black Pixels</b> <i>False/True</i> | Toggle to ignore full black (0) pixels from tile base shapes. |
| <b>Flatten Pattern Base</b> <i>False/True</i> | Adjusts tile blending behaviour with background: tiles will either intersect with background (False) or override the background when lower. |
| <b>Masking</b> |  |
| <b>Mask Random</b> <i>0.0 - 1.0</i> | Randomly hides tiles. The higher this value, the more tiles will disappear. |
| <b>Mask Random Map Multiplier</b> <i>0.0 - 1.0</i> | Treshold for mask map when to start hiding tiles. |
| <b>Mask from Bg Slope</b> <i>-1.0 - 1.0</i> | Uses Background map slope (calculated Normal) to hide tiles. |
