---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/non-uniform-rotation.html"
breadcrumb-title: ""
description: Use the Non-Uniform Rotation node to apply non-uniform rotation transformations for creating spiral and vortex effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Non-Uniform Rotation
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Non-Uniform Rotation
user-guide-description: ""
user-guide-title: ""
---

# Non-Uniform Rotation

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/nonuniformrotationgrayscale.png){width="200px"}

</td>
<td style="border: 0;" valign="top">

![](../../../../../../assets/nonuniformrotationcolor.png){width="200px"}

</td>
</tr>
</table>

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **Non-Uniform Rotation** node rotates the **Input** using the **Rotation Map** input.

The values of the image represent a *number of turns*. The rotation is performed around the position specified by the **Pivot Position** value or the **Pivot Position map** input.  
Positive values in the **Rotation Map** input result in a *clockwise* rotation.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Grayscale/Color</i> | The input grayscale image which should be rotated. |
| <b>Rotation Map</b> <i>Grayscale</i> | The map used to control the amount of rotation, in *number of turns*. The sampled values are multiplied against the **Rotation Angle Multiplier**. Negative values result in a *counter-clockwise* rotation. |
| <b>Rotation Pivot Position Map</b> <i>Color</i> | The image used to specify the position of the rotation *pivot*. The **X/Y** position is mapped to the **R/G** channels of the image. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Rotation Angle Multiplier</b> <i>Float</i> | Adjusts the intensity of the **Rotation Map** input. |
| <b>Rotation Angle Offset</b> <i>Float</i> | Applies the specified additional amount of rotation. |
| <b>Use Pivot Position Map</b> <i>Boolean</i> | Use a *bitmap input* to specify the position of the rotation pivot. The **X/Y** position is mapped to the **R/G** channels of the **Position Map** input. |
| <b>PIvot Position</b> <i>Float2</i> | The position of the pivot around which the image is rotated. |
| <b>Background Color</b> <i>Float/Float4</i> | Background color to display *outside* of the image's bounds in case the tiling is not set to **H and V Tiling**. |
| <b>Filtering Mode</b> <i>Integer</i> | Defines how to treat the sampled results when *interpolating* between pixels:<br><br>- *Nearest*: will sample exactly the *same* value (faster)<br>- *Bilinear*: will apply a bilinear filter on the result for a *smoother* look |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/nonuniformrotation-demo-02-resized.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/nonuniformrotation-variant-png.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/nonuniformrotation-node.png" />
        </td>
    </tr>
</table>
