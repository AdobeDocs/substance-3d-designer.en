---
title: "Pixel processor"
description: "Use the Pixel Processor node to process individual pixels using custom expressions for advanced texture manipulation."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Pixel processor
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/pixel-processor.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - creating-color-palettes
  - filters
  - color-grading
---




# Pixel processor

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Pixel processor](comp_pixelprocessor.png "Atomic node: Pixel processor"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Generates an image where the value of each pixel is the result of the specified [Substance function graph](../../../../function-graphs/the-function-graph/the-function-graph.md).

The Pixel Processor allows you to execute a custom function for every pixel that is returned as output, on an optional input.

It is by far the most versatile node, as it allows any mathematical operation to be run and return results inside your graph.

</td>
</tr>
</table>

Similar to [FX-Map](../../../../function-graphs/fxmaps/fxmaps.md), it requires to set up the internal functionality to perform anything. Where the Pixel processor differs from FX-Map is that it is not focused on placing patterns, with multiple functions controlling pattern shape and placement. Instead, a single function is run in parallel for every pixel, where each pixel is unaware of the calculation results of its neighbors.

The Pixel Processor is similar to the [Value processor](../value-processor/value-processor.md), which runs on only single values and can provide a nice optimization compared to the Pixel processor.

For anybody used to creating [shader](../../../../glossary/glossary.md) functions in node-based editors, the Pixel processor should offer a familiar environment.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">



</td>
<td width="100.00%" style="border: 0;" valign="top">



</td>
</tr>
</table>

>[!TIP]
>
> An annotated project file demonstrating simple uses of the Pixel processor node is available in the [Sample Substance graphs](../../../sample-compositing-graphs/sample-substance-compositing-graphs.md) section of this documentation.
> 
> The [Value processor](../value-processor/value-processor.md) node is a good starting point for learning about [Substance function graphs](../../../../function-graphs/the-function-graph/the-function-graph.md).
> 
> Also consider that working with this type of graph and performing mathematical operations is mandatory for getting anything out of this node.
> 
> We also recommend being familiar with the concept of [UVs](../../../../glossary/glossary.md), [texture sampling](../../../../glossary/glossary.md) and vectors.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Toggles between a grayscale and a color output image. |
| <b>Per pixel function</b> *Float/Float4* | [Substance function graph](../../../../function-graphs/the-function-graph/the-function-graph.md) evaluated per pixel in the output image.   Use the [Get Float2](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/get-nodes/get-nodes.md) node set to the <b>$pos</b> variable to access the [normalized](../../../../glossary/glossary.md) position of the current pixel. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input image &#35;</b> *Grayscale/Color* | Use a [Sample color](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/sampler-nodes/sampler-nodes.md) or [Sample grayscale](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/sampler-nodes/sampler-nodes.md) node to access the values in the input of the specified index. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
