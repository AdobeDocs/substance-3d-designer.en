---
title: "Non Uniform Directional Warp"
description: "Use the Non Uniform Directional Warp node to apply non-uniform directional warping for creating varied distortion effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Non Uniform Directional Warp
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/non-uniform-directional-warp.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - intermediate-advanced
helpx_learn_topic:
  - asset-warp
  - distortions
  - transform
---




# Non Uniform Directional Warp

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](non-uniform-directional-warp-color.png)![](non-uniform-directional-warp-grayscale.png)

## Non Uniform Dir. Warp (Grayscale)

**In:** *Filters/Effects*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Non-Uniform Direction Warp is an advanced version of [Directional Warp](../../../../atomic-nodes/directional-warp/directional-warp.md) that allows the intensity and direction of the warp to be driven by an image input. It Allows for much more control and can create very useful and interesting image distortion, in the same vain as [Slope Blur](../../blurs/slope-blur/slope-blur.md).

It differs from [Multi Directional Warp](../multi-directional-warp/multi-directional-warp.md) in that it allows control over the Angle through a custom Map input, whereas Multi Directional Warp only allows Direction to be controlled through parameters. This means that you can create advanced trailing and curving effects that are not possible otherwise.

## Parameters

### Inputs

* **Input**: *Grayscale Input*   
  Base map to which the warping will be applied.
* **Intensity Input**: *Grayscale Input*   
  Mandatory mask map that drives the intensity of the warping effect, must be grayscale.
* **Warp Angle Input**: *Grayscale Input*   
  Mandatory mask map that drives the Angle of the warping effect, must be grayscale.

### Parameters

* **Intensity**: *0.0 - 20.0*  
  Sets the intensity of the warp effect, how far to push pixels out.
* **Warp Angle**: *0.0 - 1.0*  
  Sets the Angle or direction in which to apply the Warp effect.
* **Warp Angle Input Multiplier**: *0.0 - 1.0*  
  Sets the effect of the Warp Angle Input Map. The Warp Angle Input map will the be used to interpolate from 0 to the value of this parameter.
* **Trail Mode**: *Min, Max, Average*  
  Sets how the Trails are blended.
* **Trail Length**: *0.0 - 1.0*  
  Sets Length of Trails.
* **Trail Fade**: *0.0 - 1.0*  
  Sets how much each Trail should fade out
* **Trail Curve**: *-1.0 - 1.0*Only has effect if Trail Fade i not 0. Sets how the fading effect behaves.

## Example Images

</td>
</tr>
</table>
