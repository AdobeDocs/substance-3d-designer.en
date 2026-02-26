---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/fx-map.html"
breadcrumb-title: ""
description: Use the FX-Map node to apply function graphs to textures for creating procedural patterns and effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > FX-Map
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: FX-Map
user-guide-description: ""
user-guide-title: ""
---

# FX-Map

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: FX-Map](../../../../assets/fxmap.png "Atomic node: FX-Map"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

The FX-Map can replicate and subdivide an image or pattern input over and over again, and control the distribution of each pattern thanks to parameters and logical functions.

It is one of the most powerful atomic nodes, as well as the most complex node available in the application.

</td>
</tr>
</table>

Similar to the [Pixel processor](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/pixel-processor/pixel-processor.md), it is up to you to define and create the functions that determine the behavior and output of this node.

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
> Take a look a the [dedicated guide](../../../../function-graphs/fxmaps/fxmaps.md) to learn and understand more about the FX-Map process.

>[!IMPORTANT]
>
> It is recommended to be very familiar with all aspects of the software and have no problems creating [mathematical functions](../../../../function-graphs/function-graphs.md) for parameters before attempting to use the FX-Map node.

## Examples

## Parameters

Keep in mind that unlike other nodes, the majority of an FX-Map's behavior is not determined by the parameters, but rather [by editing the FX-Map functions](../../../../function-graphs/fxmaps/fxmaps.md) inside of it.

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Toggles between a grayscale and a color output image. Color will be much slower than grayscale. |
| <b>Background</b> *Float/Float4* | Sets the background starting color onto which to composite results. |
| <b>Render region</b> *Float4* | Lets you set the starting pixel range for each side of the FX-Map, resulting in a stretching effect. |
| <b>Tiling region</b> *Float4* | Lets you offset the tiling distance of the FX-Map. |
| <b>Cull outside</b> *Boolean* | Performs an optimization by [culling](../../../../glossary/glossary.md) patterns that fall outside of the normal range. |
| <b>Roughness</b> *Float* | Functions as a depth and opacity multiplier. It applies a bias to the FX-map blending process. |
| <b>Global opacity</b> *Float* | Sets the global opacity of the FX-map's output. |

## FX-Map guide

*Coming soon.*

## Input connectors

|  |  |
| --- | --- |
| <b>Background</b> *Grayscale/Color* PRIMARY | The output image's background color. |
| <b>Input image &#35;</b> *Grayscale/Color* |  |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

![](../../../../assets/image2015-9-10-17-28-32.png)
