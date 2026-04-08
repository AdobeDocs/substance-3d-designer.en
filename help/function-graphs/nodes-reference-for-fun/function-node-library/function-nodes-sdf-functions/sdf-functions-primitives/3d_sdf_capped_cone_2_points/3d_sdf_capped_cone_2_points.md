---
title: "Capped cone 2 points"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Capped cone 2 points"
---

# Capped cone 2 points

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Capped cone 2 points icon](./3d_sdf_capped_cone_2_points.png "Capped cone 2 points")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a capped cone defined by the positions of its base and top.<br>The base and top have adjustable radiuses.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>Position base</b> *Float3* | The position of the capped cone's base.<br><br><i>Default: (0, 0, 0)</i> |
| <b>Position top</b> *Float3* | The position of the capped cone's top.<br><br><i>Default: (0, 0, 1)</i> |
| <b>Radius base</b> *Float* | The radius of the capped cone's base.<br><br><i>Default: 0.5</i> |
| <b>Radius top</b> *Float* | The radius of the capped cone's top.<br><br><i>Default: 0.2</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
