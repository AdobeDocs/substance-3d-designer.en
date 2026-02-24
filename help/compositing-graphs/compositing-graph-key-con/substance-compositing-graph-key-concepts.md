---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/substance-compositing-graph-key-concepts.html"
breadcrumb-title: ""
description: Learn the key concepts of Substance compositing graphs including nodes, connections, and workflow fundamentals.
helpx_creative_field: ""
helpx_description: Designer > Substance graphs > Substance graph key concepts
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Substance graph key concepts
user-guide-description: ""
user-guide-title: ""
---



# Substance graph key concepts

This page lists the important concepts to understand for working with Substance graphs in Substance 3D Designer.

## Sub-graphs/Publishing

[Publishing a graph](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) or creating a sub-graph are two very similar, abstract concepts. It means that any graph or network of nodes can be "packaged" together and turned into a re-useable, standalone resource. Creating [sub-graphs](../../help/compositing-graphs/creating-compositing-gra/graph-instances-sub-gra/graph-instances-sub-graphs.md) is mostly done inside the application to make certain content re-useable in an efficient, smart workflow, as this avoids duplicating a set of nodes over and over. Publishing involves an additional step to export to [Substance 3D asset (SBSAR)](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) format, making your node network graph useable outside of the application, such as when you create a material for Unreal Engine.

Inputs, Outputs and Exposed Parameters are extremely important for this concept, as they are the only ways to still interact with the graph once it is used as a sub-graph or as a published Substance 3D asset. The reasons are the following:

* No outputs would mean your graph <b>generates nothing,</b> no data at all.
* No exposed Parameters means your graph <b>can not be customized</b> in any way. You would not be able to set things such as the intensity of an effect, the opacity of an image being blended, the color of a specific area, etc...
* No Inputs means that in some cases, you wouldn't be able to customize a graph's result with<b> your own image data</b>, such as baked mesh maps to generate effects from, an input image to perform a blur on, or a custom mask to isolate certain areas of an image.

## Inputs &amp; outputs

An [Output ](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md)is a Node that generates a single 2D result. It's an endpoint, a terminus for your graph, a finished result. Only data connected to an output can be exported outside of Designer, or even used in other graphs.

Here are a few things you should know about Outputs:

* You can have as many outputs as you want, but you must have <b>at least one output</b>.
* An output can be <b>any resolution</b> up to 8192px wide or tall, it can be<b> color or grayscale</b> and can be exported to any filetype supported.
* Outputs can and should be <b>named uniquely</b> to identify them, it helps when exporting.
* Every connector on the right side of any Node is actually an Output (see "Sub-graphs for more info)

An [Input](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/input/input.md) is similar to an Output, it's an empty, open slot for you or another user to connect your own data to. It allows for the creation of graph that in external, user-defined image data, such as a Filter that modifies an input image (a Blur, or a Contrast adjustment for example).

Here are a few things you should know about Inputs:

* Inputs are completely <b>optional</b>, you should only add them if needed. There is no minimum or maximum amount.
* Inputs have a set resolution (linked to the graph generally) that you define, as well as if they are grayscale or color. Anything connected to it will be converted to match this.
* Inputs can be bitmap files from your harddrive, other graphs, Layers from Painter or Alchemist, etc..
* Every connector on the left side of any Node is an Input (see "Sub-graphs for more info)

## Inheritance

As images and values are passed from nodes to others, some *attributes* of these images – i.e. their <b>Base Parameters</b> – are *propagated* across the graph as well, such as resolution, precision (i.e., bitdepth), tiling and random seed.

This propagation is defined by the [inheritance methods](../../help/compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) each nodes apply for these attributes. Indeed, nodes can *inherit attributes* from other nodes or the graph they exist in.  
The inheritance methods can be:

* *Relative to parent*
* *Relative to input*
* *Absolute* – i.e., no inheritance

Inheritance can be abstract and tricky to manage, therefore we strongly recommend you take a look at the [dedicated page](../../help/compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) discussing it in detail.

## Exposing parameters

Exposing parameters is a concept that can go very deep, but it can be summarized as picking certain properties of nodes in your graph, and creating a dedicated UI control element for them, that is easily available once the graph is used as a Sub-graph or if it is Published as an Archive. Because you can no longer quickly or easily select Nodes and tweak their properties, the goal is to create another primary control panel that groups any and all properties relevant for this specific graph.

here are some things you should know about Exposed Parameters:

* Exposed Parameters <b>move a control from the Node, to the graph</b>, essentially up a level in the hierarchy.
* Exposed Parameters can thus not be changed on the node anymore, only on the graph.
* Exposed Parameters can be fully customized with names, labels, values, UI editor type and even be hidden and shown for certain conditions.

Exposing Parameters is an abstract and difficult concept for beginners,[ there is more dedicated documentation on this topic](../../help/compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md), but it is recommended to fully familiarize yourself with other basic aspects of the software before diving into Exposing Parameters.
