---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/bitmap.html"
breadcrumb-title: ""
description: Use the Bitmap node to import and use bitmap images as textures in Substance compositing graphs.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Bitmap
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Bitmap
user-guide-description: ""
user-guide-title: ""
---


# Bitmap

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Bitmap](comp_bitmap.png "Atomic node: Bitmap"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Loads a [bitmap resource](../../../../resources/bitmap-resource/bitmap-resource.md) into the graph.

This node is used to either import a [bitmap](../../../../glossary/glossary.md) into your graph or to create a new bitmap for use with the [bitmap painting tools](../../../../resources/bitmap-resource/bitmap-painting-tools/bitmap-painting-tools.md).

There are a few ways to create this node, and all of them require you to understand[ the difference between linking and importing resources.](../../../../resources/importing-linking-and-new/importing-linking-and-new-resources.md)

</td>
</tr>
</table>

You can either create the node from scratch, or by dropping a [bitmap](../../../../glossary/glossary.md) in a supported format into the Graph view.

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

>[!TIP]
>
> Generated or imported 8-bit bitmaps can be painted using the [bitmap painting tools](../../../../resources/bitmap-resource/bitmap-painting-tools/bitmap-painting-tools.md) in the [2D view](../../../../interface/2d-view/2d-view.md) dock.

>[!IMPORTANT]
>
> This node is dependent on an external resource, hence there are a few points to keep in mind when working with them:
> 
> * Bitmap nodes can return either color or grayscale, but defaults to color even if the resource is a grayscale bitmap. This can affect graph performance and complexity, so always make sure to switch to the 'Grayscale' [color mode](#parameters) if needed.
> * Deleting a bitmap node does not delete the [Bitmap resource](../../../../resources/bitmap-resource/bitmap-resource.md) in your [package](../../../../glossary/glossary.md), you have to manually do that in the [Explorer](../../../../interface/the-explorer-window/the-explorer-window.md).
> * On the other hand, be careful when deleting a [Bitmap resource](../../../../resources/bitmap-resource/bitmap-resource.md) in the Explorer: it will still work in the graph for that session as it is kept in cache, but the resource will be marked as missing the next time you load the [package](../../../../glossary/glossary.md).
> * When a Substance graph is [cooked](../../../../glossary/glossary.md), the bitmap resolution will be fixed at its resolution inside the graph and not based on its original size. It is recommended to make sure the 'Output size' [base parameter](../../../../glossary/glossary.md) of a Bitmap node uses the 'Absolute' [inheritance method](../../../../glossary/glossary.md), and the node is followed by a [Transform 2D](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/transformation-2d/transformation-2d.md) node set to 'Relative to parent' (I.e., the host graph's resolution).

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Parameters

</td>
<td style="border: 0;" valign="top">

### Bitmap painting tools

</td>
<td style="border: 0;" valign="top">

### Output connectors

</td>
<td style="border: 0;" valign="top">

### Examples

</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Determines the output type of the node, to either return in color or grayscale. |
| <b>PKG resource path</b> *String* | Path to the [Bitmap resource](../../../../resources/bitmap-resource/bitmap-resource.md) being referenced by the node.   It is recommended not to type manually but either copy a resource from the explorer and paste it in the parameter text field, or drag-and-drop a bitmap resource directly from the [Explorer](../../../../interface/the-explorer-window/the-explorer-window.md) onto the Bitmap node in the graph.. |
| <b>Resize method</b> *Integer* | The resampling method to use when up or downscaling a bitmap:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Smooth stretch:</i> Apply [bilinear filtering](../../../../glossary/glossary.md) to interpolate over the source pixels of the stretched image.</li> <li data-preserve-html="true"><i>Nearest stretch:</i> Stretch the image and use the color of the nearest source pixel as is.</li> </ul> |

## Bitmap painting tools

Bitmaps can be edited in Designer. Learn more about the editing tools in [this section](../../../../resources/bitmap-resource/bitmap-painting-tools/bitmap-painting-tools.md).

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
