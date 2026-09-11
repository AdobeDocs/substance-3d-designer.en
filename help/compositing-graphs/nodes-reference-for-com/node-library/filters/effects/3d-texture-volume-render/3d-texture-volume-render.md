---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/3d-texture-volume-render.html"
breadcrumb-title: ""
description: Use the 3D Texture Volume Render node to render volumetric textures from 3D data for creating cloud and fog effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > 3D Texture Volume Render
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Texture Volume Render
user-guide-description: ""
user-guide-title: ""
---

# 3D Texture Volume Render

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](3d-texture-volume-render.resources/3dtexturevolumerender.png){width="200px"}

<b>In:</b> Filter &gt; Effect

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **3D Texture Volume Render** node renders the volume of a shape described by a *3D texture*, using its corresponding *signed distance field* from the **3D Signed Distance Field** image input.

The volume is represented within the bounds of a *unit cube*. The lighting is computed using *directional light* and an *hemispherical skylight*.

>[!NOTE]
>
> The signed distance field is expected to be a **4096x4096** texture describing the shape with a **16x16** grid of 256 slices.  
> You may use the [3D Texture SDF](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/3d-texture-sdf/3d-texture-sdf.md) node to compute the signed distance field for a 3D texture of 256 slices.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>3D Signed Distance Field</b> <i>Grayscale</i> | The 4096x4096 image representing the 256 <i>slices</i> of a shape's <i>signed distance field</i>, arranged in a 16x16 grid.<br>You may use the [3D Texture SDF](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/3d-texture-sdf/3d-texture-sdf.md) node to compute the signed distance field for a 3D texture of 256 slices. |
| <b>Density</b> <i>Grayscale</i> | The 4096x4096 image representing the 256 <i>slices</i> of a shape's <i>density</i>, arranged in a 16x16 grid. Density is mapped using grayscale values from 0 (entirely transparent) to 1 (entirely opaque).<br>You may use [3D Volume Mask](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/3d-volume-mask/3d-volume-mask.md) or 3D noise nodes ([3D Perlin Noise](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/3d-perlin-noise/3d-perlin-noise.md), [3D Voronoi](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/3d-voronoi/3d-voronoi.md), [3D Ridged Noise Fractal](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/3d-ridged-noise-fractal/3d-ridged-noise-fractal.md), etc.), combined with a [3D Texture Position](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/3d-texture-position/3d-texture-position.md) node as position input, to generate a volume mask as a 3D texture of 256 slices. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Output Resolution</b> <i>Integer2</i> | The resolution of the output image in <b>X</b> and <b>Y</b>, expressed as a <i>power of two</i>. |
| <b>Camera Position</b> <i>Float2</i> | The position of the camera around the shape.<br>When the node is selected, you may use the position gizmo in the <b>2D View</b> to <i>orbit</i> the camera. |
| <b>Light Position</b> <i>Float2</i> | The position of the <i>directional light</i> around the shape.<br>When the node is selected, you may use the position gizmo in the <b>2D View</b> to <i>orbit</i> the light source. |
| <b>Camera Distance</b> <i>Float</i> | The distance from the camera to the shape. |
| <b>Camera FOV</b> <i>Float</i> | The field of view of the camera in <i>degrees</i>. |
| <b>Absorption</b> <i>Float</i> | Adjusts how much light is absorbed as it passes <i>through</i> the volume. |
| <b>Feather</b> <i>Float</i> | Multiplies the value supplied by the <b>Density</b> input with the <i>inner</i> distance field value.<br>This effectively adjusts the width of the <i>fading gradient</i> from the volume's outer limit inwards. |
| <b>Light Color Mode</b> <i>Integer</i> | Sets the method of acquiring the color of the directional light:<br>- <i>Temperature (Kelvin)</i>: The color results from the light temperature, where a <i>lower</i> value results in a <i>warmer</i> color<br>- <i>RGB Color</i>: Define the color using RGB values |
| <b>Light Temperature (Kelvin)</b> <i>Float</i> | The temperature of the directional light, which impacts its <i>color</i>. A <i>lower</i> value results in a <i>warmer</i> color.<br>Useful values:<br>1800 K - Candle light<br>2800 K - Incandescent bulb<br>5500 K - Daylight<br>6200 K - Natural white<br>7000 K - Overcast sky<br><i>Note</i>: This parameter is only available when the <b>Light Color Mode</b> parameter is set to <i>Temperature (Kelvin)</i>. |
| <b>Light Color</b> <i>Float3</i> | The color of the directional light.<br><i>Note</i>: This parameter is only available when the <b>Light Color Mode</b> parameter is set to <i>RGB Color</i>. |
| <b>Light Intensity</b> <i>Float</i> | The intensity of the directional light. |
| <b>Ambient Color</b> <i>Float3</i> | The color of the ambient skylight. |
| <b>Ambient Intensity</b> <i>Float</i> | The intensity of the ambient skylight. |
| <b>Albedo</b> <i>Float3</i> | The albedo color of the volume. |
| <b>Background Mode</b> <i>Integer</i> | The method of shading the background of the rendered scene, based on the <b>Background Color</b>:<br>- <i>Shaded</i>: The color is impacted by the directional light's <i>color</i> and <i>intensity</i><br>- <i>Constant Color</i>: The color is applied uniformly <i>regardless</i> of the directional light |
| <b>Background Color</b> <i>Float4</i> | The color used to fill the background of the rendered scene. |
| <b>Dithering</b> <i>Float</i> | Adjusts the intensity of the <i>blue noise dithering</i> used to smooth out the shading. |
| <b>Enable Ground Plane</b> <i>Boolean</i> | When <i>True</i>, renders an <i>infinite</i> ground plane. The <i>unit cube</i> enclosing the shape rests on this plane. |
| <b>Infinite Plane</b> <i>Boolean</i> | Sets the ground plane to <i>extend infinitely</i> to the horizon.<br><i>Note</i>: This parameter is only available when the <b>Enable Ground Plane</b> parameter is set to <i>True</i>. |
| <b>Ground Plane Size</b> <i>Float2</i> | Adjusts the size of the ground plane.<br><i>Note</i>: This parameter is only available when the <b>Enable Ground Plane</b> parameter is set to <i>True</i> and the <b>Infinite Plane</b> parameter is set to <i>False</i>. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="3d-texture-volume-render.resources/3dtexturevolumerender-variant2.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-volume-render.resources/3dtexturevolumerender-variant5.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-volume-render.resources/3dtexturevolumerender-variant3.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-volume-render.resources/3dtexturevolumerender-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-volume-render.resources/3dtexturevolumerender-variant4.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-texture-volume-render.resources/3dtexturevolumerender-node.png" />
        </td>
    </tr>
</table>
