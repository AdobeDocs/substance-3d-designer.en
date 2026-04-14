---
title: "Cone"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Cone"
---

# Cone

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Cone icon](./3d-sdf-cone.png "Cone")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a cone of adjustable height, radius and position.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Radius</b> *Float* | The radius of the cone's base.<br><br><i>Default: 0.5</i> |
| <b>Height</b> *Float* | The Z-up height of the cone's apex from its base.<br><br><i>Default: 1</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the cone.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
