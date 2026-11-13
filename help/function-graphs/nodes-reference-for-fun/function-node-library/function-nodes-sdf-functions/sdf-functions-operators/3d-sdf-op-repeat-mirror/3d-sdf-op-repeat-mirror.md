---
title: "Repeat mirror range"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Operator > Repeat mirror range"
---

# Repeat mirror range

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Repeat mirror range icon](./3d-sdf-op-repeat-mirror.png "Repeat mirror range")

<b>In:</b> SDF function &gt; Operator

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Mirrors and duplicates an SDF shape any number of times at a regular spacing in the X, Y and Z positive or negative axes.<br>Every time this operator repeats a shape, it also mirrors it. This visually results in an alternating between the original orientation of the shape and a flipped copy.

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
| <b>Amount +</b> *Integer3* | The amount of duplications along the positive X, Y, Z axes.<br><br><i>Default: (2, 0, 0)</i> |
| <b>Amount -</b> *Integer3* | The amount of duplications along the negative X, Y, Z axes.<br><br><i>Default: (2, 0, 0)</i> |
| <b>Spacing</b> *Float3* | The world space between each duplicate.<br><br>The spacing is visualized by a cubic helper, which size is the space between duplicates in the X, Y and Z directions. The spacing starts at the <b>Origin position</b> and is increased symmetrically from it.<br><br><i>Default: (2, 2, 2)</i> |
| <b>Origin position</b> *Float3* | Defines the center of the SDF shape that will be duplicated.<br><br>The origin position is visualized by the cubic helper's center position.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
