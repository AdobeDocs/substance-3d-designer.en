---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/waveform-1.html"
breadcrumb-title: ""
description: Use the Waveform 1 node to generate waveform patterns for creating organic textures and procedural variations.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Waveform 1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Waveform 1
user-guide-description: ""
user-guide-title: ""
---

# Waveform 1

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Waveform 1 - Icon](waveform-1.resources/waveform_01_v2.png "Waveform 1 - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A horizontal arrangement of user-selected patterns stacked into a shape akin to a waveform.

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
| <b>Samples</b> <i>Integer</i> | The amount of patterns placed along the X axis to draw the waveform, where a lower value results in a more stepped look. |
| <b>Function</b> <i>Integer</i> | The function used to draw the waveform.   This controls the vertical size of the pattern placed at each sample:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Value noise:</i> A random distribution of values</li> <li data-preserve-html="true"><i>Cosine:</i> Values follow the progression of a cosine function</li> <li data-preserve-html="true"><i>Custom function:</i> Use a user-authored function to drive the values</li> </ul> |
| <b>Custom function</b> <i>Float</i>   *Available when 'Function' is set to 'Custom function'* | Computes the vertical size of the pattern placed at each sample.   Available variables:<ul data-preserve-html="true"> <li data-preserve-html="true"><b>pos</b> (<i>float</i>) The position of the pattern on the X axis. This may be used to select patterns.</li> </ul> |
| <b>Roughness</b> <i>Float</i> | Interpolates between a clean and smooth waveform with one that is more rough and evenly distributed.    This can be thought of as clean signal vs. white noise. |
| <b>Scale</b> <i>Integer</i> | The horizontal span of the waveform visible in the image. |
| <b>Amplitude min.</b> <i>Float</i> | The minimum value (or thickness) of the waveform. |
| <b>Amplitude max.</b> <i>Float</i> | The maximum value (or thickness) of the waveform. |
| <b>Noise</b> <i>Float</i> | Applies noise to the waveform which randomly subtracts from its vertical span. |
| <b>Position</b> <i>Integer</i> | The position of the waveform in the image:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Centered:</i> The origin is at the vertical center of the image</li> <li data-preserve-html="true"><i>Bottom:</i> The origin is a the bottom of the image</li> </ul> |
| <b>Pattern</b> <i>Integer</i> | The pattern placed at each sample of the waveform. |
| <b>Pattern variation</b> <i>Float</i> | An additional adjustment available for some patterns. |
| <b>Disorder</b> <i>Float</i> | Displaces the values of the waveform.    This can be used to animate it. |
| <b>Disorder speed</b> <i>Float</i> | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the waveform. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Waveform 1 - Example 1](waveform-1.resources/waveform_01_v2_speed0.1_aniso0.gif "Waveform 1 - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
