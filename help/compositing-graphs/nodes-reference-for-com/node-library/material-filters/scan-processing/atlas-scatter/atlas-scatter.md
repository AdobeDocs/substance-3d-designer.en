---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/atlas-scatter.html"
breadcrumb-title: ""
description: Use the Atlas Scatter node to scatter textures across an atlas for creating tiled patterns from scanned materials.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Atlas Scatter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Atlas Scatter
user-guide-description: ""
user-guide-title: ""
---

# Atlas Scatter

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](atlas-scatter.resources/atlas-scatter-01.png){width="200px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Extract elements from an Atlas and scatter them on a background. Atlas inputs are full materials, consisting of individual elements arranged and packed on a single texture sheet. This node splits them up (using an internal [Atlas Splitter](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/atlas-splitter/atlas-splitter.md) process) and scatters them, similar to [Shape Splatter](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter/shape-splatter.md). Atlas Scatter requires at minimum an Opacity map input , and a Height map input for the Atlas, to function.

</td>
</tr>
</table>

>[!NOTE]
>
> Hundreds of [Atlases](https://source.substance3d.com/allassets?assetType=substanceAtlas), ready for use in the Atlas Scatter node, are available on [Substance Source](https://source.substance3d.com/).

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Atlas Input Resolution</b> <i>Resolution, 1 to 12</i> | Manually set the resolution of the full input atlas, to ensure a good performance vs quality ratio. |
| <b>X Amount</b> <i>1 - 64</i> | Amount of X repetitions of the pattern. |
| <b>Y Amount</b> <i>1 - 64</i> | Amount of Y repetitions of the pattern. |
| <b>Pattern</b> |  |
| <b>Pattern Range</b> <i>0 - 10</i> | Defines the range of patterns to be scattered. If set to 0, all patterns will be used. |
| <b>Pattern Distribution Mode</b> <i>Random, Pattern Index, Line Index, Column Index</i> | Defines the order in which atlas elements are used. |
| <b>Pattern Distribution Map Multiplier</b> <i>0.0 - 1.0</i> | Select shape pattern in function of the input image grayscale value. |
| <b>Pattern Rotation</b> <i>0, 90, 180, 270</i> | Applies a fixed rotation to each atlas element, by the selected amount of degrees. |
| <b>Pattern Rotation Random</b> <i>0.0 - 1.0</i> | Applies a random rotation to the set portion of atlas elements. |
| <b>Atlas Shape Detection Precision</b> <i>Simple or small shapes, Complex or big shapes, No failure mode</i> | Sets the precision with which shapes are detected. The greater the accuracy, the greater the impact on performance. |
| <b>Downscale Atlas Opacity (faster detection)</b> <i>-4 - 0</i> | Lets you control the downscale ratio of the input atlas opacity map, which is used for shape detection. A lower resolution improves performance at the cost of accuracy. |
| <b>Ignore Shape Smaller Than</b> <i>0.0 - 1.0</i> | Sets the minimum size a shape has to be to be detected, expressed as ratio of the overall image |
| <b>Size</b> |  |
| <b>Scale</b> <i>0.0 - 5.0</i> | Sets the relative scale of scattered shapes. |
| <b>Scale Random</b> <i>0.0 - 1.0</i> | Defines the multiplier for applying random scaling to each scattered shape. |
| <b>Scale No Overlap</b> <i>0.0 - 1.0</i> | Reduces the shape scale so that they don't overlap. |
| <b>Scale Map Multiplier</b> <i>0.0 - 1.0</i> | Multiplies the shape scale in function of the input image grayscale value. |
| <b>Size</b> <i>0.0 - 1.0</i> | Sets the relative scale of scattered shapes by length (X) and width (Y). |
| <b>Size Ratio from Bg Slope</b> <i>0.0 - 1.0</i> | Modifies the shape size ratio in function of the background height slope. |
| <b>Preserve Aspect Ratio</b> <i>0.0 - 1.0</i> | Determines by which amount the original proportions of the scattered shapes should be preserved, instead of using their grid cell ratio – i.e. the ratio of the X Amount and Y Amount values. |
| <b>Position</b> |  |
| <b>Position Random</b> <i>0.0 - 2.0</i> | A multiplier for moving each shape in a random direction from their grid starting point. |
| <b>Random Distribution</b> <i>Gaussian, Uniform</i> | Switches from a Gaussian distribution to a Uniform Distribution for the random position. The Gaussian distribution will produce a more organic result compared to the Uniform distribution. |
| <b>Vector Map Multiplier</b> <i>0.0 - 1.0</i> | Controls the influence of the vector map input for moving the shapes in the direction of the vector specified by the map's red (X) and green (Y) channels. |
| <b>Offset Horizontal</b> <i>-2.0 - 2.0</i> | A multiplier for position offset along the X axis. |
| <b>Offset Vertical</b> <i>-2.0 - 2.0</i> | A multiplier for position offset along the Y axis. |
| <b>Out of Bounds Option</b> <i>Scale Shape, Constrain Position</i> | Due to the technical nature of the splatter, shapes can't be drawn more than 2 cells size away from their original position. If a shape becomes too large or is moved too far you have two options: - Scale Shape will reduce the shape size when it hit a bound - Constrain Position will move the shape back to its original position |
| <b>Rotation</b> |  |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Lets you control the local rotation for all shapes. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | A multiplier for a random amount of rotation applied per shape. |
| <b>Rotation from Bg Slope</b> <i>0.0 - 1.0</i> | Modifies the shape rotation in function of the background height slope. Usually used in combination with the "Size Ratio from Bg Slope" parameter |
| <b>Rotation Map Multiplier</b> <i>0.0 - 1.0</i> | Multiplies the shape rotation in function of the input image grayscale value. |
| <b>Vector Map Multiplier</b> <i>0.0 - 1.0</i> | Sets the shape rotation in function of the vector image input. |
| <b>Height</b> |  |
| <b>Height Scale Auto Adjust</b> <i>False/True</i> | Automatically adjust the height in function of the pattern scale to keep the shape height proportional to the background height. |
| <b>Blend Mode</b> <i>Height Blend, Alpha Test</i> | Sets the method for solving shapes overlaps. |
| <b>Height Offset</b> <i>-1.0 - 1.0</i> | Applies a global offset to the shapes height |
| <b>Height Offset Random</b> <i>0.0 - 1.0</i> | A multiplier for a random height offset applied per shape |
| <b>Height Offset Map Mulitplier</b> <i>0.0 - 1.0</i> | Multiplies the shape height offset in function of the input image grayscale value. |
| <b>Height Scale</b> <i>0.0 - 1.0</i> | Lets you control the global height scale for the scattered shapes |
| <b>Height Scale Random</b> <i>0.0 - 1.0</i> | A multiplier for a random height scale applied per shape |
| <b>Height Scale Map Multiplier</b> <i>0.0 - 1.0</i> | Multiplies the shape height scale in function of the input image grayscale value. |
| <b>Conform to Background</b> <i>0.0 - 1.0</i> | At 0, the shape height remains intact, at 1 the shape height will be deformed by the underlying height background. |
| <b>Smooth Conformed Background</b> <i>0.0 - 2.0</i> | Lets you control the amount of smoothing applied to the height deformation of the shape when it is conformed to its background. |
| <b>Skew from Bg Slope</b> <i>0.0 - 1.0</i> | Deforms the shape height in function of the local background height slope: a linear gradient corresponding to the background slope is added to the shape height. |
| <b>Background Slope Smoothness</b> <i>0.0 - 2.0</i> | Controls the amount of smoothing applied to the background slope when the shape is skewed based on that slope. |
| <b>Cutout Black Pixels</b> <i>False/True</i> | Ignores the black value from the pattern inputs. |
| <b>Flatten Pattern Base</b> <i>False/True</i> | Lets you flatten the background height beneath a shape to match is starting height. |
| <b>Masking</b> |  |
| <b>Mask Random</b> <i>0.0 - 1.0</i> | Masks a random amount of shapes, expressed as a ratio of the total amount. |
| <b>Mask Random Map Multiplier</b> <i>0.0 - 1.0</i> | Sets the random shape masking in function of the grayscale image input. |
| <b>Mask from Bg Slope</b> <i>-1.0 - 1.0</i> | Controls the masking of the shapes based on the slope of the background at their location. |
| <b>Color</b> |  |
| <b>Color Adjustment</b> <i>-1.0 - 1.0</i> | Lets you adjust the colors for the scattered elements globally. |
| <b>Color Random</b> <i>0.0 - 1.0</i> | A multiplier for shifting the color values by a random amount per shape. |
| <b>Color from Background</b> <i>0.0 - 1.0</i> | Shifts the shape colors to the color of the background at their location. |
| <b>Normal</b> |  |
| <b>Skew from Bg Slope</b> <i>0.0 - 1.0</i> | Skew the shape normal according to the background normal. |
| <b>Normal Random</b> <i>0.0 - 1.0</i> | A multiplier for skewing the shape normal by a random amount per shape. |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switch between different Normal Map formats (inverts the green channel) |
| <b>Roughness</b> |  |
| <b>Roughness Adjustment</b> <i>-1.0 - 1.0</i> | Lets you offset the global shape roughness. |
| <b>Roughness from Background</b> <i>0.0 - 1.0</i> | Shifts the shapes roughness to the background roughness at their location. |
| <b>Roughness Random</b> <i>0.0 - 1.0</i> | A multiplier for offsetting the roughness by a random amount per shape. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="atlas-scatter.resources/atlas-scatter-02.png" />
        </td>
    </tr>
</table>
