---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/3d-texture-sdf.html"
breadcrumb-title: ""
description: Use the 3D Texture SDF node to generate signed distance field textures from 3D data for creating smooth shapes and effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > 3D Texture SDF
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Texture SDF
user-guide-description: ""
user-guide-title: ""
---

# 3D Texture SDF

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](3d-texture-sdf.resources/3d-texture-sdf-01.png){width="200px"}

<b>In:</b> Filter &gt; Effect

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **3D Texture SDF** node generates the *signed distance field* of a shape from the **Input**'s *3D texture* mask representing the slices of the shape's *volume*.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask Input</b> <i>Grayscale</i> | The <i>3D texture</i> mask representing the slices of a shape's <i>volume</i>. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Threshold</b> <i>Float</i> | When the shape volume is described by a <i>fading gradient</i>, sets the gradient value at which the <i>surface</i> of the shape is <i>detected</i>. |
| <b>Output</b> <i>Integer</i> | The type of distance field which should be output:<br>- <i>Distance Field</i>: outputs a distance field describing the distances <i>outside</i> the shape.<br>- <i>Signed Distance Field</i>: outputs a distance field describing the distances <i>outside</i> (positive) and <i>inside</i> (negative) the shape. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="3d-texture-sdf.resources/3d-texture-sdf-02.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-sdf.resources/3d-texture-sdf-03.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-sdf.resources/3d-texture-sdf-04.png" />
        </td>
    </tr>
</table>
