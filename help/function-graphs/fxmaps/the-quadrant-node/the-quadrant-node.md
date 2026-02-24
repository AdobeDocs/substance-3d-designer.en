---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/fxmaps/the-quadrant-node.html"
breadcrumb-title: ""
description: Use the Quadrant node in FXMaps to divide textures into four sections for creating tiled patterns and variations.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > FXMaps > The Quadrant Node
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: The Quadrant Node
user-guide-description: ""
user-guide-title: ""
---


# The Quadrant Node

Many FX-Maps consists entirely of chains of Quadrant nodes. Quadrant nodes are the most powerful and flexible node in the FX-Map group, so it is well worthwhile to understand how this node works.

The most important thing about Quadrant nodes is that they are the only node which can increase the depth or *octave*, of the FX-Map graph. Each Quadrant node adds to the underlying quad-tree graph; none of the other nodes do so.

The Quadrant node has a number of parameters:

## Color / Luminosity

When the node is adding an image to the FX-Map, these settings define how the channels are blended with other images in the chain. The *Color / Luminosity*parameters apply to any images rendered by this particular node.

### Branch Offset

Shifts the node's image. The offset is applied to all the other images rendered by subsequent nodes in the graph. The Branch Offset applies the translation to the current Quadrant node and all the nodes below it in the same branch of the graph.

This parameter can be controlled with a Dynamic Function.

### Pattern

Defines the image (if any) to be added to the FX-Map by this node.

Quadrant nodes support a long list of patterns, which are described later in this topic.

>[!WARNING]
>
> This parameter can't be controlled by a dynamic function in a sbsar file.

### Pattern Offset

Offsets the node's image by the specified amount, but does not affect subsequent nodes. This parameter can be controlled with a Dynamic Function.

### Pattern Size

Defines the size of the image (if applicable) to be added to the FX-Map. This parameter can be controlled with a Dynamic Function.

### Pattern Rotation

Defines the rotation of the image (if applicable) to be added to the FX-Map. This parameter can be controlled with a Dynamic Function.

### Pattern Variation

Some patterns have variants. This setting lets you choose which variant to use. This parameter can be controlled with a Dynamic Function.

### Blending Mode

Specifies the blending process to use when mixing this node's image (if applicable) to the FX-Map image. This parameter can be controlled with a Dynamic Function.

### Random Seed

Seed for the random number generator.

The generator uses this seed as a starting point, creating a sequence of what appear to be random numbers. The advantage of this approach is that, unlike in the real world, you can ensure the exact same sequence of random numbers is generated each time, producing predictable, repeatable, but random-looking results.

This parameter can be controlled with a Dynamic Function.

### Inherit Random

If set to "Yes", the random number generator seed is inherited from the previous node in the graph (i.e. the node above this one in the quad-tree.) If this is the first node, it takes its random seed from the containing [Substance graph](../../../compositing-graphs/substance-compositing-graphs.md).

## Patterns

Each Quadrant node can optionally add an image to the final FX-Map.

By default, No Pattern is selected, so no image is rendered. The Quadrant node merely subdivides the FX-Map image, splitting it into four for the next node in the chain.

The next option, *Input image*, is to use an image supplied to the FX-Map node. The FX-Map node accepts color or grayscale images for use as the background or as a replacement for one of the built-in patterns. Please note that the Quadrant node can only render a grayscale input image in a grayscale Fx-Map, and conversely, it can only render a color input image in a color FX-Map. If you want to mix color type, you need to convert your inputs before in the graph.

Finally, you can choose from one of the built-in patterns: Square, Disc, paraboloid, Bell, Gaussian, Thorn, Pyramid, Brick, Gradation, Waves, Half Bell, Ridged Bell,Crescent and Capsule.

Additional note: you have the possibility to create a dynamic function in this parameter, but it will only work in Substance 3D Designer. To have access to the image input by a dynamic function, you'll have to use values from 256 (image entry 1) to higher values (257 for image entry 2, etc.).

### Pattern types.

Patterns are all grayscale. A few can be modified a little using the *Pattern Variation* parameter.

Many of the built-in patterns have some form of radial gradient fill or similar. This makes them very useful for many types of noises and patterns. Other patterns, such as Brick, Disc and Square, are simple, flat shapes.

The Pattern Variation parameter adjusts a defined feature of the Pattern.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](fxmap-quadrants.png){width="80px"}

</td>
<td style="border: 0;" valign="top">

![](quadrant-parameters.jpg)

</td>
</tr>
</table>
