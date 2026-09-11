---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/panorama-shape.html"
breadcrumb-title: ""
description: Use the Panorama Shape node to create shapes mapped to panorama coordinates for environment texture generation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Panorama Shape
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Panorama Shape
user-guide-description: ""
user-guide-title: ""
---

# Panorama Shape

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](panorama-shape.resources/panorama-shape-1.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is a helpful node for generating procedural "Studio"-type panorama maps. Allows you to place and modify spotlight images, as well as set their HDR properties. It can be chained together for multiple shapes.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Shape Matrix</b> | Moves or translates the result, can be modified by directly interacting with the canvas. |
| <b>Shape</b> <i>square, disc</i> | Sets Shape type. |
| <b>Shape Color</b> <i>(Color value)</i> | Sets Shape color. |
| <b>Shape Intensity</b> <i>0.0 - 100.0</i> | Sets HDR-intensity of the shape. |
| <b>Shape Soft Border</b> <i>0.0 - 1.0</i> | Changes the shape's border softness. |
| <b>Hotspot Intensity</b> <i>0.0 - 100.0</i> | Sets HDR-intensity of the shape's hotspot. |
| <b>Hotspot Size</b> <i>0.0 - 1.0</i> | Changes the size of the hotspot within the shape. |
| <b>Hotspot Falloff</b> <i>0.0 - 1.0</i> | Changes the falloff, edge blending of the hotspot. |
| <b>Hotspot Position</b> <i>0.0 - 1.0</i> | Moves the hotspot in relation to the shape. |
| <b>Enable Backgound</b> <i>False/True</i> | Enables filling of the background with a solid color. Note that this means you can no longer chain them together by blending. |
| <b>Background Color</b> <i>(Color value)</i> | Sets background solid color. |
| <b>Enable Texture Input</b> <i>False/True</i> | Allows for a custom input instead of a predefined shape type. |
