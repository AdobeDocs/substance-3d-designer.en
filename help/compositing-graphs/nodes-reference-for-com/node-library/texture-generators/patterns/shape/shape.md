---
title: "Shape | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape"
---

# Shape

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shape-2.png){width="128px"}

## Shape

**In:** *Texture Generators**/Patterns*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a variety of procedural shapes, with options to modify base shapes. The shapes are always perfectly interpolated and high-precision.

Despite its simplicity, this is a very useful node: it is the building block of most procedural Heightmap generation! By combining basic shapes with transform nodes, you can create a fully-procedural Heightmap shape that is much more precise than any bitmap.

## Parameters

* **Tiling**: *1 - 16*  
  Sets the amount of times the result should tile.
* **Pattern**: *Square, Disc, Paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half Bell, Ridged Bell, Crescant, Capsule, Cone*, Hemisphere**  
  Selects what pattern shape to use.
* **Pattern Specific**: *0.0 - 1.0*  
  Lets you change the selected pattern's shape. The effect is dependent on the selected pattern.
* **Scale**: *0.0 - 1.0*Scales the entire shape.
* **Size**: *0.0 - 1.0*Allows for non-uniform scaling over either X- or Y-axis.
* **Angle**: *0.0 - 1.0*Rotates the entire shape.
* **Rotation 45°**: *False/True*Rotates at pre-set 45 degrees.
* **Non Square Expansion**: *False/True*  
  Enables compensation of squash and stretch with non-square ratios.
* **Non Square Tiling****:** *False/True*When Non Square Expansion is enabled, this will tile the shape without squashing.

## Example Images

![](shape-ex.gif)

</td>
</tr>
</table>

 