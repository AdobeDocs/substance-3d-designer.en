---
title: "Cylinder 2 points"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Cylinder 2 points"
---

# Cylinder 2 points

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Cylinder 2 points icon](./3d-sdf-cylinder-2-points.png "Cylinder 2 points")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a cylinder of adjustable radius defined by the positions of its start and end discs.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Start</b> *Float3* | The position of the cylinder's start disc.<br><br><i>Default: (0, 0, 0)</i> |
| <b>End</b> *Float3* | The position of the cylinder's end disc.<br><br><i>Default: (0, 0, 1)</i> |
| <b>Radius</b> *Float* | The radius of the cylinder.<br><br><i>Default: 0.25</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
