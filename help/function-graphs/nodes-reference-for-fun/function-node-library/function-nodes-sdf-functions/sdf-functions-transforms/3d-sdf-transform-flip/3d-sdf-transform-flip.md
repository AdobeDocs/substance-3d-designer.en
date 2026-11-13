---
title: "Flip"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Flip"
---

# Flip

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Flip icon](./3d-sdf-transform-flip.png "Flip")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Applies a mirror transform to the input SDF shape.<br>Essentially performs a negative scale on the selected axes.

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
| <b>Mirror axis</b> *Integer3* | Use an Integer3 to set the desired mirror axis.<br>E.g. (1, 0, 0) will mirror the X axis.<br><br><i>Default: (1, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
