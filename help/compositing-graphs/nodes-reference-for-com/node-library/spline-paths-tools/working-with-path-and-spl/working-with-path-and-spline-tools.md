---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/working-with-path-and-spline-tools.html"
breadcrumb-title: ""
description: Learn how to work with path and spline tools to create procedural patterns and organic shapes in your graphs.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Working with Path  Spline tools
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Working with Path  Spline tools
user-guide-description: ""
user-guide-title: ""
---


# Working with Path &amp; Spline tools

The Path and Splines toolset is a collection of nodes that lets you author and edit resolution-agnostic shapes and curves that are used to draw, map and scatter images.

## Overview

### What are paths and splines?

<b>Paths</b> are a series of points connected into straight lines.

<b>Splines</b> are smooth curves whose trajectories are shaped by control points and those points' tangents.  
Each point also controls a spline's height and thickness attributes which are used to drive the mapping, warping and scattering of images.

Each can build closed or open shapes.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

### Node output

The nodes output images that carry <b>encoded data</b> representing paths and splines.

For instance, the image on the right represents the image output by a [Paths Polygon](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-polygon/paths-polygon.md) node.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Paths Polygon output](PathsPolygon_Data.jpg "Paths Polygon output")

</td>
</tr>
</table>

As such, the images they produce are not directly usable as a graphic element. They need to be processed by other nodes in the toolset that can convert them into a graphic result that can then be used with the rest of the nodes available for Substance graphs.

As you work with paths and splines, you can preview these objects mapped in an image using the dedicated [Preview Paths](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/preview-paths/preview-paths.md) node for paths, and the dedicated <b>Preview</b> output for splines.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

### 2D View interaction

A significant number of nodes in the toolset offer the ability to perform edits directly in the [2D View](../../../../../interface/2d-view/2d-view.md) using control gizmos. These gizmos include the position gizmo and transformation matrix.

For instance, spline generation nodes such as [Spline (Cubic)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-cubic/spline-cubic.md) or [Spline (Poly Quadratic)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-poly-quadratic/spline-poly-quadratic.md) let you move the control points of the splines. For paths, [Quad Transform on Path](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/quad-transform-on-path/quad-transform-on-path.md) has similar controls when selected.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Spline Cubic in 2D View](SplineCubic-Demo.gif "Spline Cubic in 2D View")

</td>
</tr>
</table>

### Performance

Path and spline tools require intensive computations, so much so that you should be mindful of a couple of settings for ensuring the best performance and responsiveness when working with the toolset:

1. The toolset makes extensive use of <b>Substance Engine</b> features that run much faster on the GPU. Therefore, please use the GPU version of the engine for your system: <b>Direct3D</b> (Windows) or <b>OpenGL</b> (macOS).  
   You can switch engine by pressing the <b>F9</b> key, or by going to <b>Tools &gt; Switch engine...</b> in the main menu bar.
1. Then, we strongly recommend turning off <b>In-context editing</b> in the <b>Graph</b> section of the [Preferences](../../../../../interface/preferences-window/preferences-window.md) (Go to <b>Edit &gt; Preferences...</b> in the main menu bar to access this window).  
   In-context editing lets you open instance nodes in the context of the host graph, which is admittedly very convenient but has the side effect of exponentially increasing the computations required by the toolset's image cache.

You should notice a significant performance improvement when changing any of these two settings to the recommended state.

![Path tools in Library](PathsTools.jpg "Path tools in Library")

## Path tools

### Generating paths

The [Paths Polygon](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-polygon/paths-polygon.md) generates a path in the shape of a polygon of the specified radius and number of sides.

Alternatively, paths can be extracted from a grayscale image using the [Mask to Paths](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) node.  
This is currently the only way of producing complex shapes, and it lets you leverage the entire library of [Substance graph nodes](../../../../../compositing-graphs/nodes-reference-for-com/nodes-reference-for-substance-compositing-graphs.md) to produce the shapes that will eventually be converted into paths.

![Paths generation nodes](Paths_Generation.jpg "Paths generation nodes"){width="600px"}

### Editing paths

[Path 2D Transform](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/path-2d-transform/path-2d-transform.md), [Paths Warp](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-warp/paths-warp.md) and [Quad Transform on Path](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/quad-transform-on-path/quad-transform-on-path.md) let you edit the shape of paths.

You may also remove undesired paths by selecting paths by index or by length, using the [Paths Select](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-select/paths-select.md) node.

More complex processing can be done on each point of a path with the help of the [Paths Vertex Processor](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-vertex-processor/paths-vertex-processor.md) node. A [simpler version](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-vertex-processor-1/paths-vertex-processor-simple.md) exists for lighter adjustments.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

### Preview Paths node

Previewing the result of Paths nodes is done using the dedicated [Preview Paths](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/preview-paths/preview-paths.md) node.  
This node does not have outputs. Double-click LMB on the node to display the preview in the [2D View](../../../../../interface/2d-view/2d-view.md).

Separate paths have a unique color in the preview to easily tell apart each path.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Preview Paths node](PreviewPaths_Node.jpg "Preview Paths node")

</td>
</tr>
</table>

### Paths to Spline

You can leverage the entire toolset dedicated to splines with paths, by converting paths into splines using the [Paths to Spline](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) node.

Keep in mind that splines are curves thus cannot retain the sharpness of paths. Expect some smoothing of shapes when converting paths into splines.

A very useful combination for leveraging the splines toolset through paths is the following:

<b>Mask &gt; Mask to Paths &gt; Paths to Spline</b>

