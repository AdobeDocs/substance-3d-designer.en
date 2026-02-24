---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/path-tools/paths-vertex-processor.html"
breadcrumb-title: ""
description: Use the Paths Vertex Processor node to transform and manipulate path vertices with advanced options.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Paths Vertex Processor
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Paths Vertex Processor
user-guide-description: ""
user-guide-title: ""
---


# Paths Vertex Processor

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](paths-vertex-processor-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Applies a transformation on the vertices position of the input <b>Paths</b>.

The node should be used as follows:

1. Edit the <b>Per Vertex Function </b>parameter function;
1. Use <b>Get Float2</b> nodes to acquire; the *vertex.pos*, *prev.pos* and/or *next.pos* variables
1. Do some operations on those values (E.g., multiply them to scale the paths);
1. Set the result of your computation as output.

</td>
</tr>
</table>

Be sure to set the appropriate <b>Previous vertices accessed</b> and <b>Next vertices accessed</b> values before querying *prev.pos* or *next.pos*  
You can also add input images and sample them from the function. You must first connect an input to able to sample it from the function. (Be careful, first input is *Image 1*!)  
You can also access the *prev&#91;2&#93;.pos* (Float2), *next&#91;2&#93;.pos* (Float2), *vertex.corner* (bool) and *path.id* (float) variables.

>[!TIP]
>
> For advanced users, the [Paths Format Specification](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-format-spe/paths-format-specifications.md) explains how the data of paths is encoded into color images, and provides tips for manipulating this data directly.

>[!NOTE]
>
> See also [Paths Vertex Processor Simple](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-vertex-processor-1/paths-vertex-processor-simple.md).

## Input connectors

<b>Paths</b> *Color*  
A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) or to another*Path*-processing node.

<b>Input &#35;</b> *Color/Grayscale*  
Inputs for images that should be sampled in the <b>Per Vertex Function</b> parameter function.

## Output connectors

<b>Paths</b> *Color*  
The transformed Paths. You can either use [Preview Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/preview-paths/preview-paths.md) to get an idea of what the result represents, use another Paths-processing node, or input it to a [Paths to Spline](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) to further process it as Splines.

## Parameters

<b>Previous Vertices Accessed</b> *Integer*  
Using this parameter will allow you to get the position of the previous vertex along the path (*prev.pos*) and the previous previous vertex (*prev&#91;2&#93;.pos*) using <b>Get</b> nodes in the <b>Per Vertex Function</b> parameter function.

<b>Next Vertices Accessed</b> *Integer*  
Using this parameter will allow you to get the position of the following vertex along the path (*next.pos*) and the following following vertex (*next&#91;2&#93;.pos*) using <b>Get</b> nodes in the <b>Per Vertex Function</b> parameter function.

<b>Image Input Count</b> *Integer*  
The number of visible <b>Input &#35;</b> input connectors to connect images that should be sampled in the <b>Per Vertex Function</b> parameter function.  
Once you are done setting up all the desired samples, you can hide unused pins by reducing this parameter's value back to 0.

<b>Per Vertex Function</b> *Float2*  
Function applied for each vertex. Must return the new vertex position.  
See the <b>Description</b> section in this page for guidance.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 2](PathsVertexProcessor-Demo2.gif "Node example 2")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
