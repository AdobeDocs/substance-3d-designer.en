---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/uniform-color.html"
breadcrumb-title: ""
description: Use the Uniform Color node to generate uniform color textures for creating solid color fills and base layers.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Uniform color
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Uniform color
user-guide-description: ""
user-guide-title: ""
---

# Uniform color

<table>
<tr style="border: 0;">
<td style="border: 0; width:33.33%; vertical-align:top" width="33.33%" valign="top">

![Atomic node: Uniform color](uniform-color.resources/comp_uniform_1.png "Atomic node: Uniform color"){width="100%"}

<b>In:</b> Atomic Nodes

</td>
<td style="border: 0; width:66.66%; vertical-align:top" width="66.66%" valign="top">

Generates a flat grayscale or color value.

It is a simple node that is used very often as a starting point for adding colors or creating specific values.

</td>
</tr>
</table>

<table>
<tr style="border: 0">
<td style="border: 0; width: 15%" width="15%"></td>
<td style="border: 0; text-align: center" align="center"><img src="uniform-color.resources/uniform-color-tooltip.gif" alt="uniform-color tooltip" /></td>
<td style="border: 0; width: 15%" width="15%"></td>
</tr>
</table>



>[!TIP]
>
> Performance optimization
> 
> Both of these adjustments lowers the node's computation time and memory footprint:
> 
> * If a grayscale value is needed, make sure to switch the node's [color mode](#parameters) to 'Grayscale'.
> * Since the node's output is a flat color, you may use the lowest resolution possible. Set the node's '[Output size](../../../../compositing-graphs/output-size/output-size.md)' parameter to use the 'Absolute' [inheritance method](../../../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) and a resolution of 16x16 pixels.


## Parameters

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Toggles between a grayscale and a color output image. |
| <b>Output color</b> *Float/Float4* | Selects the flat color to use in the output image.   When using the 'Color' color mode, the Alpha channel is used for opacity where 0 is fully transparent and 1 is fully opaque.. |


## Examples

*Coming soon.*
