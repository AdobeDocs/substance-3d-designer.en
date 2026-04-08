---
title: "Ellipsoid"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Ellipsoid"
---

# Ellipsoid

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Ellipsoid icon](./3d_sdf_ellipsoid.png "Ellipsoid")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for an ellipsoid, which is a rounded shape of adjustable tridimensional radius.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>Radius</b> *Float3* | The radius of the ellipsoid in X, Y and Z.<br><br><i>Default: (0.35, 0.35, 0.5)</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the ellipsoid.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
