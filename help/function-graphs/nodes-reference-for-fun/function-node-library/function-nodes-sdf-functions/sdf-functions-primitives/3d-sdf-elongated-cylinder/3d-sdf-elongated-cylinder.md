---
title: "Elongated cylinder"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Elongated cylinder"
---

# Elongated cylinder

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Elongated cylinder icon](./3d-sdf-elongated-cylinder.png "Elongated cylinder")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for an elongated cylinder of adjustable length, radius and rounding of edges.<br>The elongated cylinder is the result of bridging two cylinders.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Height</b> *Float* | The Z-up height of both the start and end cylinders from their base.<br><br><i>Default: 0.5</i> |
| <b>Radius</b> *Float* | The radius of both the start and end cylinders.<br><br><i>Default: 0.5</i> |
| <b>Rounding</b> *Float* | The radius of the rounded arcs applied to the elongated cylinder's edges.<br><br><i>Note:</i> hard edges may appear where the rounding radiuses intersect.<br><br><i>Default: 0</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the elongated cylinder.<br><br><i>Default: (0, 0, 0)</i> |
| <b>Elongation distance</b> *Float* | The distance along which the start cylinder is elongated.<br>I.e. the distance between the centers of the start and end cylinders.<br><br><i>Default: 0.5</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
