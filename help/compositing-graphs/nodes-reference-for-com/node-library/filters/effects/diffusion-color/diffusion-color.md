---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/diffusion-color.html"
breadcrumb-title: ""
description: Use the Diffusion Color node to apply color diffusion effects for creating smooth color blending and transitions.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Diffusion Color
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Diffusion Color
user-guide-description: ""
user-guide-title: ""
---


# Diffusion Color

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](diffusion-color-icon.png){width="200px"}

**In:** *Filters/Effects*

**Intermediate**

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Apply a diffusion process to the colors in the **Source** image input according to the provided **Mask** image input, creating smooth gradations between colors when using [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html).

Only colors from pixels matching the mask are diffused; other pixels do not participate in the result.

</td>
</tr>
</table>

## Parameters

* **Iterations**: *0.0 - 64.0*The number of diffusion iterations to perform (higher is better but slower). Useful values are in the &#91;8, 48&#93; range.  
  Please note that if you are not looking for mathematical correctness, low values are fine or even better.  
  **Distance**: **0.0 - 1.0**Adjusts the maximum distance of the diffusion.
* **Enable Dithering**: *True/False*Controls the sampling method of each pass. Dithering allows convergence in less passes, but introduces noise.  
  Without it, each pass is faster but more passes are required to achieve a smooth result without banding artifacts.
* **Is Normal Map**: *True/False*Adds a normalization on values at every step.
* **Use Alpha as Mask**: *True/False*Use the alpha channel of the *Source* input as the diffusion mask, instead of the *Mask* input.

## Inputs

* **Source** *Color*  
  The image to diffuse.
* **Mask** *Grayscale*  
  Diffusion mask: white pixels are sampled in *Source* and diffused in black pixels. The image should be black and white. If the mask includes gradients, the cutoff value is 0.5.
* **Intensity** *Grayscale*  
  Defines locally how strong the diffusion process is applied. This map should be *contrasted* for a noticeable effect.

## Example Images

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](diffusion-color-02-before.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](diffusion-color-02a-after.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](diffusion-color-02b-after.jpg){width="256px"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](diffusion-color-01-before.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](diffusion-uv-01b-after-1.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](diffusion-uv-01a-after-1.jpg){width="256px"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](diffusion-color-normal.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](diffusion-color-normal-render.jpg){width="512px"}

</td>
</tr>
</table>
