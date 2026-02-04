---
title: "Shape Splatter | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape Splatter"
---

# Shape Splatter

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shape-splatter.png){width="128px"}

## Shape Splatter

**In:** *Texture Generators**/Patterns*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

A very complex node, designed to be used in conjunction with accompanying nodes [Shape Splatter Blend](../shape-splatter-blend/shape-splatter-blend.md), [Shape Splatter to Mask](../shape-splatter-to-mask/shape-splatter-to-mask.md) and [Shape Splatter Data Extract](../shape-splatter-data-ext/shape-splatter-data-extract.md). Used to splatter shapes in a similar way to[ Tile Sampler](../tile-sampler/tile-sampler.md) or [Generator](../tile-generator/tile-generator.md), but with a dynamic, non-destructive process that allows control over every step, through a multi-level system similar to [Flood Fill.](../../../filters/effects/flood-fill/flood-fill.md) Whereas Flood Fill takes a base input map from an external source, Shape Splatter generates the map and ensuing data in a single step, as a sort of more advanced version of [Flood Fill](../../../filters/effects/flood-fill/flood-fill.md)..

It's main purpose is to allow placement of shapes onto and driven by a height map and to then generate various maps from the Splatter Data. For example placing rocks, twigs and leaves on a landscape, oriented and driven by various maps. Different maps can then be used for height, normal, basecolor, roughness and any other channel, while all are still based on the same shared Splatter Data.

## Parameters

### Inputs

* **Background Height**: *Grayscale Input*Background height to place tiles onto and drive various effects.
* **Pattern 1-8**: *Grayscale Input**Optional Pattern*
* **Pattern Distribution**: *Grayscale Input*Grayscale map to
* **Shape Scale**: *Grayscale Input*Grayscale map to drive tile scaling.
* **Shape Rotation**: *Grayscale Input*Grayscale map to drive tile rotation.
* **Height Offset**: *Grayscale Input*Grayscale map to use as an offset for Tile height.
* **Height Scale**: *Grayscale Input*Grayscale map to use as an offset for Tile height.
* **Mask Random**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **Vector Map**: *Color Input*Color vector map to drive Tile positioning and rotation.

### Parameters

* **X Amount**: *1 - 64*  
  Amount of X repetitions of the pattern.
* **Y Amount**: *1 - 64*  
  Amount of Y repetitions of the pattern.
* **Pattern**   
  * **Pattern Input Number**: *1 - 8*Set amount of different patterns to use. Unlocks new Pattern Input slots.
  * **Pattern Distribution Mode**: *Random, Pattern Index, Line Index, Column Index*Set how to determine what pattern to use. Randomly or by pattern, line or column.
  * **Pattern Distribution Map Multiplier**: *0.0 - 1.0*Set the influence of the optional Distribution map for the placement of patterns.
  * **Pattern Rotation**: *0, 90, 180, 270*Set preset, 90 degree rotation of patterns.
  * **Pattern Rotation Random**: *0.0 - 1.0*Set the amount of random 90-degree step rotation for patterns.
* **Size**   
  * **Scale**: *0.0 - 5.0*  
    Set the uniform scale for every tile.
  * **Scale Random**: *0.0 - 1.0*Randomize uniform scale for every tile.
  * **Scale No Overlap**: *0.0 - 1.0*Scale random uniformly, but only down, to avoid overlapping tiles. Should not be used in conjunction with previous two parameters.
  * **Scale Map Multiplier**: *0.0 - 1.0*Set influence of scale map.
  * **Size**: *0.0 - 1.0*Allows for non-uniform scaling of tiles.
  * **Size Ratio from Bg Slope**: *0.0 - 1.0*Uses Background map slope (calculated Normal) to non-uniformly scale tiles. Simulates perspective warping.
  * **Size by X/Y Amount Ratio**: *0.0 - 1.0*Non-uniform scaling to compensate for a different ratio in X and Y Amounts.
* **Position**   
  * **Position Random**: *0.0 - 2.0*Randomly offset opsition for every tile.
  * **Random Distribution**: *Gaussian, Uniform*Sets calculation to use for previous parameter. Does not make a huge difference, more noticeable with high numbers. Gaussian tends to give a more even spread.
  * **Vector Map Multiplier**: *0.0 - 1.0*Influence of the vector input map on offsets.
  * **Offset Horizontal**: *-2.0 - 2.0*Global Horizontal offset.
  * **Offset Vertical**: *-2.0 - 2.0*Global Vertical offset.
  * **Out of Bounds Option**: *Scale Shape, Constrain Position*Action to perform when a tile would appear Out-of-Bounds.
* **Rotation**   
  * **Rotation**: *0.0 - 1.0*Globally rotates all tiles.
  * **Rotation Random**: *0.0 - 1.0*Rotates randomly per-tile.
  * **Rotation from Bg Slope**: *0.0 - 1.0*Uses Background map slope (calculated Normal) to rotate tiles. Can be used to have shapes point up or down on slopes.
  * **Rotation Map Multiplier**: *0.0 - 1.0*Blends in the effect of Rotation map on per-Tile rotation.
  * **Vector Map Multiplier**: *0.0 - 1.0*Blends in the effect of Rotation map on per-Tile rotation.
* **Height**   
  * **Height Scale Auto Adjust**: *False/True*Automatically adjust the height range relative to background, instead of defining an absolute range. Allows less or more control.
  * **Height Offset**: *-1.0 - 1.0*Modifier to offset/move all tiles uniformly through the range of height.
  * **Height Offset Random**: *0.0 - 1.0*Randomly changes height offset on a per-tile basis.
  * **Height Offset Map Mulitplier**: *0.0 - 1.0*Modifier to set influence of Offset Map.
  * **Height Scale**: *0.0 - 1.0*Modifier to scale/expand all tiles uniformly over the range of height. Opposed to offset this pushes values further apart, like contrast.
  * **Height Scale Random**: *0.0 - 1.0*Randomly changes height scale on a per-tile basis.
  * **Height Scale Map Multiplier**: *0.0 - 1.0*Modifier to set influence of Scale Map.
  * **Conform to Background**: *0.0 - 1.0*Affects blending of tiles with background. No conforming means heightmaps stay rigid, conforming measn the follow background shape. Good for leaves vs sticks for example.
  * **Smooth Conformed Background**: *0.0 - 2.0*Smoothing value for previous effect, to avoid incorrect or extreme variations.
  * **Skew from Bg Slope**: *0.0 - 1.0*Adjust/ slope tile height driven by Background slope (calculated normal).
  * **Background Slope Smoothness**: *0.0 - 2.0*Smoothing value for previous effect, to avoid incorrect or extreme variations.
  * **Cutout Black Pixels**: *False/True*Toggle to ignore full black (0) pixels from tile base shapes.
  * **Flatten Pattern Base**: *False/True*Adjusts tile blending behaviour with background: tiles will either intersect with background (False) or override the background when lower.
* **Masking**   
  * **Mask Random**: *0.0 - 1.0*Randomly hides tiles. The higher this value, the more tiles will disappear.
  * **Mask Random Map Multiplier**: *0.0 - 1.0*Treshold for mask map when to start hiding tiles.
  * **Mask from Bg Slope**: *-1.0 - 1.0*Uses Background map slope (calculated Normal) to hide tiles.

## Example Images

</td>
</tr>
</table>

 