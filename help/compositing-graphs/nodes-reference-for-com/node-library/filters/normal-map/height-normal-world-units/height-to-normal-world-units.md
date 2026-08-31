---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/height-to-normal-world-units.html"
breadcrumb-title: ""
description: Use the Height to Normal World Units node to convert height maps to normal maps using world unit scaling for accurate detail.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Height to Normal World Units
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Height to Normal World Units
user-guide-description: ""
user-guide-title: ""
---

# Height to Normal World Units

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](height-to-normal-world-units.resources/height-to-normal-world-units-01.png){width="128px"}

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

An advanced Height-To-Normal conversion node that makes use of real-world units during the conversion.

Useful for when you know your source Heightmap's dimensions and want to perform the most accurate conversion, such as when working with scanned material.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Surface Size (cm)</b> <i>0.0 - 1000.0</i> | Dimensions of the input Heightmap. |
| <b>Height Depth (cm)</b> <i>0.0 - 100.0</i> | Maximum depth of Heightmap details. |
| <b>Normal Format</b> <i>OpenGL, DirectX</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Sampling</b> <i>Standard, Sobel</i> | Switches between two sampling modes determining accuracy. |
