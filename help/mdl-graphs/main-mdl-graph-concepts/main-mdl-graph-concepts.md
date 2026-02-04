---
title: "Main MDL graph concepts"
description: ""
helpx_description: "Designer > MDL graphs > Main MDL graph concepts"
---

# Main MDL graph concepts

This page presents the main concepts which are *specific* to [MDL graphs](../mdl-graphs.md) and should be well understood for making the most of this graph type in Substance 3D Designer.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Iray

MDL materials use a description meant for physically-based rendering solutions., which the [Iray](../../interface/3d-view/iray/iray.md) renderer embedded in Designer supports. Therefore, displaying the result of an MDL graph *requires the Iray renderer* to be selected in an active [3D view](../../interface/3d-view/3d-view.md) panel.

</td>
<td style="border: 0;" valign="top">

[![NVIDIA Iray logo](iray-logo.jpg)](https://www.nvidia.com/en-us/design-visualization/iray/)

</td>
</tr>
</table>

When creating or loading an MDL graph, the first [unpinned](../../interface/customizing-your-wor/customizing-your-workspace.md) 3D view panel found by Designer will *automatically switch* to the [Iray](../../interface/3d-view/iray/iray.md) renderer. If no 3D view is available, a *new* 3D view panel will be created and switched to the Iray renderer to host the rendering of the MDL material being edited.

When the Iray renderer is selected in a 3D view panel, that panel’s Materials menu lets you switch between available MDL materials, which include materials loaded in the Explorer panel and materials in Designer’s MDL library. Learn more about working with MDL materials in Iray in the [Iray](../../interface/3d-view/iray/iray.md) section of this documentation.

## Root node

The result of an MDL graph is defined by the <b>Root</b> node. Any node of the graph can be set as root as long as its outputs data of type <b>material</b>, i.e., a *material definition*. An MDL graph may have *only one* Root node.

Generally, a node which can be set as Root can be *self-sufficient*, as it already contains a material definition which may be customized by passing data to its *inputs*.  
For instance, if you want to work on a glass-like material, you may want to use a Glass material definition as Root node as a starting point, but that is *not mandatory*. Many material nodes are templated which can be turned into any complex material using the extensive list of MDL nodes.

The Root node includes a thumbnail displaying a preview of its current output.

![MDL graph's root node](mdl-root-hl.png "MDL graph's root node")

*Root node in an MDL graph and its properties displayed in the [Properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html)* *panel*

## Connectors and types

As there are far more data types in MDL graphs than other graphs in Designer, you may witness unique appearances of node connectors. The important concepts to understand are list below.

Connector shape

The *shape of the connector* indicates whether the data type is *uniform* (circle) or *varying* (square).

"A variable of a uniform type can only be set to a uniform value. A variable of a varying type can be set to a varying value as well as to a uniform value. The resulting value in the variable is then always considered varying." (Source: Section 6.3 of the [MDL Specification](https://raytracing-docs.nvidia.com/mdl/specification/MDL_spec_1.7.2_17Jan2022.pdf))

Here are some examples:

* a <b>Texture</b> sample is *varying* as values are impacted by the sampled pixel
* a <b>Color</b> value is *uniform* as it is passed equally regardless of the context
* a <b>BRDF</b> is *varying* as values are impacted by the angle of incidence
* a <b>Float</b> or <b>Boolean</b> value is *uniform* as it is passed equally regardless of the context

Connector color

The *type of data* going from an output connector or expected by an input connector is color-coded and displayed between parentheses after the identifier/label when hovering the connector with the mouse.

>[!WARNING]
>
> Only connectors for *matching data types* may be linked together. The sole purpose of the color-coding is to increase readability regarding the type of data being passed in the graph, and what connectors may be linked together.

![MDL node connector types](mdl-connector-types.png "MDL node connector types"){width="512px"}

*Aspect of connectors vary according to I/O value type, which is displayed in parentheses after I/O identifier*

## Filtered node creation

You can add any node available in the <b>mdl</b> category of the <b>Library</b> in the graph by *dragging the node* from the <b>Library view</b> into the <b>Graph view</b>, or by pressing <b>Spacebar</b> to open the <b>Node menu</b> in the Graph view when *nothing is selected*. In this case, an *unfiltered* list of nodes is displayed.

However, there are cases where the list of nodes in the Node menu is filtered to only display nodes of matching data type for the target input or output:

* if a *node is selected* in the Graph view and <b>Spacebar</b> is pressed
* if clicking <b>LMB</b>, holding and *dragging* a link out of a *node connector*

You may want to keep in mind the *rules* applied for filtering:

* if the Node menu is displayed by pressing <b>Spacebar</b> when a *single* node is selected, the list includes nodes where the data type of the *first input* matches the selected node’s *output* data type
* if the Node menu is displayed by pressing <b>Spacebar</b> when *multiple* nodes are selected, the list includes nodes where the data type of the *first input* matches the *last selected* node’s *output* data type
* if the Node menu is displayed by *dragging a link* out of an *output* connector, the list includes nodes where the data type of the *first input* matches the selected *output* data type
* if the Node menu is displayed by *dragging a link* out of an *input* connector, the list includes nodes where the data type of the *output* matches the *selected input* data type

![Filtered node creation](mdl-filtered-node-creation.gif "Filtered node creation")

*Filtered node creation in MDL graph, note the list changes according to the value type for the connector*

## Graph inputs and textures

MDL materials can receive data from external sources, in the form of values and textures for instance. This is achieved by <b>exposing a node</b>, contrary to the [Substance graph](../../compositing-graphs/substance-compositing-graphs.md) where dedicated input nodes exist for this purpose.

Data can be passed to the exposed node depending on its *type*. For instance, Float values can be passed to an exposed <b>float</b> node, and a texture can be passed to an exposed <b>color</b> node (in this case, the sampled pixel’s RGBA values are passed as a color value).

![Exposed graph inputs](mdl-graph-inputs-samplers.png "Exposed graph inputs")

*Exposed nodes create graph inputs which are both raw value inputs and samplers for textures*
