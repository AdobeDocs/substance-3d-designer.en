---
title: "Tile Sampler | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Tile Sampler"
---

# Tile Sampler

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](tile-sampler.png){width="128px"}

## Tile Sampler (Color)

**In:** *Texture Generators**/Patterns*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Tile Sampler is the ultimate tile-pattern generating node. It's an evolved, more complex version of [Tile Generator](../tile-generator/tile-generator.md). As of 2017 2.1, the differences are much smaller between Tile Sampler and [Generator](../tile-generator/tile-generator.md). The main differences are now only in the seven different map slots which are available for driving Scale, Position, Rotation, Size, Color and Masking. Their effect can be blended in separately.

Tile Sampler is useful for creating man-made procedural patterns, with additional control over certain parameters driven by external input maps.

Make sure you are familiar with [Tile Generator](../tile-generator/tile-generator.md) before moving on to Tile Sampler. In most cases, you'll find [Tile Generator](../tile-generator/tile-generator.md) suffices and you won't need the added complexity of Tile Sampler.

## Parameters

### Inputs

* **Pattern Input 1-6**: *Grayscale Input / Color Input*  
  Custom pattern image, used when the "Pattern" parameter is set to "Image Input".  
  The amount of available inputs is determined by the **Pattern Input Number** parameter.
* **Scale Map Input**: *Grayscale Input*Grayscale map to drive tile scaling.
* **Displacement Map Input**: *Grayscale Input*Grayscale map to drive tile displacement.
* **Rotation Map Input**: *Grayscale Input*   
  Grayscale map to drive tile rotation.
* **Vector Map Input**: *Color Input*   
  Color vector map to drive non-uniform scaling.
* **Color Map Input**: *Grayscale Input / Color Input*Map to drive per-tile tinting.
* **Mask Map Input**: *Grayscale Input*   
  Mask slot used for hiding certain tiles.
* **Pattern Distribution Map Input**: *Grayscale Input*   
  Mask slot used to drive multiple custom pattern inputs.
* **Background Input**: *Grayscale Input / Color Input*Optional background image.

### Parameters

* **X Amount**: *0 - 64*  
  Amount of X-repetitions of the pattern.
* **Y Amount**: *0 - 64*  
  Amount of Y-repetitions of the pattern.
* **Non Square Expansion**: *False/True*  
  Enables compensation of squash and stretch with non-square ratios.
* **Pattern**   
  * **Pattern**: *Pattern Input, Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half bell, Ridged Bell, Crescent, Capsule, Cone*  
    Selects what pattern shape to use.
  * **Pattern Input Number**: *1 - 6*Amount of custom patterns to randomly choose from.
  * **Pattern Input Distribution**: *Random, Pattern Number, Distribution Map*Sets how multiple Pattern Inputs are chosen. Random means a random one is chosen, Pattern Number means they are just placed in a looping sequence. Distribution map uses a grayscale map input to drive placement.
  * **Pattern Input Filtering (Engine &gt; v4)**: *Bilinear + Mipmaps, Bilinear, Nearest*
  * **Pattern Specific**: *0.0 - 1.0*  
    Lets you change the selected pattern's shape. The effect is dependent on the selected pattern.
  * **Pattern Specific Random**: *0.0 - 1.0*The randomization effect is dependent on the selected pattern.
  * **Rotation**: *0, 90, 180, 270*Stepped rotation (90 degree).
  * **Rotation Random**: *0.0 - 1.0*Random free-rotation on a per-tile basis.
  * **Symmetry Random**: *0.0 - 1.0*Sets the number of tiles that should be randomly flipped/mirrored according to below behaviour.
  * **Symmetry Random Mode**: *Horizontal + Vertical, Horizontal, Vertical*Determines symmetry mirroring behaviour.
