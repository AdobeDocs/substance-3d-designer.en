---
title: "Rotate P"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > SDF function > Transform > Rotate P"
---

# Rotate P

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Rotate P icon](./3d-sdf-transform-rotate-p.png "Rotate P")

<b>In:</b> SDF function &gt; Transform

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Rotate the world space around an axis at an adjustable angle.<br>The output transformed world position can be connected to the <b>P</b> input of most SDF functions to define them in this transformed world space.<br><br>Use the <b>Transform pivot</b> helper of the <b>3D Viewer</b> to visualize the performed rotation.<br><br><i>Tip:</i> P transforms can be chained, but keep in mind the results depend on the order of operations.

</td>
</tr>
</table>


### [Inputs](#inputs)


<a name='inputs'></a>

## Inputs

|  |  |
| :--- | :--- |
| <b>Angle</b> *Float* | The angle, in turns, at which the world space is rotated.<br><br>The angle is visualized by a circle in the <b>Transform pivot</b> helper of the <b>3D Viewer</b>. Align the camera so as to see the <b>Axis</b> arrow as the center of this circle to clearly see the angle of your rotation as a fraction of a turn. |
| <b>Axis</b> *Float3* | The normalized vector defining the axis around which the world space is rotated.<br>E.g. (0, 1, 0) will rotate the world space around the Y axis of the pivot point.<br><br>The axis is visualized by an arrow in the <b>Transform pivot</b> helper of the <b>3D Viewer</b>. The color of the arrow is mapped on the XYZ components of this vector.<br><br><i>Default: (0, 1, 0)</i> |
| <b>Pivot position</b> *Float3* | The world space position of the pivot defining the origin of the rotation.<br><br>The pivot point is visualized by the start of the arrow in the <b>Transform pivot</b> helper of the <b>3D Viewer</b>. |
| <b>P</b> *Float3* | The transformed world space position. Use this input to apply additional transformations using the <b>Offset P</b> and <b>Rotate P</b> nodes.<br><br><i>Default: The untransformed world space position.</i> |
