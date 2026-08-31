---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/splatter.html"
breadcrumb-title: ""
description: Use the Splatter node to scatter shapes across textures for creating random patterns and organic texture details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Splatter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Splatter
user-guide-description: ""
user-guide-title: ""
---

# Splatter

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](splatter.resources/splatter-01.png)

![](splatter.resources/splatter-02.png)

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Splatter is a pattern generator intended for random placement of a map input. It has many controls for geometrically patterned placement, and is simpler in use than [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md). The latter can achieve similar results, but is much more complex.

Splatter works well for quickly getting some shapes stamped down, without needing too much tweaking.

Keep in mind that the default Splatter parameters do not look random at all: you need to tweak a few of them to get randomisation (mainly Disorder parameters). Also keep in mind that Splatter requires a map input to work.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Pattern Size Width</b> <i>0.0 - 1000.0</i> | Number of patterns to use on the X-axis. |
| <b>Pattern Size Height</b> <i>0.0 - 1000.0</i> | Number of patterns to use on the Y-axis. |
| <b>Rotation</b> <i>-360.0 - 360.0</i> | Rotates every pattern by a set amount. |
| <b>Rotation Variation</b> <i>0.0 - 360.0</i> | Introduces random rotation for every separate shape. |
| <b>Zoom</b> <i>100.0 - 10000.0</i> | Scales up the final result. Keep in mind that this breaks tiling! |
| <b>Gain</b> <i>0.0 - 10.0</i> | Adjusts blending gain of every pattern. Makes them stand out more. |
| <b>Pan X</b> <i>-100.0 - 100.0</i> | Pans whole result on X-axis. |
| <b>Pan Y</b> <i>-100.0 - 100.0</i> | Pans whole result on Y-axis. |
| <b>Disorder</b> <i>0.0 - 100.0</i> | Randomly shifts shapes. |
| <b>Grid Number</b> <i>0 - 8</i> | Jumps through different grid sizes to adjust result scale. Maintains tiling. |
| <b>Disorder Angle</b> <i>0.0 - 360.0</i> | Controls the angle of disorder shifting. |
| <b>Disorder Random</b> <i>False/True</i> | Randomises the disorder angle, adding much more chaos. |
| <b>Pattern Size</b> <i>5 - 12</i> |  |
| <b>Size Variation</b> <i>0.0 - 100.0</i> | Introduces random scaling for every shape. |
| <b>Image Input Filtering (Engine &gt; v4 only)</b> <i>Bilinear + Mipmaps, Bilinear, Nearest</i> | Which filtering to apply to the input image. |
| <b>Output Level Min</b> <i>0.0 - 1.0</i> | Out minimum level adjustment. |
| <b>Output Level Max</b> <i>0.0 - 1.0</i> | Out maximum level adjustment. |
| <b>Background Color</b> <i>(Grayscale value)</i> | Sets solid background color. |
| <b>Luminance Variation</b> <i>0.0 - 1.0 (Grayscale version only)</i> | Introduces luminance variation. |
| <b>Color Variation</b> <i>0.0 - 1.0 (Color Version Only)</i> | Introduces color variation. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="splatter.resources/splatter-03.gif" />
        </td>
    </tr>
</table>
