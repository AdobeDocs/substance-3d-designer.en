---
title: "Multi Color Equalizer"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi Color Equalizer"
---

# Multi Color Equalizer

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](color-equalizer-multi.png){width="128px"}

## Multi Color Equalizer

**In:** *Material Filters/Scan Processing*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This is the multi-input version of [Color Equalizer](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/color-equalizer/color-equalizer.md). It evens out color differences and removes unwanted tints at a user-selectable scale. It is mainly intended for use with multi-angle photos, which are then combined with [Multi-Angle to Albedo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-albedo/multi-angle-to-albedo.md) or [Multi-Angle to Normal](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-normal/multi-angle-to-normal.md).

>[!NOTE]
>
> See the original [Color Equalizer](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/color-equalizer/color-equalizer.md) for more info.

## Parameters

### Inputs

* **Input 1-8**: *Color Input*Multiple inputs to process.
* **Mask Input**: *Grayscale Input*  
  Mask slot used for masking the node's effects.

### Parameters

* **Input Count**: *1 - 8*Sets the number of inputs to process in parallel.
* **Input Tiled**: *False/True*Optionally preserves tiling on edges.
* **Radius**: *0.0 - 50.0*Sets equalising radius. A larger radius will only remove large color differences. This requires tweaking for every image.
* **Bright/Dark Balance**: *0.0 - 1.0*Bias setting to leave or remove darker tints.
* **Custom Color Variation**: *False/True*Allows you to vary the effect towards a user-specified color.
* **Color Variation**   
  Only active if Custom Color Variation is enabled. Settings allow you to select a tint offset to equalise towards.  
  * **Hue**: *0.0 - 360.0*
  * **Chroma**: *0.0 - 1.0*
  * **Luma**: *0.0 - 1.0*
* **Mask Source**: *None, Image Average, Color Parameter, Input*Sets whether any masking should happen. Color Parameter enables additional settings below, Input switches to a user-defined mask input.
* **Mask**   
  Only active with Color Parameter masking. Contains additional masking parameters to determine the mask based on the image itself. The below parameters allow you to precisely convert a tint to a binary mask on which the equalisation is applied. Note that the Radius parameter's effects can become much less pronounced when using these settings.  
  * **Color**: *(Color value)*
  * **Hue Range**: *0.0 - 360.0*
  * **Chroma Range**: *0.0 - 1.0*
  * **Luma Range**: *0.0 - 1.0*
  * **Blur**: *0.0 - 2.0*
  * **Smoothness**: *0.0 - 2.0*

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
