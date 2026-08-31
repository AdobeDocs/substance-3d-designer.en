---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/non-uniform-directional-warp.html"
breadcrumb-title: ""
description: Use the Non Uniform Directional Warp node to apply non-uniform directional warping for creating varied distortion effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Non Uniform Directional Warp
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Non Uniform Directional Warp
user-guide-description: ""
user-guide-title: ""
---

# Non Uniform Directional Warp

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](non-uniform-directional-warp.resources/non-uniform-directional-warp-01.png)![](non-uniform-directional-warp.resources/non-uniform-directional-warp-02.png)

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Non-Uniform Direction Warp is an advanced version of [Directional Warp](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/directional-warp/directional-warp.md) that allows the intensity and direction of the warp to be driven by an image input. It Allows for much more control and can create very useful and interesting image distortion, in the same vain as [Slope Blur](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blurs/slope-blur/slope-blur.md).

It differs from [Multi Directional Warp](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/multi-directional-warp/multi-directional-warp.md) in that it allows control over the Angle through a custom Map input, whereas Multi Directional Warp only allows Direction to be controlled through parameters. This means that you can create advanced trailing and curving effects that are not possible otherwise.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Grayscale Input</i> | Base map to which the warping will be applied. |
| <b>Intensity Input</b> <i>Grayscale Input</i> | Mandatory mask map that drives the intensity of the warping effect, must be grayscale. |
| <b>Warp Angle Input</b> <i>Grayscale Input</i> | Mandatory mask map that drives the Angle of the warping effect, must be grayscale. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 20.0</i> | Sets the intensity of the warp effect, how far to push pixels out. |
| <b>Warp Angle</b> <i>0.0 - 1.0</i> | Sets the Angle or direction in which to apply the Warp effect. |
| <b>Warp Angle Input Multiplier</b> <i>0.0 - 1.0</i> | Sets the effect of the Warp Angle Input Map. The Warp Angle Input map will the be used to interpolate from 0 to the value of this parameter. |
| <b>Trail Mode</b> <i>Min, Max, Average</i> | Sets how the Trails are blended. |
| <b>Trail Length</b> <i>0.0 - 1.0</i> | Sets Length of Trails. |
| <b>Trail Fade</b> <i>0.0 - 1.0</i> | Sets how much each Trail should fade out |
| <b>Trail Curve</b> <i>-1.0 - 1.0</i> | Only has effect if Trail Fade i not 0. Sets how the fading effect behaves. |
