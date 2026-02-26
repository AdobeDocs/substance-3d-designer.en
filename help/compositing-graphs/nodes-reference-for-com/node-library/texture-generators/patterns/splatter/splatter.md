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
<td style="border: 0;" valign="top">

![](../../../../../../assets/splatter.png)

![](../../../../../../assets/splatter-color.png)

## Splatter (Color)

**In:** *Texture Generators**/Patterns*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Splatter is a pattern generator intended for random placement of a map input. It has many controls for geometrically patterned placement, and is simpler in use than [Tile Generator](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md). The latter can achieve similar results, but is much more complex.

Splatter works well for quickly getting some shapes stamped down, without needing too much tweaking.

Keep in mind that the default Splatter parameters do not look random at all: you need to tweak a few of them to get randomisation (mainly Disorder parameters). Also keep in mind that Splatter requires a map input to work.

## Parameters

* **Pattern Size Width**: *0.0 - 1000.0*Number of patterns to use on the X-axis.
* **Pattern Size Height**: *0.0 - 1000.0*Number of patterns to use on the Y-axis.
* **Rotation**: *-360.0 - 360.0*Rotates every pattern by a set amount.
* **Rotation Variation**: *0.0 - 360.0*Introduces random rotation for every separate shape.
* **Zoom**: *100.0 - 10000.0*Scales up the final result. Keep in mind that this breaks tiling!
* **Gain**: *0.0 - 10.0*Adjusts blending gain of every pattern. Makes them stand out more.
* **Pan X**: *-100.0 - 100.0*Pans whole result on X-axis.
* **Pan Y**: *-100.0 - 100.0*Pans whole result on Y-axis.
* **Disorder**: *0.0 - 100.0*  
  Randomly shifts shapes.
* **Grid Number**: *0 - 8*Jumps through different grid sizes to adjust result scale. Maintains tiling.
* **Disorder Angle**: *0.0 - 360.0*Controls the angle of disorder shifting.
* **Disorder Random**: *False/True*Randomises the disorder angle, adding much more chaos.
* **Pattern Size**: *5 - 12*
* **Size Variation**: *0.0 - 100.0*Introduces random scaling for every shape.
* **Image Input Filtering (Engine &gt; v4 only)**: *Bilinear + Mipmaps, Bilinear, Nearest*Which filtering to apply to the input image.
* **Output Level Min**: *0.0 - 1.0*Out minimum level adjustment.
* **Output Level Max**: *0.0 - 1.0*Out maximum level adjustment.
* **Background Color**: *(Grayscale value)*Sets solid background color.
* **Luminance Variation**: *0.0 - 1.0 (Grayscale version only)*Introduces luminance variation.
* **Color Variation**: *0.0 - 1.0 (Color Version Only)*Introduces color variation.

## Example Images

![](../../../../../../assets/splatter-ex.gif)

</td>
</tr>
</table>
