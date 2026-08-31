---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/tile-sampler.html"
breadcrumb-title: ""
description: Use the Tile Sampler node to sample and arrange tiles from input textures to create tiled patterns in Substance 3D Designer.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Tile Sampler
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Tile Sampler
user-guide-description: ""
user-guide-title: ""
---

# Tile Sampler

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](tile-sampler.resources/tile-sampler-01.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Tile Sampler is the ultimate tile-pattern generating node. It's an evolved, more complex version of [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md). As of 2017 2.1, the differences are much smaller between Tile Sampler and [Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md). The main differences are now only in the seven different map slots which are available for driving Scale, Position, Rotation, Size, Color and Masking. Their effect can be blended in separately.

Tile Sampler is useful for creating man-made procedural patterns, with additional control over certain parameters driven by external input maps.

Make sure you are familiar with [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md) before moving on to Tile Sampler. In most cases, you'll find [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md) suffices and you won't need the added complexity of Tile Sampler.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Pattern Input 1-6</b> <i>Grayscale Input / Color Input</i> | Custom pattern image, used when the "Pattern" parameter is set to "Image Input".<br><br>The amount of available inputs is determined by the <b>Pattern Input Number</b> parameter. |
| <b>Scale Map Input</b> <i>Grayscale Input</i> | Grayscale map to drive tile scaling. |
| <b>Displacement Map Input</b> <i>Grayscale Input</i> | Grayscale map to drive tile displacement. |
| <b>Rotation Map Input</b> <i>Grayscale Input</i> | Grayscale map to drive tile rotation. |
| <b>Vector Map Input</b> <i>Color Input</i> | Color vector map to drive non-uniform scaling. |
| <b>Color Map Input</b> <i>Grayscale Input / Color Input</i> | Map to drive per-tile tinting. |
| <b>Mask Map Input</b> <i>Grayscale Input</i> | Mask slot used for hiding certain tiles. |
| <b>Pattern Distribution Map Input</b> <i>Grayscale Input</i> | Mask slot used to drive multiple custom pattern inputs. |
| <b>Background Input</b> <i>Grayscale Input / Color Input</i> | Optional background image. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>X Amount</b> <i>0 - 64</i> | Amount of X-repetitions of the pattern. |
| <b>Y Amount</b> <i>0 - 64</i> | Amount of Y-repetitions of the pattern. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |
| <b>Pattern</b> |  |
| <b>Pattern</b> <i>Pattern Input, Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half bell, Ridged Bell, Crescent, Capsule, Cone</i> | Selects what pattern shape to use. |
| <b>Pattern Input Number</b> <i>1 - 6</i> | Amount of custom patterns to randomly choose from. |
| <b>Pattern Input Distribution</b> <i>Random, Pattern Number, Distribution Map</i> | Sets how multiple Pattern Inputs are chosen. Random means a random one is chosen, Pattern Number means they are just placed in a looping sequence. Distribution map uses a grayscale map input to drive placement. |
| <b>Pattern Input Filtering (Engine &gt; v4)</b> <i>Bilinear + Mipmaps, Bilinear, Nearest</i> |  |
| <b>Pattern Specific</b> <i>0.0 - 1.0</i> | Lets you change the selected pattern's shape. The effect is dependent on the selected pattern. |
| <b>Pattern Specific Random</b> <i>0.0 - 1.0</i> | The randomization effect is dependent on the selected pattern. |
| <b>Rotation</b> <i>0, 90, 180, 270</i> | Stepped rotation (90 degree). |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Random free-rotation on a per-tile basis. |
| <b>Symmetry Random</b> <i>0.0 - 1.0</i> | Sets the number of tiles that should be randomly flipped/mirrored according to below behaviour. |
| <b>Symmetry Random Mode</b> <i>Horizontal + Vertical, Horizontal, Vertical</i> | Determines symmetry mirroring behaviour. |
| <b>Size</b> |  |
| <b>Size Mode</b> <i>Normal, Keep Ratio, Absolute, Pixel</i> | Sets general behavior of the pattern size.<br><br>Normal lets you define the size of the pattern elements. It is affected by the X and Y amount.<br><br>Keep Ratio lets you set a size affected by X and Y amount, but the X and Y ratio between the two is left intact.<br><br>Absolute lets you set an absolute size that is not affected by X and Y amount.<br><br>Pixel lets you set an absolute size in pixels, unaffected by X and Y amount. Changing the resolution will affect the size of the elements. |
| <b>Size (Absolute/Pixel)</b> <i>0.0 - 1.0</i> | Changes non-uniform proportions for tiles. Exact behaviour depends on Size Mode. |
| <b>Size Random</b> <i>0.0 - 1.0</i> | Randomizes proportions per-tile. |
| <b>Scale</b> <i>0.0 - 10.0</i> | Sets global tile scale. |
| <b>Scale Random</b> <i>0.0 - 1.0</i> | Randomizes scale per-tile. |
| <b>Scale Map Multiplier</b> <i>0.0 - 1.0</i> | Blends in the effect of the Scale map. |
| <b>Scale Vector Map Multiplier</b> <i>0.0 - 1.0</i> | Blends in the effect of the scale vector map to drive non-uniform scaling. |
| <b>Scale Parametrization Affect</b> <i>X and Y, X, Y</i> | Sets which axes the scale parametrization affects. Can be used to have Scale map only affect X or Y of elements. |
| <b>Position</b> |  |
| <b>Position Random</b> <i>0.0 - 10.0</i> | Randomizes tile position over both axes. |
| <b>Offset</b> <i>0.0 - 1.0</i> | Shifts tiles depending on Offset Type. |
| <b>Offset Type</b> <i>horizontal quincux, vertical quincux, horizontal global, vertical global</i> | Changes which direction the Offset operates in. |
| <b>Global Offset</b> <i>0.0 - 1.0</i> | Globally offsets all tiles on X- or Y-axis. |
| <b>Displacement Map Intensity</b> <i>0.0 - 1.0</i> | Blends in the strength of the Displacement map on the Offset. |
| <b>Displacement Angle</b> <i>0.0 - 1.0</i> | Sets the angle at which to displace. |
| <b>Vector Map Displacement</b> <i>0.0 - 1.0</i> | Uses Vector map to drive displacement and Angle. |
| <b>Rotation</b> |  |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Globally rotates all tiles. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Rotates randomly per-tile. |
| <b>Rotation Map Multiplier</b> <i>0.0 - 1.0</i> | Blends in the effect of Rotation map on per-Tile rotation. |
| <b>Vector Map Multiplier</b> <i>0.0 - 1.0</i> | Uses Vector Map to drive per-tile rotation. |
| <b>Color</b> |  |
| <b>Mask Map Threshold</b> <i>0.0 - 1.0</i> | Threshold for mask map when to start hiding tiles. |
| <b>Mask Map Invert</b> <i>False/True</i> | Inverts Mask map effect. |
| <b>Mask Map Sampling Technique</b> <i>Pattern Center, Pattern Bounding Box (slower)</i> | Whether hiding should be determined by a single point or by a bounding box. Avoids stray pixels causing strange effects. |
| <b>Mask Random</b> <i>0.0 - 1.0</i> | Random masking, works parallel to mask map. |
| <b>Invert Mask</b> <i>False/True</i> | Inverts random masking. |
| <b>Blending Mode</b> <i>Add/Sub, Max (Tile Sampler) / Add/Sub, Alpha Blend (Tile Sampler Color)</i> | Blend mode for tiles onto background and each other. |
| <b>Color</b> <i>(Grayscale value) / (Color value)</i> | Solid, global tile color. |
| <b>Color/Luminance Random</b> <i>0.0 - 1.0</i> | Randomization of color, per-tile. |
| <b>Color Parametrization Mode</b> <i>Color Input, Scale, Line Index, Row Index, Pattern Index (Tile Sampler) / Color Map, Scale, Line Index, Row Index, Pattern Index, Pattern Center Position, Pattern Center Position (RG) Bsphere Size (B) (Tile Sampler Color)</i> | Sets how exactly color randomization is parametrised. |
| <b>Color Parametrization Multiplier</b> <i>0.0 - 1.0</i> | Blends in the above Parametrization effect. |
| <b>Color Parametrization Affect (Color only)</b> <i>RGB+Alpha, RGB only, Alpha only</i> | Sets how the Parametrization affects color. |
| <b>Global Opacity (Grayscale only)</b> <i>0.0 - 1.0</i> | Sets global tile opacity. |
| <b>Background Color</b> <i>(Grayscale value) / (Color value)</i> | Sets solid background color. |
| <b>Reverse Rendering Order</b> <i>False/True</i> | Reverses rendering order to go from back to front. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="tile-sampler.resources/tile-sampler-02.png" /><br><i>Example shows how parameters are driven by input maps (Pattern Distribution, Scale, Rotation).</i>
        </td>
    </tr>
</table>
