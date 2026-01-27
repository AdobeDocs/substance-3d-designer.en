---
title: "Blur HQ | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blurs > Blur HQ"
---

# Blur HQ

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](blur-hq-1.png){width="128px"}

![](blur-hq-grayscale.png){width="128px"}

## Blur HQ (Grayscale)

**In:** *Filters/Blurs*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a High-Quality gaussian blur on the result. Much better quality than [the standard atomic box blur](../../../../atomic-nodes/blur/blur.md)[.](../../../../atomic-nodes/blur/blur.md)

Important: make sure to use the appropriate version for your input! Use "Blur HQ" for Color inputs, or "Blur HQ Grayscale" for Grayscale inputs.

## Parameters

* **Intensity**: *0.0 - 16.0*  
  Strength (Radius) of the blur. The higher this value, the further the blur will reach.
* **Quality**: *0 - 1*Increases internal sampling amount for even higher quality, at reduced computation speed.

## Example Images

![](hqblur-example.gif)

</td>
</tr>
</table>
