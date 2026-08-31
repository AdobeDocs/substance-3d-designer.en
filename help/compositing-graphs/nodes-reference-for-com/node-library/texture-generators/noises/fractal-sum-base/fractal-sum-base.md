---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/fractal-sum-base.html"
breadcrumb-title: ""
description: Use the Fractal Sum Base node to generate base fractal noise patterns for creating complex organic textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Fractal sum base
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Fractal sum base
user-guide-description: ""
user-guide-title: ""
---

# Fractal sum base

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Fractal sum base - Icon](fractal-sum-base.resources/fractal-sum-base-01.png "Fractal sum base - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A customisable fractal noise with an adjustable range and balance of octaves.  
  
The <b>Fractal sum</b> family of noises are all based on this node.

See also: [Fractal sum 1](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/fractal-sum-1/fractal-sum-1.md), [Fractal sum 2](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/fractal-sum-2/fractal-sum-2.md), [Fractal sum 3](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/fractal-sum-3/fractal-sum-3.md), [Fractal sum 4](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/fractal-sum-4/fractal-sum-4.md)

</td>
</tr>
</table>

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The generated noise as a grayscale bitmap. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Roughness</b> <i>Float</i> | The balance of the noise octaves.    A higher value will make the higher frequency octaves more visible. |
| <b>Min. level</b> <i>Integer</i> | The minimum octave used in the noise.    A higher value results in a higher noise frequency. |
| <b>Max. level</b> <i>Integer</i> | The maximum octave used in the noise.    A higher value results in a higher noise frequency. |
| <b>Disorder</b> <i>Float</i> | Displaces the ingredients of the noise.    This can be used to animate the noise. |
| <b>Disorder speed</b> <i>Float</i> | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the noise. |
| <b>Contrast</b> <i>Float</i> | The contrast of the final result. |
| <b>Global opacity</b> <i>Float</i> | The opacity of the noise octaves added together in the final result.    A high value may result in areas being burned to white. |
| <b>Non-square expansion</b> <i>Boolean</i> | In non-square images, keeps the generated tile square and expands the noise generation to the image's bounds. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Fractal sum base - Example 1](fractal-sum-base.resources/fractal-sum-base-02.png "Fractal sum base - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Fractal sum base - Example 2](fractal-sum-base.resources/fractal-sum-base-03.gif "Fractal sum base - Example 2"){zoomable="yes"}

</td>
</tr>
</table>
