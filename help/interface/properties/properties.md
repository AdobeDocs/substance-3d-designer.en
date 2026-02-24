---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/properties.html"
breadcrumb-title: ""
description: Use the Properties panel in Substance 3D Designer to view and edit node properties and graph parameters.
helpx_creative_field: ""
helpx_description: Designer > Interface > Properties
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Properties
user-guide-description: ""
user-guide-title: ""
---


# Properties

This page presents the <b>Properties </b>panel of Substance 3D Designer, its layout and the different rollouts and categories and parameters you can find within. It is focused on properties for[ Substance graphs](../../help/compositing-graphs/substance-compositing-graphs.md). [function graphs](../../help/function-graphs/function-graphs.md), [MDL graphs](../../help/mdl-graphs/mdl-graphs.md) and [FX-Map graphs](../../help/function-graphs/fxmaps/fxmaps.md) have simpler layouts.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Overview

The <b>Properties </b>panel is a context-sensitive panel that changes based on your selection in [the Graph View](../../help/interface/the-graph-view/the-graph-view.md) and the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) window.

</td>
<td style="border: 0;" valign="top">

![Properties dock](image2020-11-9-13-49-48.png "Properties dock")

</td>
</tr>
</table>

It lets you change the properties of selected nodes and resources, together with [the Graph View](../../help/interface/the-graph-view/the-graph-view.md), it is probably your second most used UI panel in Designer.

The Properties panel is split into a few different rollouts, depending on your selection, for example:

* <b>Base Parameters</b>, and <b>Input-</b> or <b>Specific Parameters</b> for nodes
* <b>Attributes</b> and <b>Metadata</b> for most nodes and Packages

A key feature of the Substance Ecosystem, [Exposing parameters](../../help/compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md), is done through the Properties panel.

>[!NOTE]
>
> Most numerical fields support *basic math formulas* as an input – E.g., `17+3.5`, `7/3`, `(4+2)*3`. Press *Enter* to validate the formula and the result will be input in the field. If the formula is invalid, the field reverts to its previous value.  
> Some numerical fields in other parts of the application, such as the [Expose parameter](../../help/compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md) dialog, also support this feature.

## Nodes &amp; Substance graphs

[Nodes](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/nodes-reference-129368078.html) and [Substance graphs](../../help/compositing-graphs/substance-compositing-graphs.md) have a slightly overlapping set of property categories, and their functionality is similar.

<b>Base Parameters</b> and <b>Attributes</b> are identical between Nodes and Graphs.

Nodes offer <b>Specific Parameters</b> or<b> Instance Parameters</b> (depending on if they are [Atomic nodes](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/atomic-nodes.md) or [Instances](../../help/compositing-graphs/creating-compositing-gra/graph-instances-sub-gra/graph-instances-sub-graphs.md)), as well as <b>Input Values</b> for working with [Values in Substance graphs](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/values-in-substance-3d-graphs-180192235.html).

[Input ](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/input/input.md)and [Output ](../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md)atomic nodes are exceptions as they feature <b>Integration Attributes</b> and <b>Conditions</b> for visiblity. These two sets of properties can also be accessed centrally in the Graph properties, under Inputs and Outputs.

Graphs have a few extra categories. <b>Input Parameters</b> lists [exposed parameters](../../help/compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md), <b>Inputs</b> and <b>Outputs</b> list all properties of Input and Output nodes. [You can find all Graph properties explained in detail on a dedicated page.](../../help/compositing-graphs/graph-parameters/graph-parameters.md)

## Resources &amp; Packages

The Properties panel also responds to selection changes in the [Explorer window](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html). It can serve as another way of selecting a Graph (instead of double clicking an empty area), and also lets you change Package and [Resource ](../../help/resources/resources.md)properties.

Packages have **Information**, **Attributes** and **Metadata** sections. [The package metadata is described on a dedicated page.](../../help/package-metadata/package-metadata.md)

Resources have properties specific to their type, [detailed on dedicated pages](../../help/resources/resources.md).
