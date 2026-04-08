---
title: "Bend (inexact)"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Bend (inexact)"
---

# Bend (inexact)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Bend (inexact) icon](./3d_sdf_transform_bend.png "Bend (inexact)")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Bends an SDF shape around its local Y axis between a start and end point at an angle.<br><br><i>Note:</i>Since this transformation function is inexact, artefacts might appear when rendering it.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>SDF</b> *Float* | The input SDF shape. |
| <b>Angle</b> *Float* | The angle, in turns, of the rotation applied at the end of the bend. |
| <b>Start</b> *Float* | The world position on the Z axis where the bending starts. All the volume beneath is not bent. |
| <b>End</b> *Float* | The world position on the Z axis where the bending ends. All the volume above is uniformly rotated at the specified angle. |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
