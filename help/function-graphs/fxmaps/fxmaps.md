---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/fxmaps.html"
breadcrumb-title: ""
description: Learn how to use FXMaps in Substance 3D Designer to apply function graphs to textures for procedural pattern generation.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > FXMaps
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: FXMaps
user-guide-description: ""
user-guide-title: ""
---


# FXMaps

**The FX-Map node allows the creation of procedural images**. It is one of the most powerful features of the Substance technology.

An FX-Map represents a special type of graph, known as a Markov Chain. Markov Chains represent a simple core process: repeatedly replicating and subdividing an image over and over again. At each step, an image can be rotated, translated and blended at will. The results can be anything from simple patterns to complex noises. FX-Maps are the basis for many of the sample Substances installed with Substance 3D Designer.

## Create FX-Map graphs

If you want to see an FX-Map graph, simply add an [FX-Map node](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/fx-map/fx-map.md) to a [Substance graph](../../help/compositing-graphs/substance-compositing-graphs.md), then right-click on the node and press CMD + E (OS X) or CTRL + E (Windows) to open its graph. This FX-Map graph will appear in a new tab on the Graphs panel; you can switch between this graph and the Substance graph by clicking on the tab.

## What are FX-Maps for?

The most common uses of FX-Maps are creating repetitive patterns, such as stripes and bricks, and noises, such as Perlin, Brownian and Gaussian noises. Noises are particularly useful in creating organic, natural-looking textures like dirt, dust, concretes, stone surfaces, liquid spatters and so on.

FX-Map graphs do not work in the same way as Substance graphs: In Substance graphs, each node is independent and has no knowledge of its position in the overall graph, nor does it care where its image data comes from or where it’s going.

We'll look at each of the three FX-Map graph nodes in more detail in the next chapter, but briefly, each FX-Map node offers one of three operations:

### Quadrant

This splits the image at this step in the graph into four quadrants. This is the most common node type. A chain of Quadrant nodes can create very complex-looking images, as well as intricate patterns.

In fact, Quadrant nodes represent a level—or **octave**—in a quad-tree graph. FX-Map graphs hide this tree structure by representing each level in the tree with a single Quadrant: every time you connect one Quadrant node to another, you are actually creating a complete tree level.

The reason for this 'cheat' technique is to remove the need to represent each node at every level of a tree individually: after just four layers of depth, you would need to use 4 x 4 x 4 x 4 nodes, which is 256 individual nodes! Instead, each Quadrant node "knows" which level it's at in the tree and generates its imagery accordingly.

This probably won't make much sense to many readers, but we'll go into this in much more detail shortly.

### Iterate

Repeats the image passed into the right-hand connector over the image passed into the left-hand connector by the set number of iterations.

This node is most often used with one or more Dynamic Functions graphs to move or rotate the input image in some way at each iteration.

### Switch

This takes two inputs and simply switches between one or the other, as defined by its Selector setting. As with the Iterate node, the Selector setting is often chosen by a Dynamic Function.

## FX-Maps System Variables

FX-Maps support system variables. These variables always begin with a Dollar symbol ("$"), and are as follows:

| Name | Particularity | Data type | Purpose |
| --- | --- | --- | --- |
| $time | - | float1 | This variable returns the time in seconds since the Substance rendering engine was started.It is ideal for Substances which need to animate according to time. (E.g. the hands of a clock.)In some applications, including Substance Player, a Substance that uses $time will cause a timeline to appear in the user interface. |
| $depth | - | float1 | Returns the octave (level) number of the FX-Map node. This allows a node to modify its behavior according to which level in the quad-tree it represents. |
| $depthpow2 | - | float1 | As above, but returns 2 raised to the power of the octave (level) number. This is a helper value that comes in useful for some common calculations. |
| $number | Iterate Nodes only | float1 | Returns the number of the drawn pattern. This can be accessed by Dynamic Function graphs controlling an Iterate node to modify its behavior at each iteration step.(Note that $number starts counting from 0, not 1.) |
| $size | - | float2 | Returns the size of the current node (in pixels). |
| $sizelog2 | - | float2 | As above, but returns the size as power-of-2 values (ex: for 2048\*2048 image, $sizelog2 returns 11). |
| $pos | Quadrant Nodes only | float2 | Returns the birth position of the pattern. The result is always a value between 0 and 1. |
