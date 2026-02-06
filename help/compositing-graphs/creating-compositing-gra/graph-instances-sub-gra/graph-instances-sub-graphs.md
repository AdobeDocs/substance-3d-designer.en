---
title: "Graph instances and subgraphs"
description: ""
helpx_description: "Designer > Substance compositing graphs > Creating a Substance compositing graph > Graph instances and subgraphs"
---

# Graph instances and subgraphs

![](sub-graph.png)

Graph instances are nodes that <b>reference another graph</b>. A graph referenced by an instance node in a host graph may be called a <b>subgraph</b> of the host graph.

Using instances make a graph reusable many times in one or more graphs, even across different packages.

## Why should I use graph instances?

<b>Splitting graphs into multiple subgraphs</b> lets you to work *much* more efficiently<b>.</b>

Any time you are duplicating a chain of nodes in Designer, you could probably split that chain into a subgraph to make it easier to reuse and update.

>[!NOTE]
>
> A project file demonstrating a simple setup of a sub-graph for a *custom* filter is available in the [Sample Substance graphs](../../sample-compositing-graphs/sample-substance-compositing-graphs.md) section of this documentation.

### How do you create a graph instance?

Drag a graph A from the Explorer into another graph B to create an <b>instance node</b> referencing graph A.

Nodes can be quickly split into a new graph by selecting the nodes and using the 'Create graph from selection' in the contextual menu. You are then prompted to set the identifier of the new graph, which should be unique.

Note that if the selected nodes were connected to other nodes in the graph, you should also create [Input](../../nodes-reference-for-com/atomic-nodes/input/input.md) and [Output](../../nodes-reference-for-com/atomic-nodes/output/output.md) nodes in the new graph to carry over these connections to the subgraph.

Additionally, replacing the original nodes by an instance node referencing the new graph should be done manually afterwards.

Finally, you should decide whether the subgraph should be exposed to users when you publish your project to a shareable SBSAR file. See 'Exposed in SBSAR' parameter in the [graph's properties](../../graph-parameters/graph-parameters.md).

### A word about iNHERITANCE

Another benefit or using subgraphs is that each instance of a subgraph can <b>adapt to the context</b> it is being used into. In other words, two instances of a same graph can have different output resolutions, bitdepths and tiling modes.

This is an <b>essential concept</b> of working in graphs and we strongly recommend you learn more about [inheritance in Substance graphs](../../inheritance-compositing/inheritance-in-substance-compositing-graphs.md) when you are ready to go further with instances.

Note that while the graph instance and subgraph concepts also apply to Substance function graphs, inheritance as discussed in that page only applies to Substance graphs.

### Can I add my own graph instances to the node library?

<b>Yes, this is possible </b>but it requires some specific set-up. Learn more in the [Managing custom content and filters](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/creating-library-filters-for-projects-170459772.html) page of this documentation.

### Can you inspect the source graph of a graph instance?

![(tick)](check.svg) Yes, and *only* for instances of graphs loaded from a **Substance 3D file (SBS)**. These instance nodes have a *dark red* label.  
Right-click on the node to open its contextual menu and select the **Open reference** option.

>[!NOTE]
>
> While inspecting the source graph, you can use the input data of the instance's graph if the **In-context editing** option is *checked* in the **Graph** section of the [Preferences](../../../interface/preferences-window/preferences-window.md).

![(minus)](forbidden.svg) It is *not* possible to inspect graphs loaded from **Substance 3D asset (SBSAR)** instances, as these are already compiled. You may only load the asset in the **Explorer** panel to inspect the exposed graphs list and their parameters. These instance nodes have a *green* label.  
Right-click on the node to open its contextual menu and select the **Load package** option.

>[!NOTE]
>
> **Atomic nodes**
> 
> *Atomic* nodes are implemented directly through code in the Substance engine and are *not* instances of graphs, hence the name atomic: they are the *smallest building blocks* for *all* the other nodes in [Substance graphs](../../substance-compositing-graphs.md).
