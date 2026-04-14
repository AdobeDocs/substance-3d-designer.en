---
title: "Infinite plane"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Infinite plane"
---

# Infinite plane

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Infinite plane icon](./3d-sdf-infinite-plane.png "Infinite plane")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for an infinite plane of adjustable orientation and position.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Normal</b> *Float3* | The world space normal vector of the infinite plane, which controls its orientation.<br>The vector is normalized.<br><br><i>Default: (0, 0, 1)</i> |
| <b>Center position</b> *Float* | The world space position of the pivot of the plane, as a distance from the world origin along the plane's normal.<br><br><i>Default: 0</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
