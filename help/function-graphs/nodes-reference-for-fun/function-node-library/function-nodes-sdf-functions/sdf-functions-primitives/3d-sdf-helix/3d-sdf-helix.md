---
title: "Helix (approx.)"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Primitive > Helix (approx.)"
---

# Helix (approx.)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Helix (approx.) icon](./3d-sdf-helix.png "Helix (approx.)")

<b>In:</b> SDF function &gt; Primitive

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An SDF function for an approximation of a helix, which is a shape formed by sweeping a circle along a curve winding along an upward curve around an axis.<br><br><i>Note:</i>Since this SDF function is an approximation, artefacts might appear when rendering it.

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
| <b>Major radius</b> *Float* | The distance of the winding curve from the axis.<br><br><i>Default: 0.4</i> |
| <b>Minor radius</b> *Float* | The radius of the circle being swept along the curve to form the surface of the helix.<br><br><i>Default: 0.1</i> |
| <b>Height</b> *Float* | The Z-up height of the helix.<br><br><i>Default: 0.5</i> |
| <b>Windings</b> *Float* | The number of times the curve fully winds around the axis in steps of 0.5.<br>I.e., how many times the helix will revolve within a height of 0.5.<br><br><i>Default: 4</i> |
| <b>Center position</b> *Float3* | The world space position of the pivot of the helix.<br><br><i>Default: (0, 0, 0)</i> |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
