---
title: "Capped torus"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Capped torus"
---

# Capped torus

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Capped torus icon](./3d_sdf_capped_torus.png "Capped torus")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for a capped torus, where the sweeping of the minor circle along a major circle can be capped at an angle.<br>Both circles have adjustable radiuses.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>Major radius</b> *Float* | The radius of the major circle along which the minor circle is swept to form the surface of the torus.<br><br><i>Default: 0.5</i> |
| <b>Minor radius</b> *Float* | The radius of the minor circle being swept along the major circle to form the surface of the torus.<br><br><i>Default: 0.2</i> |
| <b>Angle</b> *Float* | The central angle, in turns, defining the trimming arc of the major circle along which the minor circle will not be swept.<br><br><i>Default: 0.75</i> |
| <b>Angle offset</b> *Float* | The offset, along the major radius, of the trimming arc along which the minor circle will not be swept.<br><br><i>Default: 0</i> |
| <b>Symmetrical</b> *Boolean* | Controls whether the trimming arc should be drawn in one or two directions.<br><br><i>Default: True</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the capped torus.<br><br><i>Default: (0, 0, 0.5)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
