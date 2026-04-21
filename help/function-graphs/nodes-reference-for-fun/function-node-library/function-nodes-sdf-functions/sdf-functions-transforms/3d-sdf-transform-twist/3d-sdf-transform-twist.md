---
title: "Twist (inexact)"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Twist (inexact)"
---

# Twist (inexact)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Twist (inexact) icon](./3d-sdf-transform-twist.png "Twist (inexact)")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Twist an SDF shape around its local Z axis between a start and end point, at an adjustable angle.<br><br><i>Note:</i>Since this transformation function is inexact, artefacts might appear when rendering it.

</td>
</tr>
</table>

<a name='inputs'></a>

>[!INFO]
> 
> To learn more about concepts and workflows involving SDF functions, go to the dedicated page: [Working with SDF functions](../../working-with-sdf-functions.md)

## Inputs

|  |  |
| :--- | :--- |
| <b>SDF</b> *Float* | The input SDF shape. |
| <b>Angle</b> *Float* | The angle, in turns, of the rotation applied at the end of the twist. |
| <b>Start</b> *Float* | The world position on the Z axis where the twisting starts. All the volume beneath is not twisted. |
| <b>End</b> *Float* | The world position on the Z axis where the twisting ends. All the volume above is uniformly rotated at the specified angle. |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
