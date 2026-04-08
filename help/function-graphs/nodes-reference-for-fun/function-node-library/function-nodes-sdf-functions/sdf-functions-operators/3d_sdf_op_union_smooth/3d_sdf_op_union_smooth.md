---
title: "Union smooth"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Operator > Union smooth"
---

# Union smooth

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Union smooth icon](./3d_sdf_op_union_smooth.png "Union smooth")

<b>In:</b> SDF function &gt; Operator

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Returns the added volumes of two SDF shapes, with adjustable smoothing of the edges of their intersection.

</td>
</tr>
</table>

<a name='inputs'></a>
## Inputs

|  |  |
| :--- | :--- |
| <b>SDF 1</b> *Float* | The first SDF shape. |
| <b>SDF 2</b> *Float* | The second SDF shape. |
| <b>Smoothness</b> *Float* | The smoothing radius, starting from the intersection's edges.<br><br><i>Default: 0</i><br><br><i>Note:</i> hard edges may appear where the smoothing radiuses intersect. |
