---
title: "Color Match | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Color Match"
---

# Color Match

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](color-match-3.png){width="128px"}

## Color Match

**In:** *Filters/Adjustments*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Tries to match the defined *Source Color* range to a *Target Color* range, with support for input slots to define Source and Target.

For simpler versions, see [Replace Color Range](../replace-color-range/replace-color-range.md) or [Replace Color](../replace-color/replace-color.md).

## Parameters

### Inputs

* **Input**: *Color* Input  
  Main input to modify for result.
* **Source Color**: *Color Input*  
  Input slot for Source color, only used when 'Source Color Mode' is set to *Input*.
* **Target Color**: *Color Input*Input slot for Target color, only used when 'Target Color Mode' is set to *Input*.

### Parameters

* **Source Color Mode**: *Average, Parameter, Input*Sets whether Source Color is defined by averaging the input image, by setting a parameter, or by using an input slot.
* **Source Color**: *(Color value)*If Source Color Mode is set to *Parameter*, this parameter determines the Source Color.
* **Target Color Mode**: *Parameter, Image Input*Sets whether Source Color is defined by averaging the input image, by setting a parameter, or using an input slot.
* **Target Color**: *(Color value)*If Target Color Mode is set to *Parameter*, this parameter determines the Target Color.
* **Custom Color Variation**: False/True  
  Enables an additional color variation.
* **Color Variation**   
  Sets Hue, Chrominance or Luminance variations to the result if enabled.
* **Use Mask**: *False/True*  
  Toggles usage of either Mask Input or Output, depending on the Mask Mode below.
* **Mask Mode**: *Parameter, Input*Parameter mode outputs a mask detailing how color where changed. Input mode enables a mask to control the strength of the Color Matching effect.
* **Mask**   
  Outputs a mask showing where exactly the Color Matching effect was applied, with additional controls for smoothing and blurring out the resulting mask.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
