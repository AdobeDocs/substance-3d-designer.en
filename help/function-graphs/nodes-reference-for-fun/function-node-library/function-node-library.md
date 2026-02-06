---
title: "Function node library"
description: ""
helpx_description: "Designer > Function graphs > Nodes reference for function graphs > Function node library"
---

# Function node library

In addition to [atomic nodes](../atomic-function-nodes/atomic-function-nodes.md), Designer also offers pre-made Substance function graphs as instance nodes. They offer many tools to speed up workflow and provide more capabilities for working with vectors or colors, remapping values, perform more advanced algebra, ...

These tools are arranged into several categories:

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Comparison

Equality boolean

Equality float2

Equality float3

Equality float4

Not equal boolean

Not equal float2

Not equal float3

Not equal float4

</td>
<td style="border: 0;" valign="top">

### Conversion

&#91;-1, 1&#93; to &#91;0, 1&#93;

&#91;0, 1&#93; to &#91;0, 1, 0&#93;

&#91;0, 1&#93; to &#91;-1, 1&#93;

&#91;0, 1&#93; to &#91;1, 0&#93;

&#91;a, b&#93; to &#91;0, 1&#93;

Boolean to float1

Degrees to radians

Degrees to turns

Height balance

Sawtooth wave

Triangle wave

Turns to degrees

</td>
<td style="border: 0;" valign="top">

### Constant

2 Pi

Pi

### Parity

Even count

Odd count

Parity test

</td>
</tr>
</table>

### Maths

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

acos

asin

Average float

Average float2

Average float3

Average float4

Clamp

Cross product

Cross product vec2

Distance float2

Distance float3

</td>
<td style="border: 0;" valign="top">

Scalar division float2

Scalar division float3

Scalar division float4

Fmod

Frac

Length float2

Length float3

Merge float3

Merge float4

Normalize vec2

Normalize vec3

Normalize vec4

</td>
<td style="border: 0;" valign="top">

One minus

Orthogonal vec2

Reflect

Round float1

Saturate

Saturate float2

Sign

Smoothstep

Step

Truncate float

</td>
</tr>
</table>

### Color

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

ACEScg to linear sRGB

Direction to normal

HCL to RGB

HSI to RGB

HSL offset

HSL to RGB

HSV to RGB

Linear sRGB to ACEScg

Linear to sRGB (Luminance)

Linear to sRGB

Random color

Random luminosity

</td>
<td style="border: 0;" valign="top">

RGB chroma 2 polar

RGB chroma hexagonal

RGB hue 2 polar

RGB hue hexagonal

RGB lightness average

RGB lightness bi-hexcone

RGB lightness hexcone

RGB lightness luma Rec.601

RGB lightness luma Rec.709

RGB saturation HSI

RGB saturation HSL

RGB saturation HSV

</td>
<td style="border: 0;" valign="top">

RGB to HCL

RGB to HSI

RGB to HSL

RGB to HSV

sRGB to linear (Luminance)

sRGB to linear

Temperature to RGB

ACES tonemapper

Agx tonemapper (approx)

Hejl tonemapper

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

### Transformation

Cartesian to polar

Directional offset

Matrix invert

Matrix multiply

Polar to cartesian

Rotate vec2

Rotate vec2 (Radian)

Rotation matrix

Scale matrix

Tile matrix

</td>
<td width="66.67%" style="border: 0;" valign="top">

### Random

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

Random discrete &#91;a, b&#93;

Global random

[Hash 11](function-nodes-random/hash-functions/hash-functions.md)

[Hash 14](function-nodes-random/hash-functions/hash-functions.md)

[Hash 21](function-nodes-random/hash-functions/hash-functions.md)

[Hash 22](function-nodes-random/hash-functions/hash-functions.md)

[Hash 24](function-nodes-random/hash-functions/hash-functions.md)

[Hash 31](function-nodes-random/hash-functions/hash-functions.md)

[Hash 32](function-nodes-random/hash-functions/hash-functions.md)

</td>
<td style="border: 0;" valign="top">

Normal distribution

Random uniform &#91;-1, 1&#91;

Random uniform &#91;a, b&#91;

Random uniform float2 &#91;a, b&#91;

Random uniform float3 &#91;a, b&#91;

Random uniform float4 &#91;a, b&#91;

</td>
</tr>
</table>

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

### Easings

Ease in circ

Ease in cubic

Ease in expo

Ease in out circ

Ease in out cubic

Ease in out expo

Ease in out quad

Ease in out quart

Ease in out quint

Ease in out sine

Ease in quad

Ease in quart

Ease in quint

Ease in sine

Ease out circ

Ease out cubic

Ease out expo

Ease out quad

Ease out quart

Ease out quint

Ease out sine

</td>
<td width="66.67%" style="border: 0;" valign="top">

### Various

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

Curve

Non-square expansion UV scale

Non-square output size

Roughness

Switch float 2 inputs

Switch float2 2 inputs

Switch float2 4 inputs

Switch float2 8 inputs

Switch float3 2 inputs

Switch float3 4 inputs

Switch float3 8 inputs

Switch float3 8 inputs

Switch float4 2 inputs

Switch float4 4 inputs

Switch float4 8 inputs

</td>
<td style="border: 0;" valign="top">

Switch integer 2 inputs

Switch integer 4 inputs

Switch integer 8 inputs

Switch integer2 2 inputs

Switch integer2 4 inputs

Switch integer2 8 inputs

Switch integer3 2 inputs

Switch integer3 4 inputs

Switch integer3 8 inputs

Switch integer4 2 inputs

Switch integer4 4 inputs

Switch integer4 8 inputs

</td>
</tr>
</table>

</td>
</tr>
</table>
