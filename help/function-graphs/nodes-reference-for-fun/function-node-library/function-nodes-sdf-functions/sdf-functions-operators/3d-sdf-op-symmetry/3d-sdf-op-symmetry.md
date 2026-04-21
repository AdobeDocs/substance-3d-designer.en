---
title: "Symmetry"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Operator > Symmetry"
---

# Symmetry

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Symmetry icon](./3d-sdf-op-symmetry.png "Symmetry")

<b>In:</b> SDF function &gt; Operator

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Flips and duplicates an SDF shape across a mirror plane, then returns the union of the base SDF shape and its duplicate(s).<br>Symmetry can be applied on any axes concurrently.

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
| <b>SDF</b> *Float* | The input SDF shape. |
| <b>Mirror plane position</b> *Float3* | The world space position of the center of the mirror plane.<br>This position is shared by all mirror planes if the symmetry is applied on several axes.<br><br><i>Default: (0, 0, 0)</i> |
| <b>Mirror axis</b> *Integer3* | Sets the desired mirror axes.<br><br>E.g., (1, 0, 0) will apply symmetry on the X axis.<br><br><i>Default: (1, 0, 0)</i> |
| <b>Flip axis</b> *Integer3* | Sets which axes should be flipped.<br><br>E.g., (1, 0, 0) will flip the direction of symmetry on the X axis.<br><br><i>Default: (0, 0, 0)</i> |
| <b>Pre-offset</b> *Float3* | The offset on the X, Y, Z axes applied to the shape before applying the symmetry operator. |
