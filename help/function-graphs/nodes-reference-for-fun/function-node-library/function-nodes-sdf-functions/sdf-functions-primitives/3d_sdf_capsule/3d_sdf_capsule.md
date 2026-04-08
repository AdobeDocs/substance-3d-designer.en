---
title: "Capsule"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Capsule"
---

# Capsule

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Capsule icon](./3d_sdf_capsule.png "Capsule")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a capsule of adjustable length and radius.<br>The capsule is the result of bridging two spheres.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>Start</b> *Float3* | The position of the start sphere.<br><br><i>Default: (0, 0, 0)</i> |
| <b>End</b> *Float3* | The position of the end sphere.<br><br><i>Default: (0, 0, 1)</i> |
| <b>Radius</b> *Float* | The radius of both the start and end spheres.<br><br><i>Default: 0.25</i> |
| <b>Start/end at tip</b> *Boolean* | Controls whether the <b>Start</b> and <b>End</b> positions should be at the extremities of the spheres.<br>I.e., controls if the height of the capsule should include the radius of the spheres.<br><br><i>Default: False</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the capsule.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
