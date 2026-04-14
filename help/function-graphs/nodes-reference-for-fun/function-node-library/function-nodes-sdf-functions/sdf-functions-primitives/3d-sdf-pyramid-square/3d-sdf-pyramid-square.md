---
title: "Pyramid square"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Pyramid square"
---

# Pyramid square

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Pyramid square icon](./3d-sdf-pyramid-square.png "Pyramid square")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a pyramid with a square base, with adjustable height and base position.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Height</b> *Float* | The Z-up height of the pyramid's apex from its base.<br><br><i>Default: 1</i> |
| <b>Base size</b> *Float* | The length of the pyramid's base edges.<br>All edges are of equal length.<br><br><i>Default: 1</i> |
| <b>Base position</b> *Float3* | The world space position of the pyramid's base.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
