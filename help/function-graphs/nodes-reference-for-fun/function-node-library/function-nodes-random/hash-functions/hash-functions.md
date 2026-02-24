---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/function-node-library/function-nodes-random/hash-functions.html"
breadcrumb-title: ""
description: Use hash functions in function graphs to generate deterministic random values based on input coordinates.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Function node library > Random > Hash
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Hash functions
user-guide-description: ""
user-guide-title: ""
---


# Hash functions

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Hash node: icon](hash-icon.png "Hash node: icon"){width="200px"}

<b>In:</b> Functions &gt; Random

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Computes a pseudo-random value between 0 and 1, based on an input value used as a seed.

The number in the title shows the type of value in and value out. E.g.: Hash 23 takes a float2 value as input and outputs a float3 value.

</td>
</tr>
</table>

When a Hash node outputs a value of multiple components, each component has a different pseudo-random value.

Available versions, with their input type and output type:

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<b>Hash 11:</b> Float → Float

<b>Hash 14:</b> Float → Float4

<b>Hash 21:</b> Float2 → Float

<b>Hash 22:</b> Float2 → Float2

</td>
<td style="border: 0;" valign="top">

<b>Hash 24:</b> Float2 → Float4

<b>Hash31:</b> Float3 → Float

<b>Hash 32:</b> Float3 → Float2

</td>
</tr>
</table>

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> | The value used as a seed to compute the pseudo-random output. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Hash 14 example](hash14-example.png "Hash 14 example"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Hash 32 example](hash32-example.png "Hash 32 example"){zoomable="yes"}

</td>
</tr>
</table>
