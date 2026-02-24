---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/white-noise.html"
breadcrumb-title: ""
description: Use the White Noise node to generate white noise patterns for creating texture variations and random effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > White noise
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: White noise
user-guide-description: ""
user-guide-title: ""
---



# White noise

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![White noise - Icon](white_noise_v2.png "White noise - Icon"){width="200px"}

<b>In:</b> Texture generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a white noise using one of three methods targeting different histogram shapes: uniform, Gaussian and triangle.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Outputs

</td>
<td style="border: 0;" valign="top">

### Parameters

</td>
<td style="border: 0;" valign="top">

### Examples

</td>
</tr>
</table>

## Outputs

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* | The generated noise as a grayscale bitmap. |

## Parameters

|  |  |
| --- | --- |
| <b>Noise distribution</b>  Integer | The method of distributing the ingredients to target a histogram shape:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Uniform:</i> A flat histogram.</li> <li data-preserve-html="true"><i>Gaussian:</i> A histogram representing a normal distribution, akin to a bell curve.</li> <li data-preserve-html="true"><i>Triangle:</i> A triangular histogram.</li> </ul> |
| <b>Disorder</b>  Float | Displaces the ingredients of the noise.    This can be used to animate the noise. |
| <b>Disorder speed</b>  Float | Adjusts the distance of displacement applied by the <b>Disorder</b> parameter.    This can be used to control the speed of displacement when animating the noise. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![White noise - Example 1](white_noise_v2.png "White noise - Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![White noise - Example 2](white_noise_v2_speed0.6_aniso0.gif "White noise - Example 2"){zoomable="yes"}

</td>
</tr>
</table>

</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
