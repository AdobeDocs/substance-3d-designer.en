---
title: "Offset"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Offset"
---

# Offset

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Offset icon](./3d-sdf-transform-offset.png "Offset")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Offset an SDF shape along a vector.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

|  |  |
| :--- | :--- |
| <b>SDF</b> *Float* | The input SDF shape. |
| <b>Offset</b> *Float3* | The distance the SDF shape will be offset in the X, Y, Z directions.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
