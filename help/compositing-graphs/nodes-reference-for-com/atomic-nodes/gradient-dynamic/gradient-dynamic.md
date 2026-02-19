---
title: "Gradient (Dynamic)"
description: "Use the Gradient (Dynamic) node to create dynamic gradients that can be controlled by input parameters and values."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Gradient (Dynamic)
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/gradient-dynamic.html"
helpx_creative_field:
  - painting-illustration
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - gradients
  - creating-color-palettes
  - shading
---




# Gradient (Dynamic)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Gradient dynamic](comp_dyngradient.png "Atomic node: Gradient dynamic"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Remaps the grayscale values in an image, using a gradient supplied by a row or column of pixels in another image.

It serves as a slight alternative to the Gradient Node, but unlike the Gradient node, Gradient color keys are not defined internally, but come from an external input.

</td>
</tr>
</table>

This mainly allows to avoid the problem where parameters cannot be exposed, as the parameters for color are moved outside of the node. This is what makes it "dynamic".

While Gradient (Dynamic) is not a difficult node to use by itself, its usecases are a bit more advanced: most standard usages can be covered by the regular Gradient node.

This node comes in play when you are too limited by the Gradient editor's key system, and want colors and ramp positions to be driven by other inputs, parameters and parts of your graph.

Alternatively, the Gradient Input Position slider can be used to alternate between multiple gradients stored inside a single Ramp input.

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



</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Gradient addressing</b> *Boolean* | Sets if the Gradient repeats (tiles) or clamps.   This parameter determines how out of &#91;0, 1&#93; range HDR  pixels of the grayscale input are handled: clamped or fold up to &#91;0, 1&#93;. |
| <b>Gradient orientation</b> *Integer* | Sets the axis along which the 'Gradient input' should be sampled:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Horizontal:</i> Sample a row of pixels on the X axis.</li> <li data-preserve-html="true"><i>Vertical:</i> Sample a column of pixels on the Y axis.</li> </ul> |
| <b>Gradient input position</b> *Float* | The normalized position of the row or column of pixels to be sampled in the 'Gradient input'. |

## Input connectors

|  |  |
| --- | --- |
| <b>Grayscale input</b> *Grayscale* PRIMARY | The grayscale image to remap. |
| <b>Gradient input</b> *Color/Grayscale* | The gradient is sampled from this image |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Color/Grayscale* |  |

## Examples

*Coming soon.*
