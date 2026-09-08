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
<td style="border: 0;" valign="top">

![](../../../../../../assets/mask-builder.png){width="128px"}

## Mask Builder

**In:** *Mesh Based Generators**/Mask Generators*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. This is pretty much the Designer version of Painter's Mask Builder.

It is a complicated tool intended as an all-encompassing mask builder, based on baked maps, user parameters and grunge patterns and maps. It is mainly intended as a very advanced, full-control node to blend in crease dirt and edge wear. This node is powerful enough to mimic every other Mask Generator.

No bakes are explicitely required, but the more you supply, the more this node is capable of doing.

## Parameters

### Inputs

* **Ambient Occlusion**: *Grayscale Input*
* **Curvature**: *Grayscale Input*
* **World Space Normal**: *Color Input*
* **Grunge Input**: *Grayscale Input*
* **Grunge Input 2**: *Grayscale Input*
* **Scatter Input**: *Grayscale Input*   
  Custom scatter stamp, required to make use of the Scatter parameters.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.
* **Position**: *Color Input*   
  Used for Triplanar and Top-Bottom effects.

### Parameters

* **Level**: *0.0 - 1.0*  
  Sets the total level of the effect, gradually revealing.
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result.
* **Invert**: *False/True*  
  Inverts the result. Useful to achieve the opposite of the mask you are building.
* **Use Triplanar**: *False/True*Enables Triplanar projection, avoiding any seams with grunge maps.
* **Triplanar Blending Contrast**: *0.0 - 1.0*Sets the contrast for the Triplanar Blending.
* **Grunge**: *0.0 - 1.0*Sets amount of Grunge to blend in globally.
* **Grunge**   
  * **Scale**: *0 - 10*Sets the scale of the global Grunge.
  * **Use Custom Grunge**: *False/True*Enables custom Grunge input.
  * **Secondary Custom Grunge**: *0.0 - 1.0*Enables a second custom Grunge input.
  * **Invert**: *False/True*  
    Inverts the Grunge map.
* **AO**: *-1.0 - 1.0*Sets extent to which the effect should appear in occluded AO areas. Can be tweaked with the below group.
* **AO**   
  * **Range**: *0.0 - 1.0*Sets the treshold or range for the appearance of dirt.
  * **Contrast**: *0.0 - 1.0*  
    Adjusts the contrast of the AO effect.
  * **Noisiness**: *0.0 - 1.0*Sets amount of noise/grunge to blend into the AO effect.
  * **Noise Scale**: *0 - 10*Sets the scale of the AO noise/grunge.
  * **Noise Type**: *Spots, Cloud, Moisture, White Noise*Switches between 4 different types of AO noise.
  * **Invert**: *False/True*  
    Inverts the interpretation of the AO map: noise will appear in bright AO areas, not dark ones.
* **Curvature**: *0.0 - 1.0*Sets how much effect should appear on Curvature edges; can be both Convex and Concave. Tweak this with the group below.
* **Curvature**   
  * **Convex Range**: *-1.0 - 1.0*Sets how much effect to appear on Convex (bright) curvature edges.
  * **Convex Contrast**: *0.0 - 1.0*Sets the contrast of the Convex effect.
  * **Convex Invert**: *False/True*Inverts the interpretation of the Convex edges.
  * **Concave Range**: *-1.0 - 1.0*Sets how much effect to appear on Concave (dark) curvature edges.
  * **Concave Contrast**: *0.0 - 1.0*Sets the contrast of the Concave Range.
  * **Concave Invert**: *False/True*Inverts the interpretation of the concave edges.
  * **Smoothness**: *0.0 - 16.0*Amount of blurring and smoothing to apply to Curvature edges.
  * **Level Boost**: *0.0 - 1.0*Additional booster if the effect is not visible enough.
  * **Noisiness**: *0.0 - 1.0*Sets the influence of the noise/grunge on the Curvature effect.
  * **Noise Scale**: *0 - 10*Sets the scale of the noise.
  * **Noise Type**: *Spots, Cloud, Moisture, White Noise*Choose between 4 different Noise types.
* **Top/Down Gradient**: *-1.0 - 1.0*Blends over or masks with a top-to-bottom gradient based on the Position map. Positive values make things brighter, negative values mask away existing effects.
* **Gradient**   
  * **Range**: *0.0 - 1.0*Sets the position of the gradient.
  * **Contrast**: *0.0 - 1.0*  
    Adjusts the contrast of the gradient.
  * **Invert**: *False/True*  
    Inverts the gradient. Effectively swaps bottom and top.
* **World Space Normal**: *0.0 - 1.0*Similar to Top/Down Gradient, but with the position map and in six directions, akin to fake lighting. Positive values brighten, negative values darken.
* **World Space Normal**   
  * **Top Intensity**: *-1.0 - 1.0*
  * **Bottom Intensity**: *-1.0 - 1.0*
  * **Front Intensity**: *-1.0 - 1.0*
  * **Back Intensity**: *-1.0 - 1.0*
  * **Right Intensity**: *-1.0 - 1.0*
  * **Left Intensity**: *-1.0 - 1.0*
* **Scratches**: *-1.0 - 1.0*Blends scratches into the white areas.
* **Scratches**   
  * **Amount**: *0 - 4096*Sets total amount of scratches.
  * **Scale**: *0.0 - 1.0*Sets the scale of individual scratches.
* **Scatter**: *-1.0 - 1.0*Scatters a custom stamp within white areas.
* **Scatter**   
  * **Scale**: *0 - 50*Total scale of the effect.
  * **Density**: *0.0 - 1.0*Scattering density control, number that should appear.
  * **Size**: *0.0 - 4.0*Size of the scattered stamp.
  * **Size Variation**: *0.0 - 1.0*Variation within stamp size.
  * **Opacity Variation**: *0.0 - 1.0*Variation within stamp opacity.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
