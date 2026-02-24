---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/fxmaps/using-functions-in-fxmaps/using-the-sampler-nodes.html"
breadcrumb-title: ""
description: Learn how to use sampler nodes in FXMaps to sample textures and create procedural material variations.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > FXMaps > Using Functions in FXMaps > Using the Sampler nodes
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Using the Sampler nodes
user-guide-description: ""
user-guide-title: ""
---


# Using the Sampler nodes

![](sampler-graph.jpg)

The sampler node can be used to sample pixel values in an image input plugged to the fx-map node. The sampled values can then be used to drive any parameters using functions.

## Simple Example

In this example a chain of quadrant nodes have been created to generate a grid of pattern. A function is created in the Opacity/Luminance parameter of the last quadrant.

![](sampler-function.jpg){width="300px"}![](sampler-result-1.jpg){width="300px"}

The Sample node takes a float2 input as the sampling coordinates (x, y). In this example we used the $pos variable: for each pattern, the pixel value is sampled at the pattern position in the first image input plugged to the FxMap node.

The Sample Gray node returns a float1 value in the 0, 1 range.

The Sample Color node returns a float4 (rgba) value in the 0, 1 range.

## Advanced Example

Here, we compare the sampled value to a constant (0.3). If the sampled value is greater than 0.3 the function returns 1, else, it returns 0.

![](sampler-function-advanced.jpg){width="300px"}![](sampler-result-advanced.jpg){width="300px"}

## Download sample

[![SBS file icon](sbs-1.png){width="64px"}](https://shared-assets.adobe.com/link/d5f9adf3-0bb5-49a1-4eb9-a0506d4f3f32)
