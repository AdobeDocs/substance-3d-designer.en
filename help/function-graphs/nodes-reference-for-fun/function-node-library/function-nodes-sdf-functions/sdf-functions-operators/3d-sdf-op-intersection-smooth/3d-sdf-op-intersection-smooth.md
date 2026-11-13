---
title: "Intersection smooth"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Operator > Intersection smooth"
---

# Intersection smooth

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Intersection smooth icon](./3d-sdf-op-intersection-smooth.png "Intersection smooth")

<b>In:</b> SDF function &gt; Operator

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Returns the volume common to two SDF shapes, effectively the volume created where two shapes overlap, with adjustable smoothing of the edges of their intersection.

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
| <b>SDF 1</b> *Float* | The first SDF shape. |
| <b>SDF 2</b> *Float* | The second SDF shape. |
| <b>Smoothness</b> *Float* | The smoothness of the edges at the intersection of the two SDF shapes.<br><br><i>Note:</i> hard edges may appear where the smoothing radiuses intersect.<br><br><i>Default: 0</i> |
