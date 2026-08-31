---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/pbr-utilities/pbr-render.html"
breadcrumb-title: ""
description: Use the PBR Render node to render physically-based materials with realistic lighting for previewing material appearance.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > PBR Render
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: PBR Render
user-guide-description: ""
user-guide-title: ""
---

# PBR Render

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](pbr-render.resources/pbr-render-01.png){width="250px"}

<b>In:</b> Material Filters &gt; PBR Utilities

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Renders a PBR material onto a sphere, plane or cylinder using Image Based Lighting (IBL).This is a render-engine inside a node, which can be very useful for generating thumbnails, previews or 2D assets. It is not a render like the 3D view, but an actual texture being generated in your graph.

This node requires at least a full PBR material to be plugged in. Ideally you make use of Link Creation Modes to connect the material to PBR Render. Additionally, you will need a spherically-unwrapped HDRI environment for the render to calculate lighting from. Materials for testing can be found under PBR Materials, Environment maps can be found under [3D View in the library.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/3d-view-library/3d-view-library.md)

</td>
</tr>
</table>

>[!WARNING]
>
> **CPU (SSE2) Engine**
> 
> The PBR Render Node is very heavy and does not work well with the SSE2 CPU engine. Switch to another engine by pressing F9, if node performs extremely bad.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Material channel inputs</b> | Multiple material inputs are used to render the material on the geometry:<br><br>- Base Color<br>- Normal<br>- Emissive<br>- Roughness<br>- Metallic<br>- Specular Level<br>- Height<br>- Ambient Occlusion<br>- Opacity Mask<br>- Anisotropy Level<br>- Anisotropy Angle<br>- Translucency<br>- Scattering Distance Scale |
| <b>Lens Dirt Map</b> <i>Grayscale Input</i> | Custom map for dirt on lens, that appears when lens flares are visible. |
| <b>Lens Aperture Map</b> <i>Grayscale Input</i> | Can be used to override Bokeh, out-of-focus shape. The more contrasted, the more visible it is. Keep in mind only a circle within the texture is sampled, so any shape has to fit within a circle. |
| <b>Background input</b> <i>Color input</i> | Custom map used as background when the <b>Background Mode</b> parameter is set to <i>Backgroud Input</i> |
| <b>Environment Map</b> <i>Color Input</i> | Enviroment map used to calculate lighting. Must be spherically-mapped and in HDR. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Beauty</b> | The final render |
| <b>Raw Irradiance</b> | The irradiance data of the final render<br><br><i>Alpha:</i> Opacity map |
| <b>Raw Specular</b> | The specular data of the final render<br><br><i>Alpha:</i> Specular shadow map |
| <b>Normal World Space</b> | The world space normals data of the final render<br><br><i>Alpha:</i> World space height map |
| <b>Normal Tangent Space</b> | The tangent space normals data of the final render<br><br><i>Alpha:</i> Tangent space height map |
| <b>UVs</b> | The UV data of the final render<br><br><i>Alpha:</i> Opacity map |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Shape</b> <i>Sphere, Plane, Cylinder</i> | Sets the shape used for rendering. Custom shapes are not possible. |
| <b>Displacement Intensity</b> <i>0.0 - 0.5</i> | Set the intensity of displacement from height. |
| <b>Environment Rotation</b> <i>0.0 - 1.0</i> | Rotates the lighting environment. Pre-rotates compared to moving the camera. |
| <b>Background Mode</b> <i>Color, Environment, Ambient, Background Input</i> | Set what is shown in the background. Color is a solid color, Environment is the map you plugged in with an optional blur. Ambient is a very blurred version of the environment. |
| <b>Background Color</b> <i>(Color value)</i> | Only available when Background mode is set to Color. |
| <b>Environment Background Blur</b> <i>0.0 - 1.0</i> | Only available when Background mode is set to Environment. |
| <b>Shape</b> |  |
| <b>Scale</b> <i>0.0 - 2.0</i> | Set the scale for the Sphere. |
| <b>Plane Size</b> <i>0.0 - 1.0</i> | Set the scale for the Plane. |
| <b>Cylinder Radius</b> <i>0.0 - 1.0</i> | Set the radius for the Cylinder. |
| <b>Cylinder Length</b> <i>0.0 - 1.0</i> | Set the length for the Cylinder. |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Rotates shape without rotating lighting. |
| <b>Rotation Direction</b> <i>0.0 - 1.0</i> | Sets the axis of rotation in 2D. |
| <b>Rotation Around Direction</b> <i>0.0 - 1.0</i> | Spins shape on the rotation axis. |
| <b>Shape Position</b> <i>-1.0 - 1.0</i> | Moves shapes. |
| <b>UV Tiling</b> <i>1.0 - 6.0</i> | Sets the amount of UV-Tiling. |
| <b>Sphere UV Scale</b> <i>0.0 - 4.0</i> | Sets the scale of UV's on the Sphere. |
| <b>Plane UV Scale</b> <i>1.0 - 4.0</i> | Sets the scale of UV's on the Plane. |
| <b>Cylinder UV Scale</b> <i>1.0 - 6.0</i> | Sets the scale of UV's on the Cylinder. |
| <b>UV Offset</b> <i>0.0 - 1.0</i> | Offsets UV's |
| <b>Tilt UVs</b> <i>False/True</i> | Tilts UV's by 45 degrees for the Sphere. |
| <b>Camera</b> |  |
| <b>Exposure</b> <i>-4.0 - 4.0</i> | Set camera exposure. |
| <b>Tone Mapper</b> <i>Linear, ACES, Filmic Hejl</i> | Set which tone mapping solution to use for the final image. |
| <b>Camera Mode</b> <i>Perspective, Orthographic</i> | Switch camera between two projection modes. |
| <b>Field of View</b> <i>0.01 - 100.0</i> | Set camera FOV angle. |
| <b>Distance</b> <i>0.0 - 4.0</i> | Set the distance of the camera from the object center. |
| <b>Vignette Intensity</b> <i>0.0 - 1.0</i> | Set intensity of vignette effect. |
| <b>Vignette Radius</b> <i>0.0 - 1.0</i> | Set radius of the vignette effect. |
| <b>Screen Position</b> | Moves the camera around the object, can be changed with a gizmo in the 2D view as well. |
| <b>Depth of Field</b> |  |
| <b>Aperture Radius</b> <i>0.0 - 0.1</i> | Sets radius of the aperture. Higher values mean out-of-focus areas get blurrier (bokeh). |
| <b>Aperture Blades</b> <i>3 - 9</i> | Sets the shape of the bokeh blur. |
| <b>Aperture Ring</b> <i>0.0 - 1.0</i> | Adds an inner gradient to the bokeh shape. |
| <b>Aperture Difraction</b> <i>0.0 - 2.0</i> | Adds chromatic aberration to the bokeh. |
| <b>Swirly Bokeh</b> <i>0.0 - 1.0</i> | Adds a swirl or spinning type of effect to out-of-focus bokeh blur areas. |
| <b>Focus Mode</b> <i>Auto, Point</i> | Set if focus is pre-determined or user-set. Point focus lets you move a point in the 2D view to determine the focus distance. |
| <b>Focus Point</b> | If focus is set to Point, this lets you move that point. has a 2D view gizmo. |
| <b>Focus Offset</b> <i>-0.5 - 0.5</i> | If focus is set to Auto, allows you to shift it back and forth. |
| <b>Use Custom Aperture Map</b> <i>False/True</i> | Overrides Aperture settings above and use Aperture map input to determine the bokeh shape. Requires an input. |
| <b>Post Effects</b> |  |
| <b>Enable Post Effects</b> <i>False/True</i> | Toggles <i>all</i> post-effects in the final render. |
| <b>Bloom Intensity</b> <i>0.0 - 2.0</i> | Sets strength of the bloom effect. |
| <b>Bloom Threshold</b> <i>0.0 - 2.0</i> | Sets low threshold for bloom to appear. |
| <b>Bloom Chroma Shift</b> <i>0.0 - 1.0</i> |  |
| <b>Lens Halo Intensity</b> <i>0.0 - 1.0</i> | Sets intensity for the lens halo effect. |
| <b>Lens Flares Intensity</b> <i>0.0 - 1.0</i> | Sets intensity for the lens flare. Make sure the light from your environment background is in view to properly see this effect. |
| <b>Lens Dirt Intensity</b> <i>0.0 - 1.0</i> | Sets effect of lens dirt map on the Lens flares. |
| <b>Render Settings</b> |  |
| <b>Diffuse Quality</b> <i>16 Samples, 32 Samples, 64 Samples, 128 Samples</i> | Switch between quality levels for the diffuse map. |
| <b>Diffuse Emissive Mulitplier</b> <i>0.0 - 1.0</i> | Controls how much the emissive parts are contributing to the irradiance. |
| <b>Diffuse Shadow Intensity</b> <i>0.0 - 1.0</i> | Controls the intensity of the diffuse shadows. |
| <b>Specular Dithering</b> <i>0.0 - 1.0</i> | Set the amount of dithering for the specular. |
| <b>Specular Shadow Multiplier</b> <i>0.0 - 1.0</i> | Controls the intensity of shadows in the specular reflections. |
| <b>Opacity Mode</b> <i>Dithered Alpha test, Simple Alpha Blend</i> | Controls the method of applying transparency. The <i>Simple Alpha Blend</i> mode is most visible on uniform backgrounds. |
| <b>Ambient Occlusion Intensity</b> <i>0.0 - 1.0</i> | Sets the intensity of ambient occlusion shadows. |
| <b>Material Adjustements</b> |  |
| <b>Recompute Normals</b> <i>False/True</i> | Normals will be recomputed from the height map according to the displacement intensity. |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switch between different Normal Map formats (inverts the green channel) |
| <b>Dielectric F0 Input</b> <i>Constant Value, Specular Level input</i> | Set what drives F0 values. Specular Level input means it will be driven by an input map. |
| <b>Dielectric F0</b> <i>0.0 - 0.08</i> | If Constant Value is chosen for Dielectric F0 Input, this slider lets you set the global value. |
| <b>Clear Coat</b> |  |
| <b>Enable Clear Coat</b> <i>False/True</i> | Enables an additional, simple clear coat layer on top of the input material. |
| <b>Clear Coat Weight</b> <i>0.0 - 1.0</i> | Sets intensity or strength of the clearcoat layer. |
| <b>Clear Coat Specular Level</b> <i>0.0 - 1.0</i> | Sets the roughness of the clearcoat layer. |
| <b>Inherit Normal from Base Layer</b> <i>False/True</i> | Set if clearcoat ignores or uses normals from the base material. |
| <b>Emissive</b> |  |
| <b>Enable Emissive Lighting</b> <i>True/False</i> | Toggles the diffuse contribution of emissive lighting. |
| <b>Emissive Intensity</b> <i>0.0 - 10.0</i> | Sets global multiplier for the emissive map. |
| <b>Subsurface Scattering</b> |  |
| <b>Enable Subsurface Scattering</b> <i>True/False</i> | Toggles subsurface scattering in the final render.<br><br><i>Note:</i> Subsurface scattering requires the <b>Translucency</b> input value be <i>higher than 0.0</i> |
| <b>Scattering Distance</b> <i>0.0 - 1.0</i> | Adjusts the maximum distance of the scattering effect.<br><br><i>Note:</i> This value is multipled against the <b>Scattering Distance Scale</b> input value <i>per color channel</i>. |
| <b>Red Shift</b> <i>0.0 - 1.0</i> | Adjusts the intensity of the Red shift effect in the scattering. |
| <b>Rayleigh</b> <i>0.0 - 1.0</i> | Adjusts the intensity of the Rayleigh effect in the scattering. |

## Examples

All images were generated directly inside of Designer, in the 2D viewport, using materials from the [Substance 3D assets](https://substance3d.adobe.com/assets) library.

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-02.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-03.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-04.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-05.jpg" />
        </td>
    </tr>
    <tr style="border: 0; background: transparent">
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-06.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-07.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-08.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="pbr-render.resources/pbr-render-09.jpg" />
        </td>
    </tr>
</table>
