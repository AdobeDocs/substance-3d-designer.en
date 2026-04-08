---
title: "Offset P"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Offset P"
---

# Offset P

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Offset P icon](./3d_sdf_transform_offset_p.png "Offset P")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Offsets the world space along a vector.<br>The output transformed world position can be connected to the <b>P</b> input of most SDF functions to define them in this transformed world space.<br><br><i>Tip:</i> P transforms can be chained, but keep in mind the results depend on the order of operations.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>Offset</b> *Float3* | The distance the world space will be offset in the X, Y and Z directions. |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
