---
title: "Graph parameters"
description: ""
helpx_description: "Designer > Substance compositing graphs > Graph parameters"
---

# Graph parameters

This page describes the standard parameters for the <b>Substance graph</b>.

A graph has several parameters that you can modify. You can find them by either clicking on *empty space* in the graph, or selecting the *graph item* in the <b>Explorer</b> panel. Parameters will be then displayed in the .

## Base parameters

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

This section includes parameters which have an impact on *all the nodes it contains*.

Indeed, every node in this graph which have base parameters set to the 'Relative to parent' [inheritance method](../inheritance-compositing/inheritance-in-substance-compositing-graphs.md) will get their values from the *graph's* base parameters.

In turn, the graph's base parameters values will depend on the context in which the graph is used in.

</td>
<td style="border: 0;" valign="top">

![Base parameters](doc-graph-props-base-params.png "Base parameters"){width="512px" zoomable="yes"}

</td>
</tr>
</table>

For instance, when the graph is used in another graph as an instance node, its base parameters use the 'Relative to input' inheritance method by default, which means they will get their values from the node connected to its primary input. (Unless they were )

In most cases, inheritance plays a significant role in defining these values, and how these values change throughout the graph. It is therefore strongly recommended to acquire a good understanding of [inheritance in Substance graphs](../inheritance-compositing/inheritance-in-substance-compositing-graphs.md) before using these parameters.

|  |  |
| --- | --- |
| <b>Output size</b> | This parameter allows you to chose the *base resolution* of images in the graph.  Use the <div><img data-preserve-html="true" height="22" src="props-output-size-lock.jpg"/></div> lock button to have the heighta and width values match and keep the image square when making size adjustments.  *Default: (0,0) - Relative To Parent*    [  Learn more ](../output-size/output-size.md) |
| <b>Output format</b> | Allows to choose *base bit depth* in the graph, from these options:<ul data-preserve-html="true"><li data-preserve-html="true">8 bit</li><li data-preserve-html="true">16 bit</li><li data-preserve-html="true">HDR Low Precision 16F (16 bit floating point)</li><li data-preserve-html="true">HDR High Precision 32F (32 bit floating point)</li></ul>*Default: 8 Bits per Channel - Relative To Parent* |
| <b>Pixel size</b> | Defines the pixel size. We recommend leaving both **Width** and **Height** values set to **1**.*Default: (1,1) - Relative To Parent* |
| <b>Tiling mode</b> | Defines the base *tiling mode* in the graph from these options:<ul data-preserve-html="true"> <li data-preserve-html="true">No tiling</li> <li data-preserve-html="true">Horizontal tiling</li> <li data-preserve-html="true">Vertical tiling</li> <li data-preserve-html="true">H+V Tiling (I.e., horizontal and vertical)</li> </ul>*Default: H and V Tiling - Relative To Parent* |
| <b>Random seed</b> | Defines the base *random seed* for the graph.  Use the <div><img data-preserve-html="true" height="22" src="prop-randomise.jpg"/></div> button to assign a new random value to the random seed.  *Default: 0 - Relative To Parent* |

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

## Attributes

The <b>Attributes</b> section contains *metadata* for the graph, which provides information for *identifying*, *categorising* and *applying* the graph as designed by its author.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Graph attributes](doc-graph-props-attributes.png "Graph attributes"){zoomable="yes"}

</td>
</tr>
</table>

+++List of attributes
[Explorer](../../interface/the-explorer-window/the-explorer-window.md)

[Library](../../interface/the-library/the-library.md)

[instance node](../graph-instances-sub-gra/graph-instances-sub-graphs.md)

[Explorer](../../interface/the-explorer-window/the-explorer-window.md)

[Substance graph](../substance-compositing-graphs.md)

['Send' interoperability feature](../../interface/the-explorer-window/send-to-interoperability/send-to-interoperability.md)

[.](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/send-to-215286290.html)

[built-in variable](../../function-graphs/variables/system-variables/system-variables.md)

[Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html)

<li data-preserve-html="true"><b>Browse</b>: Lets you browse your system files for the <i>existing image</i> which should be used as an icon</li>

<li data-preserve-html="true"><b>Generate</b>: This generates an icon using a <i>built-in preset</i> of the <b>PBR Render</b> node</li>

<li data-preserve-html="true"><b>Paste</b>: Lets you paste the image data currently in the <i>clipboard</i> as an icon</li>

<li data-preserve-html="true"><b>Remove</b>: This option <i>removes</i> the existing icon and leaves the icon slot <i>empty</i></li>

[template's category and subtitle](../creating-compositing-gra/creating-a-substance-compositing-graph.md)

+++

## Input parameters

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

All parameters specific to the graph, including [exposed parameters](../manage-parameters/exposing-a-parameter/exposing-a-parameter.md), are [managed](../manage-parameters/manage-parameters.md), edited and previewed here.

[Parameter presets](../manage-parameters/parameter-presets/parameter-presets.md) can also be created for some or all parameters.

</td>
<td style="border: 0;" valign="top">

![Input parameters](doc-graph-props-input-parameters.png "Input parameters"){zoomable="yes"}

</td>
</tr>
</table>

+++Overriding base parameters


When using a graph in another graph as aninstance node, you can control the default value for any  on that new instance node.



[instance node](../graph-instances-sub-gra/graph-instances-sub-graphs.md)



Open the hamburger menu at the top of the ‘Input parameters’ section and go to the ‘Override base parameters’ sub-menu to select a base parameter for which you want to set an arbitrary default value.





The editor of the selected parameter will appear on top of the list of graph input parameters. You may then adjust their value andinheritance methodas desired.



[inheritance method](../inheritance-compositing/inheritance-in-substance-compositing-graphs.md)



+++

>[!IMPORTANT]
>
> The <b>Preview</b> and <b>Presets</b> tabs are disabled when using [in-context editing](../../interface/preferences-window/preferences-window.md).

## Inputs

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

In this part, all the graph's [Input](../nodes-reference-for-com/atomic-nodes/input/input.md) nodes are listed.

You can reorder them by using drag and drop on the handle on the far left of each item.

</td>
<td style="border: 0;" valign="top">

![Inputs](doc-graph-props-inputs.png "Inputs"){zoomable="yes"}

</td>
</tr>
</table>

## Outputs

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

In this part, all the graph's [Output](../nodes-reference-for-com/atomic-nodes/output/output.md) nodes.

You can reorder them by using drag and drop on the handle on the far left of each item.

</td>
<td style="border: 0;" valign="top">

![Outputs](doc-graph-props-outputs.png "Outputs"){zoomable="yes"}

</td>
</tr>
</table>
