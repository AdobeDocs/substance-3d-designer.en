---
title: "Emboss"
description: "Use the Emboss node to create embossed effects on textures for adding depth and relief to surface details."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Emboss
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/emboss.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - pbr
  - effects
  - creative-effects
---




# Emboss

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Emboss](comp_emboss.png "Atomic node: Emboss"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Applies an embossing effect by lighting the sides of shapes in an image according to a specified light source direction.

I.e., the node performs a simple 2D shading based on 2 inputs, simulating light falling on a surface with height and depth variation.

</td>
</tr>
</table>

This node is not used often for PBR-like projects, but it can serve in certain cases where you want a simple, baked lighting in your texture. Alternatively [Emboss With Gloss](../../node-library/filters/effects/emboss-with-gloss/emboss-with-gloss.md) and [Uber Emboss](../../node-library/filters/effects/uber-emboss/uber-emboss.md) provide a similar, but more extensive functionality.

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
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Intensity</b> *Float* | Adjusts the global intensity of illumination effect.   Sets the intensity of the of the "height" map and thus the strength of the lighting effect |
| <b>Light angle</b> *Float* | Sets the angle at which the light is simulated.   Defines the illumination angle of the embossed image's highlight |
| <b>Highlight color</b> *Float/Float4* | Sets the color of areas facing towards the light angle.   Sets the color of the highlight if the input image is color. |
| <b>Shadow color</b> *Float/Float4* | Sets the color of areas facing away from the light angle.   Sets the color of the shadowed regions of the embossed image. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale/Color* PRIMARY | Provides the base, unshaded colors. See it as a sort of diffuse or basecolor texture. |
| <b>Intensity input</b> *Grayscale* | Represents the heightmap used to calculate lighting on the surface. Black is low and white is high. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
