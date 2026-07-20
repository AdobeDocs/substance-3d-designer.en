---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/3d-texture-surface-render.html"
breadcrumb-title: ""
description: Use the 3D Texture Surface Render node to render surface textures from 3D data for creating procedural surface effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > 3D Texture Surface Render
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Texture Surface Render
user-guide-description: ""
user-guide-title: ""
---

# 3D Texture Surface Render

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/3dtexturesurfacerender.png){width="200px"}

<b>In:</b> Filter &gt; Effect

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **3D Texture Surface Render** node renders the surface of a shape described by a *3D texture*, using its corresponding *distance field* from the **3D Distance Field** image input.

The surface is represented within the bounds of a *unit cube*. The lighting is computed using the **Environment** input image mapped to an infinite sphere.

>[!NOTE]
>
> The distance field is expected to be a **4096x4096** texture describing the shape with a **16x16** grid of 256 slices.  
> You may use the [3D Texture SDF](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/3d-texture-sdf/3d-texture-sdf.md) node to compute the distance field for a 3D texture of 256 slices.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>3D Distance Field</b> <i>Grayscale</i> | The 4096x4096 image representing the 256 <i>slices</i> of a shape's <i>distance field</i>, arranged in a 16x16 grid.<br>You may use the [3D Texture SDF](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/3d-texture-sdf/3d-texture-sdf.md) node to compute the distance field for a 3D texture of 256 slices. |
| <b>Environment</b> <i>Color</i> | The image representing the <i>environment</i> which should be mapped to an infinite sphere in the render, and used for computing the <i>lighting</i>.<br>The image is also used to render the scene background when the <b>Background Mode</b> parameter is set to <i>Ambient</i> or <i>Environment</i>. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Output Resolution</b> <i>Integer2</i> | The resolution of the output image in <b>X</b> and <b>Y</b>, expressed as a <i>power of two</i>. |
| <b>Camera Position</b> <i>Float2</i> | The position of the camera around the shape.<br>When the node is selected, you may use the position gizmo in the <b>2D View</b> to <i>orbit</i> the camera. |
| <b>Camera Distance</b> <i>Float</i> | The distance from the camera to the shape. |
| <b>Camera FOV</b> <i>Float</i> | The field of view of the camera in <i>degrees</i>. |
| <b>Albedo</b> <i>Float3</i> | The albedo color of the shape's surface. |
| <b>Background Mode</b> <i>Integer</i> | The method of representing the background of the rendered scene:<br>- <i>Ground Irradiance</i>: The computed irradiance of the ground plane<br>- <i>Ambient</i>: The ambient color of the <b>Environment</b> image input mapped to an infinite sphere, which is akin to a strongly blurred version of the image<br>- <i>Uniform Color</i>: Uniformly fill the background with a specified color<br>- <i>Environment</i>: The <b>Environment</b> image input mapped to an infinite sphere |
| <b>Background Color</b> <i>Float4</i> | The color used to uniformly fill the background of the rendered scene.<br><i>Note</i>: This parameter is only available when the <b>Background Mode</b> parameter is set to <i>Uniform Color</i>. |
| <b>Enable Ground Plane</b> <i>Boolean</i> | When <i>True</i>, renders a ground plane. The <i>unit cube</i> enclosing the shape rests on this plane. |
| <b>Infinite Plane</b> <i>Boolean</i> | Sets the ground plane to <i>extend infinitely</i> to the horizon.<br><i>Note</i>: This parameter is only available when the <b>Enable Ground Plane</b> parameter is set to <i>True</i>. |
| <b>Ground Plane Size</b> <i>Float2</i> | Adjusts the size of the ground plane.<br><i>Note</i>: This parameter is only available when the <b>Enable Ground Plane</b> parameter is set to <i>True</i> and the <b>Infinite Plane</b> parameter is set to <i>False</i>. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dtexturesurfacerender-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dtexturesurfacerender-variant2.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dtexturesurfacerender-variant3.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dtexturesurfacerender-variant4.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dtexturesurfacerender-node.png" />
        </td>
    </tr>
</table>
