---
title: "Pyramid"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Pyramid"
---

# Pyramid

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Pyramid icon](./3d-sdf-pyramid.png "Pyramid")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a pyramid of adjustable height, base size and base position.

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
| <b>Height</b> *Float* | The Z-up height of the pyramid's apex from its base.<br><br><i>Default: 1</i> |
| <b>Base size</b> *Float2* | The size of the pyramid's base in X and Y.<br><br><i>Default: (1, 1)</i> |
| <b>Base position</b> *Float3* | The world space position of the pyramid's base.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
