---
title: "Scale"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Scale"
---

# Scale

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Scale icon](./3d_sdf_transform_scale.png "Scale")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Uniformly scale an SDF shape.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>SDF</b> *Float* | The input SDF shape. |
| <b>Scale</b> *Float* | The uniform scale factor.<br><br><i>Default: 1</i> |
| <b>Pivot position</b> *Float3* | The world space position of the local pivot of the SDF shape, where (0, 0, 0) places the pivot at the center of the SDF shape. <br>Defines the origin of the scaling.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
