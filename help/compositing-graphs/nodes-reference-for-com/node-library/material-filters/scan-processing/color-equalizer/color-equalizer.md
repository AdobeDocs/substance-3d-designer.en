---
title: "Color Equalizer"
description: "Use the Color Equalizer node to balance color variations in scanned materials for consistent texture appearance."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Color Equalizer
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/color-equalizer.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - enhancing-color
  - color
  - color-grading
---




# Color Equalizer

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](color-equalizer.png){width="128px"}

## Color Equalizer

**In:** *Material Filters/Scan Processing*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This node works like a high-quality [Highpass](../../../filters/adjustments/highpass/highpass.md) for color differences. Where a normal Highpass removes saturation and can introduce unwanted sharpness, Color Equalizer works for evening out color differences and removing unwanted tints at a user-selectable scale.

This is very useful if a photo or scan has unwanted color differences, or a tint that you want removed. If you've used [Highpass](../../../filters/adjustments/highpass/highpass.md), this node should feel familiar.

The masking options are intended for removing very specific tints or for operating only in specific value ranges. Use these if you feel the effect is too broad.

## Parameters

### Inputs

* **Input**: *Color Input*
* **Mask Input**: *Grayscale Input*   
  Mask slot used for masking the node's effects. Only active when Mask is set to "Input".

### Parameters

* **Input Tiled**: *False/True*Optionally preserves tiling on edges.
* **Radius**: *0.0 - 50.0*Sets equalising radius. A larger radius will only remove large color differences. This requires tweaking for every image.
* **Bright/Dark Balance**: *0.0 - 1.0*Bias setting to leave or remove darker tints.
* **Custom Color Variation**: *False/True*Enables the ability to vary the effect towards a user-specified color.
* **Color Variation**   
  Only active if Custom Color Variation is enabled. Settings allow you to select a tint offset to equalise towards.  
  * **Hue**: *0.0 - 360.0*
  * **Chroma**: *0.0 - 1.0*
  * **Luma**: *0.0 - 1.0*
* **Mask Source**: *None, Image Average, Color Parameter, Input*Set if any kind of masking should happen. Color Parameter enables the below additional settings, Input switches to a user-defined mask input.
* **Mask**   
  This is only active with Color Parameter masking. Additional masking parameters to determine the mask based on the image itself. The below parameters allow you to precisely convert a tint to a binary mask on which the Equalisation is applied. Note that the Radius parameter's effects can become much less pronounced when using these settings.  
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
