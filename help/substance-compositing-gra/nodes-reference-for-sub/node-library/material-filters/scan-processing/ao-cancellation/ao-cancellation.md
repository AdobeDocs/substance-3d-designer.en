---
title: "AO Cancellation"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > AO Cancellation"
---

# AO Cancellation

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](ao-cancel.png){width="128px"}

## AO Cancellation

**In:** *Material Filters/Scan Processing*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

This node attempts to remove any Ambient Occlusion lighting information from your Albedo (Base Color) map, based on a separate AO map input. It can be used to ensure your Albedo information is PBR correct and mostly devoid of (strong) lighting information.

A useful node for when you have a baked AO map from a scanned mesh, or alternatively even an AO map generated from Height or Normal info.

## Parameters

* **AO Cancellation**: *0.0 - 1.0*Strength with which to remove lighting information.
* **AO Saturation**: *0.0 - 1.0*(De)Saturation compensation for areas where lighting is removed. This can be used to return any loss of color in darker areas.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
