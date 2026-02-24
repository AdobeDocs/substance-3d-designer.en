---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blurs/anisotropic-blur.html"
breadcrumb-title: ""
description: Use the Anisotropic Blur node to apply directional blur effects for creating motion blur and streaking effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blurs > Anisotropic Blur
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Anisotropic Blur
user-guide-description: ""
user-guide-title: ""
---


# Anisotropic Blur

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](anisotropic-blur-grayscale.png){width="128px"}

![](anisotropic-blur.png){width="128px"}

## Anisotropic Blur (Grayscale)

**In:** *Filters/Blurs*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a high quality [directional blur](../../../../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/directional-blur/directional-blur.md), with a few settings to customise appearance. Also known as "motion blur".

Important: make sure to use the appropriate version for your input! Use "Anisotropic Blur" for Color inputs, or "Anisotropic Blur Grayscale" for Grayscale inputs.

## Parameters

* **Intensity**: *0.0 - 16.0*Strength (Radius) of the blur. The higher this value, the further the blur will reach.
* **Anisotropy**: *0.0 - 1.0*Directionality of the blur. Setting this to 0.0 is the same as performing a regular blur.
* **Angle**: *0.0 - 1.0*Sets the angle for the blur direction.
* **Quality**: *0 - 1*Switches between a[ box blur](../../../../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/blur/blur.md) and an HQ blur internally. Trades in speed for quality.

## Example Images

![](aniso-blur-example.gif)

</td>
</tr>
</table>