* **Size**
  * **Size Mode**: *Normal, Keep Ratio, Absolute, Pixel*Sets general behavior of the pattern size.  
    Normal lets you define the size of the pattern elements. It is affected by the X and Y amount.  
    Keep Ratio lets you set a size affected by X and Y amount, but the X and Y ratio between the two is left intact.  
    Absolute lets you set an absolute size that is not affected by X and Y amount.  
    Pixel lets you set an absolute size in pixels, unaffected by X and Y amount. Changing the resolution will affect the size of the elements.
  * **Size (Absolute/Pixel)**: *0.0 - 1.0*Changes non-uniform proportions for tiles. Exact behaviour depends on Size Mode.
  * **Size Random**: *0.0 - 1.0*Randomizes proportions per-tile.
  * **Scale**: *0.0 - 10.0*Sets global tile scale.
  * **Scale Random**: *0.0 - 1.0*Randomizes scale per-tile
  * **Scale Map Multiplier**: *0.0 - 1.0*Blends in the effect of the Scale map.
  * **Scale Vector Map Multiplier**: *0.0 - 1.0*Blends in the effect of the scale vector map to drive non-uniform scaling.
  * **Scale Parametrization Affect**: *X and Y, X, Y*Sets which axes the scale parametrization affects. Can be used to have Scale map only affect X or Y of elements.
* **Position**   
  * **Position Random**: *0.0 - 10.0*Randomizes tile position over both axes.
  * **Offset**: *0.0 - 1.0*  
    Shifts tiles depending on Offset Type.
  * **Offset Type**: *horizontal quincux, vertical quincux, horizontal global, vertical global*Changes which direction the Offset operates in.
  * **Global Offset**: *0.0 - 1.0*Globally offsets all tiles on X- or Y-axis.
  * **Displacement Map Intensity**: *0.0 - 1.0*Blends in the strength of the Displacement map on the Offset.
  * **Displacement Angle**: *0.0 - 1.0*Sets the angle at which to displace.
  * **Vector Map Displacement**: *0.0 - 1.0*Uses Vector map to drive displacement and Angle.
* **Rotation**   
  * **Rotation**: *0.0 - 1.0*Globally rotates all tiles.
  * **Rotation Random**: *0.0 - 1.0*Rotates randomly per-tile.
  * **Rotation Map Multiplier**: *0.0 - 1.0*Blends in the effect of Rotation map on per-Tile rotation.
  * **Vector Map Multiplier**: *0.0 - 1.0*Uses Vector Map to drive per-tile rotation.
* **Color**   
  * **Mask Map Threshold**: *0.0 - 1.0*Threshold for mask map when to start hiding tiles.
  * **Mask Map Invert**: *False/True*Inverts Mask map effect.
  * **Mask Map Sampling Technique**: *Pattern Center, Pattern Bounding Box (slower)*Whether hiding should be determined by a single point or by a bounding box. Avoids stray pixels causing strange effects.
  * **Mask Random**: *0.0 - 1.0*Random masking, works parallel to mask map.
  * **Invert Mask**: *False/True*Inverts random masking.
  * **Blending Mode**: *Add/Sub, Max (Tile Sampler) / *Add/Sub, Alpha Blend* (Tile Sampler Color)*Blend mode for tiles onto background and each other.
  * **Color**: *(Grayscale value) / (Color value)*Solid, global tile color.
  * **Color/Luminance Random**: *0.0 - 1.0*Randomization of color, per-tile.
  * **Color Parametrization Mode**: *Color Input, Scale, Line Index, Row Index, Pattern Index (Tile Sampler)*   
    */ *Color Map, Scale, Line Index, Row Index, Pattern Index, Pattern Center Position, Pattern Center Position (RG) Bsphere Size (B) (Tile Sampler Color)**Sets how exactly color randomization is parametrised.
  * **Color Parametrization Multiplier**: *0.0 - 1.0*Blends in the above Parametrization effect.
  * **Color Parametrization Affect (Color only):** **RGB+Alpha, RGB only, Alpha only**Sets how the Parametrization affects color.
  * **Global Opacity (Grayscale only)**: *0.0 - 1.0*Sets global tile opacity.
  * **Background Color**: *(Grayscale value) / (Color value)*Sets solid background color.
  * **Reverse Rendering Order**: *False/True*Reverses rendering order to go from back to front.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="tilesampler-ex2.png" width="256px"/></div> |
| --- |
|  |

*Example shows how parameters are driven by input maps (Pattern Distribution, Scale, Rotation).*

</td>
</tr>
</table>
