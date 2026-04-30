---
title: "Elongate"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Elongate"
---

# Elongate

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Elongate icon](./3d-sdf-transform-elongate.png "Elongate")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Elongate an SDF shape from an adjustable position.<br>Effectively linearly extends the volume of an SDF shape starting at an adjustable slice.

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
| <b>Elongation</b> *Float3* | The elongation length on the X, Y, Z axes. |
| <b>Center position</b> *Float3* | The world space position from which the shape will be elongated.<br>I.e., the position of the slice being elongated. |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
