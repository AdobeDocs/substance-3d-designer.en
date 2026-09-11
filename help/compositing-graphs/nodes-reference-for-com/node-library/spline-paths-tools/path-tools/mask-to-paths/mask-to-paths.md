---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/path-tools/mask-to-paths.html"
breadcrumb-title: ""
description: Use the Mask to Paths node to convert mask textures into path data for procedural path generation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Mask to Paths
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mask to Paths
user-guide-description: ""
user-guide-title: ""
---

# Mask to Paths

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](mask-to-paths.resources/mask-to-paths-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Converts a grayscale input pattern <b>Mask</b> into a list of path segments encoded in the output <b>Paths</b>.

Controls over the start position of generated paths as well as their order in the list are available.

The generated Paths can be further processed using dedicated nodes – E.g., [Path 2D Transform](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/path-2d-transform/path-2d-transform.md), [Paths Warp](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-warp/paths-warp.md) – or converted into splines using the [Path to Spline](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) node to map or scatter shapes along them.

</td>
</tr>
</table>

>[!NOTE]
>
> The method used to encode Paths is explained in the [Paths Format Specifications](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-format-spe/paths-format-specifications.md) page.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask</b> <i>Grayscale</i> | The input pattern which should be converted into a list of Paths. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Preview</b> <i>Color</i> | A preview composited on top of the mask to help visualizing the effects of the parameters. |
| <b>Paths</b> <i>Color</i> | A list of paths encoded in a color image. each path describes a list of encoded segments.<br>The result can be processed using another Paths-processing node, or sent to a [Paths to Spline](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) node to further process it as Splines. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Smooth Mask</b> <i>Float</i> | Apply smoothing on the input mask.<br>Useful when the input pattern has very sharp edges, which usually causes artifacts. |
| <b>Mask Threshold Value</b> <i>Float</i> | The grayscale value of <b>Mask</b> that will be used to separate the outside (values &lt; Mask Threshold Value) and the inside (values &gt; Mask Threshold Value) of the shape. |
| <b>Decimate Path</b> <i>Float</i> | Implicitly controls the amount of segments that will be generated.<br>A high amount of decimation will make round shapes somewhat polygonal, while no decimation will generate almost one segment by pixel.<br>A reasonable amount will better match the shape of both straight lines and curves without creating a lot of intermediary points for straight lines. |
| <b>Close opened Paths</b> <i>Boolean</i> | Create a segment between the start and the end vertices of open paths.<br>Disabling this may fix undesirable lines traversing your pattern in an unexpected way, however paths may not be closed anymore. |
| <b>Corner Threshold</b> <i>Float</i> | Each vertex encoded in paths can hold a flag indicating whether it is hard (I.e., a corner) or smooth.<br>This parameter lets you mark more or less corners according to the angle between their adjacent segments.<br><i>Note:</i> This 'corner' flag is currently not supported by any existing node but are available to be used in a [Path Vertex Processor](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-vertex-processor/paths-vertex-processor.md) node. You may also visualize the corners with the [Preview Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/preview-paths/preview-paths.md) node. |
| <b>Path Startup Mode</b> <i>Integer</i> | The method of selecting which vertex should be the start of each generated Path around the shapes in the Mask.<br>This has a significant impact when converting the generated <b>Paths to Splines</b> using the dedicated node, as multiple Spline nodes use the Splines' start and end.<br>*- Most acute vertex:* The vertex forming the lowest angle with its previous and next vertices<br>*- Vertex at extreme of a specified direction:* The last vertex in a given direction<br>*- Vertex closest to a specified position<br>* Vertex farthest from a specified position<br>* Custom startup function:* Use a custom function to select the vertex which should be used as the start each Path |
| <b>Startup Direction</b> <i>Float</i> | The angle describing the direction used to select the startup vertex. For each Path, the last vertex in this direction is selected.<br>The value is a *number of turns* used to rotate an X-leftdirection vector. This means 0 sets a direction vector of (-1, 0), and 0.25 (90 degrees) sets a direction vector of (0, 1).<br><i>Note:</i> This parameter is available when <b>Path Startup Mode</b> is set to 'Vertex at extreme of a specified direction' |
| <b>Startup Target Position</b> <i>Float2</i> | The position in the image used to select the startup vertex.<br>For each Path, the vertex closest to or farthest from this position is selected, according to the selected <b>Path Startup Mode</b>.<br><i>Note:</i> This parameter is available when <b>Path Startup Mode</b> is set to 'Vertex closest to a specified position' or 'Vertex farthest from a specified position' |
| <b>Startup Function</b> <i>Float</i> | The function used to select the startup vertex. It returns a Float value.<br>For each vertex, the function is executed and the vertex for which the function returns the *highest result* is selected.<br>Available variables:<br>*-* vertex.cornerness(Float)*:* The score of the vertex as a candidate to be a corner<br>*-* vertex.pos(Float2)*:* The vertex position in image space<br><i>Note:</i> This parameter is available when Path Startup Mode is set to 'Vertex closest to a specified position' or 'Custom startup function' |
| <b>Order Mode</b> <i>Integer</i> | The method of ordering the generated Paths.<br>The position or size Paths' *bounding box* (Bbox) may be used as a criterion for ordering the Paths.<br>This has a significant impacts when converting the generated <b>Paths to Splines</b> using the dedicated node, as multiple Spline nodes use the Splines' order.<br>*- Legacy (fast):* The method used in the previous version of this node, which offers significantly better performance<br>*- By Bbox center position along direction:* Paths are ordered according to the position of the center of their Bbox, from first to last along the specified direction<br>*- By Bbox Bbox top-left position along direction:* Paths are ordered according to the position of the top-left corner of their Bbox, from first to last along the specified direction<br>*- By Bbox size - Largest to smallest:* Paths are ordered according to the size of their Bbox, from largest to smallest<br>*- By Bbox size - Smallest to largest:* Paths are ordered according to the size of their Bbox, from smallest to largest<br>*- Custom ordering function:* Use a custom function to order Paths |
| <b>Ordering direction</b> <i>Float</i> | The angle describing the direction used to order the Paths from first to last along that direction.<br>The value is a *number of turns* used to rotate an X-left direction vector. This means 0 sets a direction vector of (-1, 0), and 0.25 (90 degrees) sets a direction vector of (0, 1). |
| <b>Ordering function</b> <i>Float</i> | The function used to order the Paths. It returns a Float value.<br>Paths are ordered in *ascending order* according to this function's value. In other words, the result of the function for each Path is the *sorting key* used to order the Paths.<br>Available variables:<br>* bbox.center (Float2): The position of the Path Bbox's center<br>* bbox.topleft (Float2): The position of the Path Bbox's top-left corner<br>* bbox.size (Float2): The size of the Path Bbox (X: width, Y: height) |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="mask-to-paths.resources/MaskToPaths-Variant2-Before.jpg" alt="MaskToPaths-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="mask-to-paths.resources/MaskToPaths-Variant2-After.jpg" alt="MaskToPaths-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="mask-to-paths.resources/MaskToPaths-Variant1-Before.jpg" alt="MaskToPaths-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="mask-to-paths.resources/MaskToPaths-Variant1-After.jpg" alt="MaskToPaths-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 2](mask-to-paths.resources/MaskToPaths-Demo2.gif "Node example 2"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Node example 1](mask-to-paths.resources/MaskToPaths-Demo1.gif "Node example 1"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 3: Startup modes](mask-to-paths.resources/MaskToPaths-Demo3.gif "Node example 3: Startup modes"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Node example 3: Ordering modes](mask-to-paths.resources/MaskToPaths-Demo4.gif "Node example 3: Ordering modes"){zoomable="yes"}

</td>
</tr>
</table>
