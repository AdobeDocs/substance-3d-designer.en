---
title: "Torus"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Torus"
---

# Torus

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Torus icon](./3d-sdf-torus.png "Torus")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a torus, which is a shape formed by sweeping a minor circle along a major circle.<i>Both circles have adjustable radiuses.

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
| <b>Radius major</b> *Float* | The radius of the circle along which the minor disc is swept to form the surface of the torus.<br><br><i>Default: 0.5</i> |
| <b>Radius minor</b> *Float* | The radius of the circle being swept along the major circle to form the surface of the torus.<br><br><i>Default: 0.2</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the torus.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
