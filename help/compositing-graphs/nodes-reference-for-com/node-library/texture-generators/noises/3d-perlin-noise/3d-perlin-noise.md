---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/3d-perlin-noise.html"
breadcrumb-title: ""
description: Use the 3D Perlin Noise node to generate smooth Perlin noise patterns in 3D space for creating natural-looking volumetric textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Perlin Noise
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Perlin Noise
user-guide-description: ""
user-guide-title: ""
---

# 3D Perlin Noise

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/3dperlinnoise.png){width="200px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The <b>3D Perlin Noise</b> node generates a Perlin noise in 3D space based on the <b>Position Map</b> input.

This node can be tested with [Cube 3D GBuffers](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d-gbuffers/cube-3d-gbuffers.md) as input instead of an actual baked map (as seen in the Example Image below).

</td>
</tr>
</table>

>[!WARNING]
>
> This noise is meant to be used with the <i>GPU engine only</i> (i.e., <b>Direct3D</b> or <b>OpenGL</b>). Go to <b>Tools &gt; Switch engine...</b> or press the <b>F9</b> key to select the desired engine.

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Invert</b> <i>Boolean</i> | Inverts the output image. |
| <b>Scale</b> <i>Float</i> | Controls the scale of the 3D Perlin noise. |
| <b>Size</b> <i>Float3</i> | Controls the size of the 3D Perlin noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. Non-uniform values result in a <i>stretching or squashing</i> effect. |
| <b>Offset</b> <i>Float3</i> | Applies an offset to the <i>position</i> of the 3D Perlin noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. |
| <b>Distortion Intensity</b> <i>Float</i> | Controls the intensity of a <i>warping effect</i> applied on the 3D Perlin noise. |
| <b>Distortion Scale Multiplier</b> <i>Float</i> | Controls the scale of the <i>deforming pattern</i> used in the warping effect controlled by the <b>Distortion Intensity</b>. |
| <b>Baseline</b> <i>Float</i> | Applies an <i>offset</i> to the baseline <i>luminance</i> value for the 3D Perlin noise value distribution. |
| <b>Contrast</b> <i>Float</i> | Adjusts the contrast of the 3D Perlin noise. |
| <b>Absolute</b> <i>Boolean</i> | Uses absolute values in the 3D Perlin noise. This effectively <i>inverts</i> the value distribution for values <i>below 0.5</i>. |
| <b>Enable Tiling</b> <i>Boolean</i> | Adjusts the 3D Perlin noise so its resulting pattern <i>repeats</i> in the X, Y and Z axes. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dperlin.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dperlinnoise-variant2.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dperlinnoise-variant.jpg" />
        </td>
    </tr>
</table>
