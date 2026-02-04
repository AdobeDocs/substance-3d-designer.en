---
title: "3D renderers"
description: ""
helpx_description: "Designer > Interface > 3D view > 3D renderers"
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



+++

>[!TIP]
>
> You can select the renderer used by default when starting a new 3D View in the ['3D view' section of the project settings](../../preferences-window/project-settings/project-settings.md).

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Rasterizer

+++Parameters
<li data-preserve-html="true"><i>No shadows:</i> No shadows will be rendered.</li>

<li data-preserve-html="true"><i>Voxel marched:</i> March shadow rays into a voxelized scene.</li>

+++

+++Ground plane


+++

![Rasterizer - Example 1](3dRendererRasterizer.jpg "Rasterizer - Example 1"){zoomable="yes"}

## GPU Pathtracer

+++Parameters
<li data-preserve-html="true"><i>No cycling:</i> Disables pixel cycling and computes each full pixel sample.</li>

<li data-preserve-html="true"><i>Device optimal:</i> Selects the ideal pixel cycling resolution based on the device used for rendering.</li>

<li data-preserve-html="true"><i>4x4:</i> Samples 1/16th of the pixels per cycle pass.</li>

<li data-preserve-html="true"><i>8x8:</i> Samples 1/64th of the pixels per cycle pass.</li>

+++

+++Ground plane


+++

![GPU pathtracer - Example 1](3dRendererPathtracer.jpg "GPU pathtracer - Example 1"){zoomable="yes"}

## OpenGL

The OpenGL renderer offers fast real-time rendering, with a few shaders available by default depending on your use case: see the list below.

+++Adobe Standard Material (default)


New generation standardized shader. Ensures correct looks between al Adobe Substance 3D applications and supports the most features out of all shaders.





Two techniques are available for visualizing height:





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.





The Adobe Standard Material is documented in detail inthis sectionof our documentation.



[this section](https://helpx.adobe.com/substance-3d-general/adobe-standard-material.html)

+++

+++AxF SVBRDF


A shader dedicated for visualising materials extracted fromAxF filesand using theSVBRDFrepresentation.



[AxF files](../../../resources/axf-appearance-exchange/axf-appearance-exchange-format.md)



Two techniques are available for visualizing height:





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.





This shader is currently awork in progressand provides an overview of the materials' characteristics, but should not be used for fine adjustments and some features are still unsupported.





Please switch to theIrayrenderer and use themdl::alg::materials &gt; svbrdfMDL shader for a more accurate visualization.



[Iray](../iray/iray.md)

+++

+++Blinn


"Old - generation", non-PBR correct shader. Uses Diffuse, Specular and Glossiness channels next to standard channels like Opacity, Height and Normal.





Two techniques are available for visualizing height:





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.



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





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.



+++

+++Metallic Roughness - Coated


Coated PBR material for the Metallic Roughness model. Uses Basecolor, Metallic and Roughness channels as well as extra "Coat" channels.





Two techniques are available for visualizing height:





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.



+++

+++Metallic Roughness - SSS


Sub-Surface-Scattering PBR material for the Metallic Roughness model. Uses Basecolor, Metallic and Roughness channels as well as extra Scattering channel.





Two techniques are available for visualizing height:





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.



+++

+++Specular Glossiness


Standard PBR material for the Specular Glossiness model. Uses Diffuse, Specular and Glossiness channels.





Two techniques are available for visualizing height:





Parallax Occlusion- Fakes height displacement without modifying geometry through localized UV deformation and occlusion.





Tesselation + Displacement- Subdivides geometry and displaced the vertices along their normals.



+++

+++Unlit


Unlit debug shader to visualize texture maps without any lighting. Only uses a 'color' channel.



+++

Designer also offers the possibilty to configure your own shaders for the OpenGL renderer [using GLSLFX files](../glslfx-shaders/glslfx-shaders.md).

>[!IMPORTANT]
>
> Deprecated
> 
> This renderer will not receive new features and will be retired in a future version of Designer.

![OpenGL - Example 1](3dRendererOpenGL.jpg "OpenGL - Example 1"){zoomable="yes"}

## Iray (deprecated)

>[!NOTE]
>
> The Iray renderer is documented in [this dedicated section](../iray/iray.md).

>[!IMPORTANT]
>
> Deprecated
> 
> This renderer will not receive new features and will be retired in a future version of Designer.

![Iray - Example 1](3dRendererIray.jpg "Iray - Example 1"){zoomable="yes"}
