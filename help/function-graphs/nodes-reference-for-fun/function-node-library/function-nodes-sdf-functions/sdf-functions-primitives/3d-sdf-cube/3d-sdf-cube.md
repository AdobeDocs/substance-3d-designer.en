---
title: "Cube"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Cube"
---

# Cube

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Cube icon](./3d-sdf-cube.png "Cube")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a cube, with adjustable XYZ size and rounding of edges.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Size</b> *Float3* | The size of the cube on X, Y and Z.<br><br><i>Default: (1, 1, 1)</i> |
| <b>Rounding</b> *Float* | The radius of the rounded arcs applied to the cube's edges.<br><br><i>Note:</i> hard edges may appear where the rounding radiuses intersect.<br><br><i>Default: 0</i> |
| <b>Pivot position (local)</b> *Float3* | The world space position of the local pivot of the cube, where (0, 0, 0) places the pivot at the center of the cube.<br><br><i>Default: (0, 0, -0.5)</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the cube.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
