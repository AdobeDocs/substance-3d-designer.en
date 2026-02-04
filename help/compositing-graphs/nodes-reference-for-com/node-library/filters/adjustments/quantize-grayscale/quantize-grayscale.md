---
title: "Quantize Grayscale"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Quantize Grayscale"
---

# Quantize Grayscale

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Quantize Grayscale icon](quantize-grayscale.png "Quantize Grayscale icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a single spline in the shape of a circle.

</td>
</tr>
</table>

## Parameters

<b>Steps</b> *Integer*The number of separate values the input range should be approximated to.

<b>Offset</b> *Float*Applies an offset to the input range, which *shifts* the results along the range.

<b>Slope</b> *Float*Applies a slope gradient to the *transitions* between approximated values, up to the *full span of a step*.

<b>Slope Curve</b> *Integer*Sets the method of acquiring the curve for the slope set by the <b>Slope</b> parameter:  
* *Linear*: Applies a linear curve, resulting in a straight slope  
* *Smoothstep*: Applies a smoothstep curve, resulting in a smooth slope  
* *Curve input*: Applies the curve described by the <b>Curve Input</b> input map. You may use a [Curve](../../../../atomic-nodes/curve/curve.md) node to describe this curve with a great amount of control.

## Examples

![Example 1](quantizegrayscale.gif "Example 1")

![Example 2](quantizegrayscale.png "Example 2")
