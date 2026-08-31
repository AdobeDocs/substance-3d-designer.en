---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/tile-random-2.html"
breadcrumb-title: ""
description: Use the Tile Random 2 node to create randomized tile patterns with advanced variation controls in Substance 3D Designer.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Tile Random 2
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Tile Random 2
user-guide-description: ""
user-guide-title: ""
---

# Tile Random 2

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](tile-random-2.resources/tile-random-2-01.jpg){width="200px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **Tile Random 2** node generates adjacent tiles of random sizes and height-to-width ratios.

The grid may be tweaked by randomly *slanting* the sides of the shapes to break up the angles.

Shapes may be adjusted with options for *scaling*, *bevelling*, *rounding of the corners* as well as *disorted rotation*.

These adjustments may be controlled by *input maps*.

A dedicated output lets you input the shape's **UVs** into **Flood Fill to (...)** nodes for applying additional variation.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Random Size Map</b> <i>Grayscale</i> | The grayscale input image which controls the random scale of the shapes.<br><br>Its impact is controlled by the <b>Random Size Input Map Multiplier</b> parameter. |
| <b>Random Slant Map</b> <i>Grayscale</i> | The grayscale input image which controls the random slanting of the shapes.<br><br>Its impact is controlled by the <b>Random Slant Input Map Multiplier</b> parameter. |
| <b>Round Corners Radius Map</b> <i>Grayscale</i> | The grayscale input image which controls the radius of the shapes' rounded corners.<br><br>Its impact is controlled by the <b>Round Corners Radius Input Map Mult.</b> parameter. |
| <b>Bevel Distance Map</b> <i>Grayscale</i> | The grayscale input image which controls the bevelling of the shapes.<br><br>Its impact is controlled by the <b>Bevel Distance Input Map Mult.</b> parameter. |
| <b>Mask Map</b> <i>Grayscale</i> | The grayscale input image which controls the masking of the shapes.<br><br>Its impact is controlled by the <b>Mask Map Input Start</b> and <b>Mask Map Input End</b> parameters. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Amount X</b> <i>Integer</i> | The number of cells on the <b>X</b> axis. |
| <b>Amount Y</b> <i>Integer</i> | The number of cells on the <b>Y</b> axis. |
| <b>Size</b> |  |
| <b>Random Size Multiplier</b> <i>Float</i> | Applies a <i>global</i> adjustment to the intensity of the random scaling. |
| <b>Random Size Input Map Multiplier</b> <i>Float</i> | Adjusts the intensity of the random scaling using the values <i>sampled</i> from the <b>Random Size Map</b> input. |
| <b>Random Size X</b> <i>Float</i> | Adjusts the intensity of the random scaling on the <b>X</b> axis <i>only</i>. |
| <b>Random Size Y</b> <i>Float</i> | Adjusts the intensity of the random scaling on the <b>Y</b> axis <i>only</i>. |
| <b>Random Size Distribution</b> <i>Integer</i> | Controls the method of distributing random scaling values:<br><br>- <i>Uniform</i>: the random scale is applied the <i>same way</i> on all cells<br>- <i>Blue Noise</i>: the random scale is <i>adjusted</i> using a blue noise pattern |
| <b>Shape Aspect - Transform</b> |  |
| <b>Interstice Thickness</b> <i>Float</i> | Adjusts the thickness of the gap between shapes. It is <i>equal for all</i> shapes. |
| <b>Random Position Multiplier</b> <i>Float</i> | Applies a random position offset to the shape up to it <i>meeting its cell's border</i>. |
| <b>Round Corners Radius</b> <i>Float</i> | Adjusts the <i>radius</i> of the rounded corners of the shapes. A value of <b>0</b> means no rounding is applied.<br><br><i>Note</i>: This effect cannot be applied when the <b>Enable per Axis Bevel Control</b> parameter is set to <i>True</i>. |
| <b>Round Corners Radius Input Map Mult.</b> <i>Float</i> | Adjusts the intensity by which the <b>Round Corners Radius Map</b> input map impacts the radius of the rounded corners.<br><br>The map acts as a <i>per-pixel</i> multiplier for the <b>Round Corners Radius</b> parameter.<br><br><i>Note</i>: This effect cannot be applied when the <b>Enable per Axis Bevel Control</b> parameter is set to <i>True</i>. |
| <b>Scale Multiplier</b> <i>Float</i> | Adjusts the size of each shape, as a proportion of the <i>area of its cell</i>. |
| <b>Scale Random</b> <i>Float</i> | Adjusts the intensity by which a random scale is applied to <i>each</i> shape. |
| <b>Rotation</b> <i>Float</i> | Rotates shapes in their cells by moving each <i>corner</i> to its <i>neighbour</i> along the cell's border.<br><br>This method results in some amount of <i>distortion</i> and <i>scaling</i> being applied to the shape at is rotates. |
| <b>Rotation Random</b> <i>Float</i> | Adjusts the intensity by which a random amount of rotation is applied to each shape.<br><br>The method of rotation is described in the <b>Rotation</b> parameter. |
| <b>Corners Position Random</b> <i>Float</i> | Distorts the shapes by applying a random amount of <i>offset</i> to each of their <i>corners</i> along their cell's border. |
| <b>Slant</b> |  |
| <b>Random Slant Multiplier</b> <i>Float</i> | Applies a <i>global</i> adjustment to the intensity of the random slanting. |
| <b>Random Slant Input Map Multiplier</b> <i>Float</i> | Adjusts the intensity of the random slanting using the values <i>sampled</i> from the <b>Random Slant Map</b> input. |
| <b>Random Slant X</b> <i>Float</i> | Adjusts the intensity of the random slanting on the <b>X</b> axis <i>only</i>. |
| <b>Random Slant Y</b> <i>Float</i> | Adjusts the intensity of the random slanting on the <b>Y</b> axis <i>only</i>. |
| <b>Random Slant Distribution</b> <i>Integer</i> | Controls the method of distributing random slanting values:<br><br>- <i>Uniform</i>: the random slant is applied the <i>same way</i> on all cells<br>- <i>Blue Noise</i>: the random slant is <i>adjusted</i> using a blue noise pattern |
| <b>Bevel</b> |  |
| <b>Bevel Distance Mode</b> <i>Integer</i> | Sets the method of <i>acquiring the distance</i> by which shapes should be beveled:<br><br>- <i>Relative to Grid Size</i>: Shapes are beveled by the specified <i>proportion of their grid size</i><br>- <i>Relative to Shape Size</i>: Shapes are beveled by the specified <i>proportion of their size</i><br>- <i>Relative to Image Size</i>: Shapes are beveled by the specified <i>proportion of the image</i> |
| <b>Bevel Distance Multiplier</b> <i>Float</i> | Applies a <i>global</i> adjustment to the distance of the bevelling. |
| <b>Bevel Distance Input Map Mult.</b> <i>Float</i> | Adjusts the distance of the bevelling using the <b>Bevel Distance Map</b> input map as a <i>per-pixel</i> multiplier. |
| <b>Bevel Rounded Curve</b> <i>Float</i> | Adjusts the intensity of the rounding applied to the bevelling angle to make it more <i>convex</i>. |
| <b>Enable per Axis Bevel Control</b> <i>Boolean</i> | When <i>True</i>, bevelling can be applied and adjusted <i>separately</i> on the <b>X</b> and <b>Y</b> axes.<br><br><i>Note</i>: This <i>cancels</i> the <b>Round Corners</b> effect. |
| <b>Bevel Distance X</b> <i>Float</i> | Adjusts the distance of the bevelling on the <b>X</b> axis <i>only</i>. This distance depends on the value of the <b>Bevel Distance Mode</b> parameter.<br><br><i>Note</i>: This parameter is only available when the <b>Enable per Axis Bevel Control</b> parameter is set to <i>True</i>. |
| <b>Bevel Distance Y</b> <i>Float</i> | Adjusts the distance of the bevelling on the <b>Y</b> axis <i>only</i>. This distance depends on the value of the <b>Bevel Distance Mode</b> parameter.<br><br><i>Note</i>: This parameter is only available when the <b>Enable per Axis Bevel Control</b> parameter is set to <i>True</i>. |
| <b>Mask</b> |  |
| <b>Mask Random Invert</b> <i>Boolean</i> | Inverts the random masking of shapes. |
| <b>Mask Random Start</b> <i>Float</i> | For a given <b>Random Seed</b>, pseudo-random masking is applied following a <i>specific order</i> from a start shape to an end shape. This parameter lets you <i>offset the index</i> of the <i>start</i> shape.<br><br><i>Note</i>: This determines one limit of a <i>value range</i> for masking. The value may therefore be <i>greater</i> than the <b>Mask Random End</b> value. |
| <b>Mask Random End</b> <i>Float</i> | For a given <b>Random Seed</b>, pseudo-random masking is applied following a <i>specific order</i> from a start shape to an end shape. This parameter lets you <i>offset the index</i> of the <i>end</i> shape.<br><br><i>Note</i>: This determines one limit of a <i>value range</i> for masking. The value may therefore be <i>greater</i> than the <b>Mask Random Start</b> value. |
| <b>Mask by Cell Area Invert</b> <i>Boolean</i> | Inverts the masking of shapes by the area of their cells. |
| <b>Mask by Cell Area Start</b> <i>Float</i> | Adjusts the <i>minimum</i> cell's area threshold for masking shapes.<br><br><i>Note</i>: This determines one limit of a <i>value range</i> for masking. The value may therefore be <i>greater</i> than the <b>Mask by Cell Area End</b> value. |
| <b>Mask by Cell Area End</b> <i>Float</i> | Adjusts the <i>maximum</i> cell's area threshold for masking shapes.<br><br><i>Note</i>: This determines one limit of a <i>value range</i> for masking. The value may therefore be <i>lower</i> than the <b>Mask by Cell Area Start</b> value. |
| <b>Mask Map Input Invert</b> <i>Boolean</i> | Inverts the masking of shapes by the <b>Mask Map</b> input map. |
| <b>Mask Map Input Start</b> <i>Float</i> | Adjusts the <i>minimum grayscale value</i> threshold in the <b>Mask Map</b> input map for masking shapes.<br><br><i>Note</i>: This determines one limit of a <i>value range</i> for masking. The value may therefore be <i>greater</i> than the <b>Mask Map Input End</b> value. |
| <b>Mask Map Input End</b> <i>Float</i> | Adjusts the <i>maximum grayscale value</i> threshold in the <b>Mask Map</b> input map for masking shapes.<br><br><i>Note</i>: This determines one limit of a <i>value range</i> for masking. The value may therefore be <i>lower</i> than the <b>Mask Map Input Start</b> value. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-02.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-03.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-04.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-05.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-06.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-07.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="tile-random-2.resources/tile-random-2-08.png" />
        </td>
    </tr>
</table>
