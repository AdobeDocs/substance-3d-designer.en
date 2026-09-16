---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/value-processor.html"
breadcrumb-title: ""
description: Use the Value Processor node to process and manipulate texture values using mathematical operations for custom adjustments.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Value processor
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Value processor
user-guide-description: ""
user-guide-title: ""
---

# Value processor

<table>
<tr style="border: 0;">
<td width="20%" style="border: 0;" valign="top">

![Atomic node: Value processor](value-processor.resources/comp_valueprocessor_1.png "Atomic node: Value processor")

</td>
<td style="border: 0;" valign="top">

Computes a [Substance function graph](../../../../function-graphs/the-function-graph/the-function-graph.md) and outputs its result.

It is comparable to a [Pixel processor](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/pixel-processor/pixel-processor.md), with the difference that it does not compute a function for every pixel, but rather a single value and makes it [available in a Substance graph](../../../../compositing-graphs/values-compositing-graphs/values-in-substance-compositing-graphs.md).

</td>
</tr>
</table>

<div data-preserve-html="true" style="text-align: center;"><img src="value-processor.resources/value-processor-tooltip.gif" alt="value-processor tooltip" /></div>


>[!TIP]
>
> This node is a good starting point for learning about [Substance function graphs](../../../../function-graphs/the-function-graph/the-function-graph.md).
> 
> Also consider that working with this type of graph and performing mathematical operations is mandatory for getting anything out of this node.


## Parameters

|  |  |
| --- | --- |
| <b>Value processor function</b> *Any available value type* | [Substance function graph](../../../../function-graphs/the-function-graph/the-function-graph.md) evaluated to compute the output value. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input image &#35;</b> *Grayscale/Color* | Use a [Sample color](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/sampler-nodes/sampler-nodes.md) or [Sample grayscale](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/sampler-nodes/sampler-nodes.md) node to access the values in the input of the specified index. |


## Examples

*Coming soon.*
