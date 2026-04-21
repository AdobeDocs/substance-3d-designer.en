---
title: "Set material"
description: "Set the base color, roughness and metalness of the material of an SDF scene."
---

# Set material

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Set material icon](set-material.png "Set material")

<b>In:</b> 3D Function &gt; Material

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Set the base color, roughness and metalness of the material of an SDF scene.

These values can then be retrieved for all splattered SDF shapes in the outputs of the [Shape splatter v2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter-v2/shape-splatter-v2.md).

</td>
</tr>
</table>

>[!INFO]
> 
> To learn more about concepts and workflows involving SDF functions, go to the dedicated page: [Working with SDF functions](../../working-with-sdf-functions.md)

## Inputs

|                            |                                  |
|----------------------------|----------------------------------|
| <b>SDF scene</b> *Float*   | The input SDF scene.             |
| <b>Base color</b> *Float3* | The RGB base color value to set. |
| <b>Metalness</b> *Float*   | The metalness value to set.      |
| <b>Roughness</b> *Float*   | The roughness value to set.      |
