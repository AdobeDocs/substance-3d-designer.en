---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/mask-builder.html"
breadcrumb-title: ""
description: Use the Mask Builder node to combine multiple mask inputs and create complex mask patterns for material effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Mask Builder
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mask Builder
user-guide-description: ""
user-guide-title: ""
---

# Mask Builder

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](mask-builder.resources/mask-builder.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. This is pretty much the Designer version of Painter's Mask Builder.

It is a complicated tool intended as an all-encompassing mask builder, based on baked maps, user parameters and grunge patterns and maps. It is mainly intended as a very advanced, full-control node to blend in crease dirt and edge wear. This node is powerful enough to mimic every other Mask Generator.

No bakes are explicitely required, but the more you supply, the more this node is capable of doing.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> |  |
| <b>Curvature</b> <i>Grayscale Input</i> |  |
| <b>World Space Normal</b> <i>Color Input</i> |  |
| <b>Grunge Input</b> <i>Grayscale Input</i> |  |
| <b>Grunge Input 2</b> <i>Grayscale Input</i> |  |
| <b>Scatter Input</b> <i>Grayscale Input</i> | Custom scatter stamp, required to make use of the Scatter parameters. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |
| <b>Position</b> <i>Color Input</i> | Used for Triplanar and Top-Bottom effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total level of the effect, gradually revealing. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Invert</b> <i>False/True</i> | Inverts the result. Useful to achieve the opposite of the mask you are building. |
| <b>Use Triplanar</b> <i>False/True</i> | Enables Triplanar projection, avoiding any seams with grunge maps. |
| <b>Triplanar Blending Contrast</b> <i>0.0 - 1.0</i> | Sets the contrast for the Triplanar Blending. |
| <b>Grunge</b> <i>0.0 - 1.0</i> | Sets amount of Grunge to blend in globally. |
| <b>Grunge</b> |  |
| <b>Scale</b> <i>0 - 10</i> | Sets the scale of the global Grunge. |
| <b>Use Custom Grunge</b> <i>False/True</i> | Enables custom Grunge input. |
| <b>Secondary Custom Grunge</b> <i>0.0 - 1.0</i> | Enables a second custom Grunge input. |
| <b>Invert</b> <i>False/True</i> | Inverts the Grunge map. |
| <b>AO</b> <i>-1.0 - 1.0</i> | Sets extent to which the effect should appear in occluded AO areas. Can be tweaked with the below group. |
| <b>AO</b> |  |
| <b>Range</b> <i>0.0 - 1.0</i> | Sets the treshold or range for the appearance of dirt. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the AO effect. |
| <b>Noisiness</b> <i>0.0 - 1.0</i> | Sets amount of noise/grunge to blend into the AO effect. |
| <b>Noise Scale</b> <i>0 - 10</i> | Sets the scale of the AO noise/grunge. |
| <b>Noise Type</b> <i>Spots, Cloud, Moisture, White Noise</i> | Switches between 4 different types of AO noise. |
| <b>Invert</b> <i>False/True</i> | Inverts the interpretation of the AO map: noise will appear in bright AO areas, not dark ones. |
| <b>Curvature</b> <i>0.0 - 1.0</i> | Sets how much effect should appear on Curvature edges; can be both Convex and Concave. Tweak this with the group below. |
| <b>Curvature</b> |  |
| <b>Convex Range</b> <i>-1.0 - 1.0</i> | Sets how much effect to appear on Convex (bright) curvature edges. |
| <b>Convex Contrast</b> <i>0.0 - 1.0</i> | Sets the contrast of the Convex effect. |
| <b>Convex Invert</b> <i>False/True</i> | Inverts the interpretation of the Convex edges. |
| <b>Concave Range</b> <i>-1.0 - 1.0</i> | Sets how much effect to appear on Concave (dark) curvature edges. |
| <b>Concave Contrast</b> <i>0.0 - 1.0</i> | Sets the contrast of the Concave Range. |
| <b>Concave Invert</b> <i>False/True</i> | Inverts the interpretation of the concave edges. |
| <b>Smoothness</b> <i>0.0 - 16.0</i> | Amount of blurring and smoothing to apply to Curvature edges. |
| <b>Level Boost</b> <i>0.0 - 1.0</i> | Additional booster if the effect is not visible enough. |
| <b>Noisiness</b> <i>0.0 - 1.0</i> | Sets the influence of the noise/grunge on the Curvature effect. |
| <b>Noise Scale</b> <i>0 - 10</i> | Sets the scale of the noise. |
| <b>Noise Type</b> <i>Spots, Cloud, Moisture, White Noise</i> | Choose between 4 different Noise types. |
| <b>Top/Down Gradient</b> <i>-1.0 - 1.0</i> | Blends over or masks with a top-to-bottom gradient based on the Position map. Positive values make things brighter, negative values mask away existing effects. |
| <b>Gradient</b> |  |
| <b>Range</b> <i>0.0 - 1.0</i> | Sets the position of the gradient. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the gradient. |
| <b>Invert</b> <i>False/True</i> | Inverts the gradient. Effectively swaps bottom and top. |
| <b>World Space Normal</b> <i>0.0 - 1.0</i> | Similar to Top/Down Gradient, but with the position map and in six directions, akin to fake lighting. Positive values brighten, negative values darken. |
| <b>World Space Normal</b> |  |
| <b>Top Intensity</b> <i>-1.0 - 1.0</i> |  |
| <b>Bottom Intensity</b> <i>-1.0 - 1.0</i> |  |
| <b>Front Intensity</b> <i>-1.0 - 1.0</i> |  |
| <b>Back Intensity</b> <i>-1.0 - 1.0</i> |  |
| <b>Right Intensity</b> <i>-1.0 - 1.0</i> |  |
| <b>Left Intensity</b> <i>-1.0 - 1.0</i> |  |
| <b>Scratches</b> <i>-1.0 - 1.0</i> | Blends scratches into the white areas. |
| <b>Scratches</b> |  |
| <b>Amount</b> <i>0 - 4096</i> | Sets total amount of scratches. |
| <b>Scale</b> <i>0.0 - 1.0</i> | Sets the scale of individual scratches. |
| <b>Scatter</b> <i>-1.0 - 1.0</i> | Scatters a custom stamp within white areas. |
| <b>Scatter</b> |  |
| <b>Scale</b> <i>0 - 50</i> | Total scale of the effect. |
| <b>Density</b> <i>0.0 - 1.0</i> | Scattering density control, number that should appear. |
| <b>Size</b> <i>0.0 - 4.0</i> | Size of the scattered stamp. |
| <b>Size Variation</b> <i>0.0 - 1.0</i> | Variation within stamp size. |
| <b>Opacity Variation</b> <i>0.0 - 1.0</i> | Variation within stamp opacity. |
