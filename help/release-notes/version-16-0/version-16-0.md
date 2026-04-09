---
helpx_url: ""
breadcrumb-title: ""
description: Review release notes for Substance 3D Designer version 16.0 to learn about new features, improvements, and bug fixes.
helpx_creative_field: ""
helpx_description: Designer > Release Notes > Version 16.0
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Version 16.0
user-guide-description: ""
user-guide-title: ""
---

# Version 16.0

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Version 16.0

</td>
<td style="border: 0;" valign="top">

*Release date: April ##th, 2026*

</td>
</tr>
</table>

![Banner Designer 16-0](./version-16-0-banner.jpg)

## Shape splatter v2 nodes

### New ways of scattering shapes

The new Shape splatter v2 nodes unlock complex scattering behaviors that have been challenging until now, with **more shape distribution methods** (Poisson disc, uniform) that are *collisionless* by default, and control over the *clean gathering* of shapes in specific areas with a **density map**.
Advanced users can set up *custom distributions* defined by a function graph.

[Examples: Poisson, uniform, density map]

### 3D shapes

Scattered shapes are now **3D objects** that can be moved, rotated and scaled on all XYZ axes.

Use **simple primitives** such a cubes, spheres and cylinders, or **complex custom shapes** formed by *extruding a height map* or authoring *3D SDF shapes*. (More on that below)

This unlocks scatterings that are more dynamic, more varied and more believable across the board. And it is now possible to repurpose 3D shapes for variations by flipping them. (We see you, environment artists!)

[Examples: Primitives, extrude height map, 3D SDF]

### Companion nodes

Similarly to the Shape splatter v1 family of nodes, Shape splatter v2 comes with its own cohort of companion nodes.

**Shape splatter v2 mapper** nodes enable projection of textures on the scattered 3D shapes, with support for *triplanar projection* and *material IDs* for mapping multiple textures. Results can be adjusted globally or per shape for texture offsets and color variations.
Again, advanced users can set up *custom texture mappings* defined by a function graph.

**Shape splatter v2 to mask** creates masks for specific selection of shapes and/or material IDs, enabling more granular use of shapes downstream in the graph.

[Examples: Mapper standard, mapper triplanar, to mask]

### Grid atlas

Custom patterns can be provided separately to the Shape splatter v2 node, or packed into a grid atlas for leaner and more efficient workflows. Packing patterns is simplified thanks to the new Grid atlas nodes.

[Examples: Grid atlas, grid atlas interop with Shape splatter v2 nodes]

---

The new Shape Splatter nodes overcome the limitations of the previous version with uncapped scaling and randomizing options, as well as expanded pattern ingestion through atlas input.

Beyond that it introduces a new way to scatter shapes, with more distribution options, a density multiplier to drive the concentration of patterns as well as the possibility to rotate them in 3D. 

In combination with the SDF nodes, this toolset gives you more creative freedom and advanced scattering capabilities.

## 3D SDF nodes (signed distance field)

Designer 16.0 adds a powerful method of generating 3D shapes in a function graph using a vast catalogue of nodes for authoring SDF functions.

Signed distance fields are representations of space as a distance to surfaces defined mathematically. They can be used to define shapes of increasing complexity as these surfaces are transformed and combined using various operators.

### Authoring 3D SDF functions

SDF functions involve a new family of nodes which come in 3 categories:

* Primitives are the basic building blocks, they generate simple adjustable shapes with a few controls that let you tailor them as needed.
* Operators combine or replicate shapes in straightforward or complex ways depending on the node: from simple boolean operators to morphs, shell and symmetries, they dramatically expand the possibilities of what kind of 3D shape can be achieved
* Transforms let you adjust the shapes' position, rotation and size as you might expect and beyond with bending, twisting and elongation.

[Examples: SDF primitives, operators, transforms]

Lightweight nodes with clear and readable icons make building 3D SDF functions easier than you might think, especially with this next addition to the toolset...

### 3D viewer node

As you author 3D SDF functions, you will need to visualize the resulting shapes in 3D space. The 3D viewer node renders 3D SDF or intersection functions as a 3D scene with adjustable camera controls, custom environment light and support for rendering basic materials. (Color, roughness and metalness)

The node also includes features for checking the generated shapes in detail and debugging issues: separate rendering passes (AOV), SDF isolines and visual helpers. (E.g. Bbox bleed coloration, grid and rotation arcs)

[Examples: Adjustable camera, AOVs, helpers + isolines]

## OpenPBR support

The OpenPBR material model is now supported throughout the application, with dedicated shaders in both our new renderers (Rasterizer, GPU Pathtracer) and the OpenGL renderer.

Get started with this widely adopted industry standard with new graph templates, or go through the built-in material samples now based on OpenPBR.

[Examples: OpenPBR template, OpenPBR material sample]

The OpenPBR shader is now the default for the 3D View and natively supports graphs from previous versions by matching legacy PBR usages to OpenPBR's.

OpenPBR shaders support more effects than the existing shaders, such as thin film and thin wall. All effects are available in rasterization (Rasterizer, OpenGL), including refraction at long last!

[Examples: OpenPBR shader in each renderer]

It is also easier to keep workflows involving specific shaders in sync, with a new <code>Material model</code> attribute for Substance graphs that ensures that graphs viewed in the 3D View use the appropriate shader for the graph's material model.

**Note:** The attribute is also included in published SBSAR files to integrate in your material workflow.

## Displacement controls in the 3D View

It is now faster and easier to adjust displacement and tessellation in the 3D View, with direct access in a new Displacement pop-up available in the 3D View toolbar.

Adjust the height scale, height level and tessellation values without repeated back and forth in material properties and renderer settings.

These controls are available for both our new renderers (Rasterizer, GPU Pathtracer) and the OpenGL renderer.

[Examples: Displacement pop-up in each renderer]

In the scene includes multiple materials, select the object of the scene that you want to adjust beforehand by holding Shift and clicking it (Rasterizer and GPU Pathtracer only) or select it in the Scene browser.

Please note that tessellation is per object in Rasterizer and GPU Pathtracer, and per material in OpenGL.

**Tip:** Tooltips are available for each parameter to better understand their effect.

## Other changes

### Constant value nodes

For easier access to constant values in Substance graphs, nodes have been added for generating a simple value of each type.

[Example: Constant value nodes]

### MDL graphs and Iray end-of-life

As you have been notified in the 15.1 release, the MDL graph feature set and the Iray renderer are now removed from Designer.

Our in-house GPU Pathtracer is the renderer of choice for high-quality photorealistic rendering in Designer.

Designer is moving away from MDL in favor of MaterialX as its shading language of choice for interchangeable, widely-supported material definitions.

MaterialX has rapidly gained traction in the computer graphics industries, and can be carried by USD files for full scene portability across DCCs and renderers.

**Note:** The documentation for MDL graphs and the Iray renderer is available through their dedicated end-of-life page.

### VFX platform upgrades & macOS minimal version

The following libraries have been upgraded to meet the latest VFX platform standard:

* C++ 20
* Python 3.13
* Qt 6.8
* Boost 1.88
* OpenColorIO 2.5
* OpenSubDiv 3.7
* OpenEXR 3.4
* oneTBB 2022

The requirement for the minimal supported version of macOS has been updated to macOS 14 Sonoma.

## Release notes

### 16.0.0

*(Released April ##th, 2026)*

### Added

* &#91;Category&#93; Item

### Fixes

* &#91;Category&#93; Item

### KNOWN ISSUES

* &#91;Category&#93; Item
