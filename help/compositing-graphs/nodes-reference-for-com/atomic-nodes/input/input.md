---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/input.html"
breadcrumb-title: ""
description: Use the Input node to create input parameters for Substance graphs that can be exposed and adjusted by users.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Input
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Input
user-guide-description: ""
user-guide-title: ""
---


# Input

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Atomic node: Input color](comp_inputcolor.png "Atomic node: Input color"){width="200px"}

</td>
<td style="border: 0;" valign="top">

![Atomic node: Input grayscale](comp_inputgrayscale.png "Atomic node: Input grayscale"){width="200px"}

</td>
<td style="border: 0;" valign="top">

![Atomic node: Input value](comp_inputnumeric.png "Atomic node: Input value"){width="200px"}

</td>
</tr>
</table>

Input nodes are a special type of node that creates a dynamic slot in your graph, allowing for any input to be connected once your Graph is used in another context.

Unlike [Output nodes](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md), you have to explicitly place either a Color, Grayscale or Value input. It is not possible to create your own "agnostic" inputs that change type depending on what is connected to them.

Input nodes are not as crucial as [Output nodes](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md): you can have perfectly functioning, advanced Graphs that have no need for an Input. Inputs are only used when you want to base your Graph or node Instance's result on an external input, for example when creating an [Instance ](../../../../compositing-graphs/creating-compositing-gra/graph-instances-sub-gra/graph-instances-sub-graphs.md)or a [Filter](https://helpx.adobe.com/substance-3d-painter/features/effects/filter.html) for Substance 3D Painter.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">



</td>
<td width="100.00%" style="border: 0;" valign="top">



</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## PARAMETERS

</td>
<td style="border: 0;" valign="top">

### aTTRIBUTES

</td>
<td style="border: 0;" valign="top">

### iNHERITANCE

</td>
<td style="border: 0;" valign="top">

### iNTEGRATION ATTRIBUTES

</td>
</tr>
</table>

## Parameters

By default an Input Color or Grayscale returns black if nothing is plugged in. You can either set a different default value, or drag an existing[ Bitmap Resource](../../../../resources/importing-linking-and-new/importing-linking-and-new-resources.md) from the [Explorer](../../../../interface/the-explorer-window/the-explorer-window.md) onto the Input node in your graph, to preview this data in the slot. This only works for Color and Grayscale Inputs. The default value is persistent when used in other contexts, the preview bitmap is discarded everywhere else.

If you want to see it with the outputs of another Graph, you'll have to either export that Graph to Bitmap for the above method, or make use of "In-Context" editing.

|  |  |
| --- | --- |
| <b>PKG resource path</b> *String* | Points to a custom bitmap resource for previewing. |
| <b>Default value</b> *Color/Grayscale/Value* | Lets you use another value than black as default input, if nothing is connected to this slot. |

## Attributes

|  |  |
| --- | --- |
| <b>Identifier</b> *String* | The only mandatory, unique Attribute. Can not contains spaces.   This one is used for labeling inputs if no Label is set up, and for telling different outputs apart. Don't just leave these at "input\_1"! |
| <b>Description</b> *String* | Optional Description used in Designer's library and Painter's shelf. |
| <b>Label</b> *String* | UI Label used for nice labeling in Designer and Painter UI. Can contain spaces.   Recommended to set up with a name similar to the Identifier, just with spacebars instead of underscores. |
| <b>User data</b> *String* | Additional, optional User Data that can be used for specific filtering operations, Basically a wildcard, custom data field. |
| <b>Group</b> *String* | Group Attribute used to group inputs together for Designer's [Link Creation Modes](../../../../interface/the-graph-view/link-creation-modes/link-creation-modes.md).   Inputs with an identical (case-sensitive) Group Attribute, will be presented as a single connection in Compact Material Mode. |

## Inheritance

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

When multiple inputs are present, you need to pay attention to the way the graph will [inherit its Base parameters](../../../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) from these inputs.  
Base parameters include, among others, the <b>Output Size</b>, <b>Output Format</b> and <b>Tiling Mode</b>.

</td>
<td width="33.33%" style="border: 0;" valign="top">

[![Primary input in Substance graph](node-primary-input.png)](https://helpx.adobe.com/Primary%20input%20in%20Substance%20graph)

</td>
</tr>
</table>

An input can be defined as the [Primary input](../../../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md). This input then drives the attributes of all inputs which inheritance method is set to *Relative to parent*. This is the inheritance method *set by default* on Input nodes.

You may set an input node as a graph's Primary input by clicking *RMB* on the node and selecting the <b>Set as Primary input</b> option in the contextual menu.  
The Primary input of a node is marked with a *small dark dot in the connector* (circled in red in the example next to this section).

Alternatively, any input set to the *Relative to input* inheritance method will inherit the attributes from the node it is connected to, *regardless* of the Primary input.

Finally, you may override any value for a given attribute by setting its inheritance method to *Absolute*.

>[!TIP]
>
> To learn more about inheritance, go to the [Inheritance in Substance graphs](../../../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) page of this documentation.

>[!IMPORTANT]
>
> The *Relative to input* inheritance method for Input nodes is *not supported* in [Substance 3D assets (SBSAR)](https://helpx.adobe.com/substance-3d-assets.html). Set all Input nodes' inheritance methods to *Relative to parent* before publishing your package.

## Integration attributes

Inputs are not directly sent to the 3D View, but their Usage Attributes are used by [Substance 3D Painter](https://helpx.adobe.com/substance-3d-painter/home.html) for automatically filling slots with certain maps (mostly used with [Filters](https://helpx.adobe.com/substance-3d-painter/features/effects/filter.html)).

Additionally the Usage attributes are also used with [Link Creation Modes](../../../../interface/the-graph-view/link-creation-modes/link-creation-modes.md), to match the correct input and output slots.

<b>Usage</b>

|  |  |
| --- | --- |
| <b>Component</b> *String* | This determines what channels are actually in the resulting input.   This is a legacy setting this is not used by integrations and graphs anymore. |
| <b>Usage</b> *String* | Define a type or usage for this input. It indicates how other nodes should connect to this input.. |
| <b>Color space</b> *String* | Sets the colorspace this input should be interpreted in. |
