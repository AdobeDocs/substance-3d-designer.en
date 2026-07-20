---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/3d-volume-mask.html"
breadcrumb-title: ""
description: Use the 3D Volume Mask node to create volumetric masks based on 3D position for advanced material effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > 3D Volume Mask
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Volume Mask
user-guide-description: ""
user-guide-title: ""
---

# 3D Volume Mask

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/3dvolumemask.png){width="256px"}

<b>In:</b> Generator &gt; Pattern

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **3D Volume Mask** node generates a representation of a *primitive shape* based on the **Position** input map.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Position</b> <i>Color</i> | The map describing the *3D space coordinates* the primitive is represented into.<br><br>The **X/Y/Z** coordinates are mapped to the **R/G/B** channels respectively. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Shape</b> <i>Integer</i> | The primitive shape which should be represented:<br><br>- *Cube*<br>- *Cylinder*<br>- *Sphere* |
| <b>Scale</b> <i>Float</i> | Defines the *global* scale of the primitive, applied *uniformly* on all axes. |
| <b>Size</b> <i>Float3</i> | Defines the size of the shape on each axis. |
| <b>Position Input</b> <i>Integer</i> | The method of *representing space* through the **Position** input:<br><br>- *UV Position*: Use a *UV map*. The X/Y (U/V) coordinates are mapped to the R/G channels respectively. The Z axis is assumed to be the *orthogonal forward* vector.<br>- *World Space Position*: Use a *position map* to map the primitive in 3D space. The X/Y/Z coordinates are mapped to the R/G/B channels respectively. |
| <b>Position UV</b> <i>Float2</i> | The position of the primitive in UV space.<br><br>*Note*: This parameter is only available when the **Position Input** parameter is set to *UV Position*. |
| <b>Position</b> <i>Float3</i> | The position of the primitive in world space.<br><br>*Note*: This parameter is only available when the **Position Input** parameter is set to *World Space Position*. |
| <b>Rotation</b> <i>Float3</i> | Defines the rotation of the shape in world space. |
| <b>Feather Width</b> <i>Float</i> | Adjusts the width of the *fading gradient* from the primitive's surface inwards. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvolumemask-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvolumemask-variant2.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvolumemask-variant3.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvolumemask-variant4.jpg" />
        </td>
    </tr>
</table>
