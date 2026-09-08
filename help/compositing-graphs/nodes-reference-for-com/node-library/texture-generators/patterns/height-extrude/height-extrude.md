---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/height-extrude.html"
breadcrumb-title: ""
description: Use the Height Extrude node to extrude shapes based on height maps for creating 3D-like depth effects in textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Height Extrude
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Height Extrude
user-guide-description: ""
user-guide-title: ""
---

# Height Extrude

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/height-extrude.png){width="200px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Height Extrude renders 3D Z-Depth from an input Height map. Just like [Shape Extrude](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-extrude/shape-extrude.md) and [Cube 3D](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d/cube-3d.md) it lets you spin a camera around in the 2D View. Its main goal is to serve as a Generator for creating 3D-rotated shapes from a flat heightmap. These shapes can then be used with [Shape Splatter](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-splatter/shape-splatter.md).

The main diffence with [Shape Extrude](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-extrude/shape-extrude.md) is that the input map does not have to be a binary "alpha" type of map, but a full-range grayscale map. This means you have more control over the extrusion height (Organic, complex shapes), but no control over anything like beveling profiles (Hard-Surface, simpler shapes).

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Camera Angle</b> | Euler angles of the camera, in half-turns. Please note that horizontal rotation and scale are applied directly to the input. |
| <b>Camera Scale</b> <i>0.001 - 3.0</i> | Global scale applied to the output. |
| <b>Height Scale</b> <i>0.0 - 2.0</i> | Applies a global factor on the input height values. |
| <b>Vertical Offset</b> <i>-1.0 - 1.0</i> | Moves the final output up or down. |
| <b>Ground</b> <i>Off/On</i> | If Ground is off, a black background is shown where the input is 0 rather than a ground-like plane. |
| <b>Normal Format</b> <i>DirectX/OpenGL</i> | The <b>Normal Format</b> parameter inverts y coordinate of the normal map. |
| <b>Normal Intensity</b> <i>0.0 - 256.0</i> | Same as <b>Intensity</b> parameter of <b>Normal</b> node. Set it to 256 to get a shar-free normal while rotating. |
