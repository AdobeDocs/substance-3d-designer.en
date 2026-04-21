---
title: "Plane"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Plane"
---

# Plane

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Plane icon](./3d-sdf-plane.png "Plane")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a plane of adjustable orientation, position and size.

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
| <b>Normal</b> *Float3* | The world space normal vector of the plane, which controls its orientation.<br>The vector is normalized.<br><br><i>Default: (0, 0, 1)</i> |
| <b>Size</b> *Float2* | The size of the plane in X and Y.<br><br><i>Default: (1, 1)</i> |
| <b>Thickness</b> *Float* | The thickness of the plane, applied in all directions.<br>The plane is rounded when thickness is increased.<br><br><i>Default: 0</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the plane.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
