---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/3d-texture-offset.html"
breadcrumb-title: ""
description: Use the 3D Texture Offset node to offset textures in 3D space for creating parallax effects and surface variations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > 3D Texture Offset
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Texture Offset
user-guide-description: ""
user-guide-title: ""
---

# 3D Texture Offset

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](3d-texture-offset.resources/3dtextureoffsetgrayscale.png){width="200px"}

</td>
<td style="border: 0;" valign="top">

![](3d-texture-offset.resources/3dtextureoffsetcolor.png){width="200px"}

</td>
</tr>
</table>

<b>In:</b> Filter &gt; Transformation

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **3D Texture Offset** node applies an *offset transformation* in the **X**, **Y** and **Z** axes on an object described by the *3D texture* connected to the **Input**.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Grayscale/Color</i> | The <i>3D texture</i> describing a 3D object.<br>The object is commonly described in a <i>unit cube</i>. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Offset</b> <i>Float3</i> | The amount of offset in <i>world space</i> applied on the object described by the <i>3D texture</i> connected to the <b>Input</b>. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="3d-texture-offset.resources/3dtextureoffset-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-offset.resources/3dtextureoffset-node.png" />
        </td>
    </tr>
</table>
