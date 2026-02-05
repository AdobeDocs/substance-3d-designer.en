---
title: "Parameters not working as expected"
description: ""
helpx_description: "Designer > Technical issues > Parameters not working as expected"
---

# Parameters not working as expected

This page lists common causes for parameters not working as expected in Substance 3D Designer, and offers troubleshooting steps for each.

## Parameter not working in Preview mode and published Substance 3D asset (SBSAR)

<b>!&#91;(error)&#93;(error.svg) Issue</b>

Some exposed parameters for a graph are *not listed* when using [Preview mode](../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md) in Designer, or in the parameters list of [Substance 3D assets](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) (SBSAR) published out of that graph.

<b>!&#91;(tick)&#93;(check.svg)Recommended steps</b>

The missing parameters are likely [static parameters](../../glossary/glossary.md), which *cannot be edited on-the-fly* after the graph has been *cooked* – i.e., processed in order to run its algorithm quickly and efficiently. Cooking occurs in Designer every time the graph is *edited* or *published*. Parameters impacted by such limitations are listed in the [Limitations](../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md) section of the [Exposing a parameter](../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md) page of this documentation.

As such, static parameters are visible and editable in Designer, but are *hidden* in a published Substance 3D asset. You may use [Preview mode](../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md) to see these limitations in effect before publishing to a Substance 3D asset.

Here is a list of static parameters:

| Node | Parameter |
| --- | --- |
| All nodes | Tiling mode  Pixel ratio |
| [Uniform color](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/uniform-color/uniform-color.md) | Color mode |
| [Pixel processor](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/pixel-processor/pixel-processor.md) | Color mode |
| [Blend](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blend/blend.md) | Blending mode  Alpha blending  Cropping area |
| [FX-Map](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/fx-map/fx-map.md) | Blending mode |
| [Quadrant](../../function-graphs/fxmaps/the-quadrant-node/the-quadrant-node.md) | Pattern  Input image alpha  Input image filtering |

## Incorrect result for Substance function graph applied to parameter

<b>!&#91;(error)&#93;(error.svg) Issue</b>

A Substance function graph applied to a node parameter does not output the expected value when a negative integer is used.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

Negative integers are currently not properly supported. As a workaround, use the negative integer value in an [Integer2](../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/constant-nodes/constant-nodes.md) value and extract it using a [Swizzle Integer](../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/vector-and-swizzle-nodes/vector-and-swizzle-nodes.md) node.