![Path to Spline](Spline_PathToSpline.jpg "Path to Spline")

### Path format specifications

The Preview Paths node is required because Paths nodes output the data of paths encoded in a color image.  
This encoding follows a specification described in the [Paths Format Specifications](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-format-spe/paths-format-specifications.md) page.

You can use this specification to produce your own nodes using this format, and make the most of the [Paths Vertex Processor](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-vertex-processor/paths-vertex-processor.md) nodes.

![Spline tools in Library](SplineTools.jpg "Spline tools in Library")

## Spline tools

### Generating splines

Splines can be generated using nodes such as [Spline Circle](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-circle/spline-circle.md), [Spline (Cubic)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-cubic/spline-cubic.md) or [Spline (Poly Quadratic)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-poly-quadratic/spline-poly-quadratic.md). These nodes let you draw a spline of an arbitrary trajectory using different controls depending on the node.

Alternatively, splines can be extracted from paths using the [Paths to Spline](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) node.  
Keep in mind that splines are curves thus cannot retain the sharpness of paths. Expect some smoothing of shapes when converting paths into splines.

A very useful combination for leveraging the splines toolset through paths is the following:

<b>Mask &gt; Mask to Paths &gt; Paths to Spline</b>

Splines can also help you generate more splines. For example, the [Spline Bridge (2 Splines)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-bridge-2-splines/spline-bridge-2-splines.md) and [Spline Bridge (List)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-bridge-list/spline-bridge-list.md) generate splines traversing a list of splines in order.

### Editing Splines

[Spline 2D Transform](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-2d-transform/spline-2d-transform.md) and [Spline Warp](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-warp/spline-warp.md) let you edit the shape of splines.

You may also remove undesired splines by selecting paths by index, as well as trim splines, using the [Spline Select](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-select/spline-select.md) node.

In addition to its trajectory, the height and thickness properties of splines can be adjusted after the fact using the [Spline Sample Height](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-sample-height/spline-sample-height.md) and [Spline Sample Thickness](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-sample-thickness/spline-sample-thickness.md).

Finally, separate splines can be merged into a single spline thanks to the [Spline Merge List](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-merge-list/spline-merge-list.md) node.

### Appending splines

As you author and edit splines, you may need to combine multiple splines together in order to adjust or use them all at once.

It is important to keep in mind that splines are stored and processed as an <b>ordered list</b>.

Combining splines is done using the [Spline Append](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-append/spline-append.md) node. Appending is the act of adding something at the end of an ordered entity. Indeed, the node combines two lists of splines by adding the second set at the end of the first set.

Therefore, it is very important to consider the order in which you append splines together.

This has an impact on nodes that need to combine splines together, such as [Spline Bridge (List)](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-bridge-list/spline-bridge-list.md), [Spline Bridge Mapper](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-bridge-mapper-gra/spline-bridge-mapper-grayscale.md) and [Spline Merge List](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-merge-list/spline-merge-list.md).

![Appending splines with link creation modes](LinkCreationMode_Splines.gif "Appending splines with link creation modes")

### Spline inputs and outputs

Splines are passed from one node to another using a group of connectors:

* <b>Spline Coords</b>*Color*The coordinates of the input splines’ points encoded in the RGBA channels of a color image.
* <b>Spline Data</b>*Color*Additional data of the input splines encoded in the RGBA channels of a color image.
* <b>Spline Amount</b>*Integer*The number of input splines.

Each output connector of the source node should be connected to the input connector of matching name in the target node.

To make these connections faster, you may use <b>Material</b> or <b>Compact Material</b> [link creation modes](../../../../../interface/the-graph-view/link-creation-modes/link-creation-modes.md). This lets you connect the three spline connectors in a single operation.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Preview output

Most of the nodes offer a <b>Preview</b> output that renders the splines in an image so you can get an idea of what their trajectories and properties are.

This preview can be tweaked in the node parameters, using the parameters in the <b>Preview</b> group.

</td>
<td style="border: 0;" valign="top">

![Preview output on spline node](Spline_PreviewOutput.jpg "Preview output on spline node")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

### Render as segments

Splines are curves with no inherent resolution, which means they can be scaled up or down indefinitely, with the only limit in representing them accurately being the precision used to store their data.

To draw spline as pixels, the toolset simplifies them into lines or segments drawn along the trajectory of the splines.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Spline rendered as segments](Spline_Segments.jpg "Spline rendered as segments")

</td>
</tr>
</table>

This means you may need to pay attention to the number of segments used to draw a spline in an image, as that number may be too low to draw smooth curves, or too high and wasted for the target resolution.

Nodes that draw splines in an image have a <b>Segments Amount</b> parameter that lets you control that amount of segments. A higher value results in smoother curves at the cost of performance.

### Creating images from splines

When you are done authoring and editing splines, they can be used to produce images that can leverage the rest of the Substance graph nodes.

There are three main ways of using splines for generating graphics:

* Render the spline using its shape and properties with the [Spline Render](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-render/spline-render.md) or [Spline Fill](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-fill/spline-fill.md) node;
* Map images along splines with mapping nodes such as [Spline Mapper](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-mapper-grayscale/spline-mapper-grayscale.md), [Spline Bridge Mapper](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-bridge-mapper-gra/spline-bridge-mapper-grayscale.md) and [Spline Flow Mapper](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-flow-mapper/spline-flow-mapper.md);
* Scatter patterns along splines with the [Scatter on Spline](../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/scatter-spline-grayscale/scatter-on-spline-grayscale.md) node.
