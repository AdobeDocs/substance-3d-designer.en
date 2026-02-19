---
title: "Trapezoid Transform"
description: "Use the Trapezoid Transform node to apply trapezoidal distortion to textures for creating perspective correction effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Trapezoid Transform
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/trapezoid-transform.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - distortions
  - asset-warp
  - perspective
---




# Trapezoid Transform

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](trapeze-transform.png){width="128px"}

![](trapeze-transform-grayscale.png){width="128px"}

## Trapezoid Transform (Grayscale)

**In:** *Filters/Transforms*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Special transform node that modifies the input in a perspective/trapezoid warp manner. Has control for Top and Bottom stretch. Values can be pushed beyond limits for stronger effects.

## Parameters

* **Top Stretch**: *0.0 - 1.0*Set the amount of stretch or squash at the top.
* **Bottom Stretch**: *0.0 - 1.0*Set the amount of stretch or squash at the botton.
* **Background Color**: *(Grayscale/Color value)*  
  Set solid background color in case tiling is turned off.
* **Sampling**: *Bilinear, Nearest*Set sampling quality.

## Example Images

![](trapeze-example.gif)

</td>
</tr>
</table>
