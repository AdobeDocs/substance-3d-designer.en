---
title: "Substance graphs and MDL materials | Substance 3D Designer"
description: "Designer > MDL graphs > Substance graphs and MDL materials"
---

# Substance graphs and MDL materials

This pages describes the synergies between [Substance graphs](../../compositing-graphs/substance-compositing-graphs.md) and MDL graphs, and how to connect textures from Substance graph [outputs](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md) to MDL graph inputs.

## Overview

The outputs of Substance graphs can be *passed to exposed parameters* of MDL materials in two ways, which are described in this page.

If the MDL material currently applied in the 3D view has exposed parameters which type is *[varying](../main-mdl-graph-concepts/main-mdl-graph-concepts.md)* – this type may be set using the <b>Type modifier</b> option in the [exposed parameter's properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/exposing-a-parameter-145654033.html), these can be connected to *textures*:

* a <b>Color</b> parameter can be connected to RGBA textures
* a <b>Float</b> parameter for Grayscale textures

In these cases, the raw uniform value is replaced by a texture sampler supplying a varying value. These samplers have a <b>usage</b> attribute defined in the exposed parameter, and this usage lets Designer connect textures output by Substance graphs to the appropriate parameter in the MDL material, by *matching usages*.

## Substance graphs in the 3D View

When using the <b>View outputs in 3D View</b> option for a Substance graph or dragging a Substance graph from the <b>Explorer</b> panel to the <b>3D view</b>, the outputs are connected to the exposed parameters of *matching usages* in the MDL material currently displayed in the 3D view.

Individual textures from a Substance graph may be connected to any of the MDL material parameters which support texture sampling, regardless of the identifier, by pressing RMB on the Substance graph node and dragging into the 3D view. A list of available sampler usages is displayed, and you may select the target usage for the selected texture.

![Exposed MDL graph inputs](mdl-graph-inputs-samplers.png "Exposed MDL graph inputs")

*Textures output by a Substance graph are connected to an MDL graph's exposed parameters in the 3D View*

## Substance graphs in MDL graphs

Substance graph instances can be placed directly into MDL graphs by dragging them from the <b>Explorer</b> panel into the MDL graph. Substance graphs from both <b>Substance 3D files</b> (SBS) and <b>Substance 3D asset files</b> (SBSAR) may be used in MDL graphs.

+++Substance graph from Substance 3D file (SBS)




Substance graphinstance fromSubstance 3D file(SBS) in MDL graph



[Substance graph](../../compositing-graphs/substance-compositing-graphs.md)

[Substance 3D file](../../getting-started/overview/overview.md)

+++

+++Substance graph from Substance 3D asset (SBSAR)




Substance graphinstance fromSubstance 3D asset(SBSAR) in MDL graph



[Substance graph](../../compositing-graphs/substance-compositing-graphs.md)

[Substance 3D asset](../../getting-started/overview/overview.md)

+++

When a Substance graph instance is created, it appears as a *node* with the following features:

* A *typed output* connector for each of the graph’s outputs. The output data is typed as follows:
  * RGBA bitmaps: Color (varying)
  * Grayscale bitmaps: Float (varying)
  * Values: Match the value type (varying)
* An *input* of type UV coordinates to specify the UV coordinates which should be used to map the textures output by the Substance graph. If left unconnected, the default value is a classic 0-1 linear gradient in X and Y in UV space
* The node is *labelled* after the Substance graph label – or identifier if no label is defined – and its first bitmap output as a thumbnail

The node properties let you modify *all dynamic properties* of the Substance graph:

* Output size
* Random seed
* Input parameters
* …

The node properties also let you set parameters specific to how textures are *mapped* in the MDL material:

* Tiling
* Use Physical size
* Normal format
* Tangent space

The Substance graph instance node’s output may be connected to any node input of matching type in the MDL graph.

Please note changing any parameter in the <b>SBS Base parameters</b> section involves recomputing one or more of the Substance graph outputs, which uses the <b>Substance engine</b> and involves a *performance overhead* on top of the MDL graph computations. Expect a performance impact when *modifying a Substance graph* which is instanced in an MDL graph applied in the 3D view.

>[!WARNING]
>
> When using a Substance graph in an MDL graph, exporting the MDL graph involves baking the Substance graph outputs into bitmaps which will be exported as textures bundled with the exported MDL file. This means the parametric nature of the Substance graph is *lost* in the exported MDL file.
