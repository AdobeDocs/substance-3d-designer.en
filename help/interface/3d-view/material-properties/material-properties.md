---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/3d-view/material-properties.html"
breadcrumb-title: ""
description: Configure material properties in the 3D view to preview and adjust how your Substance materials appear on 3D objects.
helpx_creative_field: ""
helpx_description: Designer > Interface > 3D View > Material properties
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material properties
user-guide-description: ""
user-guide-title: ""
---

# Material properties

The [3D View](../../../interface/3d-view/3d-view.md) renders the surface of models using a program called a *shader*. The shader defines the material
applied to the model using a list of properties which impact various aspects of the model's appearance.

The **Materials** menu of the 3D View lets you check which shader is used for each of the scene's materials.

<a name="openpbr"></a>

## OpenPBR

Designer uses the [OpenPBR](https://academysoftwarefoundation.github.io/OpenPBR/) material model by default, which supports several complex effects such as anisotropy,
transmission and fuzz.

The default [graph templates](../../../compositing-graphs/creating-compositing-gra/creating-a-substance-compositing-graph.md#graph-templates) and the [material samples](../../../compositing-graphs/creating-compositing-gra/creating-a-substance-compositing-graph.md#material-samples) included in Designer are all based on the OpenPBR model.

This shader's properties follow the [OpenPBR parameter reference](https://academysoftwarefoundation.github.io/OpenPBR/#parameterreference), and are *shared* across the Rasterizer,
GPU Pathtracer and OpenGL [3D renderers](../3d-renderers/3d-renderers.md).

+++ UVs

| Parameter                       | Type    | Default  | Description                                                                                                                                                                                                 |
|---------------------------------|---------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tiling                          | Float   | 1.0      | The amount of texture repetitions in one UV cell, where a higher value<br/>results in more texture repetitions.                                                                                             |
| Enable physical size from graph | Boolean | False    | Automatically adjust the tiling according to the graph's [Physical size](../../../compositing-graphs/graph-parameters/graph-parameters.md)<br/>in order to represent the material at the appropriate scale. |
| UV scale                        | Float2  | 1.0, 1.0 | Adjusts the scale of the tiling by a separate factor for U and V, where<br/>a higher value results in more texture repetitions.                                                                             |

+++

+++ Base

| Parameter         | Type         | Default       | Description                                                                                           |
|-------------------|--------------|---------------|-------------------------------------------------------------------------------------------------------|
| Weight            | Float        | 1.0           | Multiplier on the intensity of the reflection from the diffuse and metallic base.                     |
| Color             | Float3 (RGB) | 0.8, 0.8, 0.8 | Color of the reflection from the diffuse and metallic base.                                           |
| Metalness         | Float        | 0.0           | Specifies how metallic the base material appears. (Dials the base from pure dielectric to pure metal) |
| Diffuse roughness | Float        | 0.0           | Roughness of the diffuse reflection. Higher values cause the surface to appear flatter.               |

+++

+++ Specular

| Parameter  | Type         | Default       | Description                                                                                                                                        |
|------------|--------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Weight     | Float        | 1.0           | Multiplies the specular reflectivity.                                                                                                              |
| Color      | Float3 (RGB) | 1.0, 1.0, 1.0 | Color of the specular reflection. (Controls the physical edge-tint for metals,<br/>and a non-physical overall tint for dielectrics)                |
| Roughness  | Float        | 0.3           | The roughness of the specular reflection. Lower numbers produce sharper<br/>reflections, higher numbers produce blurrier reflections.              |
| Anisotropy | Float        | 0.0           | The directional bias of the roughness of the metal/dielectric base, resulting<br/>in increasingly stretched highlights along the tangent direction. |
| IOR        | Float        | 1.5           | Index of refraction of the dielectric base.                                                                                                        |

+++

+++ Transmission

| Parameter        | Type         | Default       | Description                                                                                                                                                 |
|------------------|--------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Weight           | Float        | 0.0           | Mixture weight between the transparent and opaque dielectric base.<br/>The greater the value the more transparent the material.                             |
| Color            | Float3 (RGB) | 1.0, 1.0, 1.0 | Controls color of the transparent base due to Beer's law volumetric<br/>absorption under the surface.                                                       |
| Depth            | Float        | 0.0           | Specifies the distance light travels inside the transparent base before<br/>it becomes exactly the `transmission_color` according to Beer's law. |
| Scatter          | Float3 (RGB) | 0.0, 0.0, 0.0 | Controls the color of light volumetrically scattered inside the transparent base.                                                                           |
| Anisotropy       | Float        | 0.0           | The amount of directional bias, or anisotropy, of the volumetric scattering<br/>in the transparent base.                                                    |
| Dispersion scale | Float        | 0.0           | Linearly scales the amount of dispersion.                                                                                                                   |
| Abbe number      | Float        | 20.0          | Physical Abbe number of the dielectric medium, describing how much<br/>the dielectric index of refraction varies across wavelengths.                        |

+++

+++ Subsurface

| Parameter    | Type         | Default        | Description                                                                                                                                                              |
|--------------|--------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Weight       | Float        | 0.0            | Mixture weight which dials the opaque dielectric base between<br/>diffuse reflection and subsurface scattering.                                                          |
| Color        | Float3 (RGB) | 0.8, 0.8, 0.8  | The observed reflection color of the subsurface scattering medium.                                                                                                       |
| Radius       | Float        | 1.0            | Length scale of the subsurface scattering mean free path.                                                                                                                |
| Radius scale | Float3 (RGB) | 1.0, 0.5, 0.25 | RGB multiplier to subsurface_radius, giving the per-channel scattering<br/>mean-free-paths.                                                                              |
| Anisotropy   | Float        | 0.0            | Controls the phase-function of subsurface scattering, where zero<br/>scatters light evenly, positive values scatter forwards, and negative<br/>values scatter backwards. |

+++

+++ Coat

| Parameter  | Type         | Default       | Description                                                                                                                                         |
|------------|--------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Weight     | Float        | 0.0           | The presence weight of a reflective clear-coat layer on top of the material.<br/>Use for materials such as car paint or an oily layer.              |
| Color      | Float3 (RGB) | 1.0, 1.0, 1.0 | The color of the clear-coat layer's transparency, due to absorption in the coat.                                                                    |
| Roughness  | Float        | 0.0           | The roughness of the clear-coat reflections.<br/>The lower the value, the sharper the reflection.                                                   |
| Anisotropy | Float        | 0.0           | The directional bias of the roughness of the clear-coat layer,<br/>resulting in increasingly stretched highlights along the coat tangent direction. |
| IOR        | Float        | 1.6           | The index of refraction of the clear-coat layer.                                                                                                    |
| Darkening  | Float        | 1.0           | Modulates the physical coat darkening effect.                                                                                                       |

+++

+++ Fuzz

| Parameter | Type         | Default       | Description                                                                                                                                       |
|-----------|--------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Weight    | Float        | 1.0           | The presence weight of a fuzz layer that can be used to approximate microfibers,<br/>for fabrics such as velvet and satin as well as dust grains. |
| Color     | Float3 (RGB) | 1.0, 1.0, 1.0 | The color of the fuzz layer.                                                                                                                      |
| Roughness | Float        | 0.5           | The roughness of the fuzz layer.                                                                                                                  |

+++

+++ Emission

| Parameter | Type         | Default       | Description                                          |
|-----------|--------------|---------------|------------------------------------------------------|
| Luminance | Float        | 0.0           | The amount of emitted light, as a luminance in nits. |
| Color     | Float3 (RGB) | 1.0, 0.0, 0.0 | The color of the emitted light.                      |

+++

+++ Thin-film

| Parameter | Type  | Default | Description                                                                                           |
|-----------|-------|---------|-------------------------------------------------------------------------------------------------------|
| Weight    | Float | 0.0     | Coverage weight of the thin-film.<br/>Use for materials such as multi-tone car paint or soap bubbles. |
| Thickness | Float | 0.5     | The thickness of the thin-film layer on the base. (In micrometers)                                    |
| IOR       | Float | 1.4     | The index of refraction of the thin-film.                                                             |

+++

+++ Geometry

| Parameter         | Type         | Default       | Description                                                                                                                                                                                                                                                                                                                                                               |
|-------------------|--------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Opacity           | Float        | 1.0           | The opacity of the entire material.                                                                                                                                                                                                                                                                                                                                       |
| Thin walled       | Boolean      | False         | If true the surface is double-sided and represents an infinitesimally thin shell.<br/>Suitable for extremely geometrically thin objects such as leaves or paper.                                                                                                                                                                                                          |
| Normal            | Float3 (RGB) | 0.5, 0.5, 1.0 | Input geometric normal for the surface.                                                                                                                                                                                                                                                                                                                                   |
| Tangent           | Float3 (RGB) | 1.0, 0.5, 0.0 | Input geometric tangent.                                                                                                                                                                                                                                                                                                                                                  |
| Coat normal       | Float3 (RGB) | 0.5, 0.5, 1.0 | Input normal for coat layer.                                                                                                                                                                                                                                                                                                                                              |
| Coat tangent      | Float3 (RGB) | 1.0, 0.5, 0.0 | Input geometric tangent for coat layer.                                                                                                                                                                                                                                                                                                                                   |
| Height            | Float        | 0.5           | Displacement (or bump) amount in the direction of the normal.<br/>When height is equal to the height level, there is no displacement.<br/>Displacement is a scalar change in surface position toward unperturbed,<br/>blended normal surface.<br/>In cases where tessellated displacement is not possible or desired,<br/>height may be implemented as a bump map.        |
| Height level      | Float        | 0.5           | Value of height corresponding to no displacement (zero-level value).<br/>Height level shifts (but does not scale or flip) the displacement relative<br/>to the undisplaced object's surface.<br/>If height level is 0, all displacement is above.<br/>If height level is 1, all displacement is below the surface, but it still retains<br/>the same scale and direction. |
| Height scale      | Float        | 1.0           | Scale of displacement or bump in scene space units.<br/>The magnitude and direction of scale is independent of the value of height level.                                                                                                                                                                                                                                 |
| Ambient occlusion | Float        | 1.0           | Ambient occlusion map for darkening occluded areas.<br/>White (1.0) means fully lit, black (0.0) means fully occluded.                                                                                                                                                                                                                                                     |

+++

### Compatibility with existing graphs

Some of OpenPBR material properties have different usage identifiers compared to other models included in Designer.
Designer automatically matches some identifiers to ensure compatibility with OpenPBR as its default model.

+++ Legacy to OpenPBR usage mappings

| Legacy                  | OpenPBR                     |
|-------------------------|-----------------------------|
| metallic                | metalness                   |
| specularEdgeColor       | specularColor               |
| roughness               | specularRoughness           |
| anisotropyLevel         | specularRoughnessAnisotropy |
| IOR                     | specularIOR                 |
| absorptionColor         | transmissionColor           |
| absorptionDistance      | transmissionDepth           |
| translucency            | subsurfaceWeight            |
| scatteringColor         | subsurfaceColor             |
| scatteringDistance      | subsurfaceRadius            |
| scatteringDistanceScale | subsurfaceRadiusScale       |
| coatOpacity             | coatWeight                  |
| sheenOpacity            | fuzzWeight                  |
| sheenColor              | fuzzColor                   |
| sheenRoughness          | fuzzRoughness               |
| emissive                | emissionColor               |

+++

### Further reading

To learn more about OpenPBR, here are some resources:

* [Adobe blog article](https://blog.adobe.com/en/publish/2023/08/08/openpbr-strengthens-interoperability-enabling-enhanced-creativity)
* [White paper](https://academysoftwarefoundation.github.io/OpenPBR/)
* [Adobe's OpenPBR BSDF on GitHub](https://github.com/adobe/openpbr-bsdf)
* [Designer 16.0: Support of OpenPBR](../../../release-notes/version-16-0/version-16-0.md#openpbr-support)

<a name="adobe-standard-material"></a>

## Adobe Standard Material

The Adobe Standard Material (ASM) model was introduced in Designer 11.2 and has been Designer's default shader 
up to version 15.1.

While Designer moved to OpenPBR as its new default model, ASM is still included and its properties are also shared
across the Rasterizer, GPU Pathtracer and OpenGL [3D renderers](../3d-renderers/3d-renderers.md).

The model is documented [here](https://experienceleague.adobe.com/en/docs/substance-3d/general-knowledge/asm/adobe-standard-material).

<a name="usdpreviewsurface"></a>

## UsdPreviewSurface

The purpose of the UsdPreviewSurface model is previewing materials with a basic feature set promoting compatibility
across renderers that include USD and/or Hydra.

In Designer, this material model is only supported by the Rasterizer and GPU Pathtracer [3D renderers](../3d-renderers/3d-renderers.md).

The model is documented [here](https://openusd.org/dev/spec_usdpreviewsurface.html).
