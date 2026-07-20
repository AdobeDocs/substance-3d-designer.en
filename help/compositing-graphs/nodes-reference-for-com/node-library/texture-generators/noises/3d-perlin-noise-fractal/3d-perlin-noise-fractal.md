---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/3d-perlin-noise-fractal.html"
breadcrumb-title: ""
description: Use the 3D Perlin Noise Fractal node to generate fractal Perlin noise patterns in 3D space for creating detailed volumetric textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Perlin Noise Fractal
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Perlin Noise Fractal
user-guide-description: ""
user-guide-title: ""
---

# 3D Perlin Noise Fractal

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](3d-perlin-noise-fractal.resources/3dperlinnoisefractal.png){width="200px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The <b>3D Perlin Noise Fractal</b> node generates a <i>fractal</i> Perlin noise in 3D space based on the <b>Position Map</b> input.

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
| <b>Scale</b> <i>Float</i> | Controls the scale of the fractal 3D Perlin noise. |
| <b>Size</b> <i>Float3</i> | Controls the size of the fractal 3D Perlin noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. Non-uniform values result in a <i>stretching or squashing</i> effect. |
| <b>Offset</b> <i>Float3</i> | Applies an offset to the <i>position</i> of the fractal 3D Perlin noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. |
| <b>Distortion Intensity</b> <i>Float</i> | Controls the intensity of a <i>warping effect</i> applied on the fractal 3D Perlin noise. |
| <b>Distortion Scale Multiplier</b> <i>Float</i> | Controls the scale of the <i>deforming pattern</i> used in the warping effect controlled by the <b>Distortion Intensity</b>. |
| <b>Min Level</b> <i>Integer</i> | The minimum <i>level of of repetition</i> used in the fractal pattern. A wider minimum/maximum range results in a <i>richer pattern</i> with variation on more frequency ranges. |
| <b>Max Level</b> <i>Integer</i> | The maximum <i>level of of repetition</i> used in the fractal pattern. A wider minimum/maximum range results in a <i>richer pattern</i> with variation on more frequency ranges. |
| <b>Roughness</b> <i>Float</i> | Controls the <i>balance</i> between low and high <i>levels of repetition</i> in the fractal pattern.<br><br><i>Note</i>: A value of <b>0</b> results in an output which is <i>not in line</i> with other low values following it. This is expected. |
| <b>Lacunarity</b> <i>Float</i> | Controls how the applied fractal pattern <i>fills space</i>. A <i>higher</i> value results in <i>less gaps</i> in the pattern and a <i>denser</i> noise. |
| <b>Global Opacity</b> <i>Float</i> | Controls the <i>range</i> of the fractal 3D Perlin noise values <i>around</i> the <b>Baseline</b> value. |
| <b>Baseline</b> <i>Float</i> | Applies an <i>offset</i> to the baseline <i>luminance</i> value for the 3D Perlin noise value distribution. |
| <b>Contrast</b> <i>Float</i> | Adjusts the contrast of the 3D Perlin noise. |
| <b>Absolute</b> <i>Boolean</i> | Uses absolute values in the 3D Perlin noise. This effectively <i>inverts</i> the value distribution for values <i>below 0.5</i>. |
| <b>Enable Tiling</b> <i>Boolean</i> | Adjusts the 3D Perlin noise so its resulting pattern <i>repeats</i> in the X, Y and Z axes. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="3d-perlin-noise-fractal.resources/3dfractal.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-perlin-noise-fractal.resources/3dperlinnoisefractal-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-perlin-noise-fractal.resources/3dperlinnoisefractal-variant2.jpg" />
        </td>
    </tr>
</table>
