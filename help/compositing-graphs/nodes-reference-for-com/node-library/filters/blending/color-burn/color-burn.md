---
title: "Color Burn | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Color Burn"
---

# Color Burn

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](color-burn.png){width="128px"}

## Color Burn

**In:** *Filters/Blending*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a Color Burn blend between Foreground and Background. Mathematically the formula is 1 - (1-Background) / Foreground.

## Parameters

### Inputs

* **Foreground**: *Color Input*
* **Background**: *Color Input*
* **Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Opacity**: *0.0 - 1.0*  
  Blending Opacity between Foreground and Background.
* **Alpha Blending**: *False/True*  
  Toggles blending of the Foreground and Background alpha channels. If set to False, the alpha channel of the foreground is ignored.

## Example Images

</td>
</tr>
</table>

 