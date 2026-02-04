---
title: "Reaction Diffusion Fast | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Reaction Diffusion Fast"
---

# Reaction Diffusion Fast

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Reaction Diffusion node icon](reaction-diffusion.png "Reaction Diffusion node icon")

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node performs a reaction-diffusion effect on an input grayscale image.

Reaction-diffusion is a process in which matter spreads out (diffuses) and interacts (reacts) with other matter. It is a mathematical model that simulates what happens in nature when certain patterns are formed on animal skin for example.

This node is optimised for performance and does make some accuracy trade-offs for speed.

</td>
</tr>
</table>

## Input connectors

<b>Input</b> *Grayscale*The grayscale image that the Reaction-diffusion effect should be applied to.

## Output connectors

<b>Output</b>*Grayscale*The grayscale image representing the Reaction-diffusion effect applied to the Input image.

## Parameters

<b>Radius</b> *Float*How far the effect should spread.

<b>Contrast</b> *Float*  
Adjusts the contrast of the input, serves as a sort of treshold.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Example 1](reactdiff03.png "Example 1")

</td>
<td style="border: 0;" valign="top">

![Example 2](reactdiff02.png "Example 2")

</td>
<td style="border: 0;" valign="top">

![Example 3](reactdiff01.gif "Example 3")

</td>
</tr>
</table>
