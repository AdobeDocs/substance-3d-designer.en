---
title: "SVG | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > SVG"
---

# SVG

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: SVG](comp_svg.png "Atomic node: SVG"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Renders an [SVG image](../../../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md) as a bitmap. In other words, maps vector shapes to pixels.

There are a few ways to create this node, and all of them require you to understand[ the difference between linking and importing resources](../../../../resources/importing-linking-and-new/importing-linking-and-new-resources.md).

</td>
</tr>
</table>

You can either create the node from scratch, or by dropping an SVG file into the Graph view.

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
> Generated or imported SVG images can be edited using the [vector editing tools](../../../../resources/vector-graphics-svg-res/vector-editing-tools/vector-editing-tools.md) in the [2D view](../../../../interface/2d-view/2d-view.md) dock.

>[!IMPORTANT]
>
> This node is dependent on an external resource, hence there are a few points need to be kept in mind when working with them:
> 
> * SVG nodes can return either color or grayscale, but default to color even if the resource is a grayscale vector. This can affect graph performance and complexity, so always make sure to switch to the 'Grayscale'  if needed.
> * Deleting an SVG node does not delete the [SVG resource](../../../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md) in your [package](../../../../glossary/glossary.md), you have to manually do that in the [Explorer](../../../../interface/the-explorer-window/the-explorer-window.md).
> * SVG shapes are [tessellated](../../../../glossary/glossary.md) into geometry/polygons, then *rasterized* in order to be used in Substance graphs as bitmaps. The technology used for these operations does not support several vector properties, such as outlines. Learn more about these limitations [here](../../../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md).

>[!WARNING]
>
> SVG shapes are [tessellated](../../../../glossary/glossary.md) into geometry/polygons, then *rasterized* in order to be used in Substance graphs as bitmaps.
> 
> The technology used for these operations does not support several vector properties, such as outlines.
> 
> Learn more about these limitations [here](../../../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md).

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Determines the output type of the node, to either return in color or grayscale. |
| <b>Background color</b> *Color/Grayscale* | Sets the output image's background color ot use on areas not covered by a vector shape.   *Is overridden by the '' input when that input is connected.* |
| <b>PKG resource path</b> *String* | Path to the [SVG resource](../../../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md) being referenced by the node.   It is recommended not to type manually but either copy a resource from the explorer and paste it in the parameter text field, or drag-and-drop a bitmap resource directly from the [Explorer](../../../../interface/the-explorer-window/the-explorer-window.md) onto the SVG node in the graph.. |

## Vector editing tools

Vector shapes can be edited in Designer. Learn more about the editing tools in [this section](../../../../resources/vector-graphics-svg-res/vector-editing-tools/vector-editing-tools.md).

## Input connectors

|  |  |
| --- | --- |
| <b>Background</b> *Grayscale/Color* PRIMARY | Sets the output image's background color ot use on areas not covered by a vector shape.   *Overrides the '' parameter when connected.* |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*

 