---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/manage-parameters/parameter-presets.html"
breadcrumb-title: ""
description: Learn how to create and use parameter presets in Substance 3D Designer to save and apply parameter configurations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Exposing a parameter > Parameter presets
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Parameter presets
user-guide-description: ""
user-guide-title: ""
---


# Parameter presets

Parameter Presets give the user the ability to store and transfer large amounts of pre-configured values for a set of parameters.They can help in many scenarios, and are most useful when a large amount of parameters with a large range of possibilities is present.

There are two ways for storing and loading presets, both have different use-cases, detailed below.

![Load/Save preset drop down menu](preset-menu.gif "Load/Save preset drop down menu"){width="512px"}

## External presets

External Presets involve an external file on disk, an \*.SBSPRS file. They can be transferred between different graphs and nodes, but only within the application. Their main purpose is exactly this: transferring a number of values too large to copy one-by-one.

External Presets are available for all Specific Parameters On [Graph Instances](../../../help/compositing-graphs/creating-compositing-gra/graph-instances-sub-gra/graph-instances-sub-graphs.md), for most Specific Parameters on [Atomic nodes](../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/atomic-nodes.md) ([exceptions are those parameters that can not be exposed](../../../help/compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md)), and for the exposed Input Parameters in a [Graph's Properties.](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html)

They are simply saved and loaded through this menu. The Saved SBSPRS files can be loaded on any other node or graph.

>[!NOTE]
>
> Even partial matches will work: parameters stored in an SBSPRS that do not exist on the loaded node, will simply be ignored. This means you can transfer properties between nodes that are mostly similar, [such as the color and grayscale version of Tile Sampler](../../../help/compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-sampler/tile-sampler.md)! All shared parameters will load. Matching happens on identifier and type.

![Embedded presets editing](preset-embed.gif "Embedded presets editing"){width="512px"}

## Embedded presets

Embedded Presets work differently from External Presets. Their main advantage is that they are contained within the SBS or SBSAR file, so that they can easily be transferred and loaded in Substance Painter, Maya and 3DS Max (currently not available in Substance 3D Sampler, UE4 and Unity). The user does not have to mess around with SBSPRS files either.

They serve a different purpose: it's not possible to transfer them between Nodes and Graphs (you would have to use External Presets for that). They can also only be created on the Input Parameters of a Graph's Properties, and only when within Preview Mode.

The workflow is as follows:

1. Switch to <b>Preview mode</b> for the <b>Input parameters</b>
1. Set values to desired result
1. Click the <b>+</b> next to the presets dropdown to create a new embedded preset, the preset is then immediately created and stored

Embedded presets can not be modified afterwards, though they can be renamed. Modifying as well as removing them happens by clicking the gear icon next to the dropdown and the + icon. Press the minus sign next to a preset to remove it.

Nothing more needs to be done to enable presets: once published as SBSAR, your presets will be available in Substance Painter after import.

>[!IMPORTANT]
>
> The <b>Presets</b> tab is disabled when using [in-context editing](../../../help/interface/preferences-window/preferences-window.md).
