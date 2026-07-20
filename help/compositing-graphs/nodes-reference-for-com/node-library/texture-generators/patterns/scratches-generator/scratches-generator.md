---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/scratches-generator.html"
breadcrumb-title: ""
description: Use the Scratches Generator node to create procedural scratch patterns for adding wear and damage to materials.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Scratches Generator
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Scratches Generator
user-guide-description: ""
user-guide-title: ""
---

# Scratches Generator

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](scratches-generator.resources/scratches-generator.png)

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This places random scratches with a lot of customisation options, for example allowing you to set direction, spread and distortion.

There's a special version of Scratches Generator, Scratches Generator Normal, which generates Normalmaps based on the depth of these scratches. Most options are exactly the same, but it has a few extra parameters clearly marked for Normal settings (see below).

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Spline Number</b> <i>1 - 512</i> | Amount of scratches (splines) to place. |
| <b>Max Segments Per Spline</b> <i>2 - 256</i> | Amount of segments/subdivisions over the length of a scratch. Leads to smoother curves and distortions. The effect is more noticeable with higher Distortion values. |
| <b>Spline Rotation</b> <i>0.0 - 1.0</i> | Uniform rotation of all splines, to orient them in a direction. |
| <b>Spline Rotation Random</b> <i>0.0 - 1.0</i> | Variation of angle, randomly rotates every spline. |
| <b>Spline Scale</b> <i>0.0 - 1.0</i> | Uniformly scales all splines. |
| <b>Spline Scale Random</b> <i>0.0 - 1.0</i> | Randomly scales each spline individually. |
| <b>Spline Distortion</b> <i>0.0 - 1.0</i> | Uniform distortion level across all splines. |
| <b>Spline Distortion Random</b> <i>0.0 - 1.0</i> | Randomises the level of distortion of each spline individually. |
| <b>Spline Distortion Frequency</b> <i>0.0 - 1.0</i> | Sets the frequency of distortion, controls the scale of distortion detail. |
| <b>Spline Width</b> <i>0.0 - 2.0</i> | Sets the width of all splines uniformly. |
| <b>Spline Width Random</b> <i>0.0 - 1.0</i> | Randomises the spline width of each spline individually. |
| <b>Spline Position Random</b> <i>0.0 - 1.0</i> | Randomises the position of each spline individually. The lower this value, the more splines will cluster to the center of the canvas. Can be used to create spots of scratches. |
| <b>Set Spline Width in px</b> <i>False/True</i> | Determines the units used for spline width settings. |
| <b>Luminance Random (Grayscale version only)</b> <i>0.0 - 1.0</i> | Randomises the Luminance of each spline individually. |
| <b>Normal Intensity (Normal version only)</b> <i>0.0 - 1.0</i> | Sets the strength of the Normal effect for every spline globally. |
| <b>Normal Intensity Random (Normal version only)</b> <i>0.0 - 1.0</i> | Randomises the normal strength for each spline individually. |
| <b>Normal Format (Normal version only)</b> <i>DirectX, OpenGL</i> | Switches between different Normalmap formats (inverts the green channel). |
| <b>Fade Mode</b> <i>None, Start, End, Start + End</i> | Sets whether and in what direction the splines fade. |
| <b>Fade Length</b> <i>0.0 - 1.0</i> | Sets the length of the fade effect, if enabled above. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enables compensation of squash and stretch with non-square ratios. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="scratches-generator.resources/scratches-ex1.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="scratches-generator.resources/scratches-ex2.png" />
        </td>
    </tr>
</table>
