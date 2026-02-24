---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/3d-view/3d-renderers.html"
breadcrumb-title: ""
description: Choose between rasterizer and pathtracer renderers in the 3D view for different preview quality and performance.
helpx_creative_field: ""
helpx_description: Designer > Interface > 3D view > 3D renderers
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D renderers
user-guide-description: ""
user-guide-title: ""
---



# 3D renderers

The 3D View offers four renderers:

* Two versions of Adobe's in-house 3D renderer: Rasterizer for real-time visualization  with support for shadows, and GPU Pathtracer for accurate rendering of shadows, reflections, complex material properties and more.
* Two deprecated third-party renderers: OpenGL and NVIDIA's Iray.

>[!NOTE]
>
> Keep graphics drivers up to date!
> 
> The new 3D renderers are regularly upgraded and some of these upgrades require recent GPU drivers. Please update your system's GPU drivers to the latest version for the best reliability and support of rendering features.
> 
> You may find drivers here:   [NVIDIA](https://www.nvidia.com/Download/index.aspx?lang=en-us)   [AMD](https://www.amd.com/en/support)   [Intel](https://downloadcenter.intel.com/product/80939/Graphics-Drivers)

+++Rasterizer / GPU pathtracer comparison


<table>
  <tr>
    <td>
      <img src="3dRendererRasterizer-2.jpg" alt="3dRendererRasterizer-2">
      <br><i>Before</i>
    </td>
    <td>
      <img src="3dRendererPathtracer-2.jpg" alt="3dRendererPathtracer-2">
      <br><i>After</i>
    </td>
  </tr>
</table>



![3dRendererRasterizer-2](3dRendererRasterizer-2.jpg "3dRendererRasterizer-2")

![3dRendererPathtracer-2](3dRendererPathtracer-2.jpg "3dRendererPathtracer-2")

+++

Adobe's 3D renderer is built from the ground up to support modern technologies such as [MaterialX](https://materialx.org/) shading language and the [USD](https://openusd.org/release/index.html) scene description, and is poised to offer full visual consistency across the entire Substance 3D ecosystem.

Thanks to its reliance on USD, it can leverage Adobe's [USDFileFormat plugin](https://github.com/adobe/USD-Fileformat-plugins) to import many 3D scene formats, such as FBX and GLTF, and render these scenes fully, including materials, textures, cameras and lights.

+++Scene import: Rasterizer vs. OpenGL


<table>
  <tr>
    <td>
      <img src="3dRendererRasterizer-2.jpg" alt="3dRendererRasterizer-2">
      <br><i>Before</i>
    </td>
    <td>
      <img src="3dRendererOpenGL-2.jpg" alt="3dRendererOpenGL-2">
      <br><i>After</i>
    </td>
  </tr>
</table>



![3dRendererRasterizer-2](3dRendererRasterizer-2.jpg "3dRendererRasterizer-2")

![3dRendererOpenGL-2](3dRendererOpenGL-2.jpg "3dRendererOpenGL-2")

+++

>[!TIP]
>
> You can select the renderer used by default when starting a new 3D View in the ['3D view' section of the project settings](../../../help/interface/preferences-window/project-settings/project-settings.md).

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Rasterizer

</td>
<td style="border: 0;" valign="top">

### GPU Pathtracer

</td>
<td style="border: 0;" valign="top">

### OpenGL

</td>
<td style="border: 0;" valign="top">

### Iray

</td>
</tr>
</table>

## Rasterizer

+++Parameters

|  |  |
| --- | --- |
| <b>Samples</b> Float | Specifies the number of pixel samples to compute before the image is considered to be converged. |
| <b>Tessellation factor</b> Integer | Sets the number of subdivisions for GPU tessellation. |
| <b>Enable displacement</b> Boolean | Specifies whether displacement should be enabled. |
| <b>Displacement threshold</b> Float | Sets up a threshold to enable/disable GPU tessellation. |
| <b>Enable backface culling</b> Boolean | A true value will enable the culling of triangle meshes that have normals that face away from the camera. A false value will disable backface culling. |
| <b>Diagnostic mode</b> Integer | Dictates the diagnostic mode to render. |
| <b>Rasterizer shadow mode</b> Integer | Specifies the technique to use to render shadows:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>No shadows:</i> No shadows will be rendered.</li> <li data-preserve-html="true"><i>Voxel marched:</i> March shadow rays into a voxelized scene.</li> </ul> |
| <b>Rasterizer shadow sample count</b> Integer | Specifies how many shadow rays are traced per pixel. |
| <b>Rasterizer shadow opacity</b> Float | Specifies the opacity of shadows, from 0.0 (no shadows) to 1.0 (fully shadows). |
| <b>Rasterizer order independent transparency enabled</b> Boolean | Does not account for the order of the transparent surfaces when rendering them. This sacrifices some accuracy for faster rendering of transparent surfaces. |
| <b>Enable rasterizer SSS</b> Boolean | Toggles the subsurface scattering effect. |
| <b>Rasterizer SSS sample count</b> Integer | Specifies how many samples are taken per pixel for rendering subsurface scattering. |
| <b>Enable rasterizer accumulation antialiasing</b> Boolean | Toggles accumulation antialiasing, which improves the smoothness or edges in the rendered image by jittering renders and computing the local average color of each pixel, cumulatively. I.e., it accumulates values to compute an average from. |
| <b>Rasterizer voxel grid resolution</b> Integer | Dictates the resolution of the voxel grid used in voxel marching the rasterizer.   Higher values result in more precise shadows at the cost of performance. |


+++

+++Ground plane

|  |  |
| --- | --- |
| <b>Enabled</b> Boolean | Toggles the ground plane in the rendered scene. |
| <b>Height</b> Float | Controls the height offset of the ground plane.   If authored, the value is expected to have the appropriate bias baked in, based on the scale of the scene. |
| <b>Shadow intensity</b> Float | When shadows are enabled, controls the opacity of the shadows cast on the ground plane, from 0.0 (no shadows) to 1.0 (full shadows). |


+++

![Rasterizer - Example 1](3dRendererRasterizer.jpg "Rasterizer - Example 1"){zoomable="yes"}

## GPU Pathtracer

+++Parameters

|  |  |
| --- | --- |
| <b>Samples</b> Float | Specifies the number of pixel samples to compute before the image is considered to be converged. |
| <b>Tessellation factor</b> Integer | Sets the number of subdivisions for GPU tessellation. |
| <b>Enable displacement</b> Boolean | Specifies whether displacement should be enabled. |
| <b>Displacement threshold</b> Float | Sets up a threshold to enable/disable GPU tessellation. |
| <b>Enable backface culling</b> Boolean | A true value will enable the culling of triangle meshes that have normals that face away from the camera. A false value will disable backface culling. |
| <b>Pixel cycling type</b> Integer | Specifies the technique to use to lower compute resolution for interactive rendering:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>No cycling:</i> Disables pixel cycling and computes each full pixel sample.</li> <li data-preserve-html="true"><i>Device optimal:</i> Selects the ideal pixel cycling resolution based on the device used for rendering.</li> <li data-preserve-html="true"><i>4x4:</i> Samples 1/16th of the pixels per cycle pass.</li> <li data-preserve-html="true"><i>8x8:</i> Samples 1/64th of the pixels per cycle pass.</li> </ul> |
| <b>Diagnostic mode</b> Integer | Dictates the diagnostic mode to render. |
| <b>View background through transmission</b> Boolean | A true value enables the background image to be seen through transmissive or refractive objects.   When this is false, transmissive objects will show the refracted image of the scene environment. |


+++

+++Ground plane

|  |  |
| --- | --- |
| <b>Enabled</b> Boolean | Toggles the ground plane in the rendered scene. |
| <b>Height</b> Float | Controls the height offset of the ground plane.   If authored, the value is expected to have the appropriate bias baked in, based on the scale of the scene. |
| <b>Shadow intensity</b> Float | When shadows are enabled, controls the opacity of the shadows cast on the ground plane, from 0.0 (no shadows) to 1.0 (full shadows). |
| <b>Enable local lights</b> Boolean | Controls whether direct lighting from local lights contributes to shadow catchers. |
| <b>Enable reflections</b> Boolean | Controls the visibility of all reflections on the ground plane. |
| <b>Reflections opacity</b> Float | When reflections are enabled, controls the opacity of the reflections, between 0.0 (no reflections) to 1.0 (full reflections). |
| <b>Reflections roughness</b> Float | When reflections are enabled, controls the material roughness of the ground plane contributing to the reflections, from 0.0 (fully glossy) to 1.0 (fully rough). |


+++

![GPU pathtracer - Example 1](3dRendererPathtracer.jpg "GPU pathtracer - Example 1"){zoomable="yes"}

## OpenGL

The OpenGL renderer offers fast real-time rendering, with a few shaders available by default depending on your use case: see the list below.

+++Adobe Standard Material (default)
New generation standardized shader. Ensures correct looks between al Adobe Substance 3D applications and supports the most features out of all shaders.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

The Adobe Standard Material is documented in detail in [this section](https://helpx.adobe.com/substance-3d-general/adobe-standard-material.html) of our documentation.

+++

+++AxF SVBRDF
A shader dedicated for visualising materials extracted from [AxF files](../../../help/resources/axf-appearance-exchange/axf-appearance-exchange-format.md) and using the <b>SVBRDF</b> representation.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

This shader is currently a *work in progress* and provides an overview of the materials' characteristics, but should not be used for fine adjustments and some features are still unsupported.

Please switch to the [Iray](../../../help/interface/3d-view/iray/iray.md) renderer and use the <b>mdl::alg::materials &gt; svbrdf</b> MDL shader for a more accurate visualization.

+++

+++Blinn
"Old - generation", non-PBR correct shader. Uses Diffuse, Specular and Glossiness channels next to standard channels like Opacity, Height and Normal.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

+++

+++Lambert
Very simple lambert lighting shader, only supports Diffuse channel. Uses the old point lights system, does not support HDR image lighting.

+++

+++Mesh Info
Debug unlit shader to visualize the following geometry data:

* Normal

* Tangent

* Binormal

* UV

* UV Tile

* Vertex color

* Position (world space)

The visualization is clamped to &#91;0, 1&#93;. It is therefore not possible to acquire a direct reading of values outside of that range on the screen.

+++

+++Metallic Roughness
Standard PBR material for the Metallic Roughness model. Uses Basecolor, Metallic and Roughness channels.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

+++

+++Metallic Roughness - Coated
Coated PBR material for the Metallic Roughness model. Uses Basecolor, Metallic and Roughness channels as well as extra "Coat" channels.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

+++

+++Metallic Roughness - SSS
Sub-Surface-Scattering PBR material for the Metallic Roughness model. Uses Basecolor, Metallic and Roughness channels as well as extra Scattering channel.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

+++

+++Specular Glossiness
Standard PBR material for the Specular Glossiness model. Uses Diffuse, Specular and Glossiness channels.

Two techniques are available for visualizing height:

<b>Parallax Occlusion</b> - Fakes height displacement without modifying geometry through localized UV deformation and occlusion.

<b>Tesselation + Displacement</b> - Subdivides geometry and displaced the vertices along their normals.

+++

+++Unlit
Unlit debug shader to visualize texture maps without any lighting. Only uses a 'color' channel.

+++

Designer also offers the possibilty to configure your own shaders for the OpenGL renderer [using GLSLFX files](../../../help/interface/3d-view/glslfx-shaders/glslfx-shaders.md).

>[!IMPORTANT]
>
> Deprecated
> 
> This renderer will not receive new features and will be retired in a future version of Designer.

![OpenGL - Example 1](3dRendererOpenGL.jpg "OpenGL - Example 1"){zoomable="yes"}

## Iray (deprecated)

>[!NOTE]
>
> The Iray renderer is documented in [this dedicated section](../../../help/interface/3d-view/iray/iray.md).

>[!IMPORTANT]
>
> Deprecated
> 
> This renderer will not receive new features and will be retired in a future version of Designer.

![Iray - Example 1](3dRendererIray.jpg "Iray - Example 1"){zoomable="yes"}
