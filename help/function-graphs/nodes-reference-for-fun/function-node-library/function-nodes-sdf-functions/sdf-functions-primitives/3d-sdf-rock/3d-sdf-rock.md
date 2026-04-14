---
title: "Rock"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Rock"
---

# Rock

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Rock icon](./3d-sdf-rock.png "Rock")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a parametric and randomizable rock shape, built with SDF functions.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Max. facets</b> *Integer* | The maximum number of facets of the rock (up to 32).<br><br><i>Default: 8</i> |
| <b>Smoothness</b> *Float* | The radius of the rounded arcs applied to the rock's edges.<br><br><i>Default: 0</i> |
| <b>Randomness</b> *Float* | Jitters the faces orientation and distance to the center.<br>As a result, greater values result in a smaller rock.<br><br><i>Default: 0</i> |
| <b>Seed</b> *Float* | Seed for the <b>Randomness</b> parameter.<br><br><i>Default: 0</i> |
| <b>Scale</b> *Float* | Global scale of the rock shape.<br>Applied after <b>Randomness</b>, and before <b>Smoothness</b>.<br><br><i>Default: 0.5</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the rock.<br><br><i>Default: (0, 0, 0.5)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><i>Default: The untransformed world space position.</i> |
