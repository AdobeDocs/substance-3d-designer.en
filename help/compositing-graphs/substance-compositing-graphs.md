---
title: "Substance graphs"
description: "Learn about Substance compositing graphs in Substance 3D Designer for creating procedural textures and material workflows."
helpx_description: Designer > Substance graphs
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs.html"
helpx_creative_field:
  - 3d-immersive
  - motion
helpx_experience_level:
  - any
helpx_learn_topic:
  - graphs
  - workflow
---




# Substance graphs

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

[![](graph-5.png){width="120px"}](https://substance3d.adobe.com/)

</td>
<td width="100.00%" style="border: 0;" valign="top">

[Substance graphs](https://substance3d.adobe.com/) are the main type of graph created in Substance 3D Designer. Their purpose is to <b>generate and process 2D image data</b> that is not constrained to a set resolution, color or shape. They are meant as extremely versatile image-processing and generation tools, not just static, pre-set results.

The results can be in the form of a simple black-and-white pattern, a filter that only runs on other images and doesn't generate content by itself, or even a full-fledged procedural material with multiple channels.

Substance graphs are[ the most widely supported type of graph](../getting-started/overview/overview.md), and can be exported and used in a plethora of different workflows.

</td>
</tr>
</table>

## Examples

Below you can find some typical examples of common usecases.

+++Simple shape
![Simple shape in Substance graph](simpleshape.png "Simple shape in Substance graph"){width="512px"}



A simple mask shape for a decal is created by generating[ a piece of text](nodes-reference-for-com/atomic-nodes/text/text.md) and a [disc shape](nodes-reference-for-com/node-library/texture-generators/patterns/shape/shape.md), [extracting the edge](nodes-reference-for-com/node-library/filters/effects/edge-detect/edge-detect.md) from the disc and the finally [blending them together](nodes-reference-for-com/atomic-nodes/blend/blend.md) before setting them as final [output](nodes-reference-for-com/atomic-nodes/output/output.md).

The Text with the number, or the thickness of the edge can be exposed externally to make this a more dynamic graph.

+++

+++Adjustment filter
![Adjustment filter in Substance graph](simplefilter.png "Adjustment filter in Substance graph"){width="512px"}



A filter graph takes a normal map as [input ](nodes-reference-for-com/atomic-nodes/input/input.md)(with a custom preview), [converts it to curvature](nodes-reference-for-com/node-library/filters/effects/curvature-smooth/curvature-smooth.md) and then [adjusts the contrast](nodes-reference-for-com/node-library/filters/adjustments/histogram-scan/histogram-scan.md) to create a mask of convex edges as final [output](nodes-reference-for-com/atomic-nodes/output/output.md).

The contrast values set in the Histogram can be exposed, making this a simple but useful filter in combination with the dynamic Input slot.

+++

+++Full material
![Full material in Substance graph](simplematerial.png "Full material in Substance graph"){width="512px"}



A more complicated graph[ blends two Base materials](nodes-reference-for-com/node-library/material-filters/blending-material/material-blend/material-blend.md). One[ Base material](nodes-reference-for-com/node-library/material-filters/pbr-utilities/base-material/base-material.md) is kept simple, the other uses some custom inputs to add interest. A mask is used to determine which of the two materials appear where before being set as final [outputs](nodes-reference-for-com/atomic-nodes/output/output.md).

This example makes use of [Link Creation Modes](../interface/the-graph-view/link-creation-modes/link-creation-modes.md) to simplify using multiple links.

+++
