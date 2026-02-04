---
title: "Atlas Scatter | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Atlas Scatter"
---

# Atlas Scatter

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](atlas-scatter.png){width="200px"}

## Atlas Scatter

**In:** *Material Filters/Scan Processing*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Extract elements from an Atlas and scatter them on a background. Atlas inputs are full materials, consisting of individual elements arranged and packed on a single texture sheet. This node splits them up (using an internal [Atlas Splitter](../atlas-splitter/atlas-splitter.md) process) and scatters them, similar to [Shape Splatter](../../../texture-generators/patterns/shape-splatter/shape-splatter.md). Atlas Scatter requires at minimum an Opacity map input , and a Height map input for the Atlas, to function.

>[!NOTE]
>
> Hundreds of [Atlases](https://source.substance3d.com/allassets?assetType=substanceAtlas), ready for use in the Atlas Scatter node, are available on [Substance Source](https://source.substance3d.com/).

## Inputs &amp; Parameters

### Parameters

* **Atlas Input Resolution**: *Resolution, 1 to 12*  
  Manually set the resolution of the full input atlas, to ensure a good performance vs quality ratio.
* **X Amount**: *1 - 64*  
  Amount of X repetitions of the pattern.
* **Y Amount**: *1 - 64*  
  Amount of Y repetitions of the pattern.
* **Pattern**   
  * **Pattern Range**: *0 - 10*  
    Defines the range of patterns to be scattered. If set to 0, all patterns will be used.
  * **Pattern Distribution Mode**: *Random, Pattern Index, Line Index, Column Index*Defines the order in which atlas elements are used.
  * **Pattern Distribution Map Multiplier**: *0.0 - 1.0*  
    Select shape pattern in function of the input image grayscale value.
  * **Pattern Rotation**: *0, 90, 180, 270*  
    Applies a fixed rotation to each atlas element, by the selected amount of degrees.
  * **Pattern Rotation Random**: *0.0 - 1.0*  
    Applies a random rotation to the set portion of atlas elements.
  * **Atlas Shape Detection Precision**: *Simple or small shapes, Complex or big shapes, No failure mode*  
    Sets the precision with which shapes are detected. The greater the accuracy, the greater the impact on performance.
  * **Downscale Atlas Opacity (faster detection)**: *-4 - 0*  
    Lets you control the downscale ratio of the input atlas opacity map, which is used for shape detection. A lower resolution improves performance at the cost of accuracy.
  * **Ignore Shape Smaller Than**: *0.0 - 1.0*Sets the minimum size a shape has to be to be detected, expressed as ratio of the overall image
* **Size**   
  * **Scale**: *0.0 - 5.0*  
    Sets the relative scale of scattered shapes.
  * **Scale Random**: *0.0 - 1.0*  
    Defines the multiplier for applying random scaling to each scattered shape.
  * **Scale No Overlap**: *0.0 - 1.0*  
    Reduces the shape scale so that they don't overlap.
  * **Scale Map Multiplier**: *0.0 - 1.0*  
    Multiplies the shape scale in function of the input image grayscale value.
  * **Size**: *0.0 - 1.0*  
    Sets the relative scale of scattered shapes by length (X) and width (Y).
  * **Size Ratio from Bg Slope**: *0.0 - 1.0*  
    Modifies the shape size ratio in function of the background height slope.
  * **Preserve Aspect Ratio**: *0.0 - 1.0*  
    Determines by which amount the original proportions of the scattered shapes should be preserved, instead of using their grid cell ratio – i.e. the ratio of the X Amount and Y Amount values.
* **Position**   
  * **Position Random**: *0.0 - 2.0*  
    A multiplier for moving each shape in a random direction from their grid starting point.
  * **Random Distribution**: *Gaussian, Uniform*  
    Switches from a Gaussian distribution to a Uniform Distribution for the random position. The Gaussian distribution will produce a more organic result compared to the Uniform distribution.
  * **Vector Map Multiplier**: *0.0 - 1.0*  
    Controls the influence of the vector map input for moving the shapes in the direction of the vector specified by the map's red (X) and green (Y) channels.
  * **Offset Horizontal**: *-2.0 - 2.0*  
    A multiplier for position offset along the X axis.
  * **Offset Vertical**: *-2.0 - 2.0*  
    A multiplier for position offset along the Y axis.
  * **Out of Bounds Option**: *Scale Shape, Constrain Position*  
    Due to the technical nature of the splatter, shapes can't be drawn more than 2 cells size away from their original position. If a shape becomes too large or is moved too far you have two options: - Scale Shape will reduce the shape size when it hit a bound - Constrain Position will move the shape back to its original position
* **Rotation**   
  * **Rotation**: *0.0 - 1.0*  
    Lets you control the local rotation for all shapes.
  * **Rotation Random**: *0.0 - 1.0*  
    A multiplier for a random amount of rotation applied per shape.
  * **Rotation from Bg Slope**: *0.0 - 1.0*  
    Modifies the shape rotation in function of the background height slope. Usually used in combination with the "Size Ratio from Bg Slope" parameter
  * **Rotation Map Multiplier**: *0.0 - 1.0*  
    Multiplies the shape rotation in function of the input image grayscale value.
  * **Vector Map Multiplier**: *0.0 - 1.0*  
    Sets the shape rotation in function of the vector image input.
* **Height**   
  * **Height Scale Auto Adjust**: *False/True*  
    Automatically adjust the height in function of the pattern scale to keep the shape height proportional to the background height.
  * **Blend Mode**: *Height Blend, Alpha Test*  
    Sets the method for solving shapes overlaps.
  * **Height Offset**: *-1.0 - 1.0*  
    Applies a global offset to the shapes height
  * **Height Offset Random**: *0.0 - 1.0*  
    A multiplier for a random height offset applied per shape
  * **Height Offset Map Mulitplier**: *0.0 - 1.0*  
    Multiplies the shape height offset in function of the input image grayscale value.
  * **Height Scale**: *0.0 - 1.0*  
    Lets you control the global height scale for the scattered shapes
  * **Height Scale Random**: *0.0 - 1.0*  
    A multiplier for a random height scale applied per shape
  * **Height Scale Map Multiplier**: *0.0 - 1.0*  
    Multiplies the shape height scale in function of the input image grayscale value.
  * **Conform to Background**: *0.0 - 1.0*  
    At 0, the shape height remains intact, at 1 the shape height will be deformed by the underlying height background.
  * **Smooth Conformed Background**: *0.0 - 2.0*  
    Lets you control the amount of smoothing applied to the height deformation of the shape when it is conformed to its background.
  * **Skew from Bg Slope**: *0.0 - 1.0*  
    Deforms the shape height in function of the local background height slope: a linear gradient corresponding to the background slope is added to the shape height.
  * **Background Slope Smoothness**: *0.0 - 2.0*  
    Controls the amount of smoothing applied to the background slope when the shape is skewed based on that slope.
  * **Cutout Black Pixels**: *False/True*  
    Ignores the black value from the pattern inputs.
  * **Flatten Pattern Base**: *False/True*  
    Lets you flatten the background height beneath a shape to match is starting height.
* **Masking**   
  * **Mask Random**: *0.0 - 1.0*  
    Masks a random amount of shapes, expressed as a ratio of the total amount.
  * **Mask Random Map Multiplier**: *0.0 - 1.0*  
    Sets the random shape masking in function of the grayscale image input.
  * **Mask from Bg Slope**: *-1.0 - 1.0*  
    Controls the masking of the shapes based on the slope of the background at their location.
* **Color**   
  * **Color Adjustment**: *-1.0 - 1.0*  
    Lets you adjust the colors for the scattered elements globally.
  * **Color Random**: *0.0 - 1.0*  
    A multiplier for shifting the color values by a random amount per shape.
  * **Color from Background**: *0.0 - 1.0*  
    Shifts the shape colors to the color of the background at their location.
* **Normal**   
  * **Skew from Bg Slope**: *0.0 - 1.0*  
    Skew the shape normal according to the background normal.
  * **Normal Random**: *0.0 - 1.0*  
    A multiplier for skewing the shape normal by a random amount per shape.
  * **Normal Format**: *DirectX, OpenGL*  
    Switch between different Normal Map formats (inverts the green channel)
* **Roughness**   
  * **Roughness Adjustment**: *-1.0 - 1.0*  
    Lets you offset the global shape roughness.
  * **Roughness from Background**: *0.0 - 1.0*  
    Shifts the shapes roughness to the background roughness at their location.
  * **Roughness Random**: *0.0 - 1.0*A multiplier for offsetting the roughness by a random amount per shape.

## Example Images

![](atlas-scatter-11.png){width="512px"}

</td>
</tr>
</table>

 