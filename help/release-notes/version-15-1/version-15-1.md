---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/release-notes/version-15-1.html"
breadcrumb-title: ""
description: Review release notes for Substance 3D Designer version 15.1 to learn about new features, improvements, and bug fixes.
helpx_creative_field: ""
helpx_description: Designer > Release Notes > Version 15.1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Version 15.1
user-guide-description: ""
user-guide-title: ""
---


# Version 15.1

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Version 15.1

</td>
<td style="border: 0;" valign="top">

*Release date: December 11th, 2025*

</td>
</tr>
</table>

![Banner Designer 15.1](bannerweb.png)

## Improve graph creation

In this release, the [graph creation window](../../help/compositing-graphs/creating-compositing-gra/creating-a-substance-compositing-graph.md) has been <b>comprehensively redesigned</b> to enhance the initial user experience in Substance 3D Designer. The primary goal of this update is to streamline the template selection process, allowing users to efficiently identify the most suitable template for their requirements.

Thumbnails offer instant <b>visual references</b> for the intended material types, while detailed tooltips supply all pertinent information. For improved organization, templates are now classified into specific <b>categories</b> such as materials, filters, and scan processing.

Although the main interface has been upgraded, users continue to have access to previous views, including list, packages, and directories options.

[Learn more](../../help/compositing-graphs/creating-compositing-gra/creating-a-substance-compositing-graph.md)

![redesigner new graph window](newgraph.png){zoomable="yes"}

## Embedded samples

With the launch of our redesigned graph creation window, we've added a variety of [<b>sample materials</b>](../../help/compositing-graphs/creating-compositing-gra/material-samples/material-samples.md) directly inside the software. This enhancement is in response to your request for better access to learning resources.

![New graph creation window for samples](GraphSample.png){zoomable="yes"}

To meet this need we have included material samples such as fabrics (including leather and satin), wood, metal, plastic, ceramic and more. These examples are intended to help you start your projects with ease and get acquainted with the main family nodes available in Substance 3D Designer

Each graph is <b>annotated</b>, carefully organized, and contains a minimal number of nodes to make it as easy to understand as possible.

You can access the samples in the 'Material samples' category when creating a new Substance graph, or directly from the Home screen using the convenient 'Go to samples' button.

Alongside these foundational materials, we've also provided <b>advanced samples</b> to demonstrate how to use <b>FX-map and Pixel processor</b> features more effectively.

[Learn more](../../help/compositing-graphs/creating-compositing-gra/material-samples/material-samples.md)

![wood sample in substance designer](samplegraph.png){zoomable="yes"}

## New noises

Noises play a crucial role in the majority of graphs, which is why we have focused on several key enhancements in this release to improve their functionality and usability.

With this update, we have introduced <b>better support for non-tiling scenarios</b>, ensuring that noise patterns behave as expected without mandatory tiling. Previously, noise nodes were either forced to tile or produced incorrect results when tiling was disabled.

Most noises now include <b>new parameters</b>, providing users with greater creative control. These additional options empower graph authors to fine-tune the appearance and behavior of noise within their workflows.

Finally, bitdepth is <b>no longer hard-locked to 16-bits</b>. You can now override the bitdepth setting on individual node instances, allowing you to achieve higher detail and dynamic range when needed, or optimize your graphs for performance.

