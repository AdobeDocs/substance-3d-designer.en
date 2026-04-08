---
title: "Hexagonal prism"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Hexagonal prism"
---

# Hexagonal prism

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Hexagonal prism icon](./3d_sdf_hexagonal_prism.png "Hexagonal prism")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a 6-sided prism of adjustable height, radius and rounding of edges.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>Height</b> *Float* | The Z-up height of the hexagonal prism from its base.<br><br><i>Default: 1</i> |
| <b>Radius</b> *Float* | The radius of the hexagonal prism.<br><br><i>Default: 0.5</i> |
| <b>Rounding</b> *Float* | The radius of the rounded arcs applied to the hexagonal prism's edges.<br><br><i>Note:</i> hard edges may appear where the rounding radiuses intersect.<br><br><i>Default: 0</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the hexagonal prism.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