See the full list of updated noises in the [release notes](#release-notes) below.

Examples:   [Cells 1](../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/cells-1/cells-1.md)   [Clouds 2](../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/clouds-2/clouds-2.md) [  Directional scratches](../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/directional-scratches/directional-scratches.md) [  Moisture noise 1](../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/moisture-noise/moisture-noise.md)

![directionnal disorder noise](directionaldisorder.gif){zoomable="yes"}

## Hierarchy in node menu

To address the challenge of locating specific nodes within the extensive library, we have introduced categories in the Node menu.

The vast number of available nodes can make it difficult to quickly find the desired one. To streamline this process, a new [<b>Group</b> attribute](../../help/compositing-graphs/graph-parameters/graph-parameters.md) has been implemented at the graph level. When this attribute is defined, it is used to organize and sort the search results.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![node search with category 1](search1-2.png){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![node search with category 2](search2.png){zoomable="yes"}

</td>
</tr>
</table>

## Default output

When a node has multiple [outputs](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md), it is not possible to display all of them simultaneously in the 2D view or as the node thumbnail. The prevailing guideline in such scenarios is to utilize the first connected pin, or, if none are connected, the first output by default.

However, this approach may not always yield optimal results. For instance, in some Spline nodes the first connected pin often represents spline coordinates data, which is not suitable for previewing purposes.

To address this, a default output attribute has been introduced. This feature allows the graph author to <b>specify which output should be displayed by default</b>, thereby enhancing the intuitiveness of node usage and facilitating a clearer understanding of the authored graph.

Play with the image below to see the difference before and after the default output definition.

[Learn more](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md)

<table>
  <tr>
    <td>
      <img src="defaultouput2.png" alt="defaultouput2">
      <br><i>Before</i>
    </td>
    <td>
      <img src="defaultouput1.png" alt="With the default output, thumbnails are always relevant.">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## 'Is defined' node

When working with function graphs, you may need to determine whether a [variable](../../help/function-graphs/nodes-reference-for-fun/atomic-function-nodes/get-nodes/get-nodes.md) exists within the graph.

For instance, detecting the absence of a variable enables you to provide a fallback value, ensuring the function behaves as expected without requiring every input to be explicitly set. That’s why we added the ['Is defined' node](../../help/function-graphs/nodes-reference-for-fun/atomic-function-nodes/get-nodes/get-nodes.md).

[Learn more](../../help/function-graphs/nodes-reference-for-fun/atomic-function-nodes/get-nodes/get-nodes.md)

</td>
<td style="border: 0;" valign="top">

![Is defined node](isdefined.png){zoomable="yes"}

</td>
</tr>
</table>

## Release notes

### 15.1.0

*(Released December 11th, 2025)*

### Added

* &#91;NewGraph&#93; Rework of the new graph window
* &#91;NewGraph&#93; Add materials samples and advanced samples
* &#91;NewGraph&#93; Add a new attribute for graph for the template data (category and sub-title)
* &#91;NewGraph&#93; Remove Output format option
* &#91;Content&#93; Add hash functions
* &#91;Content&#93; Add tonemappers to functions.sbs
* &#91;Content&#93; Anisotropic noise v2: add default output format, add disorder
* &#91;Content&#93; Apply sentence case to node and parameters labels
* &#91;Content&#93; BnW spots 1 v2: add default output format, no tiling support
* &#91;Content&#93; BnW spots 2 v2: add default output format, no tiling support
* &#91;Content&#93; BnW spots 3 v2: add default output format, no tiling support
* &#91;Content&#93; Cells 1,2,3,4 v2: add default output format, no tiling support, disorder options
* &#91;Content&#93; Clouds 1 v2: add default output format, no tiling support
* &#91;Content&#93; Clouds 2 v2: add default output format, no tiling support
* &#91;Content&#93; Clouds 3 v2: add default output format, no tiling support
* &#91;Content&#93; Color to mask v2
* &#91;Content&#93; Directional noise 1 v2: add default output format, no tiling support
* &#91;Content&#93; Directional noise 2 v2: add default output format, no tiling support
* &#91;Content&#93; Directional noise 3 v2: add default output format, no tiling support
* &#91;Content&#93; Directional noise 4 v2: add default output format, no tiling support
* &#91;Content&#93; Directional scratches v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 1 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 2 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 3 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 4 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 5 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt gradient v2: add default output format, new disorder options
* &#91;Content&#93; Fractal Sum Base v2: add default output format, disorder, no tiling support
* &#91;Content&#93; Fractal sum 1,2,3,4 v2: add default output format
* &#91;Content&#93; Gaussian noise v2: add default output format, no tiling support
* &#91;Content&#93; Gaussian spots 1&amp;2 v2: add default output format, no tiling support
* &#91;Content&#93; Messy fibers 1,2,3  v2: add default output format, no tiling support, disorder options
* &#91;Content&#93; Moisture noise v2: add default output format, no tiling support
* &#91;Content&#93; New 'Moisture noise 2' node
* &#91;Content&#93; Noises: update to add default outputformat
* &#91;Content&#93; Perlin noise v2: add default output format, no tiling support
* &#91;Content&#93; Shape mapper: add filtering mode
* &#91;Content&#93; UV mapper: add filtering mode
* &#91;Content&#93; Waveform 1 v2: use default output format + new options
* &#91;Content&#93; White noise v2: use default output format, add distribution options
* &#91;Bakers&#93; Display the UVs from the selected mesh only
* &#91;Bakers&#93; Add an option to select the method of matching geometry by name
* &#91;Bakers&#93; Select the closest Baker when a baker is deleted
* &#91;Bakers&#93; UDIM: define a list of UV tiles to bakes
* &#91;Bakers&#93; Update bake sdk to 3.15.4
* &#91;3D View/SceneBrowser&#93; Avoid selecting a UsdPrimitive when doing a right click on it
* &#91;ColorManagement&#93; Support ACES 2.0
* &#91;Compositing Graph&#93; Allow to set an output node as the "Default output"
* &#91;Cooker&#93; Remove warning on unconnected inputs of function instances¬†
* &#91;Functions&#93; Add isDefined operator
* &#91;Graph&#93; Group the items per 'group' attribute in the node menu
* &#91;Graph&#93; Improve thumbnail rendering

### Fixes

* &#91;3D View&#93; L16 Grayscale texture is displayed with a red tint when plugged to the environment or the baseColor
* &#91;3D View&#93; Changing the material binding of a scene with no material creates a new "default" material
* &#91;3D View&#93; Computed normals are not correct for specific OBJ meshes
* &#91;3D View&#93; Custom environment from SBSSCN is not visible on load in Pathtracer
* &#91;3D View&#93; Errors in the Console when rotating a disabled environment
* &#91;3D View&#93; Specular level is not applied correctly
* &#91;3D View&#93; Specular edge color doesn't work when using Eclair rasterizer
* &#91;3D View&#93; User added material is not applied on default scenes
* &#91;3D View&#93;&#91;Bakers&#93; Material color is too dark once overridden or when using a "Color" baker
* &#91;3D View&#93;&#91;Bakers&#93; No material color from FBX file
* &#91;Bakers&#93; Material colors in FBX files are not correctly detected
* &#91;Bakers&#93; 'recompute\_tangents' option is always 'false' in JSON preset exports
* &#91;Bakers&#93; CLI: Crash when running the same baker consecutively through JSON file
* &#91;Bakers&#93; Updating the 'color-generator' parameter does not work for 'Grayscale'
* &#91;Content&#93; Mask to paths: Failure in non-square ratios
* &#91;Content&#93; PBR Render/Icon renderer: Incorrect specular lobe function
* &#91;Content&#93; Paths to spline: Set the 'Output size' to 'Relative to parent' by default'
* &#91;Content&#93; Point list: Points are not in the correct order when data texture is non-square
* &#91;Content&#93; Spline mapper: 1px line glitch in random cases
* &#91;Content&#93; Spline mapper: stretched UVs in some cases when thickness is 0
* &#91;Graph&#93; Crash when deleting the output of a function subgraph
* &#91;Graph&#93; Input node color type can be changed in read-only packages
* &#91;Graph&#93; Primary input can be changed in read-only packages
* &#91;Properties&#93; The color of the color preview widget does not match the sRGB button state
* &#91;Scene&#93; Cannot load an OBJ file larger than 2 GB
* &#91;UI&#93; The Console and Dependency manager docking states are not restored after restart

### KNOWN ISSUES

* &#91;Bakers&#93; Crashes during baking with some specific NVIDIA drivers
* &#91;3D View&#93; OpenGL: some imported scenes may not be rendered
* &#91;3D View&#93; Pathtracer: slow performances when updating textures with tesselation/displacement enabled
* &#91;3D View&#93; Some color material properties are not color-managed correctly when overridden
* &#91;3D View&#93; Scenes with animated primitives are not properly supported
* &#91;3D View&#93; Mesh with multiples UDims are not yet supported
* &#91;3D View&#93; Mesh with multiples UVs are not yes supported and may result in invalid material rendering
* &#91;3D View&#93; Pathtracer not supported on AMD graphic cards
